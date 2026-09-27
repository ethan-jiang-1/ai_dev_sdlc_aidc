---
type: evidence_archive
collected_by: 主代理（K：检索工具摘录，待一手复核）
collected_at: 2026-09-27
serves: research-plan P0.2 · digested/03 停止条件的裁判权
status: 候选页面文本已由检索工具取得；直接 HTTP 仍是 403，待独立一手复核
quality_bar: 候选 P-mechanism（检索工具摘录，尚未完全主验）。不是 P-outcome。不升 KOL。OpenAI 仍是已有的一票
---

# 回源 K：《Unrolling the Codex agent loop》

> 观测日期：2026-09-27。发布日期：页面标注 January 23, 2026。作者：Michael Bolin, Member of the Technical Staff。
> **来源状态注记**：本档案保留检索工具取得的页面文本，供定位原文和比较终止语义；在直接页面持续 403、没有可审计的一手镜像或源码交叉验证前，下面的引句不升级为完全主验的 P-mechanism。
> 正题是 **Unrolling**，不是库内沿用的 Unwinding。URL：`https://openai.com/index/unrolling-the-codex-agent-loop/`。
> 本环境对 `unwinding-codex-agent-loop`、`unrolling-the-codex-agent-loop`、`/blog/` 与 `ga-IE` locale 的直接请求都是 HTTP 403。下面的原句来自同日检索工具抓到的该 URL 页面全文（文末有 Author 与 Acknowledgments）。同一段终止态英文也出现在检索摘录的 `ga-IE` 与 `mt-MT` locale 页面里。`engineering.fyi` 返回 200，但是第三方综述，不引作原句。
> 执行不在 DSH goal 里。外置行 K 没有被 goal 引用。这不是对照臂。

## 循环怎么转

检索摘录把 agent loop 描述为 Codex CLI 里编排用户、模型和工具的核心逻辑，并称 harness 就是这个 agent；该描述待独立一手复核。

> the agent loop, which is the core logic in Codex CLI that is responsible for orchestrating the interaction between the user, the model, and the tools the model invokes to perform meaningful software work.

一次推理之后只有两条出路：直接回复，或要一次工具调用。工具结果追加进 prompt，再问模型。

> As the result of the inference step, the model either (1) produces a final response to the user’s original input, or (2) requests a tool call that the agent is expected to perform (e.g., “run `ls` and report the output”). In the case of (2), the agent executes the tool call and appends its output to the original prompt. This output is used to generate a new input that’s used to re-query the model.

停的条件写在模型不再发出工具调用的时候：

> This process repeats until the model stops emitting tool calls and instead produces a message for the user (referred to as an assistant message in OpenAI models). In many cases, this message directly answers the user’s original request, but it may also be a follow-up question for the user.

终止态原句：

> Nevertheless, each turn always ends with an assistant message—such as “I added the `architecture.md` you asked for”—which signals a termination state in the agent loop. From the agent’s perspective, its work is complete and control returns to the user.

一个 turn 里可以有许多次推理和工具调用。用户下一条消息才开始下一个 turn，历史整段进 prompt。

> The journey from user input to agent response shown in the diagram is referred to as one turn of a conversation (a thread in Codex). Though this conversation turn can include many iterations between the model inference and tool calls.

后文又把 assistant message 说成这一 turn 的结束：

> The prompt may continue to grow until we finally receive an assistant message, indicating the end of the turn.

## 旁边两件容易误当成停止条件的事

上下文满了会 compact，不是质量验收。早期要人敲 `/compact`；现在超过 `auto_compact_limit` 就自动调用 `/responses/compact`。文中没有给出这个阈值的数字。

Codex 不用 `previous_response_id`。每次请求带上完整历史，为的是无状态和 Zero Data Retention。这是请求形态，不是停止条件。

文末说工具实现和 sandbox 留给后面的文章。这篇没有写 feature 级的授权史、priority、业务阻塞或跨 feature 验收。

## 这能说明什么

- 检索摘录**声称**「每轮以 assistant message 进入终止态、控制交还用户」；在独立复核前，这只是候选机制线索，不是已确认的 OpenAI 原文主张。
- 若摘录可被独立复核，则它支持：终止来自模型停止发出工具调用，消息可以是追问，不一定是任务做成；但当前只能作为待复核线索。
- compact 是资源兜底，和 assistant message 不是同一种停。

## 这不能说明什么

- 当前摘录中没有把循环编号成「四拍」；「四拍循环」仍只能作为库内转述标签，不能归给 OpenAI 原文。
- 不证明测试通过、人验收，或减少返工。
- 不给 OpenAI 增加第二票。auto-review 与 harness engineering 仍是同一机构。
- 不把 Bolin 升进 §A。文章在 2026-06 命名之前，讲的是 Codex 的 agent loop，不是 “loop engineering” 这个词。
