# 03_practice — 实践层

**定位**：SDLC 工程实践与方法论的沉淀（2026-09-21 自研究层拆出，用户判定其内容已是 practice 而非 research）。
五个主题**互为兄弟、互相有相对指针**，动手前先读各自 README 的分工约定。

| 主题 | 讲什么 | 入口 |
|---|---|---|
| `requirements_engineering/` | 需求表达格式：AI 时代的导读、主指南、PM 指南、规格架构、示例与术语表 | `requirements_engineering/final/00-reading-guide.md` |
| `spec_driven_development/` | SDD 工具生态（2026-09 景观）、辩论谱系与工具对照 | `spec_driven_development/README.md` |
| `beyond_spec_driven_development/` | SDD 批判之后的形态光谱（可验证规格 / plan mode / 测试优先；02 context 与 03 harness 治理已抽出，速览与判断层留作历史定位） | 目录内编号文档（`01-verifiable-specs.md` 起） |
| `harness_governance/` | ★ AI 形态下新的 SDLC：治理 agent 执行链路（harness + context + 门禁 + 漂移清理）——**环境轴**（诊断轴＝agent 缺哪句话）；2026-09-21 自 beyond 抽出升格，内容权威在分篇 | `harness_governance/README.md` |
| `loop_governance/` | ★ loop 层（五层框架第 4 层）的实践主干：停止条件 / 外层调度 / 自主度分档 / 检查点——**控制轴**（循环怎么跑、谁决定下一轮、人站在哪）；2026-09-26 立题，证据权威在 `02_research/01_agent_engineering/loop_engineering` | `loop_governance/README.md` |

统一纪律：一手源优先、来源可溯、标注观测日期。

## harness 治理与 loop 治理是同构成对的两条轴

- **`harness_governance/`（环境轴）**：单次运行受控——约束写进环境（门禁 / 传感器 / 漂移清理）。
- **`loop_governance/`（控制轴）**：多轮的治理——停止条件（跑到哪算完）、外层调度（下一轮跑什么）、自主度分档（人在哪一站）。
- **依赖方向**：loop 层的硬前提是 harness 层（单次运行不受控时，loop 只是把错误复制得更快）。
- **命名口径**：两个主题都不沿用 KOL 词——"loop engineering" 经回源判定词源＝热度碎片、外延未收敛（判定见 [`../02_research/01_agent_engineering/loop_engineering/digested/01-命名谱系.md`](../02_research/01_agent_engineering/loop_engineering/digested/01-命名谱系.md) §四）。
