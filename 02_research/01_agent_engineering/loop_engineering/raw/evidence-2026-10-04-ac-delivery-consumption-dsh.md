# 证据档案 · AC 投递与实际消费 —— DSH 源码走读（T3a）

- **路别**：反馈路径问题 · 投递与实际消费（T3a · DSH 源码走读）
- **执行日期**：2026-10-04
- **版本锚**：`@deepseek-ai/dsh` **0.2.0-rc.2**（package.json，本机 npm 全局安装）。走读对象为安装产物 `node_modules/@deepseek-ai/dsh/` 及其嵌套依赖包 `node_modules/@deepseek-ai/dsh/node_modules/@deepseek-ai/dsh-*`（以下锚点均相对该嵌套目录，简写 `⟨B⟩/dsh-<pkg>/lib/index.js`）。源码为打包产物（bundle 后的 JS，原 ts 注释保留），行号以本机该版本文件为准。
- **方法**：只读走读，未运行被测代码；实际输入层以「代码调用点 + 本会话运行时上下文比对」为证，未做运行时抓包（列入待核）。

---

## 0. 版本锚与目录事实

- `⟨dsh⟩/package.json:4` → `"version": "0.2.0-rc.2"`；`bin: { dsh: "lib/bin.js" }`；CLI 包本身只是启动器（lib 仅 6 个 js），harness 主体全部在嵌套依赖 `@deepseek-ai/*` 中。
- 观测日期：2026-10-04。

## 1. 端到端路径：一条具体失败例（bash 命令退出码非零 → 下一轮模型输入）

| 跳 | 发生什么 | 锚点 | 证据类 |
|---|---|---|---|
| ① 产生 | `bash` 工具 `execute()` 调 `ctx.shell.execute()`（本地执行器 `dsh-bash-local`），进程 stdout/stderr 各由一个 `OutputCollector` 收集（字节尾窗） | `⟨B⟩/dsh-tool-bash/lib/index.js:683-686`（execute 调 shell + `.result()`）；`⟨B⟩/dsh-bash-local/lib/index.js:107-128`（spawnSpec：stdout=`collect(stdoutMaxBytes)`、stderr=`collect(maxOutputBytes)`） | 投递机制 |
| ② 截断（executor 层） | `OutputCollector.push()`：超 `maxBytes` 后从**内存尾窗头部丢整块/半块**，置 `dropped=true`；首次溢出时全量追加到 spill 文件（上限 `maxSpillBytes`，默认 64 MiB），spill 失败则降级为纯内存尾 | `⟨B⟩/dsh-subprocess-local/lib/output.js:115-134`（push 丢头逻辑）、`:141-163`（spillAll）、`:70-83`（注释：「Tail-keep rationale (pi/OpenCode): errors and final results cluster at the end of command output; the spill file covers the head.」） | 设计意图 + 投递机制 |
| ③ finalize | 进程结束后 `finalize()` 返回 `{ text: 尾窗全文, truncated: dropped, spillPath? }` | `⟨B⟩/dsh-subprocess-local/lib/output.js:229-236` | 投递机制 |
| ④ 格式化（tool 层） | `renderResult()`：stdout → `[stderr]\n` 段 → 状态标记行。**非零退出不是 error**：`exitCode !== 0` 追加 `[exit code: N]` 文本标记；超时 `[timed out after Xms]`、信号 `[killed by signal: N]`、停止 `[stopped: …]`；被截断的流尾部追加 `[output truncated; full output: <spillPath>]`；沙箱拒绝追加 `[sandbox: file access denied under <mode> mode]`（+ 同轮升级提示） | `⟨B⟩/dsh-tool-bash/lib/index.js:150-171`（renderResult；:167 退出码标记）、`:135-138`（streamText 截断脚注）、`:160-163`（沙箱标记）；注释 :140-143「Non-zero exits are reported, not errored — the model decides how to react; only infrastructure failures … surface as isError results」 | 设计意图 + 投递机制 |
| ⑤ 注入会话 | 工具输出经 `output.render` 变成 text block；`executeToolCalls` 把 call/result 成对 append 进持久会话：`tool/call` 事件 + `tool/result` 事件（`sourceEventSeqs` 回链 call），result message 由 `createToolResultMessage` 构造（`role:"tool"`，携带 `toolCallId`、`isError`） | `⟨B⟩/dsh-tool-bash/lib/index.js:636-639`（render）；`⟨B⟩/dsh-agent-loop/lib/index.js:681-707`（appendToolCall/appendToolResult）；`⟨B⟩/dsh-llm/lib/index.js:101-112`（createToolResultMessage） | 投递机制 |
| ⑥ 投递机制（异常路径，非本例但同管线） | 工具 `execute()` **抛异常** → 管线 catch → `toolErrorResult()`：文本 `Error: <message>`，`isError:true`，error 携带 code | `⟨B⟩/dsh-tools/lib/index.js:3616-3630`（toolErrorResult） | 投递机制 |
| ⑦ 派生下一轮输入 | 每步 `buildRequest` 调 `session.deriveMessages()`：沿 surface 节点序折叠出完整 message 历史（tool/result 的 message 是 surface 的一员），冻结后作为 `messages` 直接放进请求 | `⟨B⟩/dsh-agent-loop/lib/index.js:1262-1276`（`messages: boundaryMessages`）；`⟨B⟩/dsh-session/lib/index.js:1536-1569`（deriveMessages 注释「The surface is the single source of derived history」） | 投递机制 |
| ⑧ 上线格式（adapter 层） | DeepSeek Messages 适配器把 `role:"tool"` 消息映射为 user 轮里的 `{ type:"tool_result", tool_use_id, content, is_error? }`；并强制校验 call/result 一一对应、无悬挂 | `⟨B⟩/dsh-llm-deepseek/lib/index.js:1666-1673`（映射+`is_error`）、`:1683-1693`（配对校验） | 投递机制 / 实际输入 |
| ⑨ 行为证据（本会话） | 本任务会话自身（DSH 驱动）注入的系统提示含逐字文本「Check the [exit code: N] marker on every bash result; investigate failures before moving on.」——与源码 `bashDescription`/systemPrompt 段注册一致；且本会话 bash 工具 description 与 `bashDescription()` 逐字一致，工具结果尾部带 `[exit code: N]` 约定 | `⟨B⟩/dsh-tool-bash/lib/index.js:377-381`（systemPrompt.section 注册）、`:242-244`（bashDescription）；对照本会话运行时上下文 | 实际输入（运行时产物比对，非模型自述） |

### 截断/摘要机制结论（投递层，非 compaction 层）

- **粒度**：字节（byte），不是字符；UTF-8 边界保护（`dsh-subprocess-local` 尾窗按块滑动不保证码点边界，但 `dsh-output-retention` 的 TextRetainer 版本在 cut 处 `trimTrailingPartialUtf8`/`trimLeadingContinuationUtf8`）。
- **保留什么**：**尾部**（tail-keep）。bash stdout 与 stderr 各自独立保留一个内存尾窗，默认 **64,000 字节/流**（`dsh-bash-local/lib/index.js:73` `maxOutputBytes: z.number().default(64e3)`；stdout 可被 request 覆盖，:91）。丢的是头部。
- **丢了什么去哪**：全量流尽最大努力写入 spill 文件（`/tmp` 下 0700 私有目录，默认上限 `maxSpillBytes = 64 MiB`，`dsh-bash-local/lib/index.js:31`），模型可见文本尾部一行 `[output truncated; full output: <path>]` 指回该文件（`dsh-tool-bash/lib/index.js:135-138`）——**摘要在 tool 渲染层发生**（renderResult 的 marker），**截断在 executor 收集层发生**（OutputCollector）。tool 层的 `truncated` 语义被严格约束为「预算省略」，权限失败等不计入（`dsh-output-retention/lib/index.js:1-33` 模块注释）。
- 另有独立第二层：**会话面（surface）级 tool-result 修剪** `dsh-compaction-tool-result-pruner`——仅在 compaction 触发时把 >8192 字符的结果替换为「头 4096 + middle-pruned 标记 + 尾 1024」，**会话日志中的原件不变**，仅改模型可见投影（`dsh-compaction-tool-result-pruner/README.md`「What gets trimmed / When trimming runs」节）。

## 2. 失败结果的控制分支（harness 侧独立分支？）

- **工具失败（含非零退出）本身没有 harness 侧重试/熔断/审批分支**：非零退出只是文本标记 `[exit code: N]`（设计意图：dsh-tool-bash/lib/index.js:140-143「the model decides how to react」）。唯一的「控制性」注入是 system prompt 一句话（:377-381「Check the [exit code: N] marker …」），属提示层不属控制流。
- ** isError 的三类来源**（均有锚）：① 工具抛异常 → `toolErrorResult`（dsh-tools:3616-3630）；② 取消 → `toolAbortedResult`/`toolAbortedBeforeDispatchResult`（dsh-tools:3676-3712）与 agent-loop 的 `appendSkippedToolCall`（dsh-agent-loop:662-679）；③ 步骤失败时 `ToolCallRecovery` 补录 pending 结果（见 §4）。
- **存在独立控制分支的是 LLM 请求失败**，不是工具失败：流式 finish 为 error/aborted 时走 `agent/request-error` waterfall，返回 `{kind:"retry"}` 才重试，否则抛 `LlmError`（`⟨B⟩/dsh-agent-loop/lib/index.js:1118-1134`）。重试策略来自 adapter 的 `retryPolicy`。
- 并行/排他调度有 `maxParallelToolCalls`（默认 10，dsh-agent-loop:1284-1285）与 scheduler 失败 drain 语义（:479-495 注释），属于调度控制不是失败熔断。

## 3. 审批拒绝回传与中断挂起

- **拒绝 → 模型**：沙箱升级审批链是 `bash execute()` 内 await `approveEscalation`（dsh-tool-bash:361-376, 644）→ `ApprovalService.request()`（`⟨B⟩/dsh-user-approval/lib/index.js:128-144`：先 append `approval/asked`，决策后 append `approval/decided`，配对审计强制 turn-enclosed，:130）→ outcome 非授权时 **throw**（`⟨B⟩/dsh-sandbox/lib/index.js:116-122`，rejected 分支文案：「the user rejected escalating … stop and explain instead of working around it」）。异常再走 §1⑥ 的 `toolErrorResult` → `isError` tool/result → 下一轮模型输入。即：**拒绝回传 = 抛错 → 标准错误结果管线**，无独立旁路。
- **挂起即阻塞**：审批是 await（execute 不返回，step 停在该 tool call 上）；请求 signal abort → outcome `cancelled`（dsh-user-approval:178-188），工具以 `Error: tool call aborted` 收尾。`policy:"never"` 会话直接判 `rejected` 且其文案注入 system prompt context（dsh-user-approval:39, 79-89, 175）。
- **审计落在会话日志**（approval/asked + approval/decided），恢复时随日志折叠，不需要运行态重建（dsh-user-approval:43-56 注释解释了为何必须 turn-enclosed）。

## 4. 会话恢复（resume）与旧状态

- **旧消息原样重放**：resume 只是重新打开持久日志（`resumeWith`：`persistence.open(id,"write")` + 全量 cold read，`⟨B⟩/dsh-agent-loop/lib/index.js:1927-1975`），session surface 从日志重建，下一步请求的 `messages` 仍由 `deriveMessages()` 从全量 surface 派生——**上一轮工具结果不摘要、不丢弃，逐字重发**（除非被 compaction 的 `replace` surfaceOp 遮蔽或被 pruner 修剪投影；`dsh-session/lib/index.js:1536-1544` 注释明确「a compaction `replace` deletes the shadowed nodes from the derivation」）。
- **中断的尾轮**：resume 时检测日志尾部未闭合的 turn/step，合成 closers 补齐（`interruptedTurnClosers` → `openTurnClosers`，`⟨B⟩/dsh-session/lib/index.js:747-795`；调用点 dsh-agent-loop:1950-1951）。其中**未答的工具调用**由 `ToolCallRecovery.results()` 生成**合成 isError tool/result**（`⟨B⟩/dsh-session/lib/index.js:801-893`），文案按「已启动/未启动」二分（CLOSER_TEXT，:727-736）：已启动者告知「结果未知，仅在只读/幂等时可重试，勿盲试」；未启动者「可重试」。即**恢复后旧状态不是重放执行，而是把未知结果定影为带重试指导的错误结果**。
- **inbox（待投递输入）也是持久事件**：`agent/inbox/spliced` 事件可从日志重放重建 pending 输入（dsh-agent-loop:26-48），恢复后继续走。

## 5. 证据三分类小结

- **设计意图**（注释/命名）：dsh-output-retention 模块头注（1-33）；OutputCollector tail-keep rationale（output.js:70-83）；renderResult「reported, not errored」（dsh-tool-bash:140-143）；deriveMessages「surface is the single source」（dsh-session:1536-1544）；CLOSER_TEXT 文案本身（dsh-session:727-736）。
- **投递机制**（代码路径）：§1 表①-⑦ 全链。
- **实际输入**（有调用点/运行时证明）：⑦-⑧ 是请求装配与上线的代码调用点；⑨ 为本会话运行时上下文与源码逐字比对的产物级证据。**未做独立运行时抓包**（无请求体日志取证），实际输入证据强度定为「调用点 + 本会话产物比对」，模型自述未计入。

## 6. 未答问题与待核清单

1. **运行时抓包**：未截获真实 API 请求体验证 `tool_result.is_error` 的实际出现频率与 `[exit code: N]` 在历史中的留存（可用 `dsh dump`/session log 导出复核）。
2. `dsh-compaction-basic` 的摘要请求本身如何措辞/保留哪些段（本轮只核到 pruner 层，backend 摘要 prompt 未走读）。
3. `dsh-repeat-tool-reminder`（重复工具调用提醒）未走读——疑似「同参数重复调用」的提示层控制分支，与 T3a 相邻。
4. `job_output` 后台输出读取路径（jobs ring/spill）只核到 bash 工具侧的 promote/read 入口，jobs 包内部未展开。
5. ACP/外部端（IDE）通道的审批 UI 回传细节（本机 GUI 路径之外）未核。
6. 非 DeepSeek adapter（pi-ai 等）对 tool role 的映射差异未核。

## 7. 与 plan 完成条件的对照

- 「一条端到端路径」：达成（§1 表，bash 非零退出失败例，9 跳全通）。
- 「分别标设计、投递、实际输入/控制分支、行为证据」：达成——§1 表每跳带证据类；设计意图清单见 §5；控制分支结论见 §2；行为证据为运行时上下文比对（⑨），强度已在 §5 声明。
