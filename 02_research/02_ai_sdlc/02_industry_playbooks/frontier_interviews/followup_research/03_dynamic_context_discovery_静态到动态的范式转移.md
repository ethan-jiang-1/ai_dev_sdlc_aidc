# 少即是多：Dynamic Context Discovery — 从静态注入到动态发现的范式转移

> 基于 Cursor 官方博客 "Dynamic Context Discovery" (Jediah Katz, 2026.01) 及 "Continually Improving Our Agent Harness" (Heule & Katz, 2026.04)
> 研究日期：2026-07-06

---

## 零、核心命题：为什么「少即是多」在 2026 年成立

> *"As models have become better as agents, we've found success by providing fewer details up front, making it easier for the agent to pull relevant context on its own."*
> — Jediah Katz, Cursor

这个断言之所以在 2026 年成立，是因为两件事同时发生：

1. **模型能力在涨**：前沿模型已经能从"我给你什么你看什么"进化到"我知道我还需要什么，我自己去找"
2. **上下文成本在涨**：越多的静态上下文 = 越多的噪声 = 越多的 token 浪费 = 越高的 contradictory information 导致的幻觉

**结论**：注入所有信息不再是最优解。给 agent **搜索和发现的能力**，比把所有信息塞给它更有效。

---

## 一、范式对比：两种上下文工程

```
静态上下文（过去）                      动态上下文发现（现在）
─────────────────────────              ─────────────────────────
启动时一次性注入所有信息                  Agent 运行时按需拉取
┌──────────────────────┐               ┌──────────────────────┐
│ System prompt        │               │ System prompt (精简) │
│ Rules (全部加载)      │               │ 工具名称列表          │
│ Context files (全部)  │               │ 文件路径指针          │
│ MCP tools (全部描述)  │               │ ─────────────────── │
│ Chat history         │               │ Agent 自行决定:       │
│ Skills (全部指令)     │               │  "需要什么？去哪找？"  │
│ 用户输入              │               │ grep → tail → read   │
└──────────────────────┘               └──────────────────────┘
    Token 消耗: 高                          Token 消耗: 低 46.9%
    噪声: 高                                 噪声: 低
    Agent 负担: 被动接受                      Agent 负担: 主动发现
```

### 1.1 为什么静态上下文在 2026 年开始失效

| 问题 | 表现 |
|---|---|
| **注意力稀释** | "一切重要 = 一切都不重要"，agent 在信息洪水中做局部模式匹配 |
| **上下文腐烂** | 静态文件漂移，agent 基于过期信息做决策 |
| **矛盾信息** | 多个静态源互相冲突 → agent 不知道信哪个 → 幻觉概率增加 |
| **token 浪费** | 大量上下文 token 花在 agent 不需要的信息上 |
| **维护成本** | 人必须手动维护静态文件的新鲜度 |

### 1.2 学术验证

ETH Zurich 的研究 (Galster et al., 2026) 发现了一个反直觉结论：

> *"LLM 生成的 AGENTS.md 文件实际上将任务成功率降低了约 3%，并将推理成本提高了超过 20%。人类编写的文件表现更好，但仅限于那些**不可从代码中推断的细节**。"*

也就是说：把能从代码中自动推断的信息写进 AGENTS.md，不仅没用，反而有害。

---

## 二、Files as Universal Abstraction：文件作为通用抽象

> *"It's not clear if files will be the final interface for LLM-based tools. But files have been a simple and powerful primitive to use, and a safer choice than yet another abstraction that can't fully account for the future."*

Cursor 的整个动态上下文发现体系建立在同一个抽象上：**文件系统**。

### 2.1 为什么是文件？

| 特性 | 文件系统 | 自定义协议/API |
|---|---|---|
| 模型理解 | 所有 LLM 都理解文件操作 | 需要专门训练/提示 |
| 工具支持 | `tail`, `grep`, `rg`, `head`, `jq` 都能用 | 需要自定义工具 |
| 部分读取 | 天然支持 | 需要额外实现 |
| 持久化 | 天然持久化 | 需要额外逻辑 |
| 惰性加载 | agent 自己决定读多少 | 协议层需要特殊设计 |
| 跨工具兼容 | 所有 agent 都能读写文件 | 工具专属 |

### 2.2 核心原则

```
不要注入数据 → 写入文件
不要截断输出 → 写入文件
不要压缩历史 → 写入文件
    ↓
让 agent 用 tail 检查末尾
让 agent 用 grep 搜索相关
让 agent 自己决定需要什么
```

---

## 三、五个动态上下文发现模式（逐条拆解）

### 3.1 长工具响应 → 文件

**问题**：Shell 命令和 MCP 调用可能返回巨大的 JSON 响应。传统做法是截断——可能丢失关键信息。

**Cursor 的方案**：
```
1. 完整输出写入临时文件
2. Agent 先调用 tail 检查末尾
3. 如果需要更多 → read 按需读取
4. 不需要的部分永远不会进入上下文窗口
```

**效果**：减少了因上下文超限而触发的摘要次数。因为 agent 通常只需要输出的一部分（最后几行、某个错误信息），而不是全部。

### 3.2 聊天历史文件：摘要 + 备份的双层记忆

**问题**：摘要是有损压缩。agent 可能丢失关键细节。

**Cursor 的方案**：
```
上下文快满时:
  1. 生成对话摘要（紧凑）
  2. 完整聊天历史写入 transcript 文件
  3. 摘要进入上下文窗口
  4. 如果 agent 后续需要细节 → grep transcript 文件找回
```

**这是双层记忆**：摘要提供结构化的"索引"，文件提供完整的"备份"。agent 可以在摘要中丢失的细节和文件中找到的精确信息之间自主切换。

**三档文件压缩级别**（用于超大文件）：
| 级别 | 保留内容 | 触发条件 |
|---|---|---|
| Condensed | 函数签名 | 文件较大 |
| Significantly Condensed | 仅文件名 + 标签 | 文件很大 |
| Not Included | 仅警告图标 | 超大文件 |

### 3.3 Agent Skills 开放标准：惰性加载

**问题**：Skills 的完整指令（包括示例、可执行文件）体积很大。如果全部预加载，大量 token 花在 agent 根本不会用到的 Skills 上。

**Cursor 的方案**：
```
静态上下文（始终加载）:
  - Skills 名称
  - 简短描述（路由逻辑）
  - 何时触发的说明

动态加载（agent 需要时才加载）:
  - 完整 SKILL.md 文件（指令 + 示例 + 可执行文件）
  - 通过 grep 或语义搜索发现和加载
```

这与 Anthropic 的 Agent Skills 开放标准兼容，Claude Code、GitHub Copilot、VS Code 均已采用。

### 3.4 选择性 MCP 工具加载（⭐ 46.9% token 减少）

**问题**：MCP 服务器可能暴露几十个工具，每个工具有长长的描述。大多数对话中只用到少数几个。传统做法是把所有工具描述都注入上下文。

**Cursor 的方案**：

```
文件结构:
  mcp-tools/
    ├── server-a/          ← 按服务器分文件夹（不是扁平索引）
    │   ├── tool-1.json
    │   ├── tool-2.json
    │   └── ...
    └── server-b/
        ├── tool-3.json
        └── ...

静态上下文（始终加载）:
  - 仅工具名称列表（~极少量 token）

动态加载（agent 决定调用时）:
  - grep 按需查找完整工具描述
  - 完整 schema 仅在使用时才加载
```

**A/B 测试细节**：

| 指标 | 值 |
|---|---|
| 测试范围 | 实际调用了 MCP 工具的运行 |
| Token 减少 | **46.9%**（总 agent token） |
| 统计显著性 | 确认显著 |
| 方差 | 高方差，取决于安装的 MCP 服务器数量 |
| 额外收益 | agent 可以检测 MCP 服务器认证状态 → 主动提示"请重新认证" |

**设计决策**：为什么按服务器分文件夹而不是扁平索引？

> "让模型看到一个服务器的所有工具作为一个内聚单元。agent 可以使用完整的 `rg` 参数或 `jq` 来过滤工具描述。"

### 3.5 终端会话文件

**问题**：用户通常手动从终端复制粘贴输出到聊天中。效率低、token 浪费、容易遗漏。

**Cursor 的方案**：
```
终端输出自动同步到本地文件系统
→ agent 可以 grep 相关部分
→ 不需要整个终端历史注入上下文
→ 自然的调试流程，无需手动复制粘贴
```

---

## 四、上下文腐烂（Context Rot）与防御

> *"While the agent can often self-correct, errors remain in context, wasting tokens and causing 'context rot,' where accumulated mistakes degrade the quality of the model's subsequent decisions."*
> — Heule & Katz, "Continually Improving Our Agent Harness"

### 4.1 上下文腐烂的三种形态

| 形态 | 成因 | 影响 |
|---|---|---|
| **错误累积** | Agent 的早期错误留在上下文里，后续决策被其污染 | 错误放大 |
| **工具描述过时** | MCP 服务器更新了工具，但 agent 加载的是旧描述 | 幻觉调用 |
| **Skills 漂移** | 预加载的 Skills 与当前代码库状态不匹配 | 错误模式 |

### 4.2 Cursor 的四道防线

```
防线 1: 动态上下文本身
  → 不预先加载就不存在"过期"问题
  → agent 每次使用时 grep/find → 始终是最新版本

防线 2: 工具错误分类 + 异常告警
  → 分类体系: InvalidArguments / UnexpectedEnvironment /
              ProviderError / UserAborted / Timeout
  → 未知错误 = 始终 bug → 硬告警
  → 对已知类型建立 per-tool per-model 基线
  → 异常偏离立即触发告警

防线 3: 每周自动 triage
  → Cloud Agent + log-searching skill
  → 扫描日志 → 发现新增/尖刺问题 → 创建 Linear ticket
  → 上下文腐烂在积累到临界值前就被处理了
  → 结果: 意外工具调用错误减少 10x

防线 4: MCP 认证状态检测
  → agent 可以检测 MCP 服务器是否需要重新认证
  → 主动通知用户，而不是工具静默消失
  → 防止 agent 基于"工具不可用但不知道原因"的过时上下文做决策
```

---

## 五、动态上下文对幻觉的抑制机制

> *"It can also improve the agent's response quality by reducing the amount of potentially confusing or contradictory information in the context window."*

### 5.1 幻觉的一种产生机制

```
上下文窗口包含:
  规则 A: "使用 React 18"
  规则 B: "使用最新的 React 版本"
  代码中: React 19 API 调用

→ 三条信息互相矛盾
→ Agent 不清楚哪个是权威
→ 基于"听起来最合理"的组合生成输出
→ 幻觉！
```

### 5.2 动态上下文如何减少幻觉

```
上下文窗口（精简后）:
  任务描述
  相关代码片段
  Agent 自行 grep 发现的:
    → 当前 package.json 显示 React 19
    → 相关组件使用 React 19 API

→ 只有经过 agent 主动验证的信息进入上下文
→ 不存在过时的、矛盾的静态规则
→ 幻觉的"原材料"大幅减少
```

**关键**：不是所有信息都对 agent 有帮助。矛盾的、过时的、无关的信息是幻觉的温床。动态上下文通过"不给"而不是"给更多"来减少幻觉。

---

## 六、与压缩的关系：动态上下文 ≠ 压缩

**压缩**（Compaction）是在 token 快满时被动释放空间。
**动态上下文发现**（Dynamic Context Discovery）是从源头防止 token 膨胀。

```
压缩模型（被动）:
  注入所有 → 满了 → 压缩 → 再满 → 再压缩 → ...
  问题: 每次压缩都是有损的

动态上下文模型（主动）:
  只注入必需的 → 按需拉取 → 很少满 → 很少需要压缩
  优势: 不丢信息，因为不需要的信息从未进入上下文
```

两者组合使用效果最好：
- 动态上下文防止不必要的膨胀
- 压缩作为最后的安全网

---

## 七、代价与权衡

| 代价 | 说明 |
|---|---|
| **延迟增加** | 每次动态读取是一次工具调用往返。如果 agent 需要大量上下文，动态模式可能比静态注入慢 |
| **依赖模型能力** | 假设 agent 足够聪明，能判断自己需要什么。弱模型可能漏拉关键上下文 |
| **工程复杂度** | 文件生命周期管理、并发访问、状态一致性都需要基础设施 |
| **质量 vs token 效率** | A/B 测试测量的是 token 减少，不是任务成功率。质量提升目前是定性描述 |

**适用场景判断**：
- ✅ MCP 工具多的项目 → 动态加载收益最大
- ✅ 大型代码库 → 按需搜索比全量注入更合理
- ⚠️ 简单短任务 → 静态注入可能更快（因为不需要额外工具调用往返）

---

## 八、跨工具对比：谁在用类似思路？

| 工具 | 动态上下文策略 | 亮点 |
|---|---|---|
| **Cursor** | 文件化 + 惰性加载 | 5 模式、46.9% MCP token 减少 |
| **Claude Code** | Skills 渐进式加载 + CLAUDE.md 分层 | Skills 只在 agent 判断需要时加载；CLAUDE.md 多层叠加（root → subdir） |
| **Codex CLI** | docs/ 结构化知识 + AGENTS.md 作为目录页 | "给地图，不给一千页手册"；渐进式披露 |
| **Amp (Sourcegraph)** | 换线程代替膨胀 | `/handoff` 命令，长对话本身是问题 |

**趋同点**：所有工具都在从"全量注入"转向"按需发现"。区别在于实现方式——Cursor 最激进（文件化一切），Claude Code 最分层（Skills + CLAUDE.md），Codex 最结构化（docs/ 目录体系）。

---

## 九、2026 年三层上下文架构

动态上下文发现不是"不要静态上下文"——而是把不同类型的上下文放在最合适的层：

```
Tier 1: 静态文件（偏好、规范、不可推断的规则）
  └─ AGENTS.md / CLAUDE.md
  └─ 小而精（<100 行），只写不能从代码推断的内容

Tier 2: 动态检索（agent 按需拉取）
  └─ Skills（名称在静态，指令在动态）
  └─ MCP 工具（名称在静态，schema 在动态）
  └─ 工具输出（全量写入文件，agent 按需读取）

Tier 3: 智能代码理解（结构化知识，跨越多层）
  └─ 调用图、语义索引、业务规则
  └─ 需要专门的基础设施（Sourcegraph Cody、CoreStory 等）
```

**原则**：
- 能动态的绝不静态
- 能从代码推断的绝不手写
- 能写入文件的绝不注入上下文
- 静态层只保留"指针"和"不可推断的约束"

---

## 十、实操建议

1. **审计你的静态上下文** — 检查 CLAUDE.md/AGENTS.md 里哪些信息可以从代码中自动推断。删掉它们。
2. **Skills 用名称 + 描述，不要全量注入** — 让 agent 在需要时 grep 完整指令
3. **MCP 工具多的项目优先采用惰性加载** — 这是 token 节省的最大来源
4. **长对话的历史写入文件，不要全在上下文里** — 双层记忆：摘要 + transcript 文件
5. **监控 token 使用率和上下文腐烂信号** — 如果频繁 compact 或 agent 开始做奇怪的决定，检查是否过时的静态上下文在作祟

---

## 参考资料

- Jediah Katz, "Dynamic Context Discovery", Cursor Blog, January 2026
- Stefan Heule & Jediah Katz, "Continually Improving Our Agent Harness", Cursor Blog, April 2026
- ZenML LLMOps Database: "Dynamic Context Discovery for Production Coding Agents"
- InfoQ: "AI-Powered Code Editor Cursor Introduces Dynamic Context Discovery" (Jan 2026)
- Galster et al. (ETH Zurich), "Configuring Agentic AI Coding Tools: An Exploratory Study", 2026
- Packmind, "Best Context Engineering Tools in 2026"
