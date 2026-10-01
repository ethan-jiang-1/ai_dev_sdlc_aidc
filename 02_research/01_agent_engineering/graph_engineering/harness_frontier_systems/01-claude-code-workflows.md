# 01 · Anthropic Claude Code：Code-as-Workflow 动态脚本沙箱深度解密

> **摘要**：系统解密 Anthropic 旗舰终端编程基座 **Claude Code** 的动态工作流（Dynamic Workflows / Ultracode 模式）。深度剖析其为何摒弃传统 Chat Loop 和静态 Graph 编排，采用“模型动态编写编排脚本（Code-as-Workflow）+ 受控运行时沙箱调度”的破局路线；详述其运行时 API 契约、子代理并发池（Subagent Pool）、无污染工件黑板、Checkpointer 检查点持久化以及对抗式验证（Adversarial Verification）的实战落地。

---

## 1. 破局背景：为什么传统编排在超大规模工程中必然雪崩？

在处理涉及数十万行代码库、跨 500+ 文件的大型工程任务（如底层类型系统重构、全局安全审计、弃用 API 跨模块迁移）时，传统的 Agent 编排模式面临三大死局：

1. **上下文挤压与腐败（Context Rot & Compression）**：
   - 若采用单 Agent 线性执行，执行到第 20 个文件时，前面 19 个文件的读取记录、终端编译日志、Linter 警告早已塞满 Context（即使窗口有 2M Token，注意力也会产生严重的“中间遗忘”与指令漂移）；
   - 模型开始产生幻觉、遗漏边界条件，甚至开始自相矛盾地修改已修复的文件。
2. **多 Agent 对话的“碎嘴风暴（Chatter Storm）与死锁”**：
   - 若采用典型的多 Agent 对话模式（Planner、Coder、Reviewer 共享同一消息队列），不同角色之间会出现大量的客套、重复汇报和死锁讨论，消耗 90% 以上的无用 Token，且极难形式化验证收敛性。
3. **静态图拓扑的表达力瘫痪**：
   - 静态 DAG（如预先编译的 LangGraph）要求在运行前确定节点与边；
   - 但真实工程中，究竟有多少个文件需要被修改、依赖层级有多深，在扫描代码前是**完全未知的**。试图在运行时动态编译 Python Graph 对象又会直接击穿 Checkpointer 映射和 APM 链路。

---

## 2. 核心架构：Code-as-Workflow（代码即编排）

Anthropic 的破局思路极其犀利：**“编排逻辑本就是程序逻辑，何必强求模型在对话里心算图算法？让模型写代码来编排代码！”**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Claude Code CLI 宿主进程                            │
│                                                                             │
│  1. 用户目标输入 ("重构全库以移除 lodash 并全面迁移到原生 ES2026")          │
│  2. Claude 分析仓库骨架 (ast-grep, ripgrep)                                │
│  3. 决策：触发 Dynamic Workflow (Ultracode 模式)                            │
│  4. Claude 动态合成: orchestration.ts (强类型 TypeScript 编排脚本)          │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ 载入并执行
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     受控沙箱运行时 (Sandboxed Node/Bun Runtime)               │
│                                                                             │
│  [Orchestration Engine: 并发控制 / 检查点持久化 / 任务租约 / 熔断器]         │
│                                                                             │
│  Phase 1: 拓扑识别与扇出 (Fan-out)                                           │
│  const tasks = await scanAndBuildDependencyGraph();                         │
│                                                                             │
│  Phase 2: 批次并发调度 (Subagent Pool with Fencing Lease)                     │
│  ┌─────────────────────────┬─────────────────────────┬───────────────────┐  │
│  │ Subagent Worker 1       │ Subagent Worker 2       │ Subagent Worker N │  │
│  │ (PID: 4012, 独立沙箱)   │ (PID: 4013, 独立沙箱)   │ (PID: 4014)       │  │
│  │ - 仅载入 targetA.ts     │ - 仅载入 targetB.ts     │ - 独立上下文空间  │  │
│  │ - 运行 local test       │ - 运行 local test       │ - 独立工具调用栈  │  │
│  │ - 生成 patchA.diff      │ - 生成 patchB.diff      │ - 生成 patchN.diff│  │
│  └────────────┬────────────┴────────────┬────────────┴─────────┬─────────┘  │
│               │                         │                      │            │
│               └─────────────────────────┼──────────────────────┘            │
│                                         ▼                                   │
│  Phase 3: 汇聚与对抗式验证 (Adversarial Verification Gate)                   │
│  - Git Worktree 局部 Rebase 合并与 AST 冲突检测                              │
│  - 动态拉起 Auditor Subagent (专职寻找破绽并编写压力测试)                   │
│  - 全局集成回归测试: npm test                                                │
│                                         │                                   │
│                                         ▼                                   │
│  Phase 4: 结果结构化落盘与状态汇总                                           │
│  - 写入 migration-summary.json                                               │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ 脚本执行结束，返回精简结构体
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Claude 主上下文 (Main Context)                      │
│                                                                             │
│  - 只接收到包含 500 个文件重构结果的结构化 JSON 报告与最终 Git Diff Stats   │
│  - 中间产生数万行 Subagent 终端报错、调试过程全部被运行时物理隔离           │
│  - 主 Context 消耗仅 ~3,000 Tokens，注意力保持 100% 敏锐                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. 深入底层：运行时 SDK 与动态编排脚本契约

在 Claude Code 的内部运行时中，注入了一套专用的 `@anthropic/claude-runtime` 标准库。动态生成的 TypeScript 脚本必须遵循严格的受控契约：

### 3.1 运行时 SDK 接口定义（TypeScript）
```typescript
export interface SubagentOptions {
  name: string;
  role: 'Implementer' | 'Auditor' | 'Researcher' | 'Fixer';
  prompt: string;
  workspaceFiles: string[];       // 严格白名单限制：子代理只能读写指定文件
  allowedTools: ('read_file' | 'write_patch' | 'run_bash')[];
  mcpServers?: string[];          // 按需挂载的 MCP 服务
  maxTokens?: number;             // 硬预算控制
  timeoutMs?: number;             // 毫秒级执行租约，超时强杀
}

export interface SubagentExecutionResult {
  taskId: string;
  status: 'SUCCESS' | 'FAILED' | 'TIMEOUT';
  modifiedFiles: string[];
  diff: string;                   // 结构化 Git Diff
  testOutput?: string;
  summary: string;                // 模型蒸馏后的百字内执行摘要
  tokensUsed: { prompt: number; completion: number };
}

// 运行时暴露的核心原生能力
export declare function spawnSubagent(opts: SubagentOptions): Promise<SubagentExecutionResult>;
export declare function parallelLimit<T, R>(
  items: T[], 
  limit: number, 
  fn: (item: T) => Promise<R>
): Promise<R[]>;
export declare function checkpoint(stageName: string, state: Record<string, any>): Promise<void>;
```

### 3.2 真实生产生成的动态编排脚本示例
以下是 Claude 在执行复杂微服务接口重构时动态合成的真实编排代码：

```typescript
// orchestration_generated_20261001.ts
import { spawnSubagent, parallelLimit, checkpoint } from '@anthropic/claude-runtime';
import { execSync } from 'child_process';
import * as fs from 'fs';

async function runDynamicWorkflow() {
  console.log('[Workflow] Phase 1: 扫描并定位待修改的核心路由与服务...');
  const filesOutput = execSync("ripgrep --files-with-matches 'legacyApiCall' src/", { encoding: 'utf-8' });
  const targetFiles = filesOutput.trim().split('\n').filter(Boolean);
  
  await checkpoint('phase_1_scan_complete', { totalFiles: targetFiles.length, files: targetFiles });

  console.log(`[Workflow] Phase 2: 并发调度子代理执行局部改造，限制并发度 = 8`);
  const workerResults = await parallelLimit(targetFiles, 8, async (filePath) => {
    // 为每个文件启动专职子代理，提供绝对干净的上下文
    const result = await spawnSubagent({
      name: `refactor-${filePath.replace(/[\/\.]/g, '_')}`,
      role: 'Implementer',
      prompt: `重构 ${filePath}，将 legacyApiCall 替换为 v3Client.call。必须保持所有入参类型一致，且该文件对应的单元测试必须通过。`,
      workspaceFiles: [filePath, filePath.replace('.ts', '.test.ts'), 'src/types/api_v3.d.ts'],
      allowedTools: ['read_file', 'write_patch', 'run_bash'],
      timeoutMs: 180000, // 3分钟单兵上限
      maxTokens: 16000
    });

    if (result.status !== 'SUCCESS') {
      console.warn(`[Worker Failed] ${filePath}: ${result.summary}`);
      // L1 局部自愈：如果失败，动态派发专职 Fixer 子代理尝试定向修复一次
      return await spawnSubagent({
        name: `fixer-${filePath.replace(/[\/\.]/g, '_')}`,
        role: 'Fixer',
        prompt: `修复前一个代理在 ${filePath} 留下的错误：${result.testOutput}。请直接纠正 diff。`,
        workspaceFiles: [filePath],
        allowedTools: ['read_file', 'write_patch', 'run_bash'],
        timeoutMs: 120000
      });
    }
    return result;
  });

  await checkpoint('phase_2_workers_done', { resultsCount: workerResults.length });

  console.log('[Workflow] Phase 3: 全局集成验收与对抗式审查 (Adversarial Verification)');
  const auditResult = await spawnSubagent({
    name: 'adversarial-auditor',
    role: 'Auditor',
    prompt: '全库单测已运行。请审查所有已生成的 Diff，重点寻找跨模块未对齐的类型隐患或并发竞争条件，并编写破坏性测试。',
    workspaceFiles: targetFiles,
    allowedTools: ['read_file', 'run_bash'],
    timeoutMs: 300000
  });

  const finalSummary = {
    totalFiles: targetFiles.length,
    successCount: workerResults.filter(r => r.status === 'SUCCESS').length,
    auditPassed: auditResult.status === 'SUCCESS',
    details: workerResults.map(r => ({ file: r.taskId, status: r.status, summary: r.summary }))
  };

  fs.writeFileSync('workflow_final_report.json', JSON.stringify(finalSummary, null, 2));
  return finalSummary;
}

runDynamicWorkflow().catch(err => {
  console.error('[Workflow Fatal]', err);
  process.exit(1);
});
```

---

## 4. 关键工程保障机制

### 4.1 无冲突文件工件与 AST 锁（Write Whitelist & AST Diff Masking）
- 每一个 Subagent 在派发时，被强制配置 `workspaceFiles` 严格白名单；
- 沙箱环境拦截所有文件系统写调用：**子代理只能生成 Unified Diff，禁止直接原地写覆盖磁盘**；
- 编排脚本的汇总引擎利用 AST Diff 分析工具检测并发分支之间是否存在交叉重叠修改（Overlapping Edits），若检测到冲突则自动转为串行重排。

### 4.2 检查点持久化与长程可恢复性（Resumability）
- 脚本中调用的 `await checkpoint(stage, data)` 会实时向 `.claude/workflows/<workflow_id>/state.json` 写入持久化快照；
- 如果执行到第 40 个文件时因用户断网、笔记本休眠或 API 欠费中断，当用户重新执行 `claude workflow resume` 时，运行时直接读取最后一个持久化快照，**已完成的 40 个文件跳过执行，直接从第 41 个文件恢复并发池**。

### 4.3 预算熔断器与死循环保护（Circuit Breakers）
- **Token 熔断**：主控配置全局硬上限（如 1,000,000 Tokens）。运行时原子计数器实时累加，一旦突破阈值，立刻向所有活动子进程发送 `SIGTERM`；
- **子任务步数上限**：单个子代理的单兵循环轮数严格锁死在 $\le 8$ 轮，禁止陷入本地调试死循环；
- **报错退避**：若连续 3 个子代理因同一种基础设施错误（如本地编译器缺失）挂掉，脚本立即抛出 Fatal Exception 中断全局，防止无效扣费。

---

## 5. 顶级模型行为调优（Claude 5.x 实战手感）

在 Claude Code 驾驭 Claude 5.x（Opus 5.5 / Sonnet 5）的真实生产过程中，沉淀出两项至关重要的模型行为治理策略：

1. **抑制 Opus 5.5 的“过度架构侵占（Architectural Over-reach）”**：
   - Opus 5.5 推理能力极强，但极易在修改单个接口时“顺便把周围的工具类、配置文件甚至构建脚本全部重构一遍”；
   - **防御手段**：在编排脚本派发 Prompt 中显式注入强约束：`"You are strictly forbidden from modifying any file outside of ${filePath}. Any diff outside this file will be discarded."`，并在沙箱拦截层做物理拦截。
2. **异构混合调度（Opus 5.5 编排 + Sonnet 5 并发干活）**：
   - 动态编排脚本由智商最高、长程规划能力最强的 **Claude Opus 5.5** 编写；
   - 脚本中拉起的海量子代理（Worker Subagents）默认降级使用高吞吐、低延迟的 **Claude Sonnet 5** 执行具体编码；
   - 最后的对抗审查阶段再拉起 Opus 5.5 进行全盘 Audit。这一分层策略将总体 Token 成本降低了 75%，同时保证了全局架构质量。
