# AI Coding Agent 上下文压缩策略深度研究

> 基于 Claude Code、Codex CLI、Cursor、OpenCode、Gemini CLI、Amp 六家 2026 年最新实现
> 研究日期：2026-07-06

---

## 一、为什么上下文压缩是 Agent 的「隐形杀手」

每个 AI Coding Agent 都跑在一个循环里：

```
用户输入 → 构建提示词 → 模型推理 → 工具调用 → 追加输出 → 再次推理 → ...
```

每轮工具调用都会往上下文窗口里追加内容。一个复杂任务可能触发**上百次工具调用**，上下文窗口被迅速填满。当 token 耗尽时，Agent 只有两个选择：

- **崩溃**（413 错误，用户前功尽弃）
- **压缩**（丢掉一些东西，继续干活）

**所有压缩都是有损的。丢掉什么、保留什么，直接决定 Agent 能不能把任务做完。**

---

## 二、Codex CLI：加密状态 + 用户消息神圣不可侵犯

**设计哲学：用户消息是神圣的，其余都可以压缩。**

### 2.1 核心端点：`/responses/compact`

当 token 超过 `auto_compact_limit` 时，Codex 调用专用的 `/responses/compact` API 端点。

### 2.2 关键数据结构

```json
// compact 响应中的特殊条目
{
  "type": "compaction",
  "encrypted_content": "<opaque encrypted blob>"
}
```

**`encrypted_content` 是三件事的巧妙结合：**

| 层面 | 机制 |
|---|---|
| **隐私** | 使用客户专属密钥加密，OpenAI 不存储对话原文 |
| **语义保留** | 模型在服务端解密后能"理解"之前发生了什么，不需要逐字回放 |
| **ZDR 兼容** | Zero Data Retention — 密钥单独存储，密文无密钥 = 不可读 |

### 2.3 触发机制与反叛

```
auto_compact_limit → 触发 compact
```

**v0.100.0 引入硬限制**：`effective_limit = min(user_config, context_window × 90%)`

这引发了社区反弹——强制 90% 压缩导致某些复杂项目丢失关键上下文，agent 做出破坏性修改。2026 年 6 月新增 `--disable auto_compaction` 内部开关（PR #28260）。

### 2.4 Codex 压缩的独特规则

1. **近期用户消息原样保留** — 不压缩、不摘要
2. **早期对话替换为 handoff 摘要**
3. **压缩后重新注入 `AGENTS.md`** — 这是其他家都做不到的：压缩不丢项目规范
4. **`new_context` 工具的逃生舱** — 模型可以主动请求新上下文窗口，不花 token 做摘要

### 2.5 提示缓存与压缩的深度耦合

Codex 的提示词构建遵循严格顺序：静态前缀（指令、工具定义）→ 动态后缀（用户消息、工具输出）。

压缩后的历史放在**静态前缀之后、动态后缀之前**，确保：
- 静态前缀始终缓存命中
- 压缩不会破坏已有的缓存前缀

**一个被修的 bug**：MCP 工具枚举顺序不一致 → 缓存全盘失效 → compact 之后模型"失忆"。现在工具列表被固定排序。

---

## 三、Claude Code：四层渐进防线

**设计哲学：便宜的先用，贵的最后用。压缩前先试剪裁，剪裁不行再试塌缩，塌缩不行才调 LLM。**

### 3.1 四层架构

```
Layer 1: Snip (零成本)
   → 纯 Array.filter()，直接删除空结果/被拒的轮次
   ↓ 不够

Layer 2: Microcompact (零 API 调用)
   → 裁剪 6 种工具输出 (Read, Bash, Grep, Glob, WebSearch, WebFetch)
   → 只压缩不在缓存中的消息（保护提示缓存命中率）
   决策公式: compress if (tokens_saved > tokens_lost_from_cache_invalidation)
   ↓ 不够

Layer 3: Context Collapse (低 LLM 成本)
   → "虚拟视图" — 不修改原始消息数组，用 collapse_store 投影
   → collapse 记录可跨会话恢复
   → 413 错误的第一响应：drain 所有 pending collapse
   ↓ 不够

Layer 4: AutoCompact (完整 LLM 摘要)
   → 移除图片、重注入附件
   → 调用 LLM 生成全量 session 摘要
   → 恢复文件上下文 (最多 5 文件，50K token 预算)
   → 重注入 Skills (每个最多 5K)
   → 熔断器: 连续 3 次失败 → 自动禁用
```

### 3.2 触发公式

```
autoCompactThreshold = effectiveContextWindow - 13000 tokens
```

即约 **95% 容量时才触发**。在此之前，前三层已经默默释放了大量空间。

### 3.3 三级错误恢复

```
413 Error:
  Level 1: Context Collapse Drain → 提交所有 pending collapse → retry
  Level 2: Reactive Compact → 紧急全量压缩 → retry
  Level 3: 放弃 → 返回错误给用户

max_output_tokens 截断:
  Level 1: 升级 token limit 8k → 64k
  Level 2: 注入接续元提示 "No apology. No recap. Pick up mid-thought."
```

### 3.4 已知丢失模式（五类）

研究确认**所有压缩方案都会丢失以下五类信息**：

1. **精确数值** — 阈值、端口号、版本号变散文（"retry limit = 3" → "配置了重试限制"）
2. **跨任务依赖** — 摘要器独立处理每一段，丢失段间关联
3. **硬约束** — "永远不要用库 X" 如果只出现过一次，可能被丢弃
4. **决策理由** — 保留了"做了什么"，丢失了"为什么这样做"
5. **隐式风格** — 用户演示的格式化习惯但从未明确声明

---

## 四、Cursor：不压缩，而是让 Agent 自己找

**设计哲学：文件化 + 按需拉取。A/B 测试 token 降低 46.9%。**

### 4.1 Dynamic Context Discovery

长工具输出 → **写入文件**而非保留在上下文 → Agent 需要时用 `grep`/`tail`/`rg` 检索。

### 4.2 五个应用场景

| 场景 | 实现 |
|---|---|
| 长 MCP 响应 | 写入文件，Agent 用 `tail` 检查末尾 |
| 历史引用 | 摘要时允许 Agent 回溯聊天记录文件 |
| Skills 开放标准 | Skills 只在使用时加载 |
| MCP 工具按需加载 | 只加载当前任务需要的工具 |
| 终端会话 | 暴露为可发现文件 |

### 4.3 与其他方案的关键差异

Cursor 从根本上改变了问题定义：**不是"怎么压缩上下文"，而是"怎么让上下文不膨胀"。**

---

## 五、其他三家的有趣策略

### 5.1 Gemini CLI：激进早压 + 自校正

- 压缩阈值从 70% → **20%** → 回调至 50%（20% 太激进，丢信息太多）
- 摘要分两步：先生成 XML `<state_snapshot>`，再调模型**批判性验证**是否漏了关键技术细节

### 5.2 OpenCode：可逆隐藏

- "不真删"——用时间戳标记隐藏，数据仍在数据库
- 压缩后**回放最后一条用户消息**，确保 Agent 知道当前任务是什么

### 5.3 Amp（Sourcegraph）：不压缩，换线程

- 哲学：长对话本身就是问题，换线程比压缩好
- `/handoff` 命令开新线程
- 2026 年新增 90% 自动管理

---

## 六、2026 年六条新共识

| # | 共识 | 实践含义 |
|---|---|---|
| 1 | **分层渐进** | 定义多水位线，越接近上限手段越激进，避免悬崖式塌方 |
| 2 | **成本递增** | 零成本操作（截断、过滤）→ 低成本（塌缩）→ 高成本（LLM 摘要） |
| 3 | **增量摘要 > 全量摘要** | 保留"活摘要"，每次只合并增量，避免"摘要的摘要" |
| 4 | **用真实 token，别估算** | `text.length / 3` 在中英混合场景误差 30-50%，必须用 `usage.totalTokens` |
| 5 | **用户消息有特权** | Codex 原样保留，OpenCode 压缩后回放，各家都至少保证用户纯文本不裁 |
| 6 | **保护近端 + 单调边界** | 最近 ~8K token 不压缩。滑窗式替换是隐蔽杀手：每步缓存失效一次，实测 177 step 烧了 $77.3（83% 是 cache_write） |

---

## 七、从 Michael Bolin 的 Agent Loop 看 compact 的本质

回到 Michael Bolin 揭示的 Codex 架构，`/responses/compact` 不是独立的优化，而是 **Agent Loop 的有机组成部分**：

```
Agent Loop 的主循环:
  while not done:
    prompt = build_prompt(static_prefix + history + user_msg)
    response = POST /responses (prompt)
    
    if response.tool_calls:
      execute_tools()
      history.append(tool_outputs)  ← 每次追加都在推高 token 数
      
      if token_count > auto_compact_limit:  ← 这就是 compact 介入点
        compacted = POST /responses/compact(history)
        history = [compacted]  ← 压缩后的 encrypted_content 替代全量历史
    
    if response.assistant_message:
      return response

关键洞察：compaction 必须在每次工具调用后检查。
不是"等到满了再压"，而是"每次追加后判断要不要压"。
```

这就是为什么 **prompt caching 和 compaction 是不可分割的**：compact 后的新前缀必须能命中缓存，否则 compact 省下的 token 全花在 cache_write 上，净收益为零甚至为负。

---

## 八、实操启示：给用 Claude Code 的建议

1. **别等自动 compact** — 在上下文用量 **50-60%** 时主动 `/compact`，比等到 95% 被动触发质量高得多
2. **在自然断点压缩** — Erik Schluntz 的"午饭断点"策略：任务告一段落时手动 compact，让摘要覆盖完整语义段
3. **关键约束写进文件** — 因为 compact 可能丢失硬约束（"永远不要用库 X"），把这些写进 CLAUDE.md 或 repo 文档里，不在对话里只提一次
4. **监控缓存命中率** — 如果频繁 compact 后 cache 命中率下降，可能是压缩方式在破坏前缀匹配
5. **换 session 有时比 compact 更好** — 长对话积累的不仅是 token，还有模型的"思维惯性"；Amp 的 `/handoff` 思路值得借鉴

---

## 参考资料

- Michael Bolin, "Unwinding Codex's Agent Loop", OpenAI Engineering Blog, Jan 2026
- "Shell + Skills + Compaction: Tips for long-running agents", OpenAI Developers Blog, Feb 2026
- Claude Code source analysis: `claude-code-deep-analysis/07-context-window.md`
- "Context Compression in AI Agents: Hermes vs. Claude Code", mem0.ai, 2026
- "横向拆解 Claude Code、Codex 等六大 Agent 上下文压缩策略", 知乎/腾讯云, 2026
- GitHub: openai/codex PR #28260, #27488, #29255; Issue #11805
