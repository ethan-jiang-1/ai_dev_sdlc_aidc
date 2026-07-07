# Ryan Lopopolo — OpenAI Harness Engineering 先驱

> OpenAI Frontier Product Exploration 团队 Member of Technical Staff。曾任职 Stripe、Snowflake、Citadel、Brex（领导 350 人 developer productivity）。他领导了零人手写代码实验，创造了 "Harness Engineering" 概念，已被 Martin Fowler 和 ThoughtWorks 推广。

---

## 实验：零人手写代码，零人审查

2025 年中，Lopopolo 对团队施加了一条极端约束：**不写一行代码，不做一次代码审查。** 团队构建了一个内部 beta 产品（Electron 数据分析 Agent 应用），完全由 AI Agent 产出。

| 指标 | 数据 |
|------|------|
| 团队 | 3 → 7 名工程师（+ PM 和设计师） |
| 时长 | ~5 个月 |
| 产出 | **~1,000,000 行代码（零人手写）** |
| 总 PR 数 | ~1,500+ |
| Token 消耗 | ~**10 亿 tokens/天**（~$2-3K/天） |
| 构建硬上限 | **<1 分钟** |

### PR 吞吐量演进

| 时期 | PR/工程师/周 |
|------|-------------|
| GPT-5.2 时代 (2025 末) | ~3.5 |
| GPT-5.2 + Symphony | 5-10/天 |
| GPT-5.5 时代 (2026 中) | **~70** |

Lopopolo 将其描述为 **"超过线性扩展"**——每个模型版本的改进在前一个基础上叠加，harness 基础设施立即吸收所有增益。

---

## 核心哲学

> *"Agents aren't hard; the Harness is hard."*

> *"It's borderline negligent not to use a billion tokens a day."*

当 Agent 失败时，不要 tweak prompt——问：

> *"What capability, context, or structure is missing that prevents the agent from succeeding autonomously?"*

Agent 只有**两个杠杆**：上下文 + 工具。Harness Engineering = 系统性设计两者。

---

## 五大支柱（详细版）

### 1. 结构化文档作为 System of Record

`docs/` 目录是 Agent 的**唯一真相来源**。关键文件：

| 文件 | 内容 |
|------|------|
| `agent.md` | ~100 行入口——Agent 启动时首先读取 |
| `spec.md` | 产品规格 |
| `core-beliefs.md` | 不可商量的架构原则 |
| `tech-tracker.md` | 技术栈追踪 |
| `quality-score.md` | 质量指标仪表盘 |

核心原则：**"地图，不是手册"**——从小入口渐进式披露到更深层文档。如果不在仓库里，**对 Agent 而言就不存在**。Slack、Google Docs、隐性知识 = 不可见。

### 2. AGENTS.md — Agent 的错误日志

- 活的软件工程原则 + 过往错误 + 纠正文档
- 实验中增长到 **100-150 条评论**
- 作为自动化**反 slop 系统**的种子数据
- **"Doc-gardening agents"** 在后台持续扫描代码库，识别与 AGENTS.md 的偏差，自动开启可合并的清理 PR

### 3. 机械护栏

严格分层架构由 linter 和结构测试强制执行：

```
Types → Config → Repo → Service → Runtime → UI
```

- 依赖**只能向前**流动；违规则 CI 失败
- Lint 错误格式化为**带嵌入式修复指令的散文**——Agent 可自主阅读并纠正
- 自定义 linter **由 Codex 自己生成**

### 4. Agent 优先的软件架构

- 代码为 **Agent 理解**而组织，不是为人类可读性
- ~500 个 NPM 包，深度分解——Lopopolo 称之为 **"万人架构"**（7 人团队）
- 偏好**"无聊"技术**（稳定 API，丰富训练数据覆盖）
- 一切结构化使 Agent 可通过 git worktree 启动隔离实例

### 5. 全面可观测性

从第一天起的全本地栈：

```
Vector (日志聚合) → VictoriaMetrics (指标) → Grafana (仪表盘) → 分布式追踪
```

**额外能力**：
- **Chrome DevTools Protocol** 集成——Agent 可拍 DOM 快照、截屏、导航页面
- **Per-worktree 可观测性**——Agent 直接查询 LogQL/PromQL
- 这使 prompt 如 *"确保服务启动 <800ms"* 可被自动验证
- **合并后审查**替代合并前审查——人类使用可观测性数据抽样已合并代码
- Agent 自主插桩——日志、指标、追踪 span 全部由 AI 生成

---

## Symphony：多 Agent 编排系统

Symphony 是整个实验的核心基础设施。用 **Elixir** 构建——**模型自己选的**，而非团队决定。

### 为什么是 Elixir？

模型论证：BEAM 虚拟机的 **进程监督能力**（GenServer + supervision tree）是管理大量并发编码 Agent 的理想基础设施。每个 PR 是一个独立 GenServer 进程，如果崩溃则被监督树自动重启。

### 核心机制

- **将人类从同步循环中完全移除**
- 管理完整 PR 生命周期：代码创作 → **Agent 审查 Agent** → CI → 合并冲突 → 合并
- 如果 PR 被拒绝：worktree 丢弃，ticket 重新开始——但**附带失败分析**
- **反霸凌 prompt**：Agent-reviewer 被告知偏向合并、仅标记 ≤P2 优先级问题

### "幽灵库（Ghost Library）"

Symphony 引入的最激进概念之一：

> 软件以**高保真规范**而非源代码的形式分发。依赖被"内化"——Agent 一个下午就能 vendoring 并重写中低复杂度库。实现按需再生。

---

## 构建系统演化

Lopopolo 对构建速度有硬性执念——**<1 分钟**的内循环上限。

| 阶段 | 工具 | 结果 |
|------|------|------|
| 1 | Makefiles | 太慢 |
| 2 | Bazel | 迁移成本高 |
| 3 | Turbo | 接近但不够 |
| 4 | **Nx** | **<1 分钟达成** |

Agent 友好的 CLI 输出：抑制通过的测试，只显示失败。

---

## Codex 模型演化

两条模型线：**Codex**（有主见的、harness 优化的）vs **主链 GPT-5**（通用的、可操控的）。

| 模型 | 关键能力 | 时间 |
|------|---------|------|
| **Codex Mini** | 慢，需深度分解；初始约人类 1/10 速度 | 2025 早期 |
| **GPT-5.2** | 编码 Agent 的"奇点时代"；~3.5 PR/周 | 2025/08 |
| **GPT-5.3** | 后台/并行工具调用；Agent 对阻塞操作不耐受 → 强制 <1min 构建 | — |
| **GPT-5.4** | 统一编码 + 通用推理 + Computer Use + 视觉；100 万 token 上下文 | — |
| **GPT-5.5** | 嵌入式浏览器 Computer Use；~70 PR/周 | 2026 |
| **Codex Max** | 设计用于 24hr+ 自主运行；内建上下文管理/压缩；可生成子 Agent | 2026 |

---

## 人类的新角色

Lopopolo 的时间分配变化：

| 之前 | 之后 |
|------|------|
| 50-70% 代码产出 | ~30% 最难的重构 + 0→1 构思 |
| — | ~30% 与客户对话 + 优先级 |
| — | ~30% 排期 + 人员安排 |

**周五 "GC 会议"**：每周同步站立会。团队识别反复出现的 slop 模式，编码回 harness——同样的反馈**永远不需要给两次**。

**新员工入职即高效**：每增加一个团队成员，两周内 PR 吞吐量提升 5-15%——因为他们立即受益于 harness 中积累的上下文。

**PM 和设计师也提交代码**：通过 PRD、测试、文档和 harness 规则——无需打开 IDE。PM 在实验中提交了 ~10 万行生产代码。

---

## 关键结论

### 1. 代码现在是负债，不是资产

每个工程组织都建立在"代码昂贵"的假设上。这个假设已经反转。当 Agent 可以按需生成代码，**拥有更少的代码比拥有更多的代码更有利**。

### 2. Spec-Driven Development 被反转

传统 SDD：先写 spec → AI 实现 → 人类验证。
Lopopolo 的反转：**先产出代码作为稻草人 → 完善它 → 从被接受的产物中蒸馏出规范。**

### 3. 人类注意力是瓶颈

不是 token 可用性。不是 Agent 能力。是**人类能审查和判断多少东西**。

### 4. "幽灵库"

软件以规范而非源码分发。Agent 按需再生实现。依赖不再是代码依赖，而是规范依赖。

### 5. Agent 审查 Agent

整个实验中**零人类合并前代码审查**。Agent 审查 Agent，人类只在合并后抽样。反霸凌 prompt 确保审查不吹毛求疵。

---

**Source:** [ZenML: Zero Human-Written Code](https://www.zenml.io/llmops-database/zero-human-written-code-harness-engineering-for-autonomous-ai-agents-at-scale) · [ZenML: Extreme Harness Engineering](https://www.zenml.io/llmops-database/extreme-harness-engineering-building-production-software-with-zero-human-written-code) · [InfoQ: OpenAI Harness Engineering](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/) · [Tessl Podcast #109: full transcript](https://tessl.io/podcast/109/) · [AI Native Dev Podcast](https://podcasts.apple.com/sg/podcast/ryan-lopopolo-openais-framework-for-shipping-code-at/id1756073806?i=1000771862526) · [36Kr Chinese coverage](https://eu.36kr.com/en/p/3765104802349574) · [InfoQ China](https://www.infoq.cn/article/xeXddcuzu78D7mC5wyBy) · [Tencent Cloud: Harness Engineering](https://cloud.tencent.com.cn/developer/article/2652786) · [CSDN: 百万行代码零手工撰写](https://blog.csdn.net/weixin_53961451/article/details/158600036) · [Toutiao/InfoQ: 严禁手写代码](https://m.toutiao.com/article/7650764109256000040/)
