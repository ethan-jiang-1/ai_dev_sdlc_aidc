# Claude Code 上下文压缩四层防线：深度拆解

> 基于 Claude Code 2026 年源码逆向分析（`autoCompact.ts`, `microCompact.ts`, `snipCompact.ts`, `contextCollapse.ts`, `compact.ts`, `sessionMemoryCompact.ts` 等）
> 研究日期：2026-07-06

---

## 零、全景：这不是一个功能，是一整套防御体系

Claude Code 的上下文压缩不是"满了就摘要"。它是一个**四层递进、代价严格递增、缓存深度感知**的防御体系。在每次 API 调用之前，四层按序执行：

```
原始消息数组
    │
    ▼
Layer 1: Snip ─────────── 零成本，移除整 turn（Array.filter）
    │ 不够
    ▼
Layer 2: Microcompact ─── 零 API 调用，裁剪 tool_result 内容
    │ 不够                      ├─ Time-based（缓存已冷 → 直接改消息）
    │                           └─ Cached（缓存还热 → cache_edits 服务端删）
    │ 不够
    ▼
Layer 3: Context Collapse ─ 低 LLM 成本，后台 agent 生成，读时投影
    │ 不够                      ├─ projectView() 每轮重建虚拟视图
    │                           └─ drain 作为 413 错误第一响应
    │ 不够
    ▼
Layer 4: AutoCompact ────── 高成本，fork 独立 agent 生成 9 段结构化摘要
                               ├─ Session Memory Compact（优先，零 API 调用）
                               └─ LLM Full Compact（回退，1 次 API 调用）
    │
    ▼
发送 API 请求
```

**核心原则**：能用规则不用模型；能用已有笔记不调新 API；能只删缓存的绝不改消息。

---

## 一、Layer 1：Snip — 零成本整 turn 移除

**文件**：`snipCompact.ts`
**Feature Gate**：`HISTORY_SNIP`（默认关闭，需手动启用）
**成本**：零 API 调用。纯 `Array.filter()`。

### 1.1 逻辑

```typescript
// 伪代码
function snip(messages: Message[]): Message[] {
  return messages.filter((msg, i) => {
    // 移除条件（满足任一即移除整个 assistant + tool_result turn）：
    // 1. 工具调用返回空结果（grep 没找到、glob 没匹配）
    // 2. 工具调用被用户拒绝
    // 3. 该 turn 已被 Context Collapse 覆盖
    return !isRemovable(msg)
  })
}
```

### 1.2 为什么默认关闭

- 粒度太粗：整 turn 消失意味着连 assistant 的思考过程一起没了
- 副作用：某些"空结果"本身就有信息量（"grep 没找到" = "这个符号不存在"）
- 已启用用户群体：明确知道自己在做什么的深度用户

### 1.3 关键输出

`snipTokensFreed` — 传递给后续 AutoCompact 做阈值调整。如果 Snip 已经释放了足够多的空间，下游层可以跳过后再判断。

---

## 二、Layer 2：Microcompact — 缓存感知的精简

**文件**：`microCompact.ts`, `cachedMicrocompact.js`
**成本**：零 API 调用（两条路径都不调 LLM）
**核心挑战**：删内容可以，但不能破坏 prompt cache。

### 2.1 可压缩工具白名单

只有这 8 种工具的输出可以被清理（共同特征：可重跑、无副作用）：

| 工具 | 判断依据 |
|---|---|
| `Read` | 重读文件即可恢复 |
| `Bash` / `PowerShell` | 重跑命令即可恢复 |
| `Grep` | 重新搜索即可恢复 |
| `Glob` | 重新匹配即可恢复 |
| `WebSearch` | 重新搜索即可恢复 |
| `WebFetch` | 重新抓取即可恢复 |
| `Edit` | 操作已体现在文件系统中 |
| `Write` | 操作已体现在文件系统中 |

**MCP 工具默认不可压缩**——未知副作用，无法假设可重跑。

### 2.2 两条执行路径

```
Microcompact 入口
    │
    ├─ Path A: Time-Based (先执行)
    │   触发条件: 最后一条 assistant message 之后
    │            空闲时间 > gapThresholdMinutes (默认 60 分钟)
    │             → 对齐 Anthropic 1 小时 prompt cache TTL
    │   策略: 缓存已冷，直接修改消息是安全的
    │   操作: 将旧 tool_result.content 替换为
    │         "[Old tool result content cleared]"
    │   短路: 执行后直接 return，跳过后面的 Cached Path
    │
    └─ Path B: Cached Microcompact (Time-Based 未触发时)
        触发条件: 注册的可压缩工具数 > triggerThreshold
        策略: 缓存还热，绝不修改本地消息
        操作: 构建 cache_edits block → 随 API 请求发送
              服务端删除对应 cache_reference，
              本地消息数组完全不变
```

### 2.3 Cached Path 的核心：`cache_edits` 协议

这是整个 Microcompact 最具工程含量的部分。

```typescript
// 每次 API 请求附加的 cache_edits
{
  cache_edits: [
    { type: 'delete', cache_reference: 'cr_abc123' },
    { type: 'delete', cache_reference: 'cr_def456' },
    // ...
  ]
}
```

**关键约束**：
- 本地消息数组不修改 → prompt 字节流不变 → prefix hash 不变 → **缓存命中率不变**
- 服务端在推理前执行删除 → 实际消耗 token 减少
- edits 被"钉住"（pinned）：后续每轮 API 调用都重新发送相同的 edit 列表，维持前缀稳定

**`baselineCacheDeletedTokens` 机制**：
```typescript
// 防止 cache_edits 被误判为缓存损坏
// 基线 = 累计删除的 token 数
// 实际缓存 token = reported - baseline
// 这样即使编辑改变了缓存区域，
// 监控系统也不会错误告警
```

### 2.4 Time-Based Path 的阈值设计

为什么默认 60 分钟？

Anthropic 的 prompt cache TTL 是 **1 小时**。最后一条消息之后超过 60 分钟 → 缓存一定已过期 → 直接改消息没有任何缓存损失。这是把**外部 API 行为编码进内部逻辑**的典型案例。

### 2.5 状态机：跨 turn 持久化

```typescript
class MicroCompactState {
  registeredTools: Set<string>     // 所有见过的可压缩 tool_use ID
  toolOrder: string[]              // FIFO 队列，决定删除优先级
  deletedRefs: Set<string>         // 已删除的 ID，防止重复删除
  keepRecent: number = 5           // 安全阀：永远保留最近 N 个工具结果
}
```

这个状态跨 turn 保持，确保：
- 不会重复删除（浪费 cache_edit 配额）
- 先来的先删（FIFO = 最早的工具结果最不重要）
- 最近的结果永远保留（`keepRecent` = 当前上下文通常需要最新的输出）

### 2.6 额外防线：Per-Tool 结果大小上限

在 Microcompact 之前，单个工具结果就已经被截断过：

| 工具 | `maxResultSizeChars` |
|---|---|
| Bash | 30,000 |
| Grep | 20,000 |
| Glob | 100,000 |
| WebFetch | 100,000 |
| Edit / Write | 100,000 |
| **Read** | **∞**（有自己的 offset/limit 机制） |

超限内容落盘到 `tool-results/{tool_use_id}.txt`，上下文中只保留截断预览。这意味着 **Microcompact 处理的是已经经过第一轮截断的数据**。

---

## 三、Layer 3：Context Collapse — 读时投影（最具创新性）

**内部代号**：`marble_origami`
**Feature Gate**：`CONTEXT_COLLAPSE`
**核心创新**：**不修改原始消息，创建虚拟视图。**

### 3.1 设计哲学：SQL VIEW 类比

```typescript
原始消息: [M1, M2, M3, M4, M5, M6, M7, M8, M9, M10]

// Collapse 操作："将 M3-M7 总结为 S1"
Collapse Store:  { range: [3,7], summary: S1 }

// projectView() 输出:
[M1, M2, S1, M8, M9, M10]

// 原始消息数组不变！collapse 是可逆的！
```

### 3.2 为什么用虚拟视图而不是直接改消息

两个原因：

1. **跨重启持久化**：collapse 记录存在 collapse store 里，重启后回放 commit log 重建投影。如果直接改了消息，重启后摘要就丢了——原始消息已被替换，无法恢复。

2. **与 AutoCompact 解耦**：如果 collapse 已经让 token 降到阈值以下，AutoCompact 就不需要触发。直接改消息无法区分"已经 collapse 过了"和"还需要 AutoCompact"。

### 3.3 两级生命周期：Staged → Committed

```
STAGED (stagedQueue, 存在 snapshot 中)
  ├─ 由 ctx-agent (后台 LLM 分析) 生成
  ├─ 持久化到磁盘 snapshot
  └─ 尚未应用到对话视图
         │
         │ applyCollapsesIfNeeded() — 毫秒级，零 API 调用
         ▼
COMMITTED (commit log, append-only)
  ├─ fold 正式生效
  ├─ projectView() 实际替换消息
  └─ 持久化到磁盘 commit log
```

### 3.4 Commit Log 格式

```typescript
type ContextCollapseCommitEntry = {
  type: 'marble-origami-commit'
  collapseId: string
  summaryUuid: string
  summaryContent: string       // 完整 XML collapse tag
  summary: string              // 纯文本摘要
  firstArchivedUuid: string    // collapse 范围起点
  lastArchivedUuid: string     // collapse 范围终点
}
```

### 3.5 projectView() — 每轮的虚拟视图重建

```typescript
// query.ts 每次循环迭代
if (contextCollapse) {
  const collapseResult = await contextCollapse.applyCollapsesIfNeeded(
    messagesForQuery, toolUseContext, querySource
  )
  messagesForQuery = collapseResult.messages  // 这是投影，不是突变
}
```

`projectView()` 每轮**重放整个 commit log**，从原始消息 + 所有已提交的 collapse 记录重建当前应发送给模型的视图。

### 3.6 ctx-agent：后台异步分析引擎

Collapse 摘要的生成**不阻塞用户**：

```
主线程: [用户输入] → [压缩流水线] → [API 请求] → [响应]
                                        ↕ (并行，非阻塞)
ctx-agent: [分析对话] → [识别已完成任务区间]
           → [LLM 生成摘要] → [Stage 到队列]
           ↑_____________________________|
           (空闲时重新 spawn，继续分析新对话)
```

这是延迟优化的关键——用户永远不为 collapse 摘要的生成等待。

### 3.7 阈值与 AutoCompact 的互斥

```
effectiveContextWindow
├─ 90% → commit-start: applyCollapsesIfNeeded() 开始提交 staged fold
├─ 93% → AutoCompact 旧触发点 (Collapse 开启后被禁)
└─ 95% → blocking-spawn: 强制 ctx-agent 紧急 collapse
```

当 `CONTEXT_COLLAPSE` 开启时，**AutoCompact 的主动触发被显式禁用**。原因：

> "Collapse 就是开启后的上下文管理系统。90% commit / 95% blocking 的流程已经覆盖了空间管理。AutoCompact 在 ~93% 触发，正好夹在中间——它会和 collapse 竞速，并且通常先赢，把 collapse 即将保存的细粒度上下文全部碾碎成粗粒度摘要。"

### 3.8 PTL 恢复中的优先级

```
API 返回 413 (prompt_too_long)
  │
  ├─ 第 1 级: Context Collapse drain ⭐
  │   条件: CONTEXT_COLLAPSE 开启
  │   操作: recoverFromOverflow() — 提交所有 staged collapse
  │   成本: 零 API 调用
  │   结果:
  │     committed > 0 → 用投影重试 API ✓
  │     committed = 0 → 进入第 2 级
  │
  ├─ 第 2 级: Reactive Compact
  │   操作: 紧急全量 AutoCompact
  │   成本: 1 次 API 调用
  │
  └─ 第 3 级: 放弃 → yield 错误给用户
```

### 3.9 缓存代价

Context Collapse 的读时投影**刻意牺牲了缓存效率**：每次 collapse 范围变化，所有后续 cache entry 失效。这是有意的取舍——**缓存效率换上下文保真度**。

---

## 四、Layer 4：AutoCompact — LLM 全量摘要

**文件**：`autoCompact.ts` (~350 行), `compact.ts` (~1600 行)
**触发阈值**：`effectiveContextWindow - 13,000 tokens`
**成本**：1 次 LLM 调用（Session Memory Compact 路径为 0 次）

### 4.1 两条路径：Session Memory Compact 优先

```
AutoCompact 入口
    │
    ├─ Path A: Session Memory Compact (优先！)
    │   触发: 后台已维护会话笔记
    │   操作: 直接用笔记替代旧消息，不调 API
    │   成本: 零 API 调用
    │   压缩率: ~60-80%
    │
    └─ Path B: LLM Full Compact (回退)
        触发: 无可用会话笔记
        操作: fork 独立 compact agent → 调 LLM → 生成 9 段摘要
        成本: 1 次 API 调用
        压缩率: ~80-95%
```

### 4.2 Session Memory Compact 详解

后台持续维护一份 Markdown 格式的会话笔记（9 区段模板）。压缩时直接用笔记替代旧消息。

**后台提取触发条件（双条件 AND）**：
```typescript
shouldExtract = (
  (tokenThresholdMet && toolCallThresholdMet) ||  // token + 工具调用都达标
  (tokenThresholdMet && !hasToolCallsInLastTurn)  // token 达标 + 自然断点
)
// 自然断点优先：无工具调用的回合是安全写入时机
```

**保留策略**：
```typescript
{
  minTokens: 10_000,            // 至少保留 10K tokens 近期消息
  minTextBlockMessages: 5,      // 至少保留 5 条文本消息
  maxTokens: 40_000,            // 硬上限 40K tokens
}
```

**API 不变量保护**：
```typescript
function adjustIndexToPreserveAPIInvariants() {
  // 1. Tool 配对：保留的 tool_result 必须能找到对应 tool_use
  // 2. Message ID 内聚：streaming 模式下同 message.id 的
  //    content blocks（thinking + tool_use）必须一起保留
}
```

这两条修复将 Sonnet 4.6 上 SM-compact 的失败率从 **2.79% → 0%**。

### 4.3 LLM Full Compact：9 段结构化摘要

当 Session Memory Compact 不可用时，fork 一个独立 compact agent。

**关键设计 1：`NO_TOOLS_PREAMBLE`**

```text
CRITICAL: Respond with TEXT ONLY. Do NOT call any tools.
- Do NOT use Read, Bash, Grep, Glob, Edit, Write, or ANY other tool.
- You already have all the context you need in the conversation above.
- Tool calls will be REJECTED and will waste your only turn — you will fail the task.
- Your entire response must be plain text: <analysis> block followed by <summary> block.
```

为什么需要这么强硬？Compact agent 为复用 prompt cache 必须继承主 agent 的完整工具集。Sonnet 4.6 在自适应思考模式下有 **2.79% 的概率会忍不住调用工具**。`maxTurns: 1` 的限制意味着一旦调用工具，整个 compact 就失败了。因此 preamble 在最前面，再加一份 `NO_TOOLS_TRAILER` 在末尾，"首尾夹心"双重保险。

**关键设计 2：`<analysis>` 草稿区（事后被剥离）**

```xml
<analysis>
  [模型自由发散：用户意图 → 技术决策 → 代码变更 → 错误修复]
  [这是草稿纸，不受格式限制，但最终会被删除]
</analysis>
```

```typescript
// 生成后立即剥离
formattedSummary = formattedSummary.replace(
  /<analysis>[\s\S]*?<\/analysis>/, ''
)
```

这是 **drafting scratchpad pattern（草稿本模式）**——思考过程消耗 token 提高了摘要质量，但**不进入压缩后的上下文**，不污染后续对话。Chain-of-Thought 的变体，但 CoT 保留思考过程，这里主动删除。

**关键设计 3：`<summary>` 9 段结构化输出**

```xml
<summary>
1. Primary Request and Intent      — 所有用户明确请求和意图
2. Key Technical Concepts          — 技术概念、框架、架构决策
3. Files and Code Sections         — 每个操作过的文件、完整代码、修改理由
4. Errors and Fixes                — 每个错误及其修复方案
5. Problem Solving                 — 已解决问题和进行中的排查
6. All User Messages               — 所有用户消息原文（不压缩！）★
7. Pending Tasks                   — 明确要求的待办任务
8. Current Work                    — 压缩前最后一刻的精确工作描述
9. Optional Next Step              — 下一步计划（必须附对话原文引用）
</summary>
```

**第 6 节是最关键的防漂移锚点**："All User Messages" 要求列出所有用户消息**原文**。用户的纠正、偏好、隐含语境——摘要可能平滑掉，但原文保留确保模型不会偏离用户真正说过的话。

**第 9 节的引用约束**：要求包含最近对话的 **verbatim quotes**（逐字引用原文）来证明建议的下一步确实在推进中。防止模型自己"编造"下一步。

### 4.4 后压缩恢复链

AutoCompact 完成后，重新注入关键上下文：

```typescript
async function rebuildAfterCompact() {
  // 1. 恢复文件上下文（最多 5 个文件，50K token 预算）
  // 2. 重注入 Skills（每个最多 5K）
  // 3. 恢复 plan mode 状态
  // 4. 恢复 MCP 指令
  // 5. 恢复 CLAUDE.md 分层上下文
}
```

### 4.5 Circuit Breaker（电路断路器）

```typescript
const MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES = 3

// 来自 BQ 查询的真实数据 (2026-03-10):
// 1,279 个 session 出现 50+ 连续失败（最高 3,272 次）
// 全球每天浪费约 250,000 次 API 调用
```

**触发**：连续 3 次压缩失败 → 整个 session 自动压缩**永久禁用**。
**重置**：成功压缩。
**熔断后**：用户仍可手动 `/compact`（有独立的 PTL 重试逻辑）。

为什么需要断路器？某些 session 处于"结构性不可压缩"状态——压缩请求本身就 prompt_too_long。没有断路器的话，它会在每轮循环中都重试，持续失败。

### 4.6 PTL 重试（手动 `/compact` 路径）

```typescript
for (attempt = 0; attempt < MAX_PTL_RETRIES (3); attempt++) {
  try {
    summary = await streamCompactSummary(messages)
    break  // 成功
  } catch (PromptTooLong) {
    // 按 API round 分组，丢弃最旧的消息组
    messages = truncateHeadForPTLRetry(messages, errorResponse)
    // 无法解析 gap → 丢弃 20% 的最老消息组（crash-only 恢复）
  }
}
```

---

## 五、正确的触发顺序与计算

```typescript
// 各层阈值计算
effectiveWindow = contextWindow - min(maxOutputTokens, 20_000)
// 以 200K 窗口为例: 200K - 20K = 180K effective

autoCompactThreshold = effectiveWindow - 13_000   // ~167K → ~83.5%
warningThreshold     = effectiveWindow - 20_000   // ~160K → ~80%
blockingThreshold    = effectiveWindow - 3_000    // ~177K → ~97%

// Collapse 阈值（当 CONTEXT_COLLAPSE 开启时）
collapseCommitStart  = effectiveWindow * 0.90     // 90%
collapseBlocking     = effectiveWindow * 0.95     // 95%
```

以 200K 模型窗口为例的实际运行：
```
0% ──── 60% ──── 80% ──── 83.5% ──── 90% ──── 95% ──── 97% ──── 100%
正常   MC触发  警告     AC触发    ColCmt   ColBlk   阻塞     硬上限
```

---

## 六、各层的缓存感知对比

| 层 | 缓存策略 | 理念 |
|---|---|---|
| Snip | 直接删除消息 → 破坏后续缓存 | 只在 `HISTORY_SNIP` 手动开启，用户自担 |
| Microcompact (Cached) | `cache_edits` API 服务端删除 → 本地不变 → 缓存命中率不变 | "绝不碰消息" |
| Microcompact (Time-based) | 仅在缓存已冷（>60min 空闲）时直接修改 | "缓存反正已经过期了" |
| Context Collapse | 投影改变消息内容 → 后续缓存失效 | "缓存效率换上下文保真度" |
| AutoCompact | 全量重建消息数组 → 缓存全清 → 重新建立 | "反正已经到了极限，重来" |

---

## 七、实操建议

1. **主动 `/compact` 时机**：上下文 **50-60%** 时手动触发，比等到 80%+ 被动触发质量高得多
2. **在自然断点压缩**：任务告一段落时手动 compact，让摘要覆盖完整语义段（Erik Schluntz 的"午饭断点"策略）
3. **关键约束写进 CLAUDE.md**：compaction 可能丢失只提过一次的硬约束（"不要用库 X"），写入 repo 文档中作为持久锚点
4. **监控 compact 频率**：如果频繁 compact，说明要么任务太大（拆成多个 session），要么上下文膨胀太快（清理 CLAUDE.md 和 Skills 的冗余内容）
5. **大任务拆 session**：与其让一个 session 经历多次 compact（信息逐次衰减），不如在自然边界拆成多个 session，每个带着清晰的 handoff 上下文
6. **Collapse > AutoCompact**：如果开了 `CONTEXT_COLLAPSE` feature flag，collapse 的细粒度保存比 AutoCompact 的全量摘要保真度更高

---

## 参考资料

- Claude Code source analysis: `wuwangzhang1216/claude-code-source-all-in-one` (GitHub)
- DeepWiki: `sanbuphy/claude-code-source-code` — Context Management and Compaction
- CSDN: "Claude Code 深度拆解：Agent 执行内核 2 — Pipeline 与上下文压缩"
- CSDN: "Claude Code 的上下文压缩流水线：一个 200K 窗口是怎么被精打细算的"
- CSDN: "context-collapse-deep-dive"
- CSDN: "Claude Code 如何压缩上下文：Microcompact、Prompt Cache 与 cache_edits 工程拆解"
- dev.to: "How Claude Code Manages Infinite Conversations in a Finite Context Window"
- dev.to: "Memory management in Claude Code: Context Pipeline" & "Session Memory and Safe Compaction"
- 微信公众号: "Claude Code 压缩设计深度解读"
