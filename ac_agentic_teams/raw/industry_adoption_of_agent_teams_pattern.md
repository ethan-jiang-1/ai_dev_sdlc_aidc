# Anthropic "Agent Teams" 模式的行业采纳调研

**调研日期**: 2026-03-06
**调研目的**: 寻找与 Anthropic "Agent Teams" 核心思想高度一致（八九分相似）的外部实践。

---

## 核心特征（筛选标准）

从 Anthropic 的 C 编译器文章中提炼出的 Agent Teams 核心 DNA：

1. **多个 LLM 实例并行**工作在同一个代码库上
2. **长时间自主运行**，无需人类在场（"walk away"）
3. **无中央编排 agent**，每个 agent 自主决定做什么（"pick the next most obvious problem"）
4. **Git 同步 + 任务锁**防止冲突（文件锁、push/pull/merge）
5. **容器隔离**，每个 agent 独立环境（Docker）
6. **测试驱动的自主进展**（tests as verifier，agent 靠测试结果判断方向）
7. **Agent 角色专业化**（有的写功能、有的管质量、有的管文档、有的做性能优化）
8. **无限循环 harness**（完成一个任务自动开始下一个，永不停止）

---

## Gas Town — Steve Yegge（相似度：9/10）

**唯一与 Anthropic Agent Teams 高度吻合的外部实现。**

### 基本信息

- **作者**: Steve Yegge（前 Google/Amazon 工程师，知名技术博主）
- **发布**: 2026 年 1 月 1 日（比 Anthropic 的 C 编译器文章早一个月）
- **定位**: 开源的多 agent 编排系统，被称为"AI coding agents 的 Kubernetes"
- **核心理念**: 从单个 AI 副驾驶转变为监督一个自主的 agent 工厂（"autonomous factory of agents"）

### 架构详解

#### 1. 层级化的 Agent 角色体系

Gas Town 采用了 Mad Max 主题的角色命名：

- **The Mayor（市长/项目经理）**
  - 顶层 AI 协调者
  - 分析目标、理解现有代码库、将复杂请求分解为结构化计划
  - 创建 Beads（原子任务单元）并组织成 Convoys（任务组）
  - 管理依赖关系（例如：等待后端完成后再启动集成测试）
  - 持续跟踪所有 Polecat 的进度

- **Polecats（工作 Agent）**
  - 执行具体编码任务的 agent
  - 系统可以同时运行数十个 Polecats，每个处理不同的 Bead
  - 每个 Polecat 在独立的 Git 分支中工作
  - 完成任务后自动被"nuked"（终止）并合并分支
  - 示例 agent 名称：`obsidian`、`quartz`、`jasper`

**与 Anthropic 的对比**:
- Anthropic: 去中心化，无 orchestrator，每个 agent 自主选择任务
- Gas Town: 层级化，Mayor 分配任务给 Polecats
- 相似度: 两者都实现了多 agent 并行 + 角色专业化，只是编排策略不同

#### 2. 任务结构

- **Rigs（项目）**: 在 Town Workspace (`~/gt`) 中管理的 Git 仓库
- **Beads（任务珠）**: 明确定义的原子工作单元，由 Mayor 创建
- **Convoys（车队）**: Beads 的分组，用于跟踪依赖和管理工作流

#### 3. 并行执行模型

**"水平扩展认知"（Horizontal Scaling for Cognition）**:
- Mayor 将 Beads "slings"（投掷）给可用的 Polecats
- 多个 Polecats 同时工作在不同任务上
- 每个 Polecat 在独立的 Git 分支中操作，防止相互干扰

**隔离机制**:
- 每个 agent 运行在专用的隔离会话中
- 使用 tmux 管理多个并行 agent 会话
- 每个 agent 有自己的工作目录和环境

#### 4. Git 作为持久化和同步机制

**状态管理**:
- 所有操作都持久化到 Git 仓库中
- Polecat 写的每一行代码、Mayor 做的每个决策都记录在 Git 历史中
- 使用 shared bare repo 进行内部管理
- 配合 worktrees 和 agent 配置

**崩溃恢复**:
- 如果系统失败，Gas Town 读取 Git 历史
- 理解正在进行的工作
- 从中断点恢复流程

**分支策略**:
- 每个 agent 一个独立的 feature 分支
- 完成后自动合并到主集成分支
- Mayor 控制合并顺序

#### 5. 协调和同步

**依赖管理**:
- Mayor 智能管理任务依赖
- 确保正确的执行顺序（例如：先完成后端再做集成测试）

**Agent 生命周期**:
- Agent 完成任务后被终止（"nuked"）
- 分支自动合并
- 资源释放供新任务使用

**进度监控**:
- Mayor 持续跟踪所有 Polecat 的执行进度
- 维护 beads database 跟踪任务状态

#### 6. 数据库和配置

- **Beads Database**: 跟踪所有任务的状态
- **Agent Configurations**: 每个 agent 的配置和能力定义
- **Town Workspace**: `~/gt` 目录作为协调中心

### 与 Anthropic Agent Teams 的对比

| 特征 | Anthropic Agent Teams | Gas Town | 匹配度 |
|------|---------------------|----------|--------|
| 多 agent 并行 | ✓ 16 个 Claude 实例 | ✓ 20-30 个 Polecats | ✓✓✓ |
| 共享代码库 | ✓ 单一 git repo | ✓ Rigs (git repos) | ✓✓✓ |
| 无人值守 | ✓ 完全自主 | ✓ 自主执行 | ✓✓✓ |
| Git 同步 | ✓ push/pull/merge | ✓ 分支隔离+自动合并 | ✓✓✓ |
| 容器隔离 | ✓ Docker 容器 | ✓ 隔离会话 + tmux | ✓✓ |
| 角色专业化 | ✓ 功能/质量/文档/性能 | ✓ Mayor/Polecats 层级 | ✓✓✓ |
| 任务锁机制 | ✓ 文件锁 (current_tasks/) | ✓ Beads 分配 + 分支隔离 | ✓✓ |
| 测试驱动 | ✓ 测试作为 verifier | ✓ 测试反馈循环 | ✓✓✓ |
| 编排策略 | ✗ 去中心化，无 orchestrator | ✓ Mayor 中央编排 | ✗ |
| 无限循环 | ✓ while true bash loop | ✓ 持续任务分配 | ✓✓ |

**总体相似度: 9/10**

### 核心差异

**唯一的关键差异是编排策略**:

- **Anthropic**: 去中心化自组织
  - 每个 agent 自主决定做什么（"pick the next most obvious problem"）
  - 通过文件锁协调（`current_tasks/parse_if_statement.txt`）
  - 没有 orchestration agent
  - 更像"自组织的团队"

- **Gas Town**: 层级化编排
  - Mayor 分析目标、分解任务、分配给 Polecats
  - Polecats 执行被分配的任务
  - 有明确的指挥链
  - 更像"有组织的工厂"

**为什么仍然是 9/10**:
- 两者都实现了多 agent 并行在共享代码库上工作
- 都使用 Git 作为同步和持久化机制
- 都支持角色专业化
- 都是长时间无人值守运行
- 都使用测试驱动进展
- 编排策略的差异是实现细节，核心思想一致

### 优势与局限

**优势**:
- 依赖管理更智能（Mayor 协调）
- 任务分解更结构化（Beads + Convoys）
- 崩溃恢复机制完善
- 进度跟踪更清晰

**局限**（Gas Town 自己承认的）:
- **审查挑战**: 数十个 agent 产生的代码量巨大，难以审查
- **成本**: 同时运行大量强大的 AI agent 会快速消耗 API tokens
- **风险**: Agent 对仓库有完全访问权限，需要谨慎监督和版本控制

### 来源

- [Welcome to Gas Town - Steve Yegge (Medium)](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)
- [Gas Town: What Kubernetes for AI Coding Agents Actually Looks Like](https://cloudnativenow.com/features/gas-town-what-kubernetes-for-ai-coding-agents-actually-looks-like/)
- [Building with Gas Town: Multi-Agent AI Development Guide](https://betterstack.com/community/guides/ai/gas-town-multi-agent/)
- [The Prius of GasTown](https://trilogyai.substack.com/p/the-prius-of-gastown)
- [How-To: GasTown Workflows & 60-Second OpenClaw](https://trilogyai.substack.com/p/how-to-gastown-workflows-and-60-second)

---

## 结论

**Gas Town 是目前唯一与 Anthropic Agent Teams 高度吻合（9/10）的外部实践。**

真正做到"多个自主 LLM agent 在共享代码库上并行工作、通过 git 同步、长时间无人值守"这一完整组合的，目前只有：
1. **Anthropic 自己的实现**（C 编译器项目）
2. **Steve Yegge 的 Gas Town**

两者的核心差异仅在于编排策略（去中心化 vs 层级化），但都实现了 agent teams 的本质：多个 AI agent 像一个软件开发团队一样协作，在共享代码库上并行工作，通过 git 同步状态，长时间自主运行，无需人类持续在场。

这种模式代表了 AI 辅助编程的一个新阶段：从"AI 副驾驶"到"AI 开发团队"。
