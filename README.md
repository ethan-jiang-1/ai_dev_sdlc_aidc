# ai_dev_sdlc_aidc

**主线**：AI Coding 时代，SDLC 如何变化。

这不是一个单一交付项目，而是一个**围绕同一主线持续生长的工作站**：一端沉淀长期研究与实践方法，另一端按场交付 Keynote。
从根目录看最容易迷路的地方是——**它其实由三层构成，而且各层的活跃度已经发生了转移**。先把这件事说清。

---

## 一、三层结构：研究层 + 实践层 + 交付层

```
ai_dev_sdlc_aidc/
│
├── 01_sources/        研究层 · 证据     一手信号、论文、人物与厂商参考库
├── 02_research/       研究层 · 分析     9 个主题，各自 raw → digested → result
├── 03_practice/       实践层 · 方法     SDLC 工程实践体系：需求工程、SDD 工具生态、SDD 后继形态（2026-09-21 自研究层拆出）
├── 04_enterprise/     研究层 · 映射     SDLC 在企业侧的等价物（BPM）与案例
├── 05_output/         产出层            主线 Keynote（deck_ai_sdlc_keynote）
│
├── talk-ai-coding-evolution-opc/       交付层 · 已定稿 v8（23 页 / 45 min，只作内部参考）
├── talk-ai-coding-evolution-org-sdlc/  交付层 · 待 review（50 页 / 75–90 min）
└── talk-ai-coding-evolution-harness/   交付层 · ★ 当前活跃（42 张 = 37 页正文 + 5 停顿页 / 75–90 min）
```

**研究层与实践层**（`01`–`05`）在 2026-07～08 建立，是长期素材与认知底座，目前处于**沉淀状态**，不再逐日推进。
其中 `03_practice/` 是 2026-09-21 从研究层拆出的**实践层**：需求工程、SDD、SDD 后继形态这三个主题的内容已经是可执行的工程实践与方法论，不再算"研究"。
**交付层**（`talk-*`）从 2026-08 起成为工作重心：每一场 talk 是一个自带完整管道的独立工作区。

各层不是串联关系——`talk-*` 里的 talk **不依赖** `05_output/deck_ai_sdlc_keynote`，各自独立成篇，
直接通过 `_reference/` 的 symlink 从仓库外取材（见下一节）。

---

## 二、上游素材在仓库外，靠 symlink 挂进来

这是新人（和新对话的 agent）最容易看不懂的一点：**原始素材不在这个仓库里**。

仓库外有**四个素材根**（各 talk 内的 `_reference/rawdata_*` symlink 多于四个——同一素材根会被多场 talk 多个位置挂载，以根计为四），各 talk 通过 `_reference/rawdata_*/` 的 symlink 只读引用：

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
| `talk-ai-coding-evolution-harness/` | 37 页正文 + 5 停顿页 = 42 张 / 75–90 min | ★ **活跃** | v3.3 全链已走完，PPTX v0.4 待 review；生产路线已改为「内容事实源 → handoff 稿」 |
| `talk-ai-coding-evolution-org-sdlc/` | 50 页 / 75–90 min | 暂停在 review | v0.16 已渲染，等用户确认视觉门禁 |
| `talk-ai-coding-evolution-opc/` | 23 页 / 45 min | 已定稿（v8） | **只作内部参考**，其命名与内容不得出现在其他 talk 的对客文字里 |
| `05_output/deck_ai_sdlc_keynote/` | 40 min / 标准档 | 历史主线稿 | Phase 0 研究与 v1 大纲/讲稿已产出，2026-08 后未继续推进（`project-metadata.yaml` 中 phases 仍标 pending） |

> **不确定该动哪里时，先看 `talk-ai-coding-evolution-harness/CURRENT.md`**——它是当前态的唯一权威。

---

## 四、研究与实践层：五个桶

| 桶 | 定位 | 内容 |
|---|---|---|
| `01_sources/` | **证据层** | 一手信号与资料来源，按形态组织：真实使用样本（`field_samples/`）、学术论文（`papers/`）、人物与厂商参考库（`reference/kol` + `reference/corp`） |
| `02_research/` | **分析层** | 9 个主题，多数是自包含的 `raw → digested → result` 管道：工程实践、反馈回路、管理与编排、多智能体团队、研发体系迁移、ThoughtWorks 方法论、前沿议题、Anthropic 实践、研发原生 2.0（需求工程与 SDD 两主题已于 2026-09-21 拆出至 `03_practice/`） |
| `03_practice/` | **实践层** | SDLC 工程实践与方法论的沉淀（2026-09-21 自研究层拆出，用户判定其内容已是 practice 而非 research）：`requirements_engineering/`（需求表达格式）、`spec_driven_development/`（SDD 工具生态与辩论）、`beyond_spec_driven_development/`（SDD 批判之后的形态光谱，含最靠谱判断） |
| `04_enterprise/` | **企业视角** | SDLC 在企业侧的映射：BPM 作为企业信息加工流的等价物，以及企业 AI 重构案例 |
| `05_output/` | **产出层** | 主线 Keynote 交付物（含完整制作流程 `WORKFLOW.md` 与阶段管线） |

各研究主题遵守统一的信息处理纪律：**一手源优先、来源可溯、聚焦当前时刻**。
参考库的"来源/时间铁律"见 `01_sources/reference/kol/README.md` 与 `01_sources/reference/corp/README.md`。

> 2026-09-21：`02_research/` 与 `03_practice/` 已补齐各自的主题索引 README 与最小主题 README，
> 各主题入口见 `02_research/README.md` 与 `03_practice/README.md`。

---

## 五、从哪开始读

**人：**

1. 本文件（全景）
2. 想去活跃项目 → `talk-ai-coding-evolution-harness/README.md`
3. 想知道现在做到哪 → `talk-ai-coding-evolution-harness/CURRENT.md`

**agent：** 读根目录的 `AGENTS.md`，它会把你路由到正确的一层。
**落点明确时不必读本文件**——直接进目标目录读 `CURRENT.md`（热区，最短行动入口）；
本文件只在落点不明、或要动仓库结构 / 素材时读。历轮改动回查该 talk 的 `CURRENT-history.md`。

---

## 六、通用约定

- **临时目录**：一次性产物（构建中间体、逐页 inspect、审稿草稿）一律放仓库根目录，`.tmp-` 前缀，已被 `.gitignore` 覆盖、永不入库。版本收口即清理，不跨版本堆积。
- **记忆位置**：跨对话状态只落在各层权威文件——每个 talk 的 `README.md`（地图）+ `CURRENT.md`（当前态·热区）
  + `AGENTS.md`（手册）面向"零上下文新对话"；已收口的历轮改动移入该 talk 的 `CURRENT-history.md`（冷区，默认不读）；
  结构变更与重要决策由 git 提交信息留痕（仓库级 memory 目录 `.workbuddy/` 已于 2026-09-21 按用户决定移除）。
  **不设 HANDOFF 类交接文件**——它是某一次对话的临时件，长期留存会与 `CURRENT.md` 形成双权威。
- **单一事实来源**：每个事实只写一处，其他文件用指针引用，不复制。

## Python / uv

本目录已初始化为 `uv` 管理的 Python 项目，本地虚拟环境 `.venv`。
需要补自动化脚本或数据处理脚本时优先用 Python，统一依赖管理与执行方式。

- 激活环境：`source .venv/bin/activate`
- 安装依赖：`uv sync`
- 根目录 `.env` 存放图片生成相关配置，不入库。
