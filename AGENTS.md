# AGENTS.md — 根级路由与全局纪律

你在这个仓库里是**被驱动的 agent**：每次进来先路由，再动手，改完把状态落回源文件。
本文件只管**路由与全局纪律**；进到某个 talk 目录后，以该目录自己的 `AGENTS.md` 为准。

**主线**：AI Coding 时代，SDLC 如何变化。

---

## 1. 进来先读（按顺序）

1. 根目录 `README.md` —— 全景：两层结构、仓库外素材、当前哪一场在跑。
2. **判定落点**：用户这轮的话属于哪一层（见第 2 节）。
3. 进入对应目录，读它的入口文件（见第 3 节），**再动手**。

不要凭聊天记忆代替读文件。目录里已落盘的状态与聊天记忆冲突时，**以目录中彼此一致的当前态为准**。

---

## 2. 路由：这句话落在哪一层

| 信号 | 落点 | 动作 |
|---|---|---|
| 提到某一场 talk 的页、稿、版次、视觉、PPTX、故事线 | **交付层** `talk-ai-coding-evolution-*/` | 进对应 talk，按它自己的 `AGENTS.md` 走 |
| 提到证据、来源卡片、口径、回源 | 先确认属于哪场 talk | 走该 talk 的 `02_evidence/`，不要动根级 `01_sources/` |
| 泛泛谈研究主题、要补素材、要写一篇新研究 | **研究层** `01_sources/` / `02_research/` | 见第 4 节 |
| 说"这个仓库 / 这个项目"、要改 README、要整理结构 | **根级** | 改 `README.md` / 本文件，并同步 `.workbuddy/memory/` |

**判不出来就问，不要猜。** 尤其是"这场 talk"没指名时——三场 talk 的对象、篇幅、红线完全不同，猜错代价很高。

**默认优先交付层**：当前活跃工作在 `talk-ai-coding-evolution-harness/`。没有任何上下文线索时，先去读它的 `CURRENT.md` 确认。

---

## 3. 进入某个 talk 后的强制动作

每个 talk 目录是一套自带管道的工作区，**入口五件套**：

| 文件 | 职责 |
|---|---|
| `README.md` | 地图、素材说明、工作方式 |
| `AGENTS.md` | ★ 该 talk 的 agent 手册：步骤、门禁、红线 |
| `CURRENT.md` | ★ 当前态唯一权威：做到哪一步、下一步动哪个文件 |
| `CONTEXT.md` | 术语与禁用词唯一权威（`-opc` 无此文件） |
| `HANDOFF.md` | 零上下文新对话的交接文档（`-harness` 有，新对话优先读它） |

**管道单向加工**：`01_storyline → 02_evidence → 03_outline → 04_drafts → 05_output`。
上游结论没稳定前，不在下游定稿。review 若改变了成稿，按 `04_drafts → 03_outline → 02_evidence → 01_storyline` **反向同步**。

**每场 talk 的红线写在它自己的 `CONTEXT.md` / `AGENTS.md` 里，不是全局的。**
不要把一场 talk 的禁用词或对象设定套到另一场上（例：harness talk 禁止出现 OPC / 一人公司，这是它独有的，不能反向推导出别的规则）。

---

## 4. 研究层怎么动

`01_sources/` / `02_research/` / `03_enterprise/` 目前是**沉淀状态**，不是日常推进对象。

- 补素材、改研究结论前，先确认它是否为某场 talk 服务。**是 → 走该 talk 的 `02_evidence/`，不在根级研究层改**，避免事实分散到两处。
- `02_research/` 下多数主题没有统一 README，动手前先读该主题目录内的现有文档，摸清它的 `raw / digested / result` 分法再改。
- 研究层遵守统一纪律：一手源优先、来源可溯、标注观测日期。

---

## 5. 全局红线

- **symlink 只读**：`talk-*/_reference/rawdata_*/` 指向仓库外的素材根（`/Users/bowhead/ai_tool_deepresearch/`、`deepseek-harness/`、`awesome-dsh-plugin/`、`pi-mono/`）。**只在里面读，不在里面写。** 要引用就摘进该 talk 的 `02_evidence/` 并标注来源路径 + 证据强度。发现断链就报，不要就地新建文件。
- **单一事实来源**：每个事实只写一处；其他文件用指针引用，不复制正文。发现同一事实在两个文件里说法不一致，先停下来问，不要自行"统一"。
- **不跨 talk 搬运**：三场 talk 的对象与红线不同。除非用户明确要求，不要把一场的页面、文案或结论搬进另一场。
- **临时产物**：一律放**仓库根目录**、以 `.tmp-` 前缀 + 主题命名（`.gitignore` 已覆盖 `.tmp-*/`，永不入库）；
  该 talk 的 README 若有更具体的前缀约定（如 `.tmp-harness-talk-`），以它为准。版本收口即清理，不跨版本堆积。
- **源头冲突时以有源码锚点的一方为准**：选型研究/二手报告里的产品级结论，与源码消化层冲突时，取带源码锚点的一方（实例：Pi 的 MCP 支持状态）。
- **对外文字不泄露内部命名**：audience-facing 内容里不出现姊妹项目名、内部代号或"参考另一场 talk"这类表述。

---

## 6. 收尾：状态落盘

改完任何一层，都要做两件事：

1. **更新该层的状态文件**——talk 是 `CURRENT.md` + `01_storyline/04-open-questions.md`；根级是 `README.md` / 本文件。
   完成标准：下次进来的人（或零上下文的 agent）读这些文件就能接上，不需要聊天记录。
2. **写工作记忆**——追加 `.workbuddy/memory/YYYY-MM-DD.md`（按日期，追加不覆盖）；
   属于长期约定的（目录职责、命名规则、用户明确要求的工作方式）写进 `.workbuddy/memory/MEMORY.md`。
   不记录临时路径、搜索片段和工具报错。

---

## 7. 权威入口速查

| 想知道 | 去哪 |
|---|---|
| 这个仓库怎么回事 | 根 `README.md` |
| 现在哪场在跑、做到哪 | `talk-ai-coding-evolution-harness/CURRENT.md` |
| 某个词在这仓库里什么意思 | 对应 talk 的 `CONTEXT.md` |
| 某场 talk 的规矩 | 对应 talk 的 `AGENTS.md` |
| 长期约定与踩坑记录 | `.workbuddy/memory/MEMORY.md` |

## Python / uv

需要写脚本时用仓库根的 `uv` 环境：`source .venv/bin/activate`，依赖用 `uv sync`。不要把一次性脚本散落在 talk 目录里。
