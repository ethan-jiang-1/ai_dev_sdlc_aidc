# Cursor Rules — Official Documentation (`.cursor/rules/*.mdc` + `AGENTS.md`)

- source_url: `https://cursor.com/docs/context/rules`（2026-04-17 抓取正文，Cursor 官方文档）
- source_type: `official product documentation`
- accessed_at: `2026-04-17`
- related_topic: `shared (06 agent-format primary)；对 04 future-trends §4.6 的升级也需回引`
- trust_level: `official`（Cursor 官方）
- tier: `B`（厂商一手权威文档；对于 Cursor 产品内部约定，这是 canonical reference）
- why_it_matters: Cursor 是 2026 年市场份额最大的 coding agent IDE 之一；其 Rules 系统是本轮"AI 编程时代需求表达"的核心承载机制之一。官方文档明确了 **四类 rule（Project / User / Team / AGENTS.md）** 的优先级与组合方式，以及**明确承认 AGENTS.md 为轻量替代方案**，这是本研究线"跨工具事实标准候选"的关键证据。
- captured_excerpt: `yes`
- claims_supported: Cursor 原生支持四类 rules（Project / User / Team / AGENTS.md）；Project Rules 位置为 `.cursor/rules/*.md|*.mdc`，支持 YAML frontmatter（`description` / `globs` / `alwaysApply`）；四种激活模式（Always Apply / Apply Intelligently / Apply to Specific Files / Apply Manually）；AGENTS.md 作为轻量替代在 Cursor 中**已被正式支持**，可嵌套到子目录并以"最近文件优先"合并；Team Rules 位置为仪表盘管理，**enforcement** 开关可禁止用户本地关闭；规则合并顺序 = Team → Project → User（earlier 优先）；官方建议 rules < 500 行、用具体示例、version-control、避免 style guide 全文粘贴。
- date_scope: Cursor Rules 体系现状（2026-04-17 官方文档）；`.cursor/rules/` 的 `.mdc` frontmatter 格式是 2024 年以来的 Cursor Rules v2 方案，取代单文件 `.cursorrules`（legacy，Agent 模式下已 deprecated，第三方 2026 年指南复核）
- related_entities:
  - 厂商：Cursor (Anysphere Inc.)
  - 技术位置：`.cursor/rules/` 目录；项目根 `AGENTS.md`；Cursor Settings → Rules, Commands
  - 社区约定：AGENTS.md（与 OpenAI Codex / Amp / Aider / Google Jules / Factory 共用）
  - 下游采纳：Team / Enterprise 计划的 Team Rules 仪表盘

## 关键事实

1. **四类 Rules**（官方原文）：
   - **Project Rules**：`.cursor/rules/` 目录内 markdown（`.md` / `.mdc`），版本控制，按路径范围生效
   - **User Rules**：跨项目，Cursor Settings → Rules 中设置，**Agent (Chat) 使用，不作用于 Inline Edit (Cmd/Ctrl+K)**
   - **Team Rules**：Team / Enterprise 计划下可在仪表盘管理；支持 **enforce** 开关禁止用户本地关闭
   - **AGENTS.md**：项目根的简单 markdown（可嵌套子目录），作为 `.cursor/rules` 的轻量替代
2. **Rule 合并顺序**（官方原文）："Team Rules → Project Rules → User Rules. All applicable rules are merged; earlier sources take precedence when guidance conflicts."
3. **.mdc frontmatter 字段**（官方原文）：`description`、`alwaysApply: true|false`、`globs`；无 frontmatter 的 `.md` 文件仍可作为 rule。
4. **四种激活模式**：
   - `Always Apply`（每次 chat 注入）
   - `Apply Intelligently`（Agent 基于 description 判断）
   - `Apply to Specific Files`（glob 匹配）
   - `Apply Manually`（`@rule-name` 引用）
5. **AGENTS.md in Cursor**：官方确认 Cursor "supports AGENTS.md in the project root and subdirectories"；嵌套 AGENTS.md 按"nearest wins, combined with parent"合并。
6. **Best practices（官方）**：
   - Rules < 500 行；大 rule 拆成多个可组合小 rule
   - 使用 `@filename` 引用文件而非复制其内容，以避免 stale
   - 避免：整 style guide 粘贴、文档常见命令、罕见 edge case、codebase 重复
   - 建议：只在 Agent 反复犯错时加 rule；随 Agent 犯错迭代；check into git
7. **创建通道**：
   - `/create-rule` 在 Agent chat 中描述即生成 `.cursor/rules/*.mdc`
   - Cursor Settings → Rules, Commands → `+ Add Rule`
8. **Remote Rules (GitHub)**：可从任意 GitHub repo 拉取 `.mdc`，落到 `.cursor/rules/imported/`。
9. **User Rules 作用范围限制**：不作用于 Inline Edit，也不作用于 Cursor Tab 其他 AI 功能——仅 Agent (Chat)。

## 核心内容摘录（官方 verbatim）

### Rule 文件结构示例

```bash
.cursor/rules/
  react-patterns.mdc       # Rule with frontmatter (description, globs)
  api-guidelines.md        # Simple markdown rule
  frontend/                # Organize rules in folders
    components.md
```

### Rule frontmatter 模板（官方）

```md
---
globs:
alwaysApply: false
---

- Use our internal RPC pattern when defining services
- Always use snake_case for service names.

@service-template.ts
```

### 四种激活模式（官方表）

| Rule Type | Description |
| --- | --- |
| `Always Apply` | Apply to every chat session |
| `Apply Intelligently` | When Agent decides it's relevant based on description |
| `Apply to Specific Files` | When file matches a specified pattern |
| `Apply Manually` | When @-mentioned in chat (e.g., `@my-rule`) |

### AGENTS.md 嵌套结构示例（官方）

```bash
project/
  AGENTS.md              # Global instructions
  frontend/
    AGENTS.md            # Frontend-specific instructions
    components/
      AGENTS.md          # Component-specific instructions
  backend/
    AGENTS.md            # Backend-specific instructions
```

> "Instructions from nested AGENTS.md files are combined with parent directories, with more specific instructions taking precedence."

### Team Rules 的 enforcement（官方 verbatim）

> "Enforce this rule: When enabled, the rule is required for all team members and cannot be disabled in their Cursor settings. When not enforced, team members can toggle the rule off in Cursor Settings → Rules under the Team Rules section."

### 最小化 AGENTS.md 示例（官方）

```markdown
# Project Instructions

## Code Style
- Use TypeScript for all new files
- Prefer functional components in React
- Use snake_case for database columns

## Architecture
- Follow the repository pattern
- Keep business logic in service layers
```

## 与本研究的关系

| 研究线 | 该 reference 能直接支撑的断言 / 模块 |
|--------|-------------------------------------|
| Topic 06 `agent-format` | **主锚点 1/3**：IDE-agent 层最成熟的规则系统官方说明；AGENTS.md 在 Cursor 已获**原生支持**（不仅仅是社区约定），是本研究线"跨工具事实标准"论断的关键 primary source |
| Topic 04 `future-trends` | §4.6 "IDE 原生的需求原语"的早期信号已被本材料确证——Cursor 把 Rules（项目级 / 用户级 / 团队级）和 AGENTS.md 作为 **IDE 一等配置** |
| Topic 03 `ears` | 讨论"EARS 能否塞进 Rules"时，`.mdc` 的 `globs` + `Apply to Specific Files` 给出语法级承载路径；"keep rules under 500 lines" 是 EARS 落地 Rules 时的硬上限 |
| Topic 05 `integration-bdd` | 选型矩阵中"可版本化 / 可审计 / 可团队分发"的权重分布：Cursor Team Rules + enforcement 对大型组织最优；个体开发者用 `.cursor/rules/*.mdc` 即可 |

## 可直接引用的术语 / 概念

- Project Rules / User Rules / Team Rules / AGENTS.md（四类 + 优先级顺序）
- `.cursor/rules/*.mdc` with frontmatter（`description` / `globs` / `alwaysApply`）
- `Always Apply` / `Apply Intelligently` / `Apply to Specific Files` / `Apply Manually`（四种激活模式）
- `@filename.ts` / `@rule-name`（引用语法）
- "nearest AGENTS.md wins, combined with parent"（嵌套合并策略）
- Team Rules "enforce this rule"（企业级强制位）
- `/create-rule`（chat 内生成命令）

## 风险与局限

1. **`.cursorrules`（legacy）与 `.cursor/rules/*.mdc`（现行）的混用**：第三方指南仍有大量基于 `.cursorrules` 的材料；官方文档明确 `.cursor/rules` 为当前推荐，Agent 模式下 `.cursorrules` 不再完整支持（第三方 2026 年 guide 复核）。本研究须以**现行 `.mdc`**为准。
2. **规则"bloat"**：官方明确警告"CLAUDE.md / rules 过长导致 AI 忽略重要内容"（Anthropic 与 Cursor 共识）；"< 500 行"是经验值，不是硬规范。
3. **Team Rules enforcement 与合规**：官方文档附带提醒——"AI guidance should not be your only security control"。在合规敏感场景不能把 enforced rules 当安全边界。
4. **User Rules 作用范围有限**：仅 Agent (Chat) 使用，不作用于 Inline Edit / Tab；跨功能的规则覆盖不完整。
5. **未覆盖**：Cursor Skills（作为对标 Claude Code Skills 的功能）、Cursor Hooks、`.cursorignore` / `.cursorindexignore` 等配套文件未在本抓取入库；Topic 06 的 Wave 1 需单独补齐。

## 交叉引用

- 研究入口：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 同组 Topic 06 配对：[`00-shared-claude-code-official.md`](00-shared-claude-code-official.md)、[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- 研究线 06 入口：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
