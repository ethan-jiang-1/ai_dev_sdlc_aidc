---
type: index
content_type: readme
directory: 01_seed_reference/loop_engineering/02_neutral
description: 中性派（边界与审慎）——loop engineering 一波声音的素材索引
reorg_date: 2026-10-06
---

# 02_neutral — 中性派（边界与审慎）

> **派别判定权威在** [`02_research/.../raw/kol-roster.md` §A2 三派分野](../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)——
> 本 README 只做**素材索引**。本派深扫档案：[`raw_scan_2026-10-06_neutral.md`](raw_scan_2026-10-06_neutral.md)（2026-10-06 批，9 条 Source＋10 条负结论）。

**判定口径（一句话）**：承认循环机制真实存在且在特定条件下有效，但**划定适用边界**（什么任务、什么约束形态、人站哪里）、
或以审慎实证立场发声（先测再信、记录两面）——既不把它当默认推荐，也不整体否定。

**与另外两派的分界**：中性派说"**有条件成立**"；推动派说"**默认方向**"；反对派说"**反证在此**"。
同一人可能随时间移派（如 Steinberger 2025-12 反对 → 2026-06 词源；swyx 2026-10-06 实测后移入推动派）——派别记录以当前一手表态为准，轨迹在台账不抹平。

## 素材索引

| 人物 | 派内角色 | 台账位置 | 素材在哪 |
|---|---|---|---|
| **Gergely Orosz**（Pragmatic Engineer） | 一线记录者·**调查式怀疑**（07-14 专刊《What is "loop engineering?"》：cron 旧物判定、tokenmaxxing、"Was looping a hack?"；同时如实收录有效案例） | §A（2026-10-06 升格） | 人物卡 [`_raw_people/12`](../../voices/_raw_people/12_gergely_orosz.md) ＋ [反对派扫描档 S7/S8/S9](../03_skeptics/raw_scan_2026-10-06_skeptics.md)（⚠️ 引文纠偏："something **valuable** is being taken away"，非 "precious"） |
| **Simon Willison** | 循环实践者＋风险警告（**偏怀疑**：2026-09-24 "make software engineering **even harder**… requires extraordinary discipline and knowledge"；10-03 "hard budget caps need to be the default"） | §C1（窗口内无本词专门发声，负结论复证） | 人物卡 [`_raw_people/04`](../../voices/_raw_people/04_simon_willison.md) ＋ [evidence-i Source 4](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-27-i-high-influence-control.md) ＋ [反对派扫描档 S5/S6](../03_skeptics/raw_scan_2026-10-06_skeptics.md) |
| **Birgitta Böckeler**（Thoughtworks） | **审慎实证（最强中性样本）**：2026-08-10 自跑 eval 证伪"循环内 TDD 有益"默认信条（TDD 组 token 3–8.5x；"until I see evals"）；SE Radio 730 裸基线先行 | §B（窗口前）＋窗口内增量 | [本派扫描档 S1/S2](raw_scan_2026-10-06_neutral.md) ＋ [evidence-c](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-c-autonomy-and-convergence.md) ＋ [`_raw_orgs/thoughtworks`](../../voices/_raw_orgs/thoughtworks.md) ＋ [`_raw_people/20`](../../voices/_raw_people/20_birgitta_bockeler.md) |
| **Kief Morris**（Thoughtworks） | 阶梯／**渐进信任**（PlatformCon 2026-06-23 官方关键句 "As feedback loops tighten across the full cycle, teams progressively trust agents with more"） | §B（窗口前）＋窗口内增量 | [本派扫描档 S3](raw_scan_2026-10-06_neutral.md) ＋ [evidence-c](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-c-autonomy-and-convergence.md) ＋ [`_raw_people/10`](../../voices/_raw_people/10_kief_morris.md) |
| **Kent C. Dodds**（⚠️ **不是 Kent Beck**） | 受约束循环画像（强票）："the human does still need to be in the loop"、"trading compute for attention"、"use loop engineering judiciously" | §A（2026-10-06 新入册） | [本派扫描档 S6](raw_scan_2026-10-06_neutral.md)（2026-06-23 播客 transcript） |
| **Mitchell Hashimoto** | 皈依派限速（窗口前谱系）："excruciating" 双轨训练法；明确不跑通宵循环/多 agent；junior 技能塌陷 "deeply worries me" | 谱系登记（不入 §A，2026-02-05 窗口前） | [反对派扫描档 S11](../03_skeptics/raw_scan_2026-10-06_skeptics.md)《My AI Adoption Journey》 |
| **Kent Beck** | 节拍论；**窗口内沉默**；2026-02 与 Tacho/Yegge 联署 "We remain skeptical… and we remain human" | §B（窗口前） | [evidence-i Source 3](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-27-i-high-influence-control.md) ＋ [反对派扫描档 S9](../03_skeptics/raw_scan_2026-10-06_skeptics.md)（联署宣言经 Orosz 一手报道） |
| **marmelab**（Zaninotto） | 审慎实证（偏怀疑）："SDD adds little benefit"；增量："would be irresponsible in a low-throughput environment"、"Atomic CRM still requires a human review for every PR" | §B（窗口前） | [evidence-c](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-c-autonomy-and-convergence.md) ＋ [本派扫描档 S8](raw_scan_2026-10-06_neutral.md) |
| **Walden Yan**（Cognition） | 受约束形态（**中性票不足**——厂商利益）；⚠️ "your codebase regressing to your worst engineer" 系 swyx 编辑摘要语，**不得入 Walden 引句** | §B（窗口前） | [evidence-u Source 2](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-30-u-post-june-kols.md) ＋ [本派扫描档 S9](raw_scan_2026-10-06_neutral.md)（窗口内无新专门一手文，负结论） |
| ~~swyx~~ | ~~概念邻近~~ → **2026-10-06 移入推动派**（loopcraft 实测偏推动，见 [`../01_advocates/`](../01_advocates/README.md)） | §A | [本派扫描档 S5](raw_scan_2026-10-06_neutral.md)（收口记录） |

> 本派当前**无四件套卡**——建卡规则（独立一手长文 ≥3 份）不变，见 [上级 README](../README.md)。
> 灰色文献边缘票（不入册、供判读）：arXiv:2607.00038（"spectrum of autonomy"、"cognitive surrender"）；Thoughtworks《An Accidental Blackboard》（emergent 团队实证）——见扫描档 S7 与负结论 #8。
