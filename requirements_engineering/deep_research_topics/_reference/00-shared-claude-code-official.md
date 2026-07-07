# Anthropic Claude Code — Best Practices & `CLAUDE.md` Official Guidance

- source_url: `https://docs.anthropic.com/en/docs/claude-code/best-practices`（Claude Code Docs — Best Practices，2026-04-17 抓取正文）+ 相关页：`https://docs.anthropic.com/en/memory`（CLAUDE.md 专页）、`https://docs.anthropic.com/en/skills`、`https://docs.anthropic.com/en/sub-agents`、`https://docs.anthropic.com/en/plugins`
- source_type: `official product documentation`
- accessed_at: `2026-04-17`
- related_topic: `shared (06 agent-format primary)；对 04 future-trends §4.6 与 03 ears 的"塞 EARS 到 CLAUDE.md"讨论有用`
- trust_level: `official`（Anthropic 官方）
- tier: `B`（厂商一手权威文档；对于 Claude Code 产品内部约定，这是 canonical reference）
- why_it_matters: Claude Code 是本轮**最常被与 Cursor 并列**的 coding agent；其 `CLAUDE.md` + Skills + Plugins + Subagents 架构是与 Cursor Rules 并行的**另一个官方基线**。Anthropic 对 **"context window 是最重要资源，CLAUDE.md 过长会让 Claude 忽略指令"** 的立场，是判断"能不能把全套 EARS 塞进 agent 规约文件"的**最关键反证**。
- captured_excerpt: `yes`
- claims_supported: `CLAUDE.md` 是 Anthropic Claude Code 的项目级 / 用户级默认上下文文件（home / project root / project `.local` / parent / child）；支持 `@path/to/import` 引用其他文件；Anthropic 官方强调 CLAUDE.md 应 **保持短小可人读**，过长会导致 Claude 忽略重要规则；Skills = `.claude/skills/*/SKILL.md`，按需加载而非每轮加载；Subagents = `.claude/agents/*.md`，独立 context window + 受限 tools；Plugins = 打包 skills/hooks/subagents/MCP 的可安装单元；非 interactive 模式通过 `claude -p`；`/init` 命令可扫描仓库生成初始 CLAUDE.md；Hooks 为确定性副作用，优于 advisory 的 CLAUDE.md。
- date_scope: Claude Code 现状（2026-04-17 官方文档）；CLAUDE.md + Skills + Plugins 架构在 2024–2025 年迭代成形；`/rewind`、`/compact`、Auto mode、Checkpointing 为 2025 年后进入的能力
- related_entities:
  - 厂商：Anthropic
  - 产品：Claude Code（CLI + IDE 扩展）
  - 技术位置：`~/.claude/CLAUDE.md`、`./CLAUDE.md`、`./CLAUDE.local.md`、`.claude/skills/*/SKILL.md`、`.claude/agents/*.md`、`.claude/settings.json`
  - 配套能力：Skills、Subagents、Hooks、Plugins、MCP、Plan Mode、Auto mode、Checkpointing、Rewind
  - 相关生态：Claude Plugins marketplace（官方 + 社区）

## 关键事实

1. **CLAUDE.md 的五类位置**（官方表）：
   - `~/.claude/CLAUDE.md`：全局，所有 Claude session
   - `./CLAUDE.md`：项目根，**check into git**
   - `./CLAUDE.local.md`：个人项目备忘，**加进 .gitignore**
   - 父目录：monorepo 场景，父 + 子 CLAUDE.md 自动合并
   - 子目录：按需加载（on-demand）
2. **CLAUDE.md 必须短小**（官方明确警告）：
   > "CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows that are only relevant sometimes, use skills instead."
   > "Keep it concise. For each line, ask: 'Would removing this cause Claude to make mistakes?' If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!"
3. **CLAUDE.md 的"应放 / 不应放"对照表**（官方原文）：

   | ✅ Include | ❌ Exclude |
   | --- | --- |
   | Bash commands Claude can't guess | Anything Claude can figure out by reading code |
   | Code style rules that differ from defaults | Standard language conventions Claude already knows |
   | Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
   | Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
   | Architectural decisions specific to your project | Long explanations or tutorials |
   | Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
   | Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

4. **`@path/to/import` 语法**：CLAUDE.md 可在内联中 import 其他 markdown（如 `@README.md`、`@docs/git-instructions.md`、`@~/.claude/my-project-instructions.md`）。
5. **Skills = `.claude/skills/*/SKILL.md`**：每个 Skill 是带 YAML frontmatter（`name` / `description` / 可选 `disable-model-invocation`）的 markdown；Skills 按需加载而非每轮注入，解决 CLAUDE.md "总上下文" 膨胀问题。Skill 可定义可调用工作流（`/skill-name` 触发 + `$ARGUMENTS`）。
6. **Subagents = `.claude/agents/*.md`**：独立 context window，可限定 `tools` 与 `model`。典型 YAML：`name` / `description` / `tools` / `model`。
7. **Plugins**：绑定 skills/hooks/subagents/MCP 的可分发单元；`/plugin` 浏览市场；结构为 `plugin-name/.claude-plugin/plugin.json` + `commands/` + `agents/` + `skills/` + `hooks/` + `.mcp.json`。
8. **Hooks**：确定性副作用（"must happen every time"），高于 advisory 的 CLAUDE.md。`/hooks` 浏览，`.claude/settings.json` 配置。
9. **非交互模式**：`claude -p "prompt"` + `--output-format json|stream-json`；可集成 CI / pre-commit / 管道。
10. **Plan Mode + Explore-Plan-Implement-Commit**：Anthropic 推荐的四段式工作流；Plan Mode 只读、不写文件。
11. **Verification is the highest-leverage practice**（官方原文）：
    > "Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do."
12. **Context window 退化是一切的起点**：Anthropic 把 "context window 被填满导致性能下降" 列为 CLAUDE.md 所有建议的根因。`/clear` / `/compact` / `/rewind` / Checkpoint / Subagents 都是为了压缩 context。

## 核心内容摘录（官方 verbatim）

### CLAUDE.md 最小示例（官方）

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

### CLAUDE.md import 语法（官方）

```markdown
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md
```

### Skills 示例（官方）

```markdown
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)
```

### Skill 工作流示例（官方 `fix-issue`）

```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR
```

### Subagent 示例（官方 security-reviewer）

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.
```

### 常见失败模式（官方原文清单）

1. **Kitchen sink session** → `/clear` 在不相关任务间重置
2. **Correcting over and over** → 两次修正失败后 `/clear` 重写 prompt
3. **Over-specified CLAUDE.md** → "Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook."
4. **Trust-then-verify gap** → "Always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it."
5. **Infinite exploration** → 用 subagent 承担探索以防污染主 context

## 与本研究的关系

| 研究线 | 该 reference 能直接支撑的断言 / 模块 |
|--------|-------------------------------------|
| Topic 06 `agent-format` | **主锚点 2/3**：与 Cursor Rules 并列的另一主干格式；证据核心 = CLAUDE.md **应保持短小**、Skills 为按需加载层；"rules bloat / context rot" 有 Anthropic 官方原话支撑 |
| Topic 04 `future-trends` | §4.6 "IDE 原生的需求原语"的另一早期信号；Claude Code 把 "spec 生成"写成一条 Skill 工作流（"Interview me ... then write a complete spec to SPEC.md"）也是对 §4.3 "Spec ↔ Agent 闭环"的证据 |
| Topic 03 `ears` | 讨论"能否把完整 EARS 需求集塞进 CLAUDE.md"时，Anthropic 的官方立场是**不应该**：domain-specific 要放 Skills 或 subagent，不放 CLAUDE.md |
| Topic 05 `integration-bdd` | 九维矩阵的"按需加载 vs 全量注入"一维有了官方区分（CLAUDE.md 全量 vs Skills 按需 vs Subagent 独立 context） |

## 可直接引用的术语 / 概念

- CLAUDE.md（项目级 / 用户级 / `.local` / 父子目录）
- `@path/to/import` 语法
- `.claude/skills/*/SKILL.md`
- `.claude/agents/*.md`
- `.claude/settings.json`（hooks + permissions）
- `claude -p`（非交互）、`claude --continue` / `--resume`
- Plan Mode / Normal Mode / Auto mode / Sandboxing
- Checkpointing / `/rewind` / `/compact` / `/clear`

## 风险与局限

1. **Anthropic 尚未声明对 AGENTS.md 的原生支持**：agents.md 官方 FAQ + 第三方 2026 年指南均指出 Claude Code 仍以 CLAUDE.md 为主，AGENTS.md 支持 "pending"。如果"跨工具事实标准"要形成，Claude Code 是当前未完成对齐方。
2. **CLAUDE.md 与 AGENTS.md 的语义重叠**：本研究要特别关注两种文件的**职责边界**——若团队同时维护，会出现重复与漂移。
3. **Skills 生态仍在快速演化**：Plugins marketplace、Skill 跨项目分发的最佳实践**未稳定**；本 reference 只记录 2026-04-17 快照。
4. **"Keep CLAUDE.md short" vs "写详细 spec"天然冲突**：Anthropic 的建议是"spec 放 SPEC.md 或 Plan Mode 产出的独立文件"，CLAUDE.md 只放跨任务约束——这对 "EARS spec 在哪里落"有直接影响。
5. **第三方工具的 Claude Code 集成**：如 Claude Plugins Marketplace、Claude Code Web 版本 VM、Agent Teams 等能力，本 reference 只点到；Wave 1 如需结论须补抓。

## 交叉引用

- 研究入口：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 同组 Topic 06 配对：[`00-shared-cursor-rules-official.md`](00-shared-cursor-rules-official.md)、[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- 研究线 06 入口：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
