# AGENTS.md — 根级路由与全局纪律

你在这个仓库里是**被驱动的 agent**：每次进来先路由，再动手，改完把状态落回源文件。
本文件只管**路由与全局纪律**；进到某个 talk 目录后，以该目录自己的 `AGENTS.md` 为准。

**主线**：AI Coding 时代，SDLC 如何变化。
**全景**（三层结构图、仓库外素材表、哪一场在跑）：只在根 `README.md`，本文件不重复。

---

## 1. 进来先读：按最短路径走

**渐进式披露原则：每次会话为拿到行动权所付的读取量要最小。分层如下——**

| 层 | 文件 | 何时读 |
|---|---|---|
| L0 常驻 | 本文件（自动注入） | 免读 |
| L1 全景 | 根 `README.md` | **落点不明时才读**；落点已明确可跳过 |
| L2 talk 状态 | 该 talk 的 `CURRENT.md`（热区） | 进入 talk 后必读，最短行动入口 |
| L2 talk 纪律 | 该 talk 的 `AGENTS.md` / `CONTEXT.md` | 首次进入该 talk、或写对客文字、或踩坑时读 |
| L2 talk 冷区 | 该 talk 的 `CURRENT-history.md`（若有） | 只在需要回查历史轮次时读，**默认不读** |
| L3 内容 | 管道目录下的具体文件 | 真正动手时读 |

**读序**：① 判定落点（第 2 节）→ ② 落点明确 → 直接进该目录读 `CURRENT.md`（若无则读其 `README.md`）；
落点不明 → 先读根 `README.md` 再判。③ 动手前按该目录自己的 AGENTS.md 补纪律。

不要凭聊天记忆代替读文件。目录里已落盘的状态与聊天记忆冲突时，**以目录中彼此一致的当前态为准**。

---

## 2. 路由：这句话落在哪一层

| 信号 | 落点 | 动作 |
|---|---|---|
| 提到某一场 talk 的页、稿、版次、视觉、PPTX、故事线 | **交付层** `talk-ai-coding-evolution-*/` | 进对应 talk，按它自己的 `AGENTS.md` 走（`-agent-101` **无 `AGENTS.md`**，按它的 `README.md` + `CONTEXT.md`） |
| 提到证据、来源卡片、口径、回源 | 先确认属于哪场 talk | 走该 talk 的 `02_evidence/`，不要动根级 `01_sources/` |
| 泛泛谈研究主题、要补素材、要写一篇新研究 | **研究层** `01_sources/` / `02_research/` | 见第 4 节 |
| 提到需求工程 / SDD / SDD 后继形态等 SDLC 实践体系，要改实践方法论文档 | **实践层** `03_practice/` | 见第 4 节；先读该目录 README 的分工与单一事实源约定 |
| 提到 BPM、企业信息加工流、企业 AI 重构案例 | **研究层·映射** `04_enterprise/` | 沉淀状态：改前先确认是否为某场 talk 服务，是则走该 talk 的 `02_evidence/` |
| 提到主线 Keynote / deck_ai_sdlc_keynote | **产出层** `05_output/` | 历史主线稿（2026-08 后未推进）；talk 交付不依赖它 |
| 说"这个仓库 / 这个项目"、要改 README、要整理结构 | **根级** | 改 `README.md` / 本文件 |

**判不出来就问，不要猜。** 尤其是"这场 talk"没指名时——四场 talk 的对象、篇幅、红线完全不同，猜错代价很高。

**默认优先交付层**：主线活跃工作在 `talk-ai-coding-evolution-harness/`；**入门场**在
`talk-ai-coding-evolution-agent-101/`（20–30 min，面向会用 AI 但不写代码的人）。
没有任何上下文线索时，先去读 `harness/CURRENT.md` 确认主线，再看 `agent-101/CURRENT.md`。

---

## 3. talk 目录的入口件与子目录标准件

每个 talk 目录是一套自带管道的工作区，**入口件职责固定**：

| 文件 | 职责 | 热度 |
|---|---|---|
| `README.md` | 地图、素材说明、工作方式（talk 全景的唯一权威） | 冷，首次进入读 |
| `AGENTS.md` | 该 talk 的 agent 手册：仪式 / 门禁 / 红线 / 已知陷阱 / 工具链 | 冷，首次进入或踩坑读 |
| `CURRENT.md` | ★ 当前态唯一权威：做到哪、下一步动哪个文件。**只放热区**：一句话 / 状态表 / 定调 / 下一步 / 验收清单 / 缺口 | **热，每次必读** |
| `CURRENT-history.md` | 冷区：已收口的历轮改动与口径记录，append-only，**不是第二权威** | 冷，按需回查 |
| `CONTEXT.md` | 术语与禁用词唯一权威（`-opc` 无此文件） | 冷，写对客文字前读 |
| ~~`HANDOFF.md`~~ | **不再使用**（2026-09-17 归档）：交接件是一次性临时产物，长期留存会与 `CURRENT.md` 形成双权威 | — |

**管道单向加工**：`01_storyline → 02_evidence → 03_outline → 04_drafts → 05_output`。
上游结论没稳定前，不在下游定稿。review 若改变了成稿，按 `04_drafts → 03_outline → 02_evidence → 01_storyline` **反向同步**。

**每场 talk 的红线写在它自己的 `CONTEXT.md` / `AGENTS.md` 里，不是全局的。**
不要把一场 talk 的禁用词或对象设定套到另一场上（例：harness talk 禁止出现 OPC / 一人公司，这是它独有的，不能反向推导出别的规则）。

**子目录标准件（所有可独立工作的目录通用）**：
- 能独立承载工作流的目录（talk、研究主题、实践主题）至少配一个 **`README.md`**：定位、分工约定、信息往哪放。
- 有"当前进度"概念的目录（talk）加 **`CURRENT.md`**；状态一旦滚出热区就移入冷区文件，热文件不背历史。
- 研究主题内部按 `raw / digested / result` 分层（活跃评估系统 `repo_agent_friendliness` 除外，见 §4 例外）；没有 README 的旧主题，动手前先读目录内现有文档摸清分法，**顺手补一个最小 README**（只写定位与分法，不搬运正文）。

---

## 4. 研究层与实践层怎么动

`01_sources/` / `02_research/` / `03_practice/` / `04_enterprise/` 目前是**沉淀状态**，不是日常推进对象。
**例外**：`02_research/repo_agent_friendliness/` 是**活跃的评估系统**（2026-09-21 升级）：独立三层分法
（`10-spec / 20-instruments / 90-archive`，被测数据不落本系统——run bundle 归属被测仓库）
且有自己的 `AGENTS.md` 操作手册——路由进去后按它自己的纪律走，不适用本节"沉淀状态"与
本文件 §3 的研究层默认分法。其自举审计会在仓库根产生 `agent-friendly-runs/`（bundle 归档，勿清理）。

- 补素材、改研究结论前，先确认它是否为某场 talk 服务。**是 → 走该 talk 的 `02_evidence/`，不在根级研究层改**，避免事实分散到两处。
- `03_practice/` 是 2026-09-21 自研究层拆出的**实践层**，含四个主题：`requirements_engineering/`、`spec_driven_development/`、`beyond_spec_driven_development/`、`harness_governance/`（2026-09-21 自 beyond 抽出：AI 形态下新的 SDLC——harness/context 治理）。互为兄弟、互相有相对指针，动手前先读各自 README 的分工约定。
- 研究层与实践层遵守统一纪律：一手源优先、来源可溯、标注观测日期。

---

## 5. 全局红线

- **symlink 只读**：`talk-*/_reference/rawdata_*/` 指向仓库外的素材根（四个根的清单见根 `README.md` 第二节）。**只在里面读，不在里面写。** 要引用就摘进该 talk 的 `02_evidence/` 并标注来源路径 + 证据强度。发现断链就报，不要就地新建文件。
- **单一事实来源**：每个事实只写一处；其他文件用指针引用，不复制正文。发现同一事实在两个文件里说法不一致，先停下来问，不要自行"统一"。**本文件与根 `README.md` 的分工即是此纪律的样本：本文件管路由与纪律，README 管结构与素材。**
- **不跨 talk 搬运**：四场 talk 的对象与红线不同。除非用户明确要求，不要把一场的页面、文案或结论搬进另一场。
- **临时产物**：一律放**仓库根目录**、以 `.tmp-` 前缀 + 主题命名（`.gitignore` 已覆盖 `.tmp-*/`，永不入库）；
  该 talk 的 README 若有更具体的前缀约定（如 `.tmp-harness-talk-`），以它为准。版本收口即清理，不跨版本堆积。
- **源头冲突时以有源码锚点的一方为准**：选型研究/二手报告里的产品级结论，与源码消化层冲突时，取带源码锚点的一方（实例：Pi 的 MCP 支持状态）。
- **对外文字不泄露内部命名**：audience-facing 内容里不出现姊妹项目名、内部代号或"参考另一场 talk"这类表述。

---

## 6. 收尾：状态落盘

改完任何一层，都要做一件事：

1. **更新该层的状态文件**——talk 是 `CURRENT.md`（本轮结束即收口：新结论进热区，被取代的记录移入 `CURRENT-history.md`）+ 该 talk 内的 `01_storyline/04-open-questions.md`；根级是 `README.md` / 本文件。
   **例外（`-agent-101`）**：该场管道轻，**不设 `01_storyline/04-open-questions.md`**——
   它的开放问题与待定项登记在 `CURRENT.md` 的「待定 / 缺口」两节（见该场 `README.md` 的目录约定）。
   完成标准：下次进来的人（或零上下文的 agent）只读 L0+L2 热区文件就能接上，不需要聊天记录。

> **跨会话记忆不落盘在本仓库**（`.workbuddy/` 已于 2026-09-21 按用户决定移除）：结构变更与重要决策由 git 提交信息留痕；talk 的长期纪律写进该 talk 自己的 `AGENTS.md` / `CONTEXT.md`。不设仓库级 memory 文件。

---

## 7. 权威入口速查

| 想知道 | 去哪 |
|---|---|
| 这个仓库怎么回事（结构 / 素材 / 四场 talk 对比） | 根 `README.md` |
| 现在哪场在跑、做到哪 | `talk-ai-coding-evolution-harness/CURRENT.md`（主线）/ `talk-ai-coding-evolution-agent-101/CURRENT.md`（入门场） |
| 某个词在这仓库里什么意思 | 对应 talk 的 `CONTEXT.md` |
| 某场 talk 的规矩 | 对应 talk 的 `AGENTS.md` |
| 某场 talk 历史上改过什么 | 对应 talk 的 `CURRENT-history.md`（若有） |

## Python / uv

需要写脚本时用仓库根的 `uv` 环境：`source .venv/bin/activate`，依赖用 `uv sync`。不要把一次性脚本散落在 talk 目录里。
