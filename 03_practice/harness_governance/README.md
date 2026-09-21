# Harness / Context Governance —— AI 形态下新的 SDLC

> **定位（2026-09-21 用户定）**：本主题不是"SDD 的后继形态之一"，而是升格后的独立实践主题：
> **AI 形态下新的 SDLC（DSLC）主干**——治理对象从 spec 文档转向 **agent 执行链路**
> （harness + 上下文 + 规则文件 + 门禁 + 执行记录）。
>
> **来源**：自 [`../beyond_spec_driven_development/`](../beyond_spec_driven_development/README.md)
> 抽出其重点路线 context engineering 与 harness 治理（独立后编号 01、02）及其全部证据档案与图形。
> 升格理由：**SDD 会漂移/腐化**，spec 不是写完就稳的资产，靠原教旨 SDD 是有问题的——
> 必须有一套**持续清理、打扫卫生**的治理机制。这套机制本身值得独立成题推敲，
> 独立目录也让每次推敲的上下文装载量最小（渐进式披露）。

## 分篇与证据档案（文件名已按新主题重编号：旧 02→现 01、旧 03→现 02；摘录正文与来源未动，档案 H1 下新增编号说明引注）

**原主题内编号 → 现文件名映射**（口径说明：01a/01b「03a」、02a「04a」为档案正文 H1 自称；02/03/02c/04b 一行为 git 拆分前文件名号——深挖主文 H1 另有"深挖二/三/四"自称但不带号。git 拆分前完整文件名清单见 f598fa7^）：

| 旧编号（原 beyond 单主题内） | 新文件名 |
|---|---|
| 02（context 派深挖） | `01-context-engineering.md` |
| 03（harness 治理派深挖） | `02-harness-governance.md` |
| 03a（渐进披露证据） | `01a-progressive-disclosure-evidence.md` |
| 03a（AGENTS.md 治理证据） | `01b-agents-md-governance-evidence.md` |
| 02c（context vs harness 判定） | `01c-context-vs-harness.md` |
| 04a（收敛证据档案） | `02a-harness-convergence-evidence.md` |
| 04b（学术与度量） | `02b-harness-academic-and-metrics.md` |

> 档案正文内部遗留旧编号（自称 03a/04a 等）以各档案 H1 下引注与本映射表为准；摘录正文与来源未动，仅 H1 引注为新增。

| 文件 | 内容 |
|---|---|
| [01-context-engineering.md](01-context-engineering.md) | 01 Context engineering 派深挖：repo 级规则文件纪律，不建 feature 级工件 |
| [02-harness-governance.md](02-harness-governance.md) | ★ 02 Harness 治理派深挖：治理对象转向 agent 执行链路——团队级收敛点 |
| [01a-progressive-disclosure-evidence.md](01a-progressive-disclosure-evidence.md) | 01 证据：渐进披露 B1–B9（官方预算表 + 五 repo 实测）（档案内自称 03a 为旧编号） |
| [01b-agents-md-governance-evidence.md](01b-agents-md-governance-evidence.md) | 01 证据：AGENTS.md 治理 A/B/C/D（大厂范式 + git 史 + 度量勘误）（档案内自称 03a 为旧编号） |
| [01c-context-vs-harness.md](01c-context-vs-harness.md) | 关系判定：**context ⊂ harness**（静态层 / 动态层） |
| [02a-harness-convergence-evidence.md](02a-harness-convergence-evidence.md) | 02 证据：10 集群 78 处原文摘录 + 引用链核验（档案内自称 04a 为旧编号） |
| [02b-harness-academic-and-metrics.md](02b-harness-academic-and-metrics.md) | 02 证据：学术三篇回源 + 度量缺口论证 |

图形（`figures/`）：`01a-progressive-disclosure-layers.svg`（渐进披露三层）、
`01c-context-inside-harness.svg`（context ⊂ harness）、`02-harness-convergence-map.svg`（五层位收敛地图）。

## 核心论点（继承自原主题，正文以分篇为权威）

1. **context ⊂ harness**：context engineering 是 harness engineering 的一个静态/信息层，
   不是并列范式（判定见 `01c-context-vs-harness.md`；该二分为 01c 本文归纳，尚无第三方独立复核，与 01c §5「局限与开放问题」口径一致）。
2. **治理重心从"写对 spec"移到"工程化执行环境"**：linter / 结构测试 / 可观测性接入运行时 /
   gardener agent 定期扫漂移 / "每次犯错就工程化消灭该错误类别"（详见 `02-harness-governance.md`）。
3. **漂移与腐化是常态而非事故**：spec、规则文件、上下文都会随代码演进腐化，
   DSLC 的日常就包含对它们的持续清理——这也是本主题独立于 SDD 的立论根基。

## 分工与指针（单一事实来源）

- **SDD 工具层实践**（SDD 是什么、工具有哪些、辩论）→ [`../spec_driven_development/`](../spec_driven_development/README.md)
- **SDD 批判与剩余后继形态光谱**（验证优先 / plan mode / 测试优先 + 历史判断层）→
  [`../beyond_spec_driven_development/README.md`](../beyond_spec_driven_development/README.md)
  （本主题的"问题从哪来"与光谱定位记录在该处，冲突时**本目录分篇为权威**）
- **需求表达格式** → [`../requirements_engineering/`](../requirements_engineering/README.md)

## 纪律

与 `03_practice/` 各主题统一：一手源优先、来源可溯、标注观测日期；
每条断言 URL + 日期，直引逐字，半回源降级标注（分篇内已执行的口径不变）。

```yaml
topic: Harness / Context Governance（AI 形态下新的 SDLC）
created_at: 2026-09-21  # 自 beyond_spec_driven_development 抽出升格，用户定
scope: agent 执行链路治理：harness、context、规则文件纪律、门禁、漂移清理
related:
  - ../beyond_spec_driven_development/README.md   # 光谱定位与"问题从哪来"（批判面）
  - ../spec_driven_development/README.md          # SDD 工具层（被批判与被治理的对象侧）
```
