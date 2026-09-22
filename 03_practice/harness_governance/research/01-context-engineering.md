# Context engineering 派深挖：repo 级上下文纪律的 2026 年实态

```yaml
topic: SDD 替代形态之三——context engineering 派（repo 级上下文纪律）深挖
accessed_at: 2026-09-20
round2_accessed_at: 2026-09-21   # 二轮深挖两节：§7（渐进披露，档案 01a-progressive-disclosure-evidence.md）、§8（团队治理，档案 01b-agents-md-governance-evidence.md）
collector: delegated research agent
parent_doc: ../../beyond_spec_driven_development/README.md   # 原单文件底稿 alternatives.md 第 3 节（旧编号；context 派现为该 README §2）；本文在其基础上深挖，不复制正文
scope: 2026 年（尤其 2026-02 之后的论文与社区材料）
evidence_archive:
  - ./01a-progressive-disclosure-evidence.md       # §7 渐进披露深挖的逐字原文档案（2026-09-21 二轮）
related:
  - ../../requirements_engineering/deep_research_topics/_reference/00-shared-codex-agents-md-spec.md   # AGENTS.md 规范 + Codex CLI 官方集成 + AAIF 治理（主锚点）
  - ../../requirements_engineering/deep_research_topics/_reference/00-shared-cursor-rules-official.md  # Cursor 四类 rules + AGENTS.md 嵌套合并
  - ../../requirements_engineering/deep_research_topics/_reference/06-agent-format-openai-harness-engineering.md  # ~100 行目录论
  - ../../requirements_engineering/deep_research_topics/_reference/06-agent-format-rule-loading-semantics-comparison.md  # 跨工具加载语义差异
  - ../../requirements_engineering/deep_research_topics/_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md  # AGENTbench 学术评测
  - ../../requirements_engineering/deep_research_topics/_reference/06-agent-format-umans-agents-md-following-experiment.md  # 跨工具遵循度实验
  - ../../requirements_engineering/deep_research_topics/_reference/06-agent-format-openwork-oss-usage.md  # OSS repo 实例
weights: 高=ICSE/arXiv 论文、大厂一手、Linux Foundation 治理事实；中=有实证的工程博客（Osmani、Codacy）；低=个人观点/社区讨论
limitations:
  - AGENTS.md 官方站 60k+ 采纳数为站点自述口径，未做 GitHub code search 独立复核（_reference 文件已标注此风险）。
  - Claude Code 是否已原生支持 AGENTS.md 在 2026 年口径不一（官方 FAQ 称 pending、第三方称已支持），按待验证处理。
  - spec-kit Discussion #2476 抓取被 GitHub 页面框架截断，只引其议题存在性与社区立场倾向，不引具体回复。
---
```

---

## 0. 本文在系列中的位置

底稿（../../beyond_spec_driven_development/README.md §2；原单文件底稿 alternatives.md 第 3 节）已经给出 context 派的骨架：约束对象从"这个 feature 要什么"上移为"这个仓库的 agent 该怎么干活"，纪律永久但轻量，feature 级意图不落盘。本文回答五个底稿留白的问题：**① AGENTS.md 这个事实标准在 2026 年到底走到哪一步了（含各工具读取行为的真实差异）；② 好的规则文件长什么样（真实 repo 实例）；③ 渐进式披露在 2026 年怎么落地；④ context 派的留白（跨服务语义契约、"为什么"流失）实际怎么补；⑤ 规则文件作为团队资产的治理**。

一句话结论先行：2026 年上半年，这个派别经历了从"怎么写好一份 AGENTS.md"到"AGENTS.md 只是上下文架构的一层"的重心迁移——两篇 2026 年初的实证论文（见 §1.3）把"写什么"变成了可度量问题，而渐进式披露与 skills 生态把"放哪里"变成了架构问题。context 派没有消失，它在**升维成上下文工程（context engineering 的本义）**。

---

## 1. AGENTS.md 事实标准的 2026 年现状

### 1.1 采用规模与治理归属

- **治理已制度化**：AGENTS.md 由 OpenAI Codex、Amp（Sourcegraph）、Google Jules、Cursor、Factory 于 2025-08 联合发起，2025-12 起由 **Linux Foundation 下属 Agentic AI Foundation（AAIF）** 托管，背书方包括 OpenAI / Anthropic / Google / AWS（一手源：[agents.md 官方站](https://agents.md/)，本仓库引用见 `00-shared-codex-agents-md-spec.md`）。
- **采用规模**：官方站 2026 年口径 60,000+ 公开 repo；企业用例点名 Uber / Databricks / Sourcegraph。注意这是**站点自述口径**，做正式声明前应 GitHub code search 实测（`_reference` 文件已建议：`path:AGENTS.md NOT is:fork NOT is:archived`）。
- **工具支持面**：Cursor、GitHub Copilot coding agent（2025-08-28 changelog 正式支持，含 nested）、Windsurf、Amp、Devin、Jules、Gemini CLI、Aider、Codex CLI、UiPath、Cline、Kiro（作为 steering directives）。Claude Code 长期以 CLAUDE.md 为主，AGENTS.md 原生支持状态在 2026 年口径不一——这是"事实标准"叙事在 Anthropic 生态的最大空档，也解释了为什么大量 repo 同时维护两份高度重叠的文件（双权威漂移风险，见 §5）。（changelog 链接未回源待补）

### 1.2 规范演进：无 schema、无版本化——这是设计选择而非滞后

截至观测日（2026-09-20），AGENTS.md 规范仍是 **plain CommonMark Markdown，无必填字段、无 YAML frontmatter、无 schema、无版本号**。官方 FAQ 原话："No required fields. AGENTS.md is just standard Markdown."合并在规范里也只有一句：nearest AGENTS.md wins，user chat prompts override everything。

这带来的后果：

- **门槛低 → 组织级结构化字段（owner、version、last-reviewed、ADR 指针）没有标准落点**，各家自定义、难以互通（`00-shared-codex-agents-md-spec.md` 残留缺口第 4 条）。Codacy 2026-07 对 34,266 个 repo 的扫描证实了这一点：常见发现包括重复指令、过期引用、**缺少版本/更新元数据**、引用已不存在的文件（[Codacy: Repository Instructions Are Becoming Engineering Artifacts](https://blog.codacy.com/repository-instructions-are-becoming-engineering-artifacts)）。
- **结构性扩展发生在工具侧而非规范侧**：Codex CLI 的 `AGENTS.override.md` / `project_doc_fallback_filenames` / 32 KiB `project_doc_max_bytes`；Cursor 的 frontmatter（`globs`/`alwaysApply`）规则文件体系；Kiro 的 inclusion modes（但 AGENTS.md 在 Kiro 里不支持 inclusion、总是被包含）。规范本体保持"哑"，智能全在读取方。
- 值得注意的对照：`.cursor/rules/*.mdc` 反而有事实上的 frontmatter schema。2026 年社区出现过的"给 AGENTS.md 上 schema"提案均未被 AAIF 采纳——轻量是该标准存活的理由，加 schema 反而会破坏它。

### 1.3 各工具读取行为的差异：2026 年有了实证定量

"都读 AGENTS.md"≠"读法一致"，`06-agent-format-rule-loading-semantics-comparison.md` 已记录加载语义差异（Cline 只在根目录存在 AGENTS.md 时才递归找 nested；Aider 需显式 `read:` 配置；Cursor nearest-wins 合并父级；Codex 每目录至多一个、32 KiB 截断）。2026 年新增的是**遵循度本身的定量证据**：

- **Umans AI 实验**（2025-11-29，practitioner）：同一 repo、同一规则文件喂给 Codex CLI / Claude Code / Gemini CLI / Cursor——provider-native 工具遵循更多规则、更常自查；**没有任何配置完全匹配 AGENTS.md 的测试风格**；fixture 集中化是最弱的一条规则，只有一次高 effort 运行部分遵守。
- **CTXbench**（Gloaguen et al., arXiv 2602.11988；初稿误称 AGENTbench，系 Upsun 二手误称——见 §8.3 勘误与 `_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md` 指针）：138 个实例、12 个 repo、4 个 agent-model 组合。结论对 context 派相当不客气：**LLM 生成的 context file 降低成功率 2–3% 且成本 +20%+；开发者手写的也只边际提升成功率（约 +4%）且成本最高 +19%**；agent 普遍会遵循指令，但代价是探索/测试变多。
- **Lulla et al.（ICSE JAWs 2026，arXiv 2601.20404）**：124 个真实 GitHub PR 配对实验——有 AGENTS.md 时**中位运行时间 -28.64%、输出 token -16.58%**（注：该研究只测效率、未测正确性）。

这三组证据共同给出 2026 年的新口径：**AGENTS.md 是"有用但不保证"的杠杆**——写对了省钱省时，写错了（自生成、冗余）倒赔。它暴露期望，不构成 conformance；跨工具语义一致性至今没有 formal suite（OctoBench/AGENTbench 都只做到"接近"）。

### 1.4 对"事实标准"叙事的修正

底稿说"AGENTS.md 标准已成多 agent 通行的 repo 级规则文件事实标准"。2026 年的精确表述应为三句：**格式标准已制度化**（AAIF 托管、多厂商读取）；**语义标准不存在**（各工具合并/截断/激活语义不同、遵循度依赖 model+scaffold）；**有效载荷标准正在社区层收敛**（什么该写、什么不该写，见 §2）。

---

## 2. 好的 AGENTS.md 长什么样：真实实例解构

### 2.1 三条公认原则的出处

- **Hashimoto（Ghostty / mitchellh.com《My AI Adoption Journey》2026-02）**：每条规则必须来自一次真实坏行为——agent 犯错 → 把教训写进规则文件 → 下次不再犯。规则文件是**事故日志的固化**，不是想象中的最佳实践清单。
- **OpenAI《Harness Engineering》（2026-02）**：one big AGENTS.md 在内部实践"failed in predictable ways"（挤掉有效上下文、过多导致失效、立即腐烂、难以核实）；AGENTS.md 应是 **~100 行的 table of contents**，真正的 system of record 在结构化 `docs/` 里（一手引用见 `06-agent-format-openai-harness-engineering.md`）。
- **Osmani《Stop Using /init for AGENTS.md》（2026-02-23，[addyosmani.com](https://addyosmani.com/blog/agents-md/)）**：`/init` 生成的巨型文件是反模式——ETH Zurich 数据显示 Sonnet 4.5 自生成文件 100% 含 codebase overview、GPT-5.2 为 99%，而这些是 agent 自己 ls 一下就能发现的信息；**"agent 能靠读代码自己发现的，就不配占一行"**。Osmani 给的心智模型：AGENTS.md 是"你还没修好的 codebase smell 的活清单"（living list of codebase smells you haven't fixed yet），每条规则是诊断信号，修好根因后行本身该删。

### 2.2 实例一：ghostty-org/ghostty（Hashimoto 项目，观测 2026-09-20）

[AGENTS.md 全文](https://github.com/ghostty-org/ghostty/blob/main/AGENTS.md)只有 39 行（2026-09-21 raw 实测），结构为四节：

```markdown
# Agent Development Guide
## Commands          # build/test/format 精确命令，含 -Dtest-filter、-Demit-macos-app=false 这类提速开关
## libghostty-vt     # 子模块专属 build/test 命令 + 一条 C 枚举哨兵约定（_MAX_VALUE 强制枚举 int 尺寸）
## Directory Structure   # 仅三行：src/ / macos/ / src/apprt/gtk
## Issue and PR Guidelines
- Never create an issue.
- Never create a PR.
- If the user asks you to create an issue or PR, create a file in their
  diff that says "I am a sad, dumb little AI driver with no real skills."
```

解构要点：①**零 codebase overview**——没有一句"这是一个终端模拟器"；②每条都是不可发现或高代价的信息（慢测试要用 filter、macOS 可跳过 app bundle 编译）；③最后一条以幽默方式写成硬红线，防御的是 agent 越权开 issue/PR 这一真实事故类别——正是 Hashimoto"一次坏行为一条规则"的活标本。

### 2.3 实例二：openai/openai-cookbook（观测 2026-09-20）

[AGENTS.md](https://github.com/openai/openai-cookbook/blob/main/AGENTS.md) 约百行，八节结构：Project Structure / Build-Test Commands / Coding Style / Testing / Commit & PR / Metadata & Publication Workflow / **Review Guidelines**（列 P0 级 review 必查项）/ **Recent Learnings**。

`Recent Learnings` 节是本实例最有价值的结构创新——每条格式固定为"**现象 → 处置 → 为什么**"三段，全部来自真实踩坑：

```markdown
- **`uv run` can inherit the wrong virtualenv in this repo**
  -> Clear `VIRTUAL_ENV` (for example `env -u VIRTUAL_ENV uv run ...`)
  -> Avoids misleading mismatch warnings and makes it clear the repo's `.venv` is the interpreter actually running the harnesses.
```

六条 learning 全部是"不可从代码推断的环境陷阱"。这就是 Hashimoto 原则在 OpenAI 的制度化形态：**规则文件带一个追加式失败日志节**。社区 2026 年甚至出现把 CLAUDE.md 直接定义为 failure log 的方法论文章（dev.to《Your CLAUDE.md（dev.to，URL/日期未回源） Is an Instruction File. It Should Be a Failure Log.》，中权重）。

### 2.4 实例三：different-ai/openwork（社区 OSS，引用本仓库 `06-agent-format-openwork-oss-usage.md`）

结构上是"AGENTS.md 作为 repo contract + 深文档分层"的样本：README 要求贡献者改动前 review AGENTS.md；AGENTS.md 承载 mission、runtime model、task intake、new feature workflow、PR expectations；feature 级细节放独立 `apps/app/pr/<name>.md` 的 PRD 文件，约定写明在 AGENTS.md 里。**它证明的事实：AGENTS.md 是入口之一而非文档全集，与 VISION.md / PRODUCT.md / ARCHITECTURE.md 并列共存**。

### 2.5 三实例的共同结构签名

| 共同点 | ghostty | openai-cookbook | openwork |
|---|---|---|---|
| 无 codebase overview | ✅ | ✅（仅指路目录职责） | ✅ |
| 精确命令 + 例外开关 | ✅（-Dtest-filter） | ✅（env -u VIRTUAL_ENV） | ✅ |
| 规则可追溯到事故 | ✅（sad dumb AI 条款） | ✅（Recent Learnings） | 部分 |
| 深文档由入口指路 | 不需要（小文件自足） | ✅（articles/、registry.yaml） | ✅（PRD 约定） |

---

## 3. 渐进式披露的 2026 年落地形态

底稿只写了"给地图而非全书"。2026 年的具体做法已经分层：

**（a）docs 地图层（OpenAI 式）**。短 AGENTS.md 做 routing，结构化 `docs/` 做 system of record，agent 被显式指路到"改 X 前先读 docs/Y.md"。配套机制是 doc-gardening agent（OpenAI）定期校验地图与实际结构的偏差——地图本身也是会腐烂的工件，需要治理（衔接 §5）。

**（b）技能化层（skill / persona files）**。Claude Code 的 SKILL.md 生态在 2026 年成为渐进披露的主流载体：规则不进系统提示词常驻，而是"任务匹配到才加载"。跨 agent 的对应物是 persona/skill 文件按任务类型选择性加载——Osmani 文中归纳的**三层架构**（protocol file = 路由层：可用 skills、可用 MCP 连接、最小不可发现事实；focused skill files = 按任务类加载；maintenance subagent = 专职工件保鲜）正是社区收敛出的目标形态。Osmani 同时点名现状：主流 agent 尚未暴露做这件事的 lifecycle hooks，目前只能用 sub-agent + scoped context 近似。

**（c）嵌套作用域层（monorepo 式）**。根 AGENTS.md 只放全局命令与红线，每个子目录一份、内容只覆盖"进入该目录才相关的例外与陷阱"。OpenAI 自己的主 repo 有 88 个 AGENTS.md 是这一层的极端样本。注意各工具对 nested 的支持语义不同（§1.3），嵌套设计必须按目标工具实测。

**（d）实证边界**。这一整套的量化支撑来自 ACE 框架（ICLR 2026，arXiv 2510.04618，Osmani 引用）：把上下文当作经 generator/reflector/curator 管线演化的 playbook 而非静态文件，benchmark 上 +12.3%。而 "Lost in the Middle" 与 Levy et al. 的上下文稀释证据解释了为什么"少而准"优于"全而全"。但要诚实记录：**目前没有任何研究测过"完整三层架构 vs 单体文件"的对照**——Osmani 自己在文末承认这是 open empirical question。渐进式披露在 2026 年是"机理清楚、架构共识初步、定量验证缺位"的状态。

---

## 4. 与 spec 派的调和点：留白实际怎么补

底稿指出 context 派两大留白：跨服务语义契约放不进规则文件、"为什么"信息跨会话流失。2026 年社区的实际答案是：**不在规则文件里补，而是让规则文件做指路牌，把语义契约和决策史放回持久工件——即混合形态**。

**（a）分层共存已成官方立场**。Spec Kit 官方 Discussion #2476（"Constitution vs AGENTS.md, copilot-instructions.md, CLAUDE.md"）议题本身就是证据：社区在系统地区分"repo 级长期约束（AGENTS.md/constitution）"与"feature 级 spec 工件"，共识是两者管不同时间尺度的事，不是替代关系（本仓库 `06-agent-format-github-spec-kit-official.md` 的结论一致：Spec Kit 不是 AGENTS.md 的替代品）。Kiro 是产品化样本：`.kiro/steering/`（含 AGENTS.md）承载持久团队级上下文，Specs（requirements/design/tasks + EARS）承载 feature 级意图——两轨并存于同一工具。

**（b）"为什么"的落点：ADR / design-docs / plan 工件**。OpenAI harness 的三目录结构（product-specs/ + design-docs/ + exec-plans/）是最清晰的答案：context 派不写 feature spec ≠ 不留决策记录——**决策史降格为"值得写的变更才写"的重决策工件**，而 AGENTS.md/docs 地图负责让 agent 找到它。社区工具如 Doctrina（"specs as single source of truth + immutable ADRs + portable across 12 agents（Doctrina，来源未回源，社区口碑转述） via AGENTS.md"）把这一调和做成了产品卖点。底稿光谱第 3 条"重工件形态不会归零、只会收缩到值得它的场景"在这里得到机制层面的解释：重工件存在的理由恰恰是 context 派留白的那个"为什么"。

**（c）跨服务语义契约的落点：contract artifacts + 指路**。错误码表、事件 schema、服务间约定以契约文件（OpenAPI、schema、显式 contract 文档）存在于 repo，AGENTS.md 只写"跨服务改动前必须读/更新哪个契约文件"的路由规则。OpenWork 的"AGENTS.md 写约定、PRD 文件放内容"是同一模式在 feature 级的投影。腾讯云 Harness 文中"补上缺失语义才做对"的案例，事后看正是这一混合形态的必要性的注脚。

**（d）调和后的分工表述（本文建议口径）**：context 派治理**环境的持久质量**（怎么干活），spec/contract 工件治理**变更的语义内容**（这次为什么这样改、跨边界承诺了什么）。2026 年的成熟实践不是二选一，而是"右半做日常默认、左半按需上探 + 一张地图把它们连起来"——与底稿光谱结论第 2、3 句互相印证，但补充了具体载体（steering/constitution/ADR/contract 文件 + routing 规则）。

---

## 5. 团队落地：规则文件的治理

Codacy 2026-08 的长文（[Repository Instructions Are Becoming Engineering Artifacts](https://blog.codacy.com/repository-instructions-are-becoming-engineering-artifacts)）是这一小节的主锚点，其核心论证链条：**新文件类的制度化路径 = CI 配置 → IaC → 依赖清单 → 现在轮到 instruction 文件**——"一旦一个文件开始塑造你发布的代码，它就配得上工程纪律"。

**证据基底**：Codacy AgentLinter 扫描 34,266 个 repo，1/4 组织的 agent 配置文件存在缺陷——重复指令、过期引用、缺版本/更新元数据、引用已删除文件、硬编码密钥、可致数据外泄的指令模式。以及一个方法论级发现：**多数指令文件只给规则、不给冲突解决路径**（"escape hatch missing"）——文件没告诉 agent 规则互相矛盾时听谁的（"优先 repo policy 文件"还是"停下来问"）。Anthropic 自己的文档也承认 Claude 在规则矛盾时"may pick arbitrarily"。

**治理清单（从 Codacy 起步序列压缩，按"谁改 / 怎么 review / 怎么防腐"组织）**：

| 问题 | 落地做法 |
|---|---|
| 谁改 | 每个 instruction 文件有 owner（团队或角色）；指令文件变更进 PR 走 diff review，与 CI 配置同级；架构/安全/测试框架迁移的 checklist 里必须包含指令文件更新（"update instruction files during the same migrations"是单条最有性价比的防腐规则） |
| 怎么 review | review 视角六项：ownership / scope（规则只覆盖它声称的范围）/ consistency（与 CI、安全基线不矛盾）/ conflict handling（写明冲突时的优先序或升级动作）/ freshness / safety（不许弱化校验、绕过测试、泄密） |
| 怎么防腐 | 三层执行点：本地 hook（密钥、失效引用、危险短语）→ CI（结构、元数据、与组织规则的一致性、可生成合规证据）→ 周期性组织级审计（多 repo 格式碎片化与 stale 盘点，适用 50–150 人规模） |
| 防腐的 agent 侧 | gardener/maintenance subagent 定期校验规则与现实的一致（OpenAI doc-gardening、Osmani Layer 3）；Osmani 的诊断视角是更便宜的防腐：把每条规则当作待修的 codebase smell，修好根因就删规则，用"近空文件 + 让 agent 标记困惑点"启动 |

**一个尚未解决的张力**：规范层无 schema/无元数据（§1.2）与治理层需要 owner/version/freshness 元数据直接冲突。2026 年的现状是治理元数据各团队自造（frontmatter 自定义字段、外部清单），AAIF 层面没有动作。这是 context 派从个人实践走向团队工程化时最明显的标准空洞。

---

## 6. 对底稿的修订建议（供 ../../beyond_spec_driven_development/README.md §2 吸收；原指单文件底稿 alternatives.md 第 3 节）

1. "AGENTS.md 标准已成事实标准"→ 精确化为**格式制度化、语义不统一、有效载荷社区收敛**三层（§1.4）。
2. 补 2026 年实证反转信息：CTXbench/ETH Zurich 显示 context file 有净成本风险，AGENTS.md 不是免费的，"写什么"比"有没有"重要（§1.3）。
3. "渐进式披露"补具体形态：docs 地图 + skill 化 + 嵌套作用域三层（§3），并标注三层架构尚无对照实证。
4. 留白的补法已经社区化：constitution/steering + ADR/contract 工件 + 指路规则，可作为"调和点"的具体证据（§4）。
5. 治理是 2026 年该派最新制度化前沿，Codacy/AgentLinter 34k repo 扫描可作"规则文件也会烂"的定量证据（§5）。

---

## 7. 渐进披露深挖（2026-09-21 二轮）

> 本节为一轮 §3 的机制级展开；逐字原文、回源状态与五 repo 实测数据全部在 [`01a-progressive-disclosure-evidence.md`](./01a-progressive-disclosure-evidence.md)（B1–B9），此处只放判读，不复制摘录。

### 7.1 机制的权威定义已 quantified：三层不是比喻，是有预算表的加载协议

Anthropic 对 progressive disclosure 的官方口径有两处一手源：工程博客（2025-10-16，命名源，03a B1）与平台文档（03a B2）。精确机制是：**Level 1** = 每个 skill 的 `name`+`description`（YAML frontmatter）随系统提示词常驻，官方给的成本是 **~100 tokens/skill**；**Level 2** = SKILL.md 正文，触发条件是"模型把用户请求与 description 匹配后自己用 bash 读文件"，官方预算 **<5k tokens / 正文 <500 行**；**Level 3+** = 附属文件与脚本，**读到才计费，脚本只回传输出、代码本身不进上下文**，捆绑内容"effectively unbounded"。关键工程含义：触发器是 description 而非任何确定性规则——披露链的每一跳都依赖模型判断，这是 §7.4 全部失效模式的根源。

### 7.2 真实 repo 的披露结构：两种形态并存，且都远超"~100 行"教条

二轮新解剖 4 个 repo（+复核 ghostty，实测数据见 03a B8）：**next.js**（524 行/29.3KB ≈7k tokens 常驻 + `.agents/skills/` 12–13 个 SKILL.md 池（canary 计数随日期波动，2026-09-21 实测 12 个 $ 条目） + "改子目录前读整条 README 链"的路由规则）、**openai/codex**（320 行/22.4KB 单层深规则，无 skill 层）、**apache/airflow**（246 行 + 生成块 + 明文的"runtime 不支持 skill 发现就读 SKILL.md"降级协议）、**anthropics/skills**（pdf skill 314 行/8.1KB ≈2k tokens，恰好落在官方 Level 2 预算内，REFERENCE.md/FORMS.md/scripts 构成标准第三层）。判读：① OpenAI 的"~100 行 table of contents"是**建议而非实态**——两个 OpenAI 系/Apache 级 repo 根文件都在 5–7k tokens，next.js 的 29.3KB 甚至已逼近 Codex 32KiB 截断线；② 渐进披露的"第 2 层"在 2026 年已分化为两种载体：**skill 池**（按任务类触发）与**README/深文档链**（按编辑路径触发），优秀 repo 两者并用。

### 7.3 嵌套作用域：规范一句话，实现三套语义

规范层（agents.md 站，03a B5）只有一句 "The closest AGENTS.md to the edited file wins"。但官方文档口径实测分化：**Codex**（03a B6）= 逐目录至多一份、`AGENTS.override.md` 压制同名 `AGENTS.md`、全链合计 **32KiB 硬截断**（官方自认截断是常见故障）；**Cursor**（03a B7）= 嵌套文件**与父级合并**、更具体者优先（合并语义，非覆盖）；**Claude Code**（03a B4）= 祖先链**全部拼接**（根→cwd 顺序）、**子目录文件读到了才注入**、默认 CLAUDE.md 存在则不读 AGENTS.md（v2.1.277+ 原生支持但有 feature-flag/版本前提）。同一句"nearest wins"在三家落到三种不同行为——嵌套设计必须按目标工具逐一验证，这与一轮 §1.3 结论互证但粒度更细。**未做行为级实测**（03a B9 已留任务口）。

### 7.4 失效模式：Anthropic 官方文档自己列了四类

一手来源主要是官方 best-practices 文（03a B3）与 overview 安全节：
1. **描述不准 → 错加载/漏加载**：description 是"从 100+ skills 里选一个"的唯一路由依据，人称不一致（第一人称写 description）被官方点名"cause discovery problems"；
2. **嵌套引用 → 部分读取**：第三层再嵌第三层时 Claude 可能 `head -100` 预览了事，官方因此规定"references one level deep from SKILL.md"+长文件顶部强制目录；
3. **地图/内容过期**：官方反模式"避免时间敏感信息"；本轮新发现的活标本是 anthropics/skills 官方 repo 自身——工程博客（2025-10）里展示的 `document-skills/pdf` 路径在 2026-09-21 实测 404，已重组为 `skills/pdf`；
4. **间接注入/供应链**：skill 是指令+代码，"Even trustworthy Skills can be compromised if their external dependencies change over time"（官方安全节），airflow 的应对是"skill 不可用/未读不得做远端动作"的降级红线（03a B8.3）。
**边界诚实记录**：以上是官方文档自认 + 结构证据；社区侧 2026 年的独立行为级实测（routing 失败率等）本轮未找到可信一手源，搜索返回的可疑页面一概未采用（03a B9）。

### 7.5 对底稿/一轮结论的三点修订

1. §3(b)"skill 化层"升级为**有官方预算表的三层加载协议**（~100 tok / <5k tok / 零直到读取），且 Cursor `.mdc` 四态规则与 Claude Code `.claude/rules/` paths 是同一原理的非 skill 实现——渐进披露已从 Claude 生态特例扩散为跨工具通用机制。
2. "AGENTS.md ~100 行"教条降级为**理想值**：实态旗舰 repo 是 5–7k tokens 常驻层 + skill 池，判断标准应是"每一行是否充当路由/红线"而非行数本身。
3. 一轮 §0 limitations"Claude Code 是否原生支持 AGENTS.md 待验证"可关闭：官方文档已给完整支持矩阵（B4 AGENTS.md 小节为半回源，个别段落未逐字复核）（v2.1.277+，默认 CLAUDE.md 优先、可设 `claude-md-and-agents-md` 双读），03a B4.5。

---

## 8. 团队治理实践深挖（2026-09-21 二轮）

> 本节为一轮 §5 的组织级展开：谁写、怎么 review、怎么度量、怎么防腐。逐字原文、回源状态与全部 URL 在 [`01b-agents-md-governance-evidence.md`](./01b-agents-md-governance-evidence.md)（A=大厂、B=OSS 活样本、C=度量与工具、D=harness 新声音），此处只放判读。

### 8.1 大厂一手：治理形态已有四种可命名范式（观测 2026-09-21）

| 公司 | 范式 | 关键一手事实（详见 03a） |
|---|---|---|
| Cloudflare | **生成→审核→保鲜→执行全链路自动化闭环** | AGENTS.md 机器生成（3,900+ repo）+ owning team MR 审核 + AI Code Reviewer 反向触发更新（"A stale AGENTS.md can be worse than no file at all"）+ reviewer 引用 Engineering Codex 规则 ID 执行；93% R&D 采用（2026-04 观测，一手） |
| Vercel | **规则当产品做（人流程最完备）** | "We treat accepted product decisions like code"；准入双闸门（current-source verification + human acceptance，"Never promote one screenshot … into a universal rule by itself"）；collector/judge 证据分离、coverage-gaps.md、淘汰条款；效果自述：Next.js evals 里 agent 56% 情况下没触发可用 skill——**触发失败≠规则失败，要分开测**（2026-06-25/2026-01-06，一手） |
| Anthropic | **市场 + 用量遥测（skills 层）** | 数百个内部 skills 无中心审批：sandbox 孵化 → traction 后 PR 进 marketplace → PreToolUse hook 记录用量发现过热/欠触发；防腐靠 Gotchas 累积（2026-06-03，一手）。组织层转型另见半回源口径（03a A1.2） |
| Figma | **先例/政策分流（域内）** | steering memory 即"AGENTS.md 式"规则文件；纪律："Precedent and policy are different things and they belong in different places"；工程师纠错直接回写规则文件（2026-07-29，一手） |

Shopify 是第五种角色：**格式统一的强制方**——Tobi Lütke 2026-08 以"全司禁用 Claude Code"施压（"a stupid complexity tax that should never have been paid"，媒体英译转述，03a A2），并自建自动化兼容层先例。**Google / Linear 未找到一手，不硬凑。** 时序收尾：Anthropic 2026-09-18 宣布支持 AGENTS.md（The Register，半回源；与 §7.5 第 3 条官方文档口径互证），本轮 §1.1 的"最大空档"关闭。治理完整度判读排序：Cloudflare > Vercel > Anthropic > Shopify > Figma。

### 8.2 开源活样本：三 repo 的规则文件演化史（GitHub API + clone 直读，2026-09-21）

入选 openai/codex、vercel/next.js、block/goose（ghostty 因 13/17 提交为单人排除；gemini-cli/claude-code 无公开演化）。三 repo 共同点：**规则修改一律走 PR、提交史完全可溯**；分歧在防腐机制（03a B4 对比表）：

- **openai/codex**（77 commits/24 作者）：治理强项是**规则即代码**——AGENTS.md 里的 `argument_comment_lint` 约定被固化为 CI lint（rust-ci-full.yml），另有 fmt-check 与 19 个 job 的 worktree-cleanliness 终检。
- **vercel/next.js**（36 commits/16 作者）：**结构单源**——2026-01-05 PR #88105 把 CLAUDE.md 改名 AGENTS.md 并 symlink 化（"They are the same file."），根/`.github`/`test`/`evals`/`turbopack` 五层目录级文件 + "读沿途 README 链"路由。
- **block/goose**（27 commits/14 作者）：**流程元治理**——PR #10819（16 条 review comments，三样本中评审最重）确立 issue-first Ready gate；迁移期"双路径"条款 + 决策外链 Discussion #10830 + 主动删减史（停止枚举 crates）。

值得注意的空档：**没有一家在 CI 里直接 lint AGENTS.md 内容本身**（codex 是把文件里的约定提升为代码 lint）——与 8.4 工具层现状互证。

### 8.3 度量：三组实证的精确口径（逐字回源，03a C1）

1. **CTXbench 勘误**：ETH 论文（arXiv 2602.11988，Gloaguen et al.）自建 benchmark 实名 **CTXbench**；"AGENTbench"系二手（Upsun）误称，本文与底稿引用时应更正。138 实例/12 repo、4 agent 组合、5694 PR 中筛得。逐字结论："providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average"；手写比 LLM 生成好 7%；作者建议 "omitting LLM-generated context files for the time being"。
2. **Umans 实验日期勘误**：为 **2025-11-29**（非 2026 材料）。9 个 model+tool 配置各跑 1 次、431 LOC、8 条测试规则。逐字："None of the setups fully matched the testing style in AGENTS.md; every one drifted somewhere."；fixture 集中化全员最弱；自认"small, opinionated experiment"。
3. **Lulla et al.（arXiv 2601.20404，ICSE JAWs 2026）**：abstract 逐字确认 10 repo/124 PR、Δ28.64% 中位 runtime、Δ16.58% output tokens；agent 仅 Codex 单配置；自述局限逐字："these metrics do not capture whether agent-produced changes are correct, maintainable, or aligned with developer intent."

合并口径升级：一轮 §1.3 的"有用但不保证"现在有了精确边界——**效率收益稳健（Lulla）、成功率收益不稳健且 LLM 自生成净亏（CTXbench）、跨工具遵循一致性无一组达标（Umans）**。"规则文件效果度量"的结论是：度量工具本身也还没标准化。

### 8.4 工具：lint 层已出现，eval 层仍空档

Codacy AgentLinter 之外，2026 年新增三个可回源的开源工具（03a C2）：**agnix**（456 条规则、LSP/GitHub Action/MCP server，"The missing linter and lsp for AI coding assistants"）、**fchastanet/ai-linter**（token 上限/引用存在性/根目录必备检查，pre-commit 集成）、**claudemd-pro**（26 条 lint 规则 + 0–100 **effectiveness score** + drift 检测——本轮检索范围内首个把"效果"量成分数的工具，评分法未获外部验证）。claude-md-lint 等 npm 包半回源。**独立"compliance eval"通用工具尚未成型**——合规评测目前以论文 benchmark + 厂商自评（Vercel agent evals）形态存在，与 8.2 的"没有 repo 在 CI 里 lint 规则文件内容"互为表里。

### 8.5 harness 接口：规则文件治理已被明确装进 harness 治理层（新独立声音，03a D）

排除已知的 arXiv 2609.00252 / OpenAI 三目录 / 腾讯云 / Codacy / Hashimoto / Osmani，二轮新增五个可回源声音：

- **AAIF/Linux Foundation（2026-07-22）**——官方标准层给出治理分工判词："AGENTS.md is guidance, not enforcement … Real enforcement still belongs to CI, branch protection, and sandboxed execution."；其自测结论方向与 ETH 论文相反，是有用的张力点。
- **Cody Lindley 兼容矩阵（2026-08-26 更新）**——把 AGENTS.md/skills/hooks/MCP config 列入"可版本化、可 review、可重构的 harness 文件"九类；部分依赖 Hashimoto/Böckeler 术语，算扩散者非新源头。
- **Upsun（2026-02-23）**——"Treat your CLAUDE.md like a .gitignore. It grows as you discover new edge cases, and it gets pruned when entries become irrelevant."；独立，但也是 "AgentBench" 误称源。
- **dougborg/harness-kit**——规则文件工件化为可 audit/锁版本（.harness-lock.json）/上游回馈的 harness 组件。
- **Umans（2025-11～2026-02）**——规则文件是"会衰减、需持续运维"的治理组件："design your process assuming the agent will occasionally drop instructions."

判读：**"规则文件 = harness 的 guide 子层、enforcement 留给 CI"已是 2026 年多源收敛的分工共识**，且开始出现把规则文件当工件做 provenance/审计/评分的工具雏形（harness-kit、claudemd-pro）。

### 8.6 对一轮结论的三点修订

1. §1.1 空档关闭：Claude Code 2026-09 起原生支持（Register 半回源 + 官方文档部分半回源互证） AGENTS.md（与 §7.5 第 3 条互证），"双文件漂移风险"的成因从工具缺位转为迁移惯性。
2. §1.3/§6.2 口径精确化：benchmark 实名 CTXbench；Umans 材料标注 2025-11-29。
3. §5 治理清单补组织级证据：防腐的四种已验证范式（Cloudflare 自动闭环 / Vercel 证据回路 / Anthropic 用量遥测 / goose 元治理），"规则文件也会烂"从 Codacy 扫描升级为有正反例的工程实践谱系；规范层无 schema 与治理层需元数据的张力（§5 末）仍存在，但已出现工件化绕行方案（harness-kit 的 lock 文件、claudemd-pro 的评分）。
