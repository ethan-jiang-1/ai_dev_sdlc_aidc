# _reference —— 上游素材（只读）

本目录下全部是 **symlink，只读**。按 `AGENTS.md` 的规则，只在这里面读，不在里面写。
摘进 `02_evidence/` 时必须标注来源路径。

## 素材一览与分工

| symlink | 指向 | 给本 talk 提供什么 |
|---|---|---|
| `rawdata_ai-coding-evolution-final/` | `ai_tool_deepresearch/dpt_rb_ai-coding-evolution/final` | **宏观故事线**：五层演变最终报告（Prompt → Context → Harness → Loop → Graph，2025–2026）。核心主张：五层是**叠加**而非替代；驱动机制是"模型越强，单次交互的边际工程收益越低，工程杠杆点越往上移"。给整条故事线和论点骨架。 |
| `rawdata_harness-selection-final/` | `.../dpt_rb_harness-agent-selection-project-execution-pilot/final` | ★ **本 talk 尾巴的主料**：Harness Agent 选型研究报告（`final_v3.md`，2026-09-07）。含 11 候选评分卡、**Pi 深挖（Topic 04）**、**DSH 深挖（Topic 05）**、Codex Harness 开源（Apache-2.0，2026-08-20）、**Framework First vs Product First** 三方路线对照表。 |
| `rawdata_harness-selection-wave1/` | 同上 bundle 的 `artifacts/wave1` | 逐 topic 的 `evidence-summary.md` / `question-list.md` / `depth-review.yaml`。按需取机制细节。 |
| `rawdata_harness-selection-wave2/` | 同上 bundle 的 `artifacts/wave2` | 跨话题综合 `synthesis.md`、`cross-topic-ledger.md`、`finding-index.yaml`。 |
| `rawdata_pi-digested/` | `pi-mono/_digested` | ★ **Pi 的源码消化层**（基线 v0.84.4，2026-09-01 同步）。六个子目录，本 talk 最吃三块：**`harness/`**（Pi 作为开源 coding harness 的**评价维度**：01 架构三层接缝 / 02 **四条边界短板** / 03 开发纪律 / 04 自描述）、**`extensions/`**（极简核 + 扩充四轴 + 安全护栏）、**`composition/`**（五层配置框架、扩展七轴、安全边界、从别的 harness 迁移）。**第四幕 Pi 页的硬料与代价全在这里，且带源码锚点。** |
| `rawdata_pi-faq-on-digested/` | `pi-mono/_faq_on_digested` | ★ **Pi 二次研究问答**。最关键是 **`06_pi_vs_dsh/`（Pi 与 DSH 逐面强弱对照 + 机制表 + 双方硬伤）**；`07_pi_usage_scenarios/`（能力地图、场景手册、包生态、跨 harness）。DSH 侧与 `rawdata_dsh-*` 互为正反面。 |
| `rawdata_dsh-faq-on-digested/` | `deepseek-harness/_faq_on_digested` | **DSH 机制问答**：目录组织、Spec-Driven Development、模型 vendor 接入、根入口文档设计、SPEC 变更路径、"别的项目怎么借鉴 Harness 思路"（知识外置 / 正确路径 / 可执行反馈三条腿）。 |
| `rawdata_dsh-digested/` | `deepseek-harness/_digested` | **DSH 源码消化**：system / composition / session-and-loop / capability-seams / tools-prompt-llm / surfaces。**DSH 不用 MCP**——挂的是 `ctx.llm` adapter、`ctx.tools`、capability seam、plugin。 |
| `rawdata_dsh-plugin-seam-maturity/` | `deepseek-harness/_faq_on_digested/08_plugin-seam-maturity` | 插件接缝与成熟度：插件进入真实执行链后要补哪些合同与门禁。 |
| `rawdata_dsh-plugin-business-ladder/` | `deepseek-harness/_faq_on_digested/09_plugin-business-ladder` | 插件对 owner 的收益阶梯。 |
| `rawdata_dsh-plugin-ecosystem-distribution/` | `awesome-dsh-plugin/_faq_on_digested/01_ecosystem-distribution` | 插件生态分布快照（口径红线见 `02_evidence/00-absorption-plan.md`）。 |
| `rawdata_dsh-plugin-ecosystem/` | `awesome-dsh-plugin/_digested/ecosystem` | ★ **DSH 插件生态全景（2026-09-15 快照，census 现算）**：3722 条 / 2392 个作者 / 33 天；五阵营（做增强 51% · 做壳 21.9% · 运行与治理 19.7% · 触达 7.4%）；模型与推理域 19 天 2.21×（供应商接入 40→103）；82% 还是 0.x、老条目 7.1% 被再动过；549 条（14.8%）描述提到 api key / 登录 / 授权。**P29 借力好处 / P30 生态证据 / P32 生态代价 / P33 凭据面全吃这里**。 |
| `rawdata_ai-coding-evolution-reference/` | `ai_tool_deepresearch/dpt_rb_ai-coding-evolution/reference` | ★ **一手来源卡片层**（137 张）：每张带 `source_url / tier / source_type / trust_level / acceptance_status` 与可引原文。**五层演变报告就是这些卡的二手综合**——要回源、要引文、要核口径，来这里。 |
| `rawdata_harness-selection-reference/` | `.../dpt_rb_harness-agent-selection-project-execution-pilot/reference` | ★ **一手来源卡片层**（168 张）：同上格式。**P25 的官方博客卡、P26 的 flash 原始卡、Pi/DSH 的源码与安全通告卡都在这里**。 |

## 三层结构（2026-09-16 补链后）

上游资料是**三层**，此前只链了外两层，中间那层（一手来源卡片）没接进来——
这也正是 P6 / P7 两处「回源核对」长期挂着的真正原因：**要核的料压根没在库里**。

| 层 | 在哪 | 性质 | 本 talk 怎么用 |
|---|---|---|---|
| **综合层** | `*-final/`（报告正文） | 二手：报告作者的归纳 | 拿故事线与结论骨架 |
| **一手来源卡片层** | `*-reference/`（**305 张**） | 每张都有 `tier` 与可引原文 | **引文、口径、日期、证据强度一律以这一层为准** |
| **消化层** | `rawdata_pi-*` / `rawdata_dsh-*` | 源码级消化，带锚点 | 第四幕 Pi / DSH 的硬料 |

## ⚠️ 检索陷阱（踩过）

`_reference/` 下**全是 symlink**。`Grep` / `find` / `ls` 默认**不跟随符号链接**，
所以在这个目录里搜东西会得到 **0 命中** 或"空目录"的假象（本轮第一次 grep 就是这么被骗的）。
**正确做法**：搜真实路径，或 `find -L` / `grep -R` 显式跟随。

## 素材纯净度（2026-09-16 评估）

- ✅ **链接本身干净**：13 条 symlink 全部可达、只读、无死链。
- ⚠️ **`rawdata_harness-selection-*` 主题不纯**：那份研究是为「**项目执行 agent 选型**（PM / PMO 域）」做的，
  9 个主题里 **06–09**（PM agent 生态 / ChatBI-NL2SQL / agent 接口协作 / 行业合规平台）
  与本 talk 无关，约占该 bundle 的一半。**引用前先看卡片的 `related_topic_uid` 与文件名前缀**。
- ✅ 与本 talk 相关的主题：`01_project-execution-agent-paradigm`、`02_real-world-implementations-cases`、
  `03_harness-runtime-deployment-fit`、`04_pi-harness-deep-dive`、`05_dsh-plugin-harness-deep-dive`。

## Pi 素材的三个入口（第四幕专用）

讲 Pi 要同时讲"它好在哪"和"它在哪些环节没有护栏"。这正好对应 `_digested` 里的两块：

| 要讲什么 | 去哪读 | 关键结论 |
|---|---|---|
| Pi 的结构**好在哪** | `rawdata_pi-digested/harness/01-Architecture/` | 三层同心 seam（operations / tool / extension）按"变化轴"裁剪接口大小；统一注入点；分发闭环；生命周期护栏（两阶段绑定、stale 保护、**fail-close**） |
| Pi 的**代价在哪** | `rawdata_pi-digested/harness/02-Boundaries/` | 四条短板：**① 无默认沙箱**（扩展 = 宿主进程同等权限，`pi install` 陌生包 ≈ 执行其任意代码）② 无 MCP/ACP（生态锁定，外部工具要付适配层税）③ 内层 AgentLane 半成品 ④ 无扩展 API 版本契约 |
| Pi 与 DSH **逐面对照** | `rawdata_pi-faq-on-digested/06_pi_vs_dsh/` | `04_strengths_weaknesses.md` 有逐面强弱表，含**「对陌生插件安全：两个都烂」**——这是本 talk 第四幕"对称讲代价"的直接依据 |

**讲法提示（重要）**：`harness/02-Boundaries/` 的每条短板都做了 **severity 分层**——
"自用"与"吸纳陌生插件"的严重程度完全不同。上屏时不要说成"Pi 不安全"，
要说成"**Pi 把信任放在'谁装了它'，而不是'它是什么代码'上**"。
这既准确，也正好扣住本 talk 的核心：**那圈护栏要不要、由谁定**。

## 引用约定

- 引用上游数字、引文、机制描述时，在 `02_evidence/` 的卡片里写清**来源路径 + 证据强度**。
- **证据强度分层**是本 talk 的硬要求（听众会追问）：〔一手/官方〕/〔⚠️ 厂商自述〕/〔⚠️ 降级取证〕/〔趋势级〕四档必须标。
- 星数、插件数、成本数字一类会随日期漂移的值，一律标观测日期，只作趋势不作基准。

## 规则

1. `_reference/` 下所有 symlink **只在里面读，不在里面写**。
2. 上游结论不能直接当成本 talk 的结论；本 talk 的判断（例如"harness 才是变量"）要显式标注为**本 talk 的解释性结论**，并写清它靠哪几条素材支撑。
3. 素材只摘不搬：不要整段复制上游正文进 `02_evidence/`。
