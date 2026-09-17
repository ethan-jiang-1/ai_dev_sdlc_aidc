# 内容吸纳清单与口径红线（v0.1）

> 依据 `../_reference/README.md` 列出的十一份上游素材。本文件定"进什么货"和"什么话不能说"。
> 页编号以 `../03_outline/00-page-structure-v3.md`（36 页）为准。

## 一、进货单（哪页吸哪个锚点）

### 开场（P1–P4）

| 页 | 吸什么 | 来源 |
|---|---|---|
| P2 | 断言与追问（本 talk 自拟，无外部来源） | 立场（`01_storyline/01-thesis-and-positions.md` A1） |
| P3 | 承诺页（本 talk 自拟） | — |
| P4 | 五层 + harness + 两个进展的地图 | `00-storyline-map.md` |

### 第一幕 五层（P5–P13）

| 页 | 吸什么 | 来源 |
|---|---|---|
| P5 | 驱动机制：模型越强 → 单次交互边际工程收益越低 → 工程杠杆点上移；上移不等于替代 | 报告 01/02/06 章 |
| P6 | prompt 措辞重要性下降的观察 | 报告 01 章（⚠️ 注意口径，见第三节） |
| P7 | context rot（"更多 context ≠ 更好回忆"）；最小脚手架的表述 | 报告 02 章（**上屏前回源核对**，见 04-open-questions 待办） |
| P8 | `Agent = Model + Harness`；harness = 模型之外的一切 | 报告 03 章（Böckeler） |
| P9 | loop 黄金法则；"loop 可能错得更贵"的反转 | 报告 04 章 |
| P10 | graph 本质 = 编排（显式节点、边、状态）；可编排部分 loop | 报告 05 章 |
| P11 | 成熟度标尺：前三层成熟、Loop/Graph 新兴低置信度；五层是叠加 | 报告 06 章 |
| P12 | 团队版焊点（本 talk 新增）：五个控制面散在不同人手上 | 立场（A7） |
| P13 | 转场（本 talk 自拟） | — |

### 第二幕 harness 内部（P14–P23）

| 页 | 吸什么 | 来源 |
|---|---|---|
| P14 | 每个可执行节点最终落到一次真实执行 | 报告 04/05/06 章 |
| P15 | 模型给能力、harness 给可靠性 | 报告 03 章 + `01_storyline/06-harness-internals.md` |
| P16 | Guides（前馈）/ Sensors（反馈）两套控制 | 报告 03 章（Böckeler） |
| P17 | computational（可审计）vs inferential（不可审计）；确定性优先 | 同上 |
| P18–P20 | 圈住 / 拦住 / 看清；六个构件；**团队映射三行** | 同上 + `06-harness-internals.md` |
| P21 | 提议 → 独立检查 → 放行/拒绝并记录；GraphARC 的 plan → check → execute | 报告 04/05/06 章 |
| P22 | 2026 执行时授权缺失的因果链；`authorize at execution, not at generation` | 报告 03 章第六节 |
| P23 | 转场（本 talk 自拟） | — |

### ★ 第三幕 harness 才是变量（P24–P30）

| 页 | 吸什么 | 来源 |
|---|---|---|
| P25 | Codex Harness 开源（Apache-2.0，2026-08-20）；ARC-AGI-3 13.3% → 38.3%；**输出 token 少 6 倍**（一手口径是"输出 token"，不是"同任务 token"）；三层形态 `codex exec` / SDK / `app-server`；审批协议内建 | `rawdata_harness-selection-final/final_v3.md` §2.2 C2、§5.2 |
| P26 | 第三方 8-harness 对照实测的方向性信号 | 同上 §5.4 发现 8（⚠️ flash/news 级） |
| P27 | 主流固定 harness 的共同特征（沙箱、审批、事件流、长程记忆） | 同上 §2.2、§5.1（⚠️ 多为厂商文档主张） |
| P28–P29 | 五个自查维度的**框架**为本 talk 自拟；底层依据来自评分卡的"可部署 / 合规"两维与 capability seam 概念 | 立场 + 同上 §3、§5.3 |
| P30 | 转场（本 talk 自拟） | — |

### ★ 第四幕 Pi 与 DSH（P31–P38）

| 页 | 吸什么 | 来源 |
|---|---|---|
| P31 | `Framework First` vs `Product First` 的结构判断；"早期要速度用 Codex，企业要可控/私有化用 DSH"（⚠️ 媒体共识口径） | 同上 §5.5 发现 6 |
| P32 | Everything is a Plugin（Cordis）；**无特权核心**；"There is no privileged core to patch"。**并入两页**（D15）：四种运行模式 = 四套默认插件集（标准 / PTC / 极简 / 创造）；长程不是单一 loop——Goal / Ralph / workflow / Spawn-Fork 并存，层级式而非 swarm | 同上 §5.5 发现 1/2/5；`rawdata_dsh-digested/system/00-map.md` |
| P33 | append-only 类型化 SessionEvent 日志（single source of truth）；模型所见即被记录；回放/恢复/分叉/审计是投影 | 同上 §5.5 发现 4 |
| P34 | 官方插件市场未上线；第三方商店口径不可比；v0.1 接口快变；二次开发量高于 Product First | 同上 §5.5 发现 7/8 + §5.5 合规小节 |
| P35 | **Pi 的结构好在哪**：三层同心 seam（operations / tool / extension）按"变化轴"裁剪接口大小；统一注入点；分发闭环；生命周期护栏（两阶段绑定、stale 保护、**fail-close**）。补充：~9 万 star（趋势值，见红线 3） | `rawdata_pi-digested/harness/01-Architecture/`（1.1–1.4）；对照 `rawdata_harness-selection-final/final_v3.md` §5.4 |
| P36 | **Pi 的代价在哪**：四条短板——① **无默认沙箱**（扩展 = 宿主进程同等权限，`pi install` 陌生包 ≈ 执行任意代码）② 无 MCP/ACP（生态锁定，外部工具付适配层税）③ 内层 AgentLane 半成品 ④ 无扩展 API 版本契约。讲法见红线 13/14 | `rawdata_pi-digested/harness/02-Boundaries/`（2.1–2.4） |
| P37 | **两边都还没解决的那件事**：**"对陌生插件安全：两个都烂"**（Pi 无沙箱；DSH 插件化 ≠ 安全）→ 这两条都不是"更先进的选择"，是"**正在演进的路线**" | `rawdata_pi-faq-on-digested/06_pi_vs_dsh/04_strengths_weaknesses.md` 逐面强弱表；`.../03_mechanism_table.md` |
| P38 | 本 talk 的落点：两条路线的共同点——harness 从"产品的一部分"变成"你可以改的东西" | 立场（A8） |

### ★ 第五幕 + 收尾（P39–P45）

| 页 | 吸什么 | 来源 |
|---|---|---|
| P39–P41 | 三句落点与判据框架（本 talk 自拟） | 立场（A6/A7/A9） |
| P42 | "先用好手上的"默认答案；可组合路线另需承担治理自建成本（DSH 的 marketplace 缺口、Pi 的权限组装成本） | 同上 §5.4/§5.5 风险提示 |
| P43–P45 | 收束与 slogan | 立场 |

## 二、本 talk 的解释性结论（不是上游结论）

以下四条必须在讲法上"认领"为**本 talk 的判断**，不能假借报告背书：

1. **瓶颈已从生成移到交付**（A1）。
2. **Loop / Graph 补不上缺失的运行边界，所以问题落回 harness**（A3）。
3. **同一个模型换 harness 就是两套交付系统**（A6）——证据偏弱，必须标注。
4. **团队里那圈东西最容易散，一致性是团队专属问题**（A7）——本 talk 的观察；
   **其后果一侧已于 2026-09-16 补上外部依据**：五层 stack 综述的组织含义段
   （`rawdata_ai-coding-evolution-reference/00-cross-five-layer-stack-w4f-203.md`）指出，
   只用最上层、忽略权限的团队"会被 agent 违规惩罚"，成熟组织是五层都用、每层都有显式验证门。

## 三、口径红线（引用前必查）

| # | 事项 | 正确口径 |
|---|---|---|
| 1 | Codex 的能力提升数字 | ⚠️ **厂商自述**（developers.openai.com 博客），无第三方审计；ARC-AGI-3 13.3% → 38.3%；**一手表述是"输出 token 少 6 倍"**，不要说成"同任务 token 降 1/6"。同屏必须标"厂商自述" |
| 2 | 8-harness 对照实测 | ⚠️ **趋势级**：flash / news 类来源、无方法论文档。只作方向性信号，**不作基准结论** |
| 3 | Pi 的 GitHub star | **趋势值**，随文章日期漂移（同期 86k–98k 浮动），观测 2026-09-06。不画增长曲线 |
| 4 | DSH 插件数量 | 约 300 → 约 3000（发布后数天内，媒体口径）；第三方商店 2000+ / 3000+ **口径互不可比**。不合成一个数字 |
| 5 | DSH 的原生机制 | **不是 MCP**。说 `ctx.llm` adapter、`ctx.tools`、capability seam、plugin |
| 6 | Pi 的安全通告 | 讲**因果与后果**（无内置权限模型 + 项目本地扩展加载边界），**不堆 CVE 编号**；受影响版本区间与修复节奏素材里未定论，不复述具体版本 |
| 7 | durability / 持久化争议 | 素材里有明确对立双方（厂商文档 vs 源码级批评），若要引用必须**成对保留**，不单取一方 |
| 8 | "内置项目管理能力"一类声明 | 有媒体口径与一手机制口径的**张力**，不采信为事实 |
| 9 | 车规 / 行业合规准入口径 | 素材中该部分依赖委托方内部数据、未作答；本 talk 不引用 |
| 10 | 五层的成熟度 | 前三层成熟可信；**Loop / Graph 是 2026 夏才冒头的新兴叙事、低置信度**，不讲成既定生产范式 |
| 11 | Graph 与 Loop 的关系 | Graph **可以**编排 Loop，也可包含工具、验证器；不能把所有 Graph 节点画成 Loop |
| 12 | 听众相关 | **不出现 OPC / 一人公司 / 姊妹项目**；**不点行业名、不用行业专属术语** |
| 13 | **Pi 有没有 MCP** —— 两份素材冲突 | 选型研究 §5.4 发现 2 引 PR #3774（MCP extension）并标注"merged/发布状态未确认"；而 `rawdata_pi-digested`（基线 v0.84.4，2026-09-01 同步）**源码级核对结论是"没有 MCP/ACP 实现，grep 只有误匹配"**。→ **采信有源码锚点的一份**：讲 Pi 时说"**没有 MCP/ACP 实现，生态锁在自家 extension API，外部工具要付适配层税**"；不要把 PR #3774 当成已 GA 能力 |
| 14 | Pi 的"无沙箱"怎么说 | 不能说成"Pi 不安全"。正确口径是 **"Pi 把信任放在'谁装了它'，而不是'它是什么代码'上"**；沙箱存在但只是 opt-in 示例（`grep` 到的 example 是"给你看怎么做"，不是"帮你做了"）。且必须区分：Pi 有"沙箱执行工具"的思路，**没有"沙箱运行扩展代码"的机制**——只防了前者 |
| 15 | 涉及 harness 评价时 | `rawdata_pi-digested/harness/` 是**评价文档**，硬事实 / 解释 / 推测分开标。引用时必须保留这个分层，不要把评价写成源码事实 |

## 四、下一步

- [x] **三处回源核对全部完成（2026-09-16）**——P6 / P7 / P25，定稿引文见第五节 5.2。
- [ ] P27–P29 的"五个自查维度"需要补证：现有素材只覆盖 Codex 与 Claude 系的接口形态，
      其余产品改成不带产品名的通用说法，或补证后再点名。
      **（进展：一手卡片层已接入，`*_reference/03_harness-runtime-deployment-fit/` 里有部署面卡片，可先查）**
- [x] 证据强度标注的**统一写法**已定稿并写进 `CONTEXT.md` 第四节（一手 / ⚠️ 厂商自述 / ⚠️ 降级取证 / 趋势级）。

---

## 五、一手来源卡片层与回源核对结果（2026-09-16 补链）

### 5.1 补链：中间那一层此前没接

此前 `_reference/` 只接了「综合层（`*-final/` 报告）」与「消化层（pi / dsh 源码消化）」，
**中间的「一手来源卡片层」305 张一张都没接**——这正是 P6 / P7 长期挂在"待回源"的真正原因：
**要核的料压根不在库里。**

新增两条只读 symlink：`rawdata_ai-coding-evolution-reference/`（137 张）
与 `rawdata_harness-selection-reference/`（168 张）。素材总量 463 → **768 文件 / 5.9M**。

**⚠️ 检索陷阱**：`_reference/` 全是 symlink，`Grep` / `find` **默认不跟随** → 会看到 0 命中或空目录。
在本目录里搜东西必须走真实路径，或显式加 `-L`。

### 5.2 三处回源核对的定稿引文（可直接上屏 / 被追问时引用）

| 页 | 原状态 | 核对结果 | 出处与强度 |
|---|---|---|---|
| **P6** | ⚠️ 量化口径待核对 | 原文是**定性判断**：`the exact formatting of prompts is likely becoming less important as models become more capable`。**它不是量化结论**——上屏与讲稿都不能说成"效率掉了百分之多少"。另：同一体系 2026 年讲 prompt 缓存的文章说明 prompt 基本功在 harness 时代仍然有效，正好支撑本页"没白学"的兜底句 | Anthropic 官方工程博客 **2025-09-29**《Effective context engineering for AI agents》· **一手** |
| **P7** | ⚠️ 上屏前必须回源核对 | ① **context rot** 的独立量化：`model performance varies significantly as input length changes, even on simple tasks`——但 **Chroma 是向量库厂商，属厂商自建可复现评测，不是中立第三方**；② **最小脚手架**有一字不差的一手原文：`keep the scaffolding minimal.` **`The agent has a prompt, a Bash Tool, and an Edit Tool.`** | ① Chroma《Context Rot》2025-07 · 一手但**厂商自建**；② Anthropic SWE-bench Verified 公告 **2024-10-30**（49%）· **一手** |
| **P25** | ⚠️ 一手表述需复核 | 确认：GPT-5.6 Sol 在 ARC-AGI-3 **13.3% → 38.3%**、**输出 token 少 6 倍**；三层集成 `codex exec` / 官方 SDK / `app-server`（threads-turns-events-approvals）；human-approval 协议内置。此前二手报道为 **Tier 4**，核验后升 **Tier 1**。⚠️ 仍是**厂商自述**、无第三方审计；Relay 示例应用**显式声明虚构数据、非 production** | developers.openai.com 官方博客 · **厂商自述** |

### 5.3 顺带挖到、可加固其他页的素材（**尚未上屏，登记备选**）

| 用来加固 | 素材 | 能补什么 |
|---|---|---|
| **P12 团队焊点** | `rawdata_ai-coding-evolution-reference/00-cross-five-layer-stack-w4f-203.md` | 该 finding 的**组织含义**段：只用最上层、忽略 harness 权限的团队"会被 agent 违规惩罚"；成熟组织是**五层都用、每层都有显式验证门**。→ **本 talk 的团队版论点第一次有了外部素材**（A7 此前标注"本 talk 观察、无外部素材"） |
| **P5 发动机** | 同上（W4F-203 的 attention-upward mechanism） | 比"边际收益下降"更锋利的说法：**每一层都对下面一层做了一个假设**——Prompt→Context 假设"模型能吃上下文"；Context→Harness 假设"环境受控"；Harness→Loop 假设"单次运行受控"；Loop→Graph 假设"单 agent 受控"。**每个假设在极限处都可能失效** |
| **P15 / P16 / P17** | `00-shared-harness-engineering.md` → `martinfowler.com/articles/harness-engineering.html` | 精确出处：**Böckeler，memo 2026-02-17 / 全文 2026-04-02**；一手原句 **`Reliability is a property of the model-plus-harness system`**——P15 金句的出处 |
| **P24 命题** | `01_concept-evolution-...-www-anthropic-com-news-swe-bench-sonnet-...md` | **"同一模型换脚手架"的先例**：SWE-bench Verified 49%（Claude 3.5 Sonnet，2024-10-30）时，"around the same model"优化脚手架就改变了成绩——比 Codex 更早的历史旁证 |
| **P26 判据** | `05_stories-...-arxiv-org-abs-2506-12286-...md` | 《The SWE-Bench Illusion》（**ICSE 2026 SEIP，Tier 1 学术**）：光看 issue 文本报出 bug 文件 **76%**；换成未见于 SWE-Bench 的仓库**只剩 53%**；5-gram 相似度 35% vs 18%。→ "榜单分数本身也可能掺记忆"，是"基准门槛比看上去高"的学术支撑（**已用于 P26 的 L3 第 4 条**） |
| **P26 / P19 / P20** | `00-shared-swebench.md`（arXiv 2310.06770，Tier 1） | `Tests as an executable contract`；可比性受 dataset leakage / patch gaming / 环境差异影响 |

### 5.4 素材纯净度提示

`rawdata_harness-selection-*` 是**为「项目执行 agent 选型（PM / PMO 域）」做的研究**，
9 个主题里 **06–09**（PM agent 生态 / ChatBI-NL2SQL / agent 接口协作 / 行业合规平台）**与本 talk 无关**，
约占该 bundle 的一半。**引用前先看文件名前缀与卡片 frontmatter 的 `related_topic_uid`**，
别把无关主题的数字带进场。与本 talk 相关的只有 **01–05** 五个主题。
