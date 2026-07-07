# OpenSpec 2026 — Cross-tool spec workflow and direct comparison to Spec Kit / Kiro

- source_url: `https://github.com/Fission-AI/OpenSpec` + `https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md` + `https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/workflows.md`
- source_type: `official repository documentation + official docs`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 06 当前剩余 gap 是缺少更直接的 cross-tool workflow/config comparison。OpenSpec 官方文档不仅把同一套 spec workflow 映射到 25+ agent tools，还在 README 里直接把自己与 GitHub Spec Kit、Amazon Kiro 做官方对比。这比并列读取多个单工具文档更接近“直接比较”证据。
- captured_excerpt: `yes`
- claims_supported: `OpenSpec official docs directly compare the framework against Spec Kit and Kiro; define a stable artifact stack around proposal/specs/design/tasks; expose both core and expanded workflows; and publish tool-specific install/configuration paths for 25+ AI coding assistants including Codex, Continue, Cline, Cursor, Claude Code, GitHub Copilot, and Kiro. This upgrades Topic 06 from indirect multi-source comparison to one official cross-tool comparison anchor, while still leaving cross-tool semantic-consistency as a separate open question.`
- date_scope: `repository/docs state as crawled 2026-04-18`
- related_entities: `OpenSpec; Fission AI; Spec Kit; Kiro; Codex; Continue; Cline; Cursor; Claude Code; GitHub Copilot`

## 关键事实

1. OpenSpec README 把产品定位为 `lightweight spec-driven framework`，且明确说它 `works with 20+ AI assistants`。
2. README 的 `How we compare` 章节直接给出：
   - `vs. Spec Kit`
   - `vs. Kiro`
3. 这些官方对比不是抽象口号，而是把差异落到 workflow / config 层：
   - 对 Spec Kit：强调 OpenSpec 更轻、更少 rigid phase gates
   - 对 Kiro：强调 OpenSpec 不锁定 IDE，也不锁定 Claude-only model path
4. README 与 `getting-started` / `workflows` 文档共同锁定了一组稳定工件：
   - `proposal.md`
   - `specs/`
   - `design.md`
   - `tasks.md`
5. `supported-tools.md` 官方列出 25+ tools 的 skill path 和 command path，并覆盖：
   - `codex`
   - `continue`
   - `cline`
   - `cursor`
   - `claude`
   - `github-copilot`
   - `kiro`
   - 以及更多工具
6. 这说明 OpenSpec 不只是“又一个单工具 workflow”，而是显式尝试把同一套 artifact/workflow 映射到多 agent 环境。

## 核心内容摘录

### 直接比较层

- README 里直接有 `How we compare`。
- 官方把自己与 `Spec Kit` 和 `Kiro` 并排对照：
  - Spec Kit 被描述为更 thorough 但更 heavyweight
  - Kiro 被描述为 powerful，但被锁进其 IDE 和模型边界
- 因而，这份材料能直接支撑 Topic 06 的 `workflow/config comparison`，而不只是“各家都存在 workflow”。

### 统一 artifact graph

- OpenSpec 默认创建并维护：
  - `proposal.md`
  - `specs/`
  - `design.md`
  - `tasks.md`
- `workflows.md` 进一步把这些工件串成：
  - `proposal -> specs -> design -> tasks -> implement`
- 与 Spec Kit 的 `spec/plan/tasks`、Kiro 的 `requirements/design/tasks` 相比，OpenSpec 给出了一个更通用的 cross-tool framing。

### 跨工具配置层

- `supported-tools.md` 不是泛泛而谈“支持很多工具”，而是具体列出每种工具的安装路径模式。
- 这意味着它已经进入 config/workflow engineering 层，而不仅是 marketing claim。
- 文档同时说明：
  - skills 可装到 tool-specific 路径
  - commands 也按工具适配不同文件路径

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 这是一次更直接的官方 cross-tool comparison：同一 workflow 跨 25+ tools 分发，并在官方 README 中直接比较 Spec Kit 与 Kiro |
| Topic 04 `future-trends` | 支撑 spec-driven workflow 已开始从单工具模式向 cross-tool planning layer 演化 |

## 可直接引用的术语 / 概念

- `lightweight spec-driven framework`
- `works with 20+ AI assistants`
- `How we compare`
- `vs. Spec Kit`
- `vs. Kiro`
- `proposal.md`
- `design.md`
- `tasks.md`
- `supported tools`

## 风险与局限

1. OpenSpec 仍是某一框架作者自己的官方文档，不是独立第三方 comparative study。
2. 它更强地支持 `workflow/config comparison exists`，但不证明各工具对同一 artifact 的 runtime semantics 完全一致。
3. 因而 Topic 06 现在可以把 `direct cross-tool workflow/config comparison` 视为已补强，但仍需把 `semantic-consistency` 留作单独风险项。

## 交叉引用

- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- Spec Kit official：[`06-agent-format-github-spec-kit-official.md`](06-agent-format-github-spec-kit-official.md)
- Kiro official：[`06-agent-format-kiro-spec-workflow-official.md`](06-agent-format-kiro-spec-workflow-official.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
