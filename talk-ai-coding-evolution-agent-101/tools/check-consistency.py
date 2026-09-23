#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""agent-101 跨文件一致性检查器

为什么存在：这套文案里**同一个事实散在 6 个文件**里（上屏文案 / 手册页版 / 长版讲义 /
CONTEXT / 03 页结构 / storyline）。六轮独立复核里反复出现的病都是同一个——
"改了 04 没同步上游""改了页版没同步长版"。**人眼同步不可靠**，所以把同步判定交给脚本。

它判四类：
  A 结构不变量   页块数 / 页间恰好一条 --- / 页版每页恰好一条 [必上] / 方括号只放优先级记号 /
                 最大字号白名单 / 字段表与正文互覆盖 / 03 白名单 ⊇ 04 字段 / 页脚署名只 P4·P5
  B 渲染安全     对客件 ASCII 引号 = 0 / 无四星号 / ** 偶数 / HTML 注释配对 / 表格列数
  C 跨文件事实   每条共享事实的固定说法必须在指定文件里出现；旧写法不许在别处出现
  D 上游同步     04 的每一页在 03 页表里都要有对应行

跑法（在哪个目录下跑都一样，路径按脚本自身位置推导）：
    python3 talk-ai-coding-evolution-agent-101/tools/check-consistency.py
退出码：0 = 全过；1 = 有严重或重要问题（便于提交前手跑或接进 CI）

维护须知：**新增一条共享事实时，同步在 FACTS（或 STALE_TERMS / COUNTS）里加一行**——
检查项漏了，比漏改一处更危险，因为它会给出虚假的"全绿"。
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))   # <仓库>/talk-ai-coding-evolution-agent-101/tools
TALK = os.path.dirname(HERE)                       # <仓库>/talk-ai-coding-evolution-agent-101
# 本脚本按自身位置推导路径，所以在哪个工作目录下跑都一样
_ = HERE

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
RENDER = [PPT, PAGE]           # 渲染件
CUSTOMER = [PPT, PAGE, LONG]   # 对客件

def read(rel):
    with open(os.path.join(TALK, rel), encoding='utf-8') as f:
        return f.read()

TXT = {f: read(f) for f in ALL}

problems = []      # (严重度, 轴, 说明)
def rep(sev, axis, msg):
    problems.append((sev, axis, msg))

# ─────────────────────────────────────────────────────────
# A. 结构不变量
# ─────────────────────────────────────────────────────────
def blocks(t):
    """返回 [(页块号, 起始行, 块文本)] 与分割线行号"""
    lines = t.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('### ')]
    seps = [i for i, l in enumerate(lines) if l.strip() == '---']
    out = []
    for n, i in enumerate(idx):
        end = idx[n + 1] if n + 1 < len(idx) else len(lines)
        out.append((lines[i].split()[1], i, '\n'.join(lines[i:end])))
    return out, seps, lines

def check_structure():
    for rel, want in ((PPT, 21), (PAGE, 20)):
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

    # 页版：每页恰好一条 [必上]
    bl, _, _ = blocks(TXT[PAGE])
    for pid, _, b in bl:
        n = len(re.findall(r'\[必上\]', b))
        if n != 1:
            rep('严重', '结构', f'页版 {pid}: [必上] 有 {n} 条，应恰好 1 条')

    # 渲染件：方括号里只放优先级记号
    # 注：只查对客件——CONTEXT 是工作文档，正文里本来就要**引用**这些记号与反例（如 `> [!XXX]`）
    ok = {'必上', '可选', '例', '必给', 'INTERFACE', 'INTERFACE · 不上屏', '不上屏'}
    for rel in RENDER + [LONG]:
        bad = set()
        for m in re.finditer(r'\[([^\]\n]*)\]', TXT[rel]):
            if m.group(1).strip() in ('', 'x', 'X'):
                continue          # markdown 复选框
            if m.group(1) not in ok:
                bad.add(m.group(1))
        if bad:
            rep('重要', '结构', f'{rel}: 方括号里出现非优先级记号 {sorted(bad)}')

    # ppt-text 头部自称"只有三个记号"
    head = TXT[PPT].split('### P1 ')[0]
    if '本件只有这三个' in head:
        used = {x for x in ('必上', '可选', '例', '必给') if f'[{x}]' in TXT[PPT].split('### P1 ')[1]}
        if used != {'必上', '可选', '例'}:
            rep('严重', '结构', f'{PPT}: 头部称只有三个记号，实际用到 {sorted(used)}')

    # 最大字号白名单
    allow = {'P5', 'P12', 'P14', 'P15'}
    bl, _, _ = blocks(TXT[PPT])
    for pid, _, b in bl:
        if '（大字）' in b and pid not in allow:
            rep('重要', '结构', f'{PPT} {pid}: 用了（大字），但白名单只给 {sorted(allow)}')
    if not re.search(r'最大字号只给', TXT[OUT]):
        rep('小', '结构', f'{OUT}: 没找到"最大字号"白名单的规约')

    # 字段表 ↔ 正文 互覆盖
    def fields(t):
        out = set()
        for m in re.finditer(r'^- \*\*(.+?)\*\*(（[^）]*）)?[：]', t, flags=re.M):
            out.add(re.sub(r' \[[^\]]+\]', '', m.group(1)).strip())
        return out
    def declared(t):
        # 头部（第一个页块之前）里所有表格行中的反引号词元，都是声明过的字段/记号
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

    # 03 白名单 ⊇ 04 实际字段
    m = re.search(r'04（演讲）只允许出现：`(.+?)`', TXT[OUT])
    if m:
        wl = {x.strip() for x in m.group(1).split('／')}
        missing = {re.sub(r'（[^）]*）$', '', x).strip() for x in fields(TXT[PPT])} - wl
        if missing:
            rep('严重', '结构', f'{OUT}: 白名单漏了 04 实际字段 {sorted(missing)}')

    # 页脚：只有 P4/P5 带署名
    for pid, _, b in blocks(TXT[PPT])[0]:
        if re.search(r'L4 页脚', b) and pid not in ('P4', 'P5') and re.search(r'\d{4}', b):
            rep('小', '结构', f'{PPT} {pid}: 页脚出现年份（署名只允许 P4/P5）')

    # 必给那一句必须带 [必上]
    for k in ('结论句', '落点', '命名', '附带', '脚注'):
        tot = len(re.findall(rf'^- \*\*{k}', TXT[PPT], flags=re.M))
        tagged = len(re.findall(rf'^- \*\*{k} \[必上\]', TXT[PPT], flags=re.M))
        if tot != tagged:
            rep('严重', '结构', f'{PPT}: 「{k}」{tagged}/{tot} 带 [必上]')

# ─────────────────────────────────────────────────────────
# B. 渲染安全
# ─────────────────────────────────────────────────────────
def check_render_safety():
    for rel in CUSTOMER:
        t = TXT[rel]
        if t.count('"'):
            rep('严重', '渲染安全', f'{rel}: ASCII 双引号 {t.count(chr(34))} 个（对客件必须为 0）')
        if '****' in t:
            rep('严重', '渲染安全', f'{rel}: 出现四个星号（嵌套加粗写错）')
        stripped = re.sub(r'`[^`]*`', '', t)
        if stripped.count('**') % 2:
            rep('严重', '渲染安全', f'{rel}: ** 计数为奇数（有未闭合的加粗）')
        if t.count('<!--') != t.count('-->'):
            rep('严重', '渲染安全', f'{rel}: HTML 注释不配对')
        # 表格列数一致（按连续的表格块分组，别把不同表当一个）
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

# ─────────────────────────────────────────────────────────
# C. 跨文件事实一致性  —— 这一节是重点
# ─────────────────────────────────────────────────────────
# canon = 固定说法；must = 必须出现该说法的文件；stale = 旧写法（同一事实）
FACTS = [
    dict(name='核心命题', canon='Agent = Model + Harness',
         must=[PPT, CTX, OUT, STORY, TREAD]),
    dict(name='判据', canon='错了赔得起吗？错了多久能发现？',
         must=[PPT, CTX], halves=['错了赔得起吗？', '错了多久能发现？'],
         halves_must=[PAGE, LONG]),
    dict(name='厚薄＝加几道关', canon='几道关',
         must=[PPT, PAGE, LONG, CTX, OUT, STORY]),
    dict(name='档1上屏名', canon='你问一句，它答一句', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='档2上屏名', canon='你定好步骤，它照着走', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='档3上屏名', canon='你给个目标，它自己跑', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='档4上屏名', canon='你定好分工，它们自己配合', must=[PPT, PAGE, LONG, CTX, STORY]),
    dict(name='四档第二问', canon='是一条路，还是几条线',
         must=[PPT, PAGE, LONG, CTX, STORY],
         stale=['是一条路还是几条线', '是一条路走到底', '同时有几个在跑']),
    dict(name='命名规则', canon='下一步由你定，叫「工作流」；下一步由它定，叫「智能体」',
         must=[PPT, STORY]),
    dict(name='命名不派四档', canon='只定这两个名字', must=[CTX]),
    dict(name='挑活判断力', canon='判得出对错', must=[PPT, PAGE, LONG, CTX]),
    dict(name='挑活阈值', canon='既别拿它练', must=[CTX],
         alt=['也别让它自己跑', '也别交给它自己跑']),
    dict(name='维护闸门', canon='谁维护它？它坏了谁发现',
         must=[PPT, PAGE, LONG, STORY]),
    dict(name='答不上来先别搭', canon='答不上来，先别搭', must=[PPT, PAGE, LONG, STORY]),
    dict(name='政策未定那条', canon='都还没定的事', must=[PPT, PAGE, LONG, STORY]),
    # 两种场合两种词（已登记在 CONTEXT §三）：循环里叫「补」，劝人别加时说「加」
    dict(name='一次只动一样（循环）', canon='一次只补一条', must=[PAGE, LONG]),
    dict(name='一次只动一样（劝人别加）', canon='一次只加一条', must=[PPT]),
    dict(name='加之前先减', canon='加之前', must=[PPT, PAGE, LONG]),
    dict(name='先跑最简单的', canon='先跑最简单的', must=[PPT, LONG, STORY]),
    # 提醒里说"少一样就越危险"；演讲件的对应落点是 P16 的"那三样也一个不能少"，
    # 所以 ppt-text 不再要求这一句（原句与 P15 落点重复、且"少一样"在 P15 无先行词）
    dict(name='越往下越危险', canon='少一样就越危险', must=[PAGE, LONG]),
    dict(name='档1没有独立检查', canon='第 1 档你自己就是那一圈', must=[PPT, PAGE, LONG]),
    dict(name='政策未定闸门', canon='政策还没定', must=[CTX],
         alt=['政策已经定了'], alt_must=[PPT, PAGE, LONG]),
    dict(name='五格↔五件事映射', canon='就是那五件事', must=[PAGE, LONG, CTX]),
    dict(name='留痕释义', canon='事后查得到它每一步做了什么', must=[PPT, CTX]),
    dict(name='代码释义', canon='每次都一样', must=[PPT, PAGE, LONG, CTX]),
    dict(name='合规问谁', canon='管技术的或管合规的同事', must=[PAGE, LONG],
         stale=['IT']),
    dict(name='症状④说法', canon='兜圈子', must=[PPT, PAGE, LONG, STORY, TREAD],
         stale=['绕圈'], stale_allow=[CTX, NARR, TCUR, STORY]),
    dict(name='不是渲染输入', canon='不是渲染输入', must=[STORY]),
]

def check_facts():
    for f in FACTS:
        name, canon, must = f['name'], f['canon'], f['must']
        for rel in must:
            if canon not in TXT[rel]:
                rep('严重', '一致性', f'「{name}」的固定说法「{canon}」在 {rel} 里没有')
        for a in f.get('alt', []):
            for rel in f.get('alt_must', []):
                if a not in TXT[rel]:
                    rep('重要', '一致性', f'「{name}」的等价说法「{a}」在 {rel} 里没有')
        for h in f.get('halves', []):
            for rel in f.get('halves_must', []):
                if h not in TXT[rel]:
                    rep('重要', '一致性', f'「{name}」的半句「{h}」在 {rel} 里没有')
        for s in f.get('stale', []):
            allow = set(f.get('stale_allow', []))
            for rel in ALL:
                if rel in allow:
                    continue
                # 旧措辞出现在"改名/旧写法"记录块里属有意保留
                if re.search(r'旧写法|旧口径|原文|——\*\*' + re.escape(s), TXT[rel]):
                    continue
                if s in TXT[rel]:
                    rep('重要', '一致性',
                        f'「{name}」出现旧写法「{s}」（{rel}）——固定说法是「{canon}」')

# ─────────────────────────────────────────────────────────
# D. 上游同步：04 里新增/改动的事实，上游有没有落点
# ─────────────────────────────────────────────────────────
def check_upstream():
    # 04 的每个页块，在 03 的页表里都该有对应行
    bl, _, _ = blocks(TXT[PPT])
    for pid, _, _ in bl:
        if not re.search(rf'\*\*{pid}\*\*', TXT[OUT]):
            rep('重要', '系统', f'{OUT} 里没有 {pid} 的行（04 有这一页）')
    bl2, _, _ = blocks(TXT[PAGE])
    head2 = '\n'.join(TXT[PAGE].split('\n')[:45])
    for pid in (bl2[0][0], bl2[-1][0]):
        if pid not in head2:
            rep('小', '系统', f'{PAGE}: 头部切页说明里没提到 {pid}')


# 已废弃的说法 / 旧口径：全目录不该再出现（白名单里的是"记录旧写法"的区块）
STALE_TERMS = [
    ('不写代码',       '旧听众口径（v24 已换成"技术一般＋已经在搭 Agent"）'),
    ('文职岗',         '旧听众口径'),
    ('零术语版',       'v6 已改为"术语按序入场"'),
    ('同时有几个在跑', '四档第二问的旧写法'),
    ('两个问题定档',   '四档的派生说法（v26 已废）'),
    ('四档全部由它派生','四档的派生说法（v26 已废）'),
    ('循环往复',       'AI 腔／书面腔'),
    ('缺的是这五件',   '旧句式'),
    ('20 分钟能过一遍','对客件的阿拉伯数字'),
    ('v4 已落盘',      '过期状态'),
]
STALE_ALLOW = [CTX, NARR, TCUR, STORY]     # 工作文档里允许"记录旧写法"

def check_stale_terms():
    for term, why in STALE_TERMS:
        for rel in ALL:
            if rel in STALE_ALLOW:
                continue
            if term in TXT[rel]:
                rep('重要', '一致性', f'{rel}: 出现已废弃说法「{term}」（{why}）')

# 计数事实：三处以上必须一致
# 同一事实的若干可接受写法（检查的是"事实在不在"，不是"字面一样不一样"）
COUNTS = [
    ('正文 19 页 / 19 页正文 / 19 正文',      [CTX, OUT, STORY, TREAD]),
    ('21 张',                                 [CTX, OUT, STORY, TREAD, TCUR]),
    ('2 张停顿页 / 2 停顿页 / 2 停顿',         [CTX, OUT, STORY, TREAD]),
    ('27.5 / 27.0',                           [OUT, STORY]),
    ('28.2 / 27.7',                           [OUT, STORY]),
]
def check_counts():
    for spec, must in COUNTS:
        alts = [x.strip() for x in spec.split('/')]
        for rel in must:
            if not any(a in TXT[rel] for a in alts):
                rep('小', '一致性', f'计数事实「{alts[0]}」在 {rel} 里没有')

# ─────────────────────────────────────────────────────────
def main():
    check_structure()
    check_render_safety()
    check_facts()
    check_stale_terms()
    check_counts()
    check_upstream()
    order = {'严重': 0, '重要': 1, '小': 2}
    problems.sort(key=lambda x: (order.get(x[0], 9), x[1]))
    if not problems:
        print('✓ 全部通过（结构 / 渲染安全 / 跨文件一致性 / 上游同步）')
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
    return 1 if n['严重'] or n['重要'] else 0

if __name__ == '__main__':
    sys.exit(main())
