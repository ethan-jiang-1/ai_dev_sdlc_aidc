# OpenWork OSS repo 2026 — Public AGENTS.md usage with separate PRD workflow

- source_url: `https://github.com/different-ai/openwork` + `https://github.com/different-ai/openwork/blob/dev/AGENTS.md`
- source_type: `official repository README + official repository AGENTS.md`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends, 05 integration-bdd`
- trust_level: `official project repository`
- tier: `B`
- why_it_matters: Topic 06 当前剩余大缺口之一是“除了工具厂商自身宣布支持外，是否已有公开项目把 AGENTS.md 真正作为 repo contract 来用”。OpenWork 是一个公开 OSS 仓库，根目录直接维护 `AGENTS.md`，README 的贡献说明还明确要求 review `AGENTS.md`，并把 feature-level `PRD` 文件路径和 `AGENTS.md` 中的 conventions 连接起来。这能把风险从“只有工具厂商 adoption announcement”收窄为“已有公开 OSS usage case，但 enterprise-internal adoption 仍待补”。
- captured_excerpt: `yes`
- claims_supported: `A public OSS repo can use root AGENTS.md as project/agent contract; AGENTS.md can coexist with many companion docs instead of replacing them; feature-level PRD files can be separate artifacts while AGENTS.md carries repo workflow and contribution guidance; README-level contributor workflow can explicitly point contributors/agents to AGENTS.md before changes.`
- date_scope: `repository state observed on 2026-04-18; release activity visible through 2026-04`
- related_entities: `different-ai; openwork; AGENTS.md; PRD; OpenWork; opencode`

## 关键事实

1. `different-ai/openwork` 是 public repository，仓库根目录直接存在 `AGENTS.md` 文件。
2. 仓库 README 的 `Contributing` 段明确要求：
   - review `AGENTS.md`
   - review other project docs such as `VISION.md`, `PRINCIPLES.md`, `PRODUCT.md`, `ARCHITECTURE.md`
3. README 还明确说：new PRDs should be added under `apps/app/pr/<name>.md` following conventions described in `AGENTS.md`。
4. 这说明该项目没有把 feature details 全塞进 `AGENTS.md`，而是把：
   - repo / workflow contract 放在 `AGENTS.md`
   - feature-level requirements/PRD 放在单独路径
5. `AGENTS.md` 文件本身包含：
   - product / runtime model description
   - task intake rules
   - new feature workflow
   - PR expectations
   - development guidelines
6. 这构成了一个公开可观察的分层实践：`repo contract + companion docs + separate PRD artifacts`。

## 核心内容摘录

### README 把 AGENTS.md 当成 contributor/agent entrypoint

- OpenWork README 的贡献说明要求 contributors review `AGENTS.md` before making changes。
- 同一段还把 `AGENTS.md` 与 `VISION.md`、`PRODUCT.md`、`ARCHITECTURE.md` 并列，说明 AGENTS.md 是其中一个入口，而不是全部文档的替代品。

### PRD 与 AGENTS 分层

- README 明确要求新 PRD 放到 `apps/app/pr/<name>.md`。
- 同时要求遵循 `AGENTS.md` 中描述的 conventions。
- 这正好符合 Topic 06 当前的“三层分离”判断：repo/team contract 不等于 feature spec。

### AGENTS.md 的实际职责

- OpenWork 的 `AGENTS.md` 主要承载 repo mission、runtime model、task intake、new feature workflow、PR expectations 等 agent-facing contract。
- 它并没有被设计成完整产品需求库，而是把 deeper docs / feature docs 分离出去。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 补一个公开 OSS usage case：AGENTS.md 作为 repo contract，与单独 PRD artifacts 共存，而不是只存在于工具厂商 announcement 中 |
| Topic 04 `future-trends` | 支撑“requirements/spec artifacts 将从 repo-level contract 分离到 feature-level docs”的实际 OSS signal |
| Topic 05 `integration-bdd` | 间接支持“需求表达分层”而非单文件吞并一切 |

## 可直接引用的术语 / 概念

- `review AGENTS.md`
- `new PRDs`
- `apps/app/pr/<name>.md`
- `conventions described in AGENTS.md`
- `Task Intake`
- `New Feature Workflow`

## 风险与局限

1. 这是公开 OSS project usage case，不是企业内部 adoption case。
2. 该项目本身仍然是 agentic-work 产品，因此不能把它写成“普通企业代码库已普遍采用”的证据。
3. 更稳的表述应是：`public-oss-usage-supported; enterprise-internal-usage-pending`。

## 交叉引用

- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- Topic 06 seed：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- W2 selection matrix：[`../_artifacts/W2-selection-matrix-v2.md`](../_artifacts/W2-selection-matrix-v2.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
