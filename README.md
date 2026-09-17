# ai_dev_sdlc_aidc

**主线**：AI Coding 时代，SDLC 如何变化。

这不是一个单一交付项目，而是一个**围绕同一主线持续生长的工作站**：一端沉淀长期研究，另一端按场交付 Keynote。
从根目录看最容易迷路的地方是——**它其实由两层构成，而且两层的活跃度已经发生了转移**。先把这件事说清。

---

## 一、两层结构：研究层 + 交付层

```
ai_dev_sdlc_aidc/
│
├── 01_sources/      研究层 · 证据     一手信号、论文、人物与厂商参考库
├── 02_research/     研究层 · 分析     10 个主题，各自 raw → digested → result
├── 03_enterprise/   研究层 · 映射     SDLC 在企业侧的等价物（BPM）与案例
├── 04_output/       研究层 · 产出     主线 Keynote（deck_ai_sdlc_keynote）
│
├── talk-ai-coding-evolution-opc/       交付层 · 已归档（23 页 / 45 min）
├── talk-ai-coding-evolution-org-sdlc/  交付层 · 待 review（50 页 / 75–90 min）
└── talk-ai-coding-evolution-harness/   交付层 · ★ 当前活跃（45 页 + 4 停顿页 / 75–90 min）
```

**研究层**（`01`–`04`）在 2026-07～08 建立，是长期素材与认知底座，目前处于**沉淀状态**，不再逐日推进。
**交付层**（`talk-*`）从 2026-08 起成为工作重心：每一场 talk 是一个自带完整管道的独立工作区。

两层不是串联关系——`talk-*` 里的 talk **不依赖** `04_output/deck_ai_sdlc_keynote`，各自独立成篇，
直接通过 `_reference/` 的 symlink 从仓库外取材（见下一节）。

---

## 二、上游素材在仓库外，靠 symlink 挂进来

这是新人（和新对话的 agent）最容易看不懂的一点：**原始素材不在这个仓库里**。

仓库外有四个素材根，各 talk 通过 `_reference/rawdata_*/` 的 symlink 只读引用：

| 仓库外素材根 | 提供什么 |
|---|---|
| `/Users/bowhead/ai_tool_deepresearch/` | 五层演变研究报告、Harness Agent 选型研究（含一手来源卡片 305 张） |
| `/Users/bowhead/deepseek-harness/` | DSH 源码消化 + 机制问答 |
| `/Users/bowhead/awesome-dsh-plugin/` | DSH 插件生态分布快照 |
| `/Users/bowhead/pi-mono/` | Pi 源码消化 + 二次研究问答（含 Pi vs DSH 对照） |

**铁律：symlink 指向的目录只读。** 要引用就摘进 talk 自己的 `02_evidence/`，并标注来源路径与证据强度。
看到 `_reference/` 里有断链，说明素材根不在本机或已移动，不要就地创建文件"补上"。

---

## 三、当前状态：哪一场在跑

| 目录 | 规格 | 状态 | 说明 |
|---|---|---|---|
| `talk-ai-coding-evolution-harness/` | 45 页正文 + 4 停顿页 / 75–90 min | ★ **活跃** | 页面职责与生产稿已成型，正在推进 PPTX |
| `talk-ai-coding-evolution-org-sdlc/` | 50 页 / 75–90 min | 暂停在 review | v0.16 已渲染，等用户确认视觉门禁 |
| `talk-ai-coding-evolution-opc/` | 23 页 / 45 min | 已定稿（v8） | **只作内部参考**，其命名与内容不得出现在其他 talk 的对客文字里 |
| `04_output/deck_ai_sdlc_keynote/` | 40 min / 标准档 | 历史主线稿 | Phase 0 研究与 v1 大纲/讲稿已产出，2026-08 后未继续推进（`project-metadata.yaml` 中 phases 仍标 pending） |

> **不确定该动哪里时，先看 `talk-ai-coding-evolution-harness/CURRENT.md`**——它是当前态的唯一权威。

---

## 四、研究层四个桶

| 桶 | 定位 | 内容 |
|---|---|---|
| `01_sources/` | **证据层** | 一手信号与资料来源，按形态组织：真实使用样本（`field_samples/`）、学术论文（`papers/`）、人物与厂商参考库（`reference/kol` + `reference/corp`） |
| `02_research/` | **分析层** | 10 个主题，多数是自包含的 `raw → digested → result` 管道：需求工程、工程实践、反馈回路、管理与编排、多智能体团队、研发体系迁移、ThoughtWorks 方法论、前沿议题、Anthropic 实践、研发原生 2.0 |
| `03_enterprise/` | **企业视角** | SDLC 在企业侧的映射：BPM 作为企业信息加工流的等价物，以及企业 AI 重构案例 |
| `04_output/` | **产出层** | 主线 Keynote 交付物（含完整制作流程 `WORKFLOW.md` 与阶段管线） |

各研究主题遵守统一的信息处理纪律：**一手源优先、来源可溯、聚焦当前时刻**。
参考库的"来源/时间铁律"见 `01_sources/reference/kol/README.md` 与 `01_sources/reference/corp/README.md`。

> 注意：`02_research/` 下只有 `rnd_native_2.0/` 带 README，其余主题的口径写在各自目录内的文档里，没有统一入口。

---

## 五、从哪开始读

**人：**

1. 本文件（全景）
2. 想去活跃项目 → `talk-ai-coding-evolution-harness/README.md`
3. 想知道现在做到哪 → `talk-ai-coding-evolution-harness/CURRENT.md`

**agent：** 读根目录的 `AGENTS.md`，它会把你路由到正确的一层。

---

## 六、通用约定

- **临时目录**：一次性产物（构建中间体、逐页 inspect、审稿草稿）一律放仓库根目录，`.tmp-` 前缀，已被 `.gitignore` 覆盖、永不入库。版本收口即清理，不跨版本堆积。
- **记忆位置**：跨对话的项目记忆写在 `.workbuddy/memory/`（日志按日期、长期约定在 `MEMORY.md`）；
  每个 talk 的 `README.md`（地图）+ `CURRENT.md`（当前态）+ `AGENTS.md`（手册）面向"零上下文新对话"。
  **不设 HANDOFF 类交接文件**——它是某一次对话的临时件，长期留存会与 `CURRENT.md` 形成双权威。
- **单一事实来源**：每个事实只写一处，其他文件用指针引用，不复制。

## Python / uv

本目录已初始化为 `uv` 管理的 Python 项目，本地虚拟环境 `.venv`。
需要补自动化脚本或数据处理脚本时优先用 Python，统一依赖管理与执行方式。

- 激活环境：`source .venv/bin/activate`
- 安装依赖：`uv sync`
- 根目录 `.env` 存放图片生成相关配置，不入库。
