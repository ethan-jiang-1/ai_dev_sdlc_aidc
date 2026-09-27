# 外置工作行 K

> 写于 2026-09-27，最初在执行之前。随后的取文发生在 Cursor，没有 DSH goal。这行因此不再是干净的对照样本。不要用本文件填催问、续轮、返工或人工分钟。`authorized` 仍空。

| 字段 | 值 |
|---|---|
| id | `row-k-unwinding` |
| source | 人指定。对应 [`research-plan.md`](research-plan.md) P0 第 2 项。不是从文件里扫到的未完成项，也不是定时器 |
| 工作 | 只处理 OpenAI《Unwinding Codex's Agent Loop》（Michael Bolin，2026-01-23）。计划内已记录的 URL：`https://openai.com/index/unwinding-codex-agent-loop/`；B 路还记过 slug `unrolling-the-codex-agent-loop`。取得正文，就新开一份 evidence，只摘与循环节拍和终止态有关的原句。取不到，就在同一份档案写下 URL、状态码、观测时间，作为负结论。不改 `digested/`，不改 `03_practice/`，不加人名 |
| authorized | （空） |
| priority | P0。未变更 |
| blocked_reason | （空） |
| stop_reason | 2026-09-27 正文写入 `evidence-2026-09-27-k-unrolling-codex-agent-loop.md`。不是测试门，也不是 goal 完成 |
| accepted_by | （空） |
| goal | （空）。工作发生在 Cursor 会话，没有 DSH goal 引用本行 |

计数先空着：催问、续轮、返工、人工分钟。后两项还没有计数口径。

## 为什么 goal 没开

2026-09-27 在本机查过，没有装上 `goal-round-driver`：

- `dsh goal` 不被当成子命令。launcher 把 `goal` 读成 profile 名，并报 profile 不存在。
- `dsh --profile headless` 能回答一次任务后退出。该 profile 的 bundle 只有 `@deepseek-ai/dsh-base` 和 `@deepseek-ai/dsh-headless`。
- `@deepseek-ai/dsh-command-goal` 的 README 写明：`/goal` 跑在交互界面的命令层；没有命令适配器的 headless 不挂这套命令。

取文后来在本 Cursor 会话里做了，没有先开 goal。正题是 Unrolling。直接 HTTP 仍是 403。详情在 `evidence-2026-09-27-k-unrolling-codex-agent-loop.md`。不要把这次当作外置行对照的结果。
