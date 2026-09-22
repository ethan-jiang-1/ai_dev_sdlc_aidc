# Harness / Context Governance —— AI 形态下新的 SDLC

> **定位（2026-09-21 用户定）**：本主题不是"SDD 的后继形态之一"，而是升格后的独立实践主题：
> **AI 形态下新的 SDLC（DSLC）主干**——治理对象从 spec 文档转向 **agent 执行链路**
> （harness + 上下文 + 规则文件 + 门禁 + 执行记录）。
>
> **来源**：自 [`../beyond_spec_driven_development/`](../beyond_spec_driven_development/README.md)
> 抽出其重点路线 context engineering 与 harness 治理（现 `research/` 编号 01、02）及其全部证据档案与图形。
> 升格理由：**SDD 会漂移/腐化**，spec 不是写完就稳的资产，靠原教旨 SDD 是有问题的——
> 必须有一套**持续清理、打扫卫生**的治理机制。这套机制本身值得独立成题推敲，
> 独立目录也让每次推敲的上下文装载量最小（渐进式披露）。

## 信息流与目录结构（2026-09-21 主干定稿升格；同日定稿层更名 result/、文件去序号）

**信息流三规则**：

1. **单向加工**：`research/` 证据档案 → `research/` 分篇判读 → `result/` 定稿；review 改变定稿 → 反向同步分篇。
2. **result/ 只收过筛结论**（判据见 [`result/backbone.md`](result/backbone.md) §0）；未采纳线索留 `research/` 原位（防重复检索），不删不隔离。
3. **过程件不入流**：仓库根 `.tmp-*` 不入库、不进任何一层，版本收口即清理。

```text
harness_governance/
├── README.md / CURRENT.md     # 入口件（地图 / 热区）
├── research/                  # 调研层：8 件（判读 ×2、证据档案 ×4、关系判定 ×1）+ figures/（编号 = 封存的历史序列）
└── result/                    # 定稿层：backbone（主干总纲）+ manual（操作规程）+ 层 README（语义命名，无序号）
```

## 分篇表

### research/ 层（证据与判读——证据权威）

| 文件 | 类型 | 内容 |
|---|---|---|
| [`research/01-context-engineering.md`](research/01-context-engineering.md) | 判读 | Context engineering 派深挖：repo 级上下文纪律，不建 feature 级工件 |
| [`research/01a-progressive-disclosure-evidence.md`](research/01a-progressive-disclosure-evidence.md) | 档案 | 渐进披露 B1–B9（官方预算表 + 五 repo 实测） |
| [`research/01b-agents-md-governance-evidence.md`](research/01b-agents-md-governance-evidence.md) | 档案 | AGENTS.md 治理 A/B/C/D（大厂范式 + git 史 + 度量勘误） |
| [`research/01c-context-vs-harness.md`](research/01c-context-vs-harness.md) | 判定 | **context ⊂ harness**（静态层 / 动态层） |
| [`research/02-harness-governance.md`](research/02-harness-governance.md) | 判读 | Harness 治理派深挖：治理对象转向 agent 执行链路 |
| [`research/02a-harness-convergence-evidence.md`](research/02a-harness-convergence-evidence.md) | 档案 | 收敛证据：10 集群原文摘录 + 引用链核验 |
| [`research/02b-harness-academic-and-metrics.md`](research/02b-harness-academic-and-metrics.md) | 档案 | 学术三篇回源 + 度量缺口论证 |

图形在 [`research/figures/`](research/figures/)：渐进披露三层（01a）、context ⊂ harness（01c）、五层位收敛地图（02）。

### result/ 层（定稿——主张权威）

| 文件 | 内容 | 状态 |
|---|---|---|
| [`result/backbone.md`](result/backbone.md) | ★ 实践主干总纲：宪法 3 / 工件 8 / 回路 7 / 节奏 3 / 组织与边界 7 + 筛选判据 + 七缺口诊断轴 | 五段全部经用户确认（2026-09-21，含四处实战修订） |
| [`result/manual.md`](result/manual.md) | 手册级操作规程（十二条：Phase 0 四问表 / 棘轮 SOP / 入口模板 / 统一 P0→P4 梯子 / 反过度工程清单） | 经用户确认（2026-09-21） |

## 核心论点（继承自已往轮次；操作化见 result/backbone）

1. **context ⊂ harness**：context engineering 是 harness engineering 的一个静态/信息层，不是并列范式（判定见 `research/01c`；该二分为 01c 本文归纳，尚无第三方独立复核，与其 §5 口径一致）。
2. **治理重心从"写对 spec"移到"工程化执行环境"**：linter / 结构测试 / 可观测性接入运行时 / gardener agent 定期扫漂移 / "每次犯错就工程化消灭该错误类别"——五段操作化即 `result/backbone`。
3. **漂移与腐化是常态而非事故**：spec、规则文件、上下文都会随代码演进腐化，DSLC 的日常就包含对它们的持续清理——这也是本主题独立于 SDD 的立论根基。

## 旧编号映射（历史口径 + 指代消歧）

（口径说明：01a/01b「03a」、02a「04a」为档案正文 H1 自称；02/03/02c/04b 一行为 git 拆分前文件名号——深挖主文 H1 另有"深挖二/三/四"自称但不带号。git 拆分前完整文件名清单见 f598fa7^）

| 旧编号 / 旧文件名 | 现路径 |
|---|---|
| 02（context 派深挖） | `research/01-context-engineering.md` |
| 03（harness 治理派深挖） | `research/02-harness-governance.md` |
| 03a（渐进披露证据） | `research/01a-progressive-disclosure-evidence.md` |
| 03a（AGENTS.md 治理证据） | `research/01b-agents-md-governance-evidence.md` |
| 02c（context vs harness 判定） | `research/01c-context-vs-harness.md` |
| 04a（收敛证据档案） | `research/02a-harness-convergence-evidence.md` |
| 04b（学术与度量） | `research/02b-harness-academic-and-metrics.md` |
| final/03-practice-backbone.md（2026-09-21 升格落位名） | `result/backbone.md`（同日去序号更名） |
| final/04-practice-manual.md（2026-09-21 落位名） | `result/manual.md`（同日去序号更名） |

**指代消歧（2026-09-21 升格时定，同日 result 更名后更新）**：档案正文遗留的"03 文档 / 03 文 / 03 号文档"指代不一——`research/01a`、`research/01b` 文中指 `research/01`（context 判读），`research/02b` 文中指 `research/02`（harness 判读）；**均与 result/ 层无关**（result 层为语义命名 backbone / manual，无编号文件）。新写引用一律用"层前缀 + 名/号 + 节号"式（如 research/01 §2.2、result/manual §6）。

## 分工与指针（单一事实来源）

- **SDD 工具层实践**（SDD 是什么、工具有哪些、辩论）→ [`../spec_driven_development/`](../spec_driven_development/README.md)
- **SDD 批判与剩余后继形态光谱**（验证优先 / plan mode / 测试优先 + 历史判断层）→
  [`../beyond_spec_driven_development/README.md`](../beyond_spec_driven_development/README.md)
  （本主题的"问题从哪来"与光谱定位记录在该处，冲突时**本目录 result/ 主张层为权威**）
- **需求表达格式** → [`../requirements_engineering/`](../requirements_engineering/README.md)

## 纪律

与 `03_practice/` 各主题统一：一手源优先、来源可溯、标注观测日期；
每条断言 URL + 日期，直引逐字，半回源降级标注（research/ 分篇内已执行的口径不变）。

```yaml
topic: Harness / Context Governance（AI 形态下新的 SDLC）
created_at: 2026-09-21  # 自 beyond_spec_driven_development 抽出升格，用户定
promoted_at: 2026-09-21 # 主干定稿：research/ + result/ 信息流分层（result/backbone 总纲），用户定；同日定稿层 final/→result/ 更名、文件去序号（用户复核定）
scope: agent 执行链路治理：harness、context、规则文件纪律、门禁、漂移清理
layers:
  research/: 证据与判读（证据权威；编号 = 封存历史序列）
  result/: 定稿主张与操作规程（主张权威；语义命名，无序号）
related:
  - ../beyond_spec_driven_development/README.md   # 光谱定位与"问题从哪来"（批判面）
  - ../spec_driven_development/README.md          # SDD 工具层（被批判与被治理的对象侧）
```
