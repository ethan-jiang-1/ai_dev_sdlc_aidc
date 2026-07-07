# AGENTS.md — Open Format Specification + OpenAI Codex CLI Official Integration

- source_url: `https://agents.md/`（AGENTS.md 官方站点 + FAQ，2026-04-17 抓取正文）+ `https://developers.openai.com/codex/guides/agents-md/`（OpenAI Codex 官方 AGENTS.md 集成指南）+ 产业背景：`https://aaif.io/`（Agentic AI Foundation under Linux Foundation）
- source_type: `community standard + vendor official documentation`
- accessed_at: `2026-04-17`
- related_topic: `shared (06 agent-format primary)；对 04 future-trends §4.6、§4.3 有直接证据供给`
- trust_level: `official (agents.md + OpenAI Codex 官方站)`
- tier: `B`（官方站 + 多厂商背书；Linux Foundation 下的共同治理物料）
- why_it_matters: **本轮 Topic 06 最关键的一份材料**。AGENTS.md 是 2025-08 由 OpenAI 等多家联合发起、2025-12 归入 **Linux Foundation 的 Agentic AI Foundation (AAIF)** 的开放格式；截至 2025-09 已有 20,000+ 公开 GitHub 仓库采用，Uber / Databricks / Sourcegraph 等企业内部落地。这是"跨 coding agent 的事实标准"论断的**唯一官方级证据**。
- captured_excerpt: `yes`
- claims_supported: AGENTS.md 由 OpenAI Codex + Amp (Sourcegraph) + Jules (Google) + Cursor + Factory 多方协作发起；2025-08 公开；2025-12 托管于 Linux Foundation 下属 Agentic AI Foundation (AAIF)；格式 = plain CommonMark Markdown，**无必填 schema、无 YAML、无特殊语法**；支持 monorepo 嵌套，按 "nearest wins + user chat prompts override everything" 合并；支持工具：Cursor / GitHub Copilot / Windsurf / Amp / Devin / Google Jules / Gemini CLI / Aider / OpenAI Codex CLI / UiPath；Claude Code 使用 CLAUDE.md，AGENTS.md 支持 pending；Codex CLI 官方额外约定：`~/.codex/AGENTS.md` 全局 + `AGENTS.override.md` 临时覆盖 + `project_doc_fallback_filenames` 可自定义；默认 `project_doc_max_bytes = 32 KiB`；`CODEX_HOME` 可切换 profile；采纳统计：20,000+ 公开 repo（截至 2025-09）、60,000+ repo（截至 AGENTS.md 官方站 2026 统计口径）；企业用例：Uber / Databricks / Sourcegraph。
- date_scope: 2025-08（公开发起）→ 2025-09（20k+ 公开 repo 采用）→ 2025-12（Linux Foundation AAIF 托管）→ 2026-04-17（当前治理状态）
- related_entities:
  - 发起方：OpenAI Codex、Amp (Sourcegraph)、Jules (Google)、Cursor、Factory
  - 治理方：Agentic AI Foundation (AAIF) 下属 Linux Foundation
  - 支持者背书：OpenAI、Anthropic、Google、AWS 等（2026 年 Linux Foundation 公告）
  - 工具生态（2026-04-17 列出）：OpenAI Codex CLI、GitHub Copilot、Cursor、Windsurf、Amp、Devin、Google Jules、Gemini CLI、Aider、UiPath 等
  - 企业采纳代表：Uber、Databricks、Sourcegraph

## 关键事实

1. **定位**（官方 verbatim）：
   > "README.md files are for humans: quick starts, project descriptions, and contribution guidelines. AGENTS.md complements this by containing the extra, sometimes detailed context coding agents need: build steps, tests, and conventions that might clutter a README or aren't relevant to human contributors."
2. **格式**（官方 FAQ）："No required fields. AGENTS.md is just standard Markdown. Use any headings you like; the agent simply parses the text you provide."
3. **合并 / 优先级**（官方 FAQ）："The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything."
4. **执行语义**（官方 FAQ）：Agent **会自动尝试**运行 AGENTS.md 中列出的测试 / lint 等命令并修复失败。
5. **推荐章节**（官方）：Project overview、Build and test commands、Code style、Testing、Security、PR conventions、Deployment。
6. **Monorepo 嵌套**：每个子目录放 AGENTS.md，agent 读"最近"；OpenAI 自己的主 repo 即有 88 个 AGENTS.md。
7. **OpenAI Codex CLI 的额外约定**（Codex 官方指南）：
   - **全局**：`~/.codex/AGENTS.override.md`（若存在）> `~/.codex/AGENTS.md`
   - **项目**：从 Git root → cwd 沿路径每个目录都检查 `AGENTS.override.md` → `AGENTS.md` → `project_doc_fallback_filenames`（每目录 **至多一个**）
   - **合并**：root → leaf 依次拼接，越靠近 cwd 的文件后置覆盖前置
   - **大小限制**：`project_doc_max_bytes` 默认 32 KiB，超出会截断；可提高或拆分
   - **profile 切换**：`CODEX_HOME` 指向自定义目录
   - **fallback 文件名**：`project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]` 自定义
   - **诊断**：`codex --ask-for-approval never "Summarize the current instructions."` 可回显已加载的 instruction chain
8. **Aider 集成**（官方 agents.md FAQ）：`.aider.conf.yml` 加 `read: AGENTS.md`
9. **Gemini CLI 集成**（官方 agents.md FAQ）：`.gemini/settings.json` 设 `{"context": {"fileName": "AGENTS.md"}}`
10. **采纳规模**：
    - 20,000+ 公开 GitHub repo（2025-09 数据）
    - 60,000+ repo（2026 年 AGENTS.md 官方站计数）
    - 企业代表：Uber、Databricks、Sourcegraph
11. **治理**（官方站公告）："AGENTS.md is now stewarded by the Agentic AI Foundation (AAIF) under the Linux Foundation."（2025-12 起）；背书方 OpenAI / Anthropic / Google / AWS。
12. **与 Claude Code 的关系**：Claude Code 继续以 CLAUDE.md 为主；AGENTS.md 支持 pending（由第三方 2026 指南与 agents.md 官方并行说明）。

## 核心内容摘录（官方 verbatim）

### 最小 AGENTS.md 示例（agents.md 官方）

```markdown
# Sample AGENTS.md file

## Dev environment tips
- Use `pnpm dlx turbo run where <project_name>` to jump to a package instead of scanning with `ls`.
- Run `pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.
- Use `pnpm create vite@latest <project_name> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.
- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.

## Testing instructions
- Find the CI plan in the .github/workflows folder.
- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.
- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.
- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.
- Fix any test or type errors until the whole suite is green.
- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.
- Add or update tests for the code you change, even if nobody asked.

## PR instructions
- Title format: [<project_name>] <Title>
- Always run `pnpm lint` and `pnpm test` before committing.
```

### Codex CLI 的 Instruction Chain 发现顺序（官方 verbatim 摘要）

1. **Global scope**：在 `$CODEX_HOME`（默认 `~/.codex/`）读 `AGENTS.override.md`，不存在则读 `AGENTS.md`（只取该层第一个非空文件）。
2. **Project scope**：从 Git root 向下走到 cwd，每个目录按 `AGENTS.override.md` → `AGENTS.md` → `project_doc_fallback_filenames` 的顺序找，**每目录至多一个**。
3. **Merge**：从 root 到 leaf 依次拼接，越靠近 cwd 覆盖越高。
4. **大小限制**：`project_doc_max_bytes = 32 KiB`（可配置）。

### Codex CLI 全局配置示例（官方）

```toml
# ~/.codex/config.toml
project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
project_doc_max_bytes = 65536
```

### Codex CLI 全局 AGENTS.md 示例（官方）

```markdown
# ~/.codex/AGENTS.md

## Working agreements

- Always run `npm test` after modifying JavaScript files.
- Prefer `pnpm` when installing dependencies.
- Ask for confirmation before adding new production dependencies.
```

### Aider + Gemini CLI 映射（官方 agents.md FAQ）

- Aider：`.aider.conf.yml` → `read: AGENTS.md`
- Gemini CLI：`.gemini/settings.json` → `{"context": {"fileName": "AGENTS.md"}}`

### 治理（官方原文）

> "AGENTS.md is now stewarded by the Agentic AI Foundation (AAIF) under the Linux Foundation."

## 与本研究的关系

| 研究线 | 该 reference 能直接支撑的断言 / 模块 |
|--------|-------------------------------------|
| Topic 06 `agent-format` | **主锚点 3/3，也是最关键的一份**：AGENTS.md 的**跨工具事实标准**地位由 agents.md 官方站 + Codex CLI 官方指南 + Linux Foundation 托管共同支撑，远超单一厂商文档 |
| Topic 04 `future-trends` | §4.6 "IDE 原生的需求原语"升级为已发生事件；§4.3 "Spec ↔ Agent 闭环" 的制度化也从 AGENTS.md + `override.md` 的层级结构得到部分验证 |
| Topic 03 `ears` | EARS 句式可直接嵌入 AGENTS.md / AGENTS.override.md；32 KiB 的 `project_doc_max_bytes` 与 Anthropic "CLAUDE.md 短小" 一致——EARS 细规则应放子目录 AGENTS.md 或 Skills |
| Topic 05 `integration-bdd` | 选型矩阵的"跨工具便携 / 合规背书"权重：AGENTS.md 是唯一在 Linux Foundation 托管、跨 OpenAI / Google / Anthropic / AWS 背书的 agent-facing 格式 |

## 可直接引用的术语 / 概念

- AGENTS.md（CommonMark plain markdown，无必填字段）
- "nearest wins + user chat overrides"（合并优先级）
- `AGENTS.override.md`（临时覆盖文件，Codex 约定）
- `project_doc_max_bytes = 32 KiB`（Codex 默认）
- `project_doc_fallback_filenames`（可自定义文件名别名）
- `CODEX_HOME`（profile 切换）
- Agentic AI Foundation (AAIF) under Linux Foundation（治理）

## 风险与局限

1. **"跨工具事实标准"≠ 语义一致**：虽然多家工具读取 AGENTS.md，但 **合并策略、优先级、执行语义** 各不相同（Codex 的 32 KiB 截断、Cursor 的 nearest-wins、Aider 的 `.aider.conf.yml` 显式 read、Claude Code 暂未支持）。"跨工具采纳"不等于"跨工具行为一致"。
2. **数字需交叉验证**：60k+ 采纳数据来源为 AGENTS.md 官方站与第三方博客口径；正式声明建议用 GitHub code search `path:AGENTS.md NOT is:fork NOT is:archived` 实测再引。
3. **Claude Code 仍独立**：Claude Code 继续以 CLAUDE.md 为主；若未来无原生 AGENTS.md 支持，"事实标准"会在 Anthropic 生态形成**空档**。
4. **无 schema = 无强约束**：AGENTS.md 的"无必填"保证了门槛低，但也意味着**企业合规要求的结构化字段**（ADR / RFC 指针、owner、version、decision status）必须各家自定义，难以互通。
5. **"Agent 会自动运行命令"的权限风险**：官方 FAQ 明言会尝试执行 `testing commands`；与 Anthropic / Cursor 的 permission mode 结合时需显式放行，否则行为不一致。

## 交叉引用

- 研究入口：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 同组 Topic 06 配对：[`00-shared-cursor-rules-official.md`](00-shared-cursor-rules-official.md)、[`00-shared-claude-code-official.md`](00-shared-claude-code-official.md)
- 研究线 06 入口：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 断言审查：[`../claims-audit.md`](../claims-audit.md)（Wave 2 将用本 reference 为 claims-audit v2 新增"AGENTS.md 为事实标准"断言）
- 导航入口：[`_INDEX.md`](_INDEX.md)
