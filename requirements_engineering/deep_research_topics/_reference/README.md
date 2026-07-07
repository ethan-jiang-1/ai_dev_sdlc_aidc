# _reference/ — 本轮 Deep Research 的权威副本层（Authoritative Copy Layer）

> 本目录只承载**证据本体**（`evidence body`），不承载执行状态、综合判断或导航文字。
> 综合判断落 [`../_artifacts/`](../_artifacts/)；执行状态落 [`../../plan/dr-round-1.status.md`](../../plan/dr-round-1.status.md)；连续动作落 [`../../plan/dr-round-1.queue.md`](../../plan/dr-round-1.queue.md)。

## 定位

- 每个值得进入后续推理链条的来源，都应在此目录落一份 **Authoritative Copy**（独立 `md` 文档）。
- 完成单位不是"看过这个链接"，而是"这份链接已经被整理成可复用、可定位、可引用、可自给自足的独立 `md` 文档"。
- 下一位 agent 或研究者只读本地 `md`，就应能在不回 URL 的前提下继续推理。

## 命名约定

- 共享地基（跨多个研究线）：`00-shared-<source-slug>.md`
- 研究线专属：`<NN>-<topic-slug>-<source-slug>.md`，其中 `<NN>` 与 `<topic-slug>` 来自 [`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md) 的 **研究线注册表（topic registry）**
  - `01` re-landscape
  - `02` user-story
  - `03` ears
  - `04` future-trends
  - `05` integration-bdd
  - `06` agent-format

`<source-slug>` 使用 kebab-case，避免空格、特殊字符、版本号堆叠；必要时追加年份后缀（如 `mavin-2009-ears-re09`）。

## 必须字段

每份 Authoritative Copy 顶部建议包含：

```md
# 标题

- source_url:
- source_type:        # official / standard / academic / practitioner / community
- accessed_at:        # ISO-8601，精确到日
- related_topic:      # topic id + slug 列表
- trust_level:        # official / academic / practitioner / community
- tier:               # A / B / C / D / E / F（见 plan 的 Source Tier Policy）
- why_it_matters:     # 为什么这份材料进入本轮推理链
- captured_excerpt:   # yes / partial / no
- claims_supported:   # 本份可支撑哪些断言
- date_scope:         # 原文时间覆盖范围
- related_entities:   # 人物 / 工具 / 标准 / 机构
```

下方固定章节：

- `## 关键事实`
- `## 核心内容摘录`
- `## 与本研究的关系`
- `## 可直接引用的术语 / 概念`
- `## 风险与局限`

## 30 秒本地证据检索入口

导航层是 [`_INDEX.md`](_INDEX.md)；任何新增 / 删除 / 重命名的 Authoritative Copy 都必须同步刷新它。

## 入库判断硬标准（任一条满足即可，不满足一律不入库）

- 能补充新事实
- 能澄清机制差异
- 能提供一手或高可信二手证据
- 能帮助解释趋势、难点或争议

## 与 claims-audit 的联动

- `tier = D / E / F` 的材料只作为"某方自述 / 趋势信号 / 行业叙事"保留，不得作为效果证据。
- 所有对 [`../claims-audit.md`](../claims-audit.md) 中 10 条高流量断言的重评，最终在 Wave 2 产出 `../_artifacts/W2-claims-audit-v2.md`。
