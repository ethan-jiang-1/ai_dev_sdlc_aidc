#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""agent-101 跨文件一致性检查器（v2，按第七轮审计重写）

为什么存在：同一事实散在 6 个文件里，人眼同步不可靠，七轮复核反复栽在
"改了 04 没同步上游"。把同步判定交给脚本。

v1 的教训（第七轮审计实测出 4 类假绿，v2 全部修掉）：
  1) stale_allow 整文件豁免 → "过期状态只住在被豁免文件里"→ 探针永不触发
  2) canon 探针过松（3-4 字子串命中即过）
  3) alt 没配 alt_must → 死代码
  4) ** 只按整文件奇偶 → 两处错误互相抵消；且无 --selftest 负样本

判五类：A 结构不变量 / B 渲染安全 / C 跨文件事实 / D 上游同步 / E 红线
跑法：python3 talk-ai-coding-evolution-agent-101/tools/check-consistency.py [--selftest]
退出码：0=全过；1=有任何问题（含"小"）

维护须知：新增共享事实时同步在 FACTS/STALE_TERMS/COUNTS 加一行；
改完务必跑 --selftest——检查项漏了比漏改更危险。
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TALK = os.path.dirname(HERE)

PPT   = '04_drafts/ppt-text-v6.md'
PAGE  = '04_drafts/手册-页版-v6.md'
LONG  = '04_drafts/实战手册-v6.md'
CTX   = 'CONTEXT.md'
OUT   = '03_outline/00-page-structure-v4.md'
STORY = '01_storyline/00-storyline-map.md'
NARR  = '01_storyline/01-narrative-check.md'
TREAD = 'README.md'
TCUR  = 'CURRENT.md'

ALL = [PPT, PAGE, LONG, CTX, OUT, STORY, NARR, TREAD, TCUR]
RENDER = [PPT, PAGE]
CUSTOMER = [PPT, PAGE, LONG]

def read(rel):
    with open(os.path.join(TALK, rel), encoding='utf-8') as f:
        return f.read()

TXT = {f: read(f) for f in ALL}
problems = []
NOTES = []         # 启发式提示
def rep(sev, axis, msg):
    problems.append((sev, axis, msg))

def blocks(t):
    lines = t.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('### ')]
    seps = [i for i, l in enumerate(lines) if l.strip() == '---']
    out = []
    for n, i in enumerate(idx):
        end = idx[n + 1] if n + 1 < len(idx) else len(lines)
        out.append((lines[i].split()[1], i, '\n'.join(lines[i:end])))
    return out, seps, lines

RECORD_MARK = re.compile(r'旧写法|旧口径|原文|→|改名|已废|残留|~~|已修|改准|消除|过期|改后|改前|取代|不再写|不许再说|示意')
RECORD_FILES = {TCUR, NARR}   # 记录件：里面的 v 记录节整体视为记录块

def _record_sections(rel):
    """CURRENT/NARR 里从 '## vNN' 或 '## 补' 起到下一个 '## ' 的行区间"""
    rng = set(); lines = TXT[rel].split('\n'); start = None
    for i, l in enumerate(lines):
        if l.startswith('## ') and not l.startswith('### '):
            if start is not None:
                rng.update(range(start, i))     # 先结算上一段（连续 v 节也各算各的）
                start = None
            if re.match(r'## (v\d|补)', l):
                start = i
    if start is not None:
        rng.update(range(start, len(lines)))
    return rng

_RS = {}

def in_record_line(rel, lineno):
    if rel == NARR:
        return True              # narrative-check 整件是质检记录，无热区
    if rel not in _RS:
        _RS[rel] = _record_sections(rel) if rel in RECORD_FILES else set()
    if lineno in _RS[rel]:
        return True
    lines = TXT[rel].split('\n')
    if lineno >= len(lines):
        return False
    return bool(RECORD_MARK.search(lines[lineno]))

def check_structure():
    for rel, want in ((PPT, 20), (PAGE, 20)):
        t = TXT[rel]
        bl, seps, lines = blocks(t)
        if len(bl) != want:
            rep('严重', '结构', f'{rel}: 页块 {len(bl)}，应为 {want}')
        if len(seps) != want:
            rep('严重', '结构', f'{rel}: 分割线 {len(seps)}，应为 {want}')
        gaps = [sum(1 for s in seps if a < s < b) for (_, a, _), (_, b, _) in zip(bl, bl[1:])]
        if set(gaps) != {1}:
            rep('严重', '结构', f'{rel}: 页块之间的分割线不是恰好一条 -> {sorted(set(gaps))}')
        if sum(1 for s in seps if s < bl[0][1]) != 1:
            rep('重要', '结构', f'{rel}: 头部之后到第一个页块之间的分割线不是 1 条')
        for s in seps:
            if s > 0 and lines[s - 1].strip() and lines[s + 1].strip():
                rep('重要', '结构', f'{rel}: 第 {s+1} 行分割线前后没留空行')
        got = [pid for pid, _, _ in bl]
        want_ids = ([f'P{i}' for i in range(1, 14)] + ['B1'] + [f'P{i}' for i in range(14, 16)] + ['B2']
                    + [f'P{i}' for i in range(16, 19)]) if rel == PPT else [f'HP{i}' for i in range(1, 21)]
        if got != want_ids:
            rep('重要', '结构', f'{rel}: 页块顺序异常（应为 {want_ids[0]}..{want_ids[-1]}）')

    bl, _, _ = blocks(TXT[PAGE])
    for pid, _, b in bl:
        n = len(re.findall(r'\[必上\]', b))
        if n != 1:
            rep('严重', '结构', f'页版 {pid}: [必上] 有 {n} 条，应恰好 1 条')

    ok = {'必上', '可选', '例', '必给', 'INTERFACE', 'INTERFACE · 不上屏', '不上屏'}
    for rel in RENDER:
        bad = set()
        for m in re.finditer(r'\[([^\]\n]*)\]', TXT[rel]):
            if m.group(1).strip() in ('', 'x', 'X'):
                continue
            if m.group(1) not in ok:
                bad.add(m.group(1))
        if bad:
            rep('重要', '结构', f'{rel}: 方括号里出现非优先级记号 {sorted(bad)}')

    if '本件只有这三个' in TXT[PPT]:
        body = TXT[PPT].split('\n### ', 1)[1]
        used = {x for x in ('必上', '可选', '例', '必给') if f'[{x}]' in body}
        if used != {'必上', '可选', '例'}:
            rep('严重', '结构', f'{PPT}: 头部称只有三个记号，正文实际用到 {sorted(used)}')

    allow = {'P5', 'P12', 'P14', 'P15'}
    bl, _, _ = blocks(TXT[PPT])
    for pid, _, b in bl:
        if '（大字）' in b and pid not in allow:
            rep('重要', '结构', f'{PPT} {pid}: 用了（大字），但白名单只给 {sorted(allow)}')
    for pid in allow:
        b = next((x for p, _, x in bl if p == pid), '')
        if '（大字）' not in b:
            rep('重要', '结构', f'{PPT} {pid}: 在最大字号白名单里，却没有一处（大字）')
    if not re.search(r'最大字号只给', TXT[OUT]):
        rep('小', '结构', f'{OUT}: 没找到"最大字号"白名单的规约')

    def fields(t):
        out = set()
        for m in re.finditer(r'^- \*\*(.+?)\*\*(（[^）]*）)?[：]', t, flags=re.M):
            out.add(re.sub(r' \[[^\]]+\]', '', m.group(1)).strip())
        return out
    def declared(t):
        head = t.split('\n### ')[0]
        d = set()
        for l in head.split('\n'):
            if l.lstrip().startswith('|'):
                for tok in re.findall(r'`([^`]+)`', l):
                    d.update(x.strip() for x in tok.split('／'))
        return {re.sub(r'\s*\[[^\]]+\]$', '', x).strip() for x in d if x.strip()}
    for rel in RENDER:
        dec, use = declared(TXT[rel]), fields(TXT[rel])
        base = lambda s: re.sub(r'（[^）]*）$', '', s).strip()
        dec2, use2 = {base(x) for x in dec}, {base(x) for x in use}
        if use2 - dec2:
            rep('严重', '结构', f'{rel}: 正文用了未声明的字段 {sorted(use2-dec2)}')
        unused = {d for d in dec2 if d and d not in use2 and d not in ('版式', '大字', '小字')}
        if unused:
            rep('小', '结构', f'{rel}: 字段表声明了但正文未用 {sorted(unused)}')

    m = re.search(r'04（演讲）只允许出现：`(.+?)`', TXT[OUT])
    if m:
        wl = {x.strip() for x in m.group(1).split('／')}
        missing = {re.sub(r'（[^）]*）$', '', x).strip() for x in fields(TXT[PPT])} - wl
        if missing:
            rep('严重', '结构', f'{OUT}: 白名单漏了 04 实际字段 {sorted(missing)}')

    for pid, _, b in bl:
        mfoot = re.search(r'L4 页脚\*\*：(.+)', b)
        if not mfoot:
            continue
        foot = mfoot.group(1)
        if pid in ('P4', 'P5'):
            if not re.search(r'\d{4}', foot) or not re.search(r'(官方原文|原文出处)', foot):
                rep('重要', '结构', f'{PPT} {pid}: 页脚应署名（机构/作者+年份+日常说法等级）')
        elif re.search(r'\d{4}', foot):
            rep('小', '结构', f'{PPT} {pid}: 页脚出现年份（署名只允许 P4/P5）')

    for k in ('结论句', '落点', '命名', '附带', '脚注'):
        tot = len(re.findall(rf'^- \*\*{k}', TXT[PPT], flags=re.M))
        tagged = len(re.findall(rf'^- \*\*{k} \[必上\]', TXT[PPT], flags=re.M))
        if tot != tagged:
            rep('严重', '结构', f'{PPT}: 「{k}」{tagged}/{tot} 带 [必上]')

def check_render_safety():
    for rel in CUSTOMER:
        t = TXT[rel]
        if t.count('"'):
            rep('严重', '渲染安全', f'{rel}: ASCII 双引号 {t.count(chr(34))} 个（对客件必须为 0）')
        if '****' in t:
            rep('严重', '渲染安全', f'{rel}: 出现四个星号（嵌套加粗写错）')
        bl, _, _ = blocks(t)
        for pid, _, b in bl:
            stripped = re.sub(r'`[^`]*`', '', b)
            if stripped.count('**') % 2:
                rep('严重', '渲染安全', f'{rel} {pid}: ** 计数为奇数（未闭合的加粗）')
        head = t.split('\n### ')[0]
        if re.sub(r'`[^`]*`', '', head).count('**') % 2:
            rep('严重', '渲染安全', f'{rel}: 头部 ** 计数为奇数')
        if '[不上屏]' in t:
            rep('严重', '渲染安全', f'{rel}: 对客件出现 [不上屏] 标签')
        if '<!--' in t:
            rep('严重', '渲染安全', f'{rel}: 对客件出现 HTML 注释（off-screen 只许工作文档用）')
        L = t.split('\n'); i = 0
        while i < len(L):
            if L[i].strip().startswith('|'):
                j = i
                while j < len(L) and L[j].strip().startswith('|'):
                    j += 1
                body = [x for x in L[i:j] if not re.match(r'^\|[\s\-:|]+\|$', x.strip())]
                if body:
                    cnt = {x.count('|') for x in body}
                    if len(cnt) > 1:
                        rep('小', '渲染安全', f'{rel}: 第 {i+1} 行起的表格列数不齐 {sorted(cnt)}')
                i = j
            else:
                i += 1
    for rel in ALL:
        t = TXT[rel]
        depth = 0
        for m in re.finditer(r'<!--|-->', t):
            depth += 1 if m.group(0) == '<!--' else -1
            if depth < 0:
                rep('严重', '渲染安全', f'{rel}: HTML 注释闭合在开启之前'); depth = 0
        if depth != 0:
            rep('严重', '渲染安全', f'{rel}: HTML 注释不配对（{depth} 个未闭合）')

FACTS = [
    dict(name='P12 落点', canon='能让代码查的，别让 AI 自己说', must=[PPT, CTX, STORY, TREAD]),
    dict(name='主线＝信噪比', canon='有用的多、没用的少', must=[PPT, LONG, CTX, OUT, STORY]),
    dict(name='全场结论', canon='模型决定上限', must=[PPT, CTX, STORY, TREAD]),
    dict(name='干活的和验收的', canon='干活的和验收的，不能是同一个人', must=[PPT, PAGE, LONG, STORY, CTX],
         stale=['必须分开']),
    dict(name='上屏标题', canon='它不糊涂，是因为外面那一圈搭对了', must=[PPT, STORY, TREAD, PAGE, LONG]),
    dict(name='副标题', canon='搭对了，它跑起来就不糊涂', must=[PPT, STORY, OUT]),
    dict(name='五件事顺序', canon='先看到 → 再懂 → 再会', must=[PPT, STORY, CTX]),
    dict(name='B2 小字', canon='值多少，看这一圈归谁', must=[PPT, STORY, OUT]),
    dict(name='两问帮你认档', canon='帮你认自己在哪一档', must=[PPT, PAGE, LONG, STORY]),
    dict(name='那一圈会移动', canon='这一圈不会消失，只会移动', must=[CTX, STORY, TREAD]),
    dict(name='打磨三轮', canon='打磨三轮', must=[PAGE, LONG]),
    dict(name='五个地方枚举', canon='工作空间', must=[PAGE, LONG, CTX]),
    dict(name='P13 三条路', canon='让 AI 写，但你自己审它检查什么', must=[PPT, STORY, CTX]),
    dict(name='档1档2分界', canon='步骤是不是你事先定好的', must=[PPT, PAGE, LONG, STORY]),
    dict(name='核心命题', canon='Agent = Model + Harness', must=[PPT, CTX, OUT, STORY, TREAD]),
    dict(name='判据', canon='错了赔得起吗？错了多久能发现？', must=[PPT, CTX],
         halves=['错了赔得起吗？', '错了多久能发现？'], halves_must=[PAGE, LONG]),
    dict(name='厚薄＝加几道关', canon='几道关', must=[PPT, PAGE, LONG, CTX, OUT, STORY]),
    dict(name='档1上屏名', canon='你问一句，它答一句', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='档2上屏名', canon='你定好步骤，它照着走', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='档3上屏名', canon='你给个目标，它自己跑', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='档4上屏名', canon='你定好分工，它们自己配合', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='四档第二问', canon='是一条路，还是几条线', must=[PPT, PAGE, LONG, CTX, STORY],
         stale=['是一条路还是几条线', '是一条路走到底', '同时有几个在跑']),
    dict(name='命名规则', canon='下一步由你定，叫「工作流」；下一步由它定，叫「智能体」', must=[PPT, STORY, CTX]),
    dict(name='命名不派四档', canon='只定这两个名字', must=[CTX]),
    dict(name='挑活判断力', canon='判得出对错', must=[PPT, PAGE, LONG, CTX]),
    dict(name='挑活阈值', canon='既别拿它练、也别让它自己跑', must=[CTX],
         alt=['也别让它自己跑', '也别交给它自己跑'], alt_must=[PPT, PAGE, LONG, STORY]),
    dict(name='政策未定闸门', canon='政策还没定', must=[CTX],
         alt=['政策已经定了'], alt_must=[PPT, PAGE, LONG]),
    dict(name='维护闸门', canon='谁维护它？它坏了谁发现', must=[PPT, PAGE, LONG, STORY]),
    dict(name='答不上来先别搭', canon='答不上来，先别搭', must=[PPT, PAGE, LONG, STORY]),
    dict(name='政策未定那条', canon='都还没定的事', must=[PPT, PAGE, LONG, STORY]),
    dict(name='一次只动一样（循环）', canon='一次只补一条', must=[PAGE, LONG]),
    dict(name='一次只动一样（劝人别加）', canon='一次只加一条', must=[PPT]),
    dict(name='先跑最简单的', canon='先跑最简单的', must=[PPT, LONG, STORY]),
    dict(name='越往下越危险', canon='少一样就越危险', must=[PAGE, LONG]),
    dict(name='档1没有独立检查', canon='第 1 档你自己就是那一圈', must=[PPT, PAGE, LONG, STORY]),
    dict(name='五格↔五件事映射', canon='就是那五件事', must=[PAGE, LONG, CTX]),
    dict(name='留痕释义', canon='事后查得到它每一步做了什么', must=[PPT, CTX],
         alt=['它每一步做了什么、用了哪份数据'], alt_must=[PAGE, LONG, STORY]),
    dict(name='代码释义', canon='每次跑出来都一样', must=[PPT, CTX],
         alt=['每次都一样'], alt_must=[PAGE, LONG]),
    dict(name='加之前先减', canon='加东西之前先减', must=[PPT],
         alt=['加之前也要减'], alt_must=[PAGE, LONG]),
    dict(name='合规问谁', canon='管技术的或管合规的同事', must=[PAGE, LONG]),
    dict(name='症状④说法', canon='兜圈子', must=[PPT, PAGE, LONG, STORY, TREAD],
         stale=['绕圈'], stale_line_allow=True),
    dict(name='不是渲染输入', canon='不是渲染输入', must=[STORY]),
]

STALE_TERMS = [
    ('不写代码',       '旧听众口径（v24 已换）', [PPT, PAGE, LONG, CTX, OUT, STORY, TREAD]),
    ('文职岗',         '旧听众口径', [PPT, PAGE, LONG, CTX, OUT, STORY, TREAD]),
    ('零术语版',       'v6 已改为"术语按序入场"（否定句属合规）', [PPT, PAGE, LONG, CTX, OUT, STORY]),
    ('同时有几个在跑', '四档第二问的旧写法', [PPT, PAGE, LONG, CTX, OUT, STORY]),
    ('两个问题定档',   '四档的派生说法（v26 已废）', [PPT, PAGE, LONG, CTX, OUT, STORY]),
    ('四档全部由它派生','四档的派生说法（v26 已废）', ALL),
    ('循环往复',       'AI 腔／书面腔', [PPT, PAGE, LONG]),
    ('缺的是这五件',   '旧句式', [PPT, PAGE, LONG]),
    ('v4 已全部落盘',  '过期状态（第六轮重要1 修掉的正是这句）', [TCUR]),
]
DUAL_PROBES = [(TCUR, 'v4 已全部落盘', '文案 v6 已落盘')]

COUNTS = [
    ('18 页正文 / 18 正文', [CTX, OUT, STORY, TREAD]),
    ('20 张', [CTX, OUT, STORY, TREAD, TCUR]),
    ('2 张停顿页 / 2 停顿页 / 2 停顿', [CTX, OUT, STORY, TREAD]),
    ('27.5 / 27.0', [OUT, STORY]),
    ('28.2 / 27.7', [OUT, STORY]),
]

def check_facts():
    for f in FACTS:
        if f.get('alt') and not f.get('alt_must'):
            rep('严重', '自检', f'FACT「{f["name"]}」配了 alt 却没配 alt_must——这条检查一次都不会执行（v1 死代码）')
        for rel in f['must']:
            if rel not in ALL:
                rep('严重', '自检', f'FACT「{f["name"]}」的 must 里是不存在的文件 {rel}')
    for f in FACTS:
        listed = set(f['must']) | set(f.get('alt_must', [])) | set(f.get('halves_must', []))
        for rel in ALL:
            if rel in listed or rel in RECORD_FILES:
                continue
            if f['canon'] in TXT[rel]:
                NOTES.append(f'FACT「{f["name"]}」的 canon 也出现在 {rel}（不在 must 里）——漏列，还是该禁？')

    for f in FACTS:
        name, canon, must = f['name'], f['canon'], f['must']
        for rel in must:
            hit = canon in TXT[rel] or any(a in TXT[rel] for a in f.get('alt', []))
            if not hit:
                rep('严重', '一致性', f'「{name}」的固定说法在 {rel} 里没有（canon 与 alt 均未命中）')
        for h in f.get('halves', []):
            for rel in f.get('halves_must', []):
                if h not in TXT[rel]:
                    rep('重要', '一致性', f'「{name}」的半句「{h}」在 {rel} 里没有')
        for s in f.get('stale', []):
            for rel in ALL:
                for i, l in enumerate(TXT[rel].split('\n')):
                    if s not in l:
                        continue
                    if in_record_line(rel, i):
                        continue
                    if s == '必须分开' and '不能是同一个人' in l:
                        continue
                    rep('重要', '一致性', f'{rel}:{i+1} 旧写法「{s}」——「{name}」的 canon 是「{canon}」')

def check_stale_terms():
    for term, why, scope in STALE_TERMS:
        for rel in scope:
            for i, l in enumerate(TXT[rel].split('\n')):
                if term not in l:
                    continue
                if in_record_line(rel, i):
                    continue
                if term == '零术语版' and '不是' in l:
                    continue
                rep('重要', '一致性', f'{rel}:{i+1} 已废弃说法「{term}」（{why}）')
    for rel, old, new in DUAL_PROBES:
        if new not in TXT[rel]:
            rep('严重', '一致性', f'{rel}: 热区应出现「{new}」（旧串「{old}」的现串）')

def check_counts():
    for spec, must in COUNTS:
        alts = [x.strip() for x in spec.split('/')]
        for rel in must:
            if not any(a in TXT[rel] for a in alts):
                rep('小', '一致性', f'计数事实「{alts[0]}」在 {rel} 里没有')

def check_upstream():
    bl, _, _ = blocks(TXT[PPT])
    for pid, _, _ in bl:
        if not re.search(rf'\*\*{pid}\*\*', TXT[OUT]):
            rep('重要', '系统', f'{OUT} 里没有 {pid} 的行（04 有这一页）')
    for m in re.finditer(r'\*\*(P\d+|B\d)\*\*', TXT[OUT]):
        pid = m.group(1)
        if pid not in {p for p, _, _ in bl}:
            rep('小', '系统', f'{OUT} 提到 {pid}，但 04 里没有这一页（删页须显式登记）')
    bl2, _, _ = blocks(TXT[PAGE])
    head2 = TXT[PAGE].split('\n### ')[0]
    for pid in (bl2[0][0], bl2[-1][0]):
        if pid not in head2:
            rep('小', '系统', f'{PAGE}: 头部切页说明里没提到 {pid}')

WL_TOKEN = re.compile(r'^(?:Agent|Model|Harness|harness|harness engineering|AI|Anthropic|Trivedy|PPT|INTERFACE|md|v\d+)$')

def check_redlines():
    for rel in CUSTOMER:
        body = TXT[rel].split('[INTERFACE]', 1)[-1]
        body = re.sub(r'`[^`]*`', '', body)
        body = body.replace("If you're not the model, you're the harness.", '')
        body = body.replace('harness engineering', 'HE')
        hits = set()
        for m in re.finditer(r"[A-Za-z][A-Za-z '\-]{2,}", body):
            s = m.group(0).strip()
            if all(WL_TOKEN.match(w) for w in s.split()):
                continue
            hits.add(s)
        if hits:
            rep('重要', '红线', f'{rel}: 白名单外英文 {sorted(hits)}')
    bl, _, _ = blocks(TXT[PPT])
    for pid, _, b in bl:
        if 'harness' in b.lower() and pid not in ('P5', 'P18'):
            rep('严重', '红线', f'{PPT} {pid}: 出现 harness（只许 P5/P18）')
    STRUCT = re.compile(r'(L[1-4]|HP\d+|\bP\d+|\bB[12]\b|页码\s*\d+|第\s*\d+(?:[–-]\d+)?\s*[档轮]|第\s*\d+\s*或\s*第\s*\d+\s*档|档\s*\d+\s*和\s*档\s*\d+|≥60%|Anthropic, 2026|Trivedy, 2026|^\s*\d+\.\s)')
    for rel, start in ((PPT, 47), (PAGE, 38)):
        for i, ln in enumerate(TXT[rel].split('\n'), 1):
            if i < start:
                continue
            t = re.sub(r'`[^`]*`', '', STRUCT.sub('', ln))
            if re.search(r'[0-9]', t):
                rep('重要', '红线', f'{rel}:{i} 内容里出现阿拉伯数字：{ln.strip()[:60]}')

SELFTEST_CASES = [
    ('CURRENT 热区换回"v4 已全部落盘…PPT 事实稿"',
     lambda T: {**T, TCUR: T[TCUR].replace('文案 v6 已落盘', 'v4 已全部落盘（故事线 + 证据 + 术语 + 03 页结构 + 04 PPT 事实稿）')},
     'v4 已全部落盘'),
    ('往 P6 塞白名单外英文 Terminal Bench',
     lambda T: {**T, PPT: T[PPT].replace('### P6 · 这一圈到底在调什么', '### P6 · 这一圈到底在调什么\n\n- Terminal Bench 上排名第一')},
     'Terminal Bench'),
    ('把 P14 的一个 ** 删掉',
     lambda T: {**T, PPT: T[PPT].replace('**这一页回答的是“搭多厚”', '这一页回答的是“搭多厚”', 1)},
     'P14'),
    ('把 P15 的 [必上] 分界句删掉',
     lambda T: {**T, PPT: T[PPT].replace('  - **档 1 和档 2 的分界**：**步骤是不是你事先定好的**——没定，就是第 1 档\n', '', 1)},
     '档1档2分界'),
    ('把 P5 页脚署名去掉',
     lambda T: {**T, PPT: T[PPT].replace('Trivedy, 2026 ｜ 原文出处 ｜ 页码 5', '页码 5')},
     'P5'),
    ('把 harness 写进 P9',
     lambda T: {**T, PPT: T[PPT].replace('### P9 · ② 让它懂你的业务', '### P9 · ② 让它懂你的业务（harness）')},
     'harness'),
    ('往 P3 塞阿拉伯数字 30 天',
     lambda T: {**T, PPT: T[PPT].replace('给客户的资料／周报／报价单／对外回复', '给客户的资料／周报／报价单 30 天／对外回复')},
     '阿拉伯数字'),
]

def run_all():
    check_structure(); check_render_safety(); check_facts()
    check_stale_terms(); check_counts(); check_upstream(); check_redlines()

def run_selftest():
    global TXT, problems
    orig = dict(TXT)
    ok = fail = 0
    fails = []
    for desc, mutate, expect in SELFTEST_CASES:
        TXT = mutate(orig)
        problems = []
        NOTES.clear()
        run_all()
        joined = '\n'.join(f'{a} {b} {c}' for a, b, c in problems)
        if expect in joined:
            ok += 1
            print(f'  ✓ {desc} → 已抓到「{expect}」')
        else:
            fail += 1
            fails.append((desc, expect))
            print(f'  ✗ {desc} → 没抓到「{expect}」（假绿）')
    TXT = orig
    problems = []
    NOTES.clear()
    for desc, expect in fails:
        rep('严重', '自测', f'selftest 抓不到：{desc}（期望「{expect}」）——假绿')
    print(f'  selftest：{ok} 过 / {fail} 假绿')

def main():
    global problems
    if '--selftest' in sys.argv:
        print('【--selftest：负样本验证（门禁必须能证明自己会报警）】')
        run_selftest()
        print('\n【常规检查（真实文件）】')
        problems = []
        NOTES.clear()
        run_all()
    else:
        run_all()
    if NOTES:
        print('\n【备注 · 可能漏列的 FACT（不影响退出码，逐条人工判断）】')
        for n_ in NOTES:
            print(f'  ? {n_}')
    order = {'严重': 0, '重要': 1, '小': 2}
    problems.sort(key=lambda x: (order.get(x[0], 9), x[1]))
    if not problems:
        print('✓ 全部通过（结构 / 渲染安全 / 跨文件事实 / 上游同步 / 红线）')
        return 0
    cur = None
    for sev, axis, msg in problems:
        key = (sev, axis)
        if key != cur:
            print(f'\n【{sev} · {axis}】')
            cur = key
        print(f'  - {msg}')
    n = {s: sum(1 for p in problems if p[0] == s) for s in ('严重', '重要', '小')}
    print(f"\n合计：严重 {n['严重']} / 重要 {n['重要']} / 小 {n['小']}")
    return 1

if __name__ == '__main__':
    sys.exit(main())
