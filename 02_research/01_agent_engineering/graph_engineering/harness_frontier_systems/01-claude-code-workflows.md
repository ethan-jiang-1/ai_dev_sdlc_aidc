# 01 · Anthropic Claude Code：Code-as-Workflow 动态脚本沙箱

> **摘要**：深度剖析 Anthropic 在 Claude Code 中推出的 **Dynamic Workflows（动态工作流 / Ultracode 模式）**。解密其如何抛弃传统 Chat Loop 和静态 Graph 框架，采用“模型动态编写编排脚本（Code-as-Workflow）+ 沙箱并发调度”的破局路线，实现百量级子代理的无污染并发与可断点执行。

---

## 1. 破局背景：为什么传统 Agent 架构在超大工程中失效？

在面对数千个文件的大型代码库重构、全库安全合规审计或跨模块 API 迁移时，传统的 Agent 编排面临三座无法逾越的大山：
1. **上下文严重挤压（Context Pollution）**：如果让主控 Agent 串行处理每个文件，前面文件的工具调用输出、编译错误和修复过程会迅速塞满 Context Window，导致模型注意力急剧衰减并产生幻觉；
2. **多 Agent 对话的“碎嘴风暴（Chatter Storm）”**：如果在同一个线程里让 Planner、Coder、Reviewer 自由讨论，Token 消耗呈指数级膨胀，90% 的 Token 被用于无意义的角色客套与重复确认；
3. **静态图的扩展僵化**：用户提交的需求每次涉及的文件数量完全不确定，静态预编译的 DAG 无法提前预知应该开辟多少个分支。

---

## 2. 核心架构：Code-as-Workflow（代码即编排）

Claude Code 的 Dynamic Workflows 采用了一种极具颠覆性的工程设计：**将规划与编排逻辑从“模型对话层”剥离，下放到“可执行代码层”**。

```
[User Objective] 
      │
      ▼
[Claude 主控模型] ──(分析目标与代码库结构)──> [动态生成 Orchestration 脚本 (JS/TS)]
                                                         │
                                                         ▼
                                             [沙箱 Runtime 执行引擎]
                                                         │
                        ┌────────────────────────────────┼────────────────────────────────┐
                        │ 并发 Phase 1                   │ 并发 Phase 2                   │
                        ▼                                ▼                                ▼
              [Subagent 1: 扫描模块 A]         [Subagent 2: 扫描模块 B]         [Subagent N: 扫描模块 N]
              (独立 Context / 独立工具)        (独立 Context / 独立工具)        (独立 Context / 独立工具)
                        │                                │                                │
                        └────────────────────────────────┼────────────────────────────────┘
                                                         │ (结果写入磁盘工件 / 聚合数据)
                                                         ▼
                                             [Orchestration 脚本汇总结果]
                                                         │
                                                         ▼
                                           [返回 Claude 主上下文: 精简报告]
```

### 2.1 编排脚本的工作形态
当触发 Dynamic Workflow（例如开启 `ultracode` 模式或面对大工程目标）时，Claude **不会直接逐个改代码**，而是编写一段类似如下的编排脚本并在沙箱中启动：

```javascript
// 由 Claude 在运行时动态生成的 orchestration.ts
import { spawnSubagent, parallelLimit } from '@anthropic/claude-runtime';

async function executeMigration() {
  const targetFiles = await findTargetFiles('src/**/*.ts');
  console.log(`Found ${targetFiles.length} files to migrate.`);

  // 动态分阶段执行（Phases）与并发度控制
  const results = await parallelLimit(targetFiles, 10, async (file) => {
    // 动态生成子代理，分配独立沙箱和精简上下文
    const subagent = await spawnSubagent({
      role: 'RefactoringSpecialist',
      task: `Migrate deprecated API in ${file} to v2 spec. Run local linter and ensure tests pass.`,
      workspaceFiles: [file, 'types/v2-spec.d.ts'],
      timeoutMs: 120000
    });
    
    return await subagent.execute();
  });

  // 跨结果一致性校验
  await runGlobalIntegrationTests();
  return generateAuditSummary(results);
}
```

### 2.2 为什么 Code-as-Workflow 极其强大？
1. **极致的上下文纯净度**：
   数百个子代理各自在完全独立的临时会话中运行，它们尝试了多少次、报错了多少次、输出了多少万 Token 的终端日志，**主 Claude 上下文完全看不到**。主会话只接收脚本最终返回的结构化 JSON 报告；
2. **确定性控制与并发控制**：
   复杂的调度逻辑（并发度限制、批次依赖、错误跳过、全局聚合）全部由编程语言（JavaScript/TypeScript）的原生控制流处理，不需要通过反复 Prompt 让大模型去心算调度，执行零随机性；
3. **断点持久化与可恢复性（Resumability）**：
   Runtime 对脚本执行的每一步状态进行持久化检查点写入。如果因网络抖动中断，用户可以无缝使用 `resume` 续跑，无需从头重来；
4. **内置熔断器（Circuit Breakers）**：
   系统强制配置最大步骤数（Step Limit）与 Token 预算硬上限，防止因脚本内部逻辑死循环引发天价账单。

---

## 3. 典型落地场景

- **大规模代码库 API 升级**：针对 500+ 个存量文件的废弃 API 进行系统化改写并分别就地执行单测；
- **全系统安全漏洞扫描与修补**：对整个仓库的输入输出路径进行并发污点分析，各模块结果在汇总阶段进行依赖交叉比对；
- **对抗式验证（Adversarial Verification）**：编排脚本动态拉起一组“实现 Agent”和一组“审查 Agent”，审查 Agent 专门编写针对性的测试用例尝试击穿实现 Agent 的代码，直至双方达成共识。

---

## 4. 架构启示

Claude Code 的实践证明：**对于超复杂长程任务，最优雅的“动态图”不是在 Python 内存里维护复杂的动态 Graph 对象，而是直接让模型回归其最擅长的能力——编写一段严谨的编排代码，让底层系统去无脑执行。**
