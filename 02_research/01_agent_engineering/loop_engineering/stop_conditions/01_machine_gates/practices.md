# ① 机器可核判据逐轮闸门 — 工程实践做法库（自说明版）

> **本文件自说明**：每条做法就地携带最有意义的核心片段（原句/代码/参数，保留原文语言），读完本文件即得工程要领；`源` 行只作全量逐字与引用链的出处（evidence 档案）。
> **判定句**（收敛判定权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：测试/类型/linter/静态分析/构建退出码做逐轮"接受/拒绝"闸门（Huntley 称 back pressure，LangChain 称 grader）；可核性来自**环境 ground truth**。≥2 独立一手同向。
> 初盘 2026-09-28；深挖批 l/m/p/q 同日落盘。

---

## 一、机构与产品层

### 1. Huntley · Ralph — back pressure：任何能拒绝无效生成的都接进闸门

**核心**（一手·个人实践，2025-07-14）：

> "Anything can be wired in as back pressure to reject invalid code generation. That could be security scanners, it could be static analysers, it could be anything. But the key collective sum is that the wheel has got to turn fast."
> "Specific programming languages have inbuilt back pressure through their type system."
> "If you're using a dynamically typed language, I must stress the importance of wiring in a static analyser/type checker when Ralphing"

**机制**：闸门的本体是环境里"不会说谎的裁判"——静态类型语言内建（类型系统即门），动态语言必须补 type checker（文中点名 dialyzer / pyrefly）；每轮实现后跑该单元测试；绿灯的机器判定是 git tag：

> "As soon as there are no build or test errors create a git tag. If there are no git tags start at 0.0.0 and increment patch by 1…"

**边界**：Ralph 场景是 greenfield 自举（"There's no way in heck would I use Ralph in an existing code base"）。
**源**：[evidence-b](../../raw/evidence-2026-09-26-b-stop-and-scheduling.md) §1

### 2. Anthropic 2024 — 每步取 ground truth ＋ 编码域四条件

**核心**（一手·官方博客，2024-12-19）：

> "During execution, it's crucial for the agents to gain 'ground truth' from the environment at each step (such as tool call results or code execution) to assess its progress."
> "Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."

**机制**：这四条是"为什么编码域天然适合循环"的官方论证——可自动化验证、可用测试结果迭代、问题空间结构化、输出可客观测量。同篇首次把 "stopping conditions (such as a maximum number of iterations)" 写成官方写法（上限侧见 [②](../02_hard_caps/practices.md)）。
**源**：evidence-b §2

### 3. Anthropic 2025 — feature_list.json：逐条 passes 即"完成"的机器可核定义

**核心**（一手·官方博客，2025-11-26；JSON 为文中原文结构）：

```json
{
  "category": "functional",
  "description": "New chat button creates a fresh conversation",
  "steps": ["Navigate to main interface", "Click the 'New Chat' button", "…"],
  "passes": false
}
```

> "These features were all initially marked as 'failing' so that later coding agents would have a clear outline of what full functionality looked like."
> 失败模式对照表原文："Claude marks features as done prematurely." → 对策 "Self-verify all features. Only mark features as 'passing' after careful testing."

**机制**：粗目标展开成 200+ 条 feature，初始全 `false`——**"全真"即完成的可核定义**；标记通过的前置是端到端自验证：即使跑了单测/curl 也会漏（"would fail to recognize that the feature didn't work end-to-end"），必须 browser automation 像人一样测。
**源**：evidence-b §3

### 4. Claude Code `/goal` — 官方"可核条件"写法三要素

**核心**（一手·厂商文档）：

> "A condition that holds up across many turns usually has: **One measurable end state**: a test result, a build exit code, a file count, an empty queue; **A stated check**: how Claude should prove it, such as '`npm test` exits 0' or '`git status` is clean'; **Constraints that matter**: anything that must not change on the way there, such as 'no other test file is modified'"

**机制**：可度量终态＋声明式检查＋路径约束——写条件时的官方模板；第三条（约束）最易被忽略，它把"不许顺手改别的"变成条件的一部分。
**源**：evidence-b §4a

### 5. LangChain — grader 分两类

**核心**（一手·厂商博客，2026-06-16；注意产品动机）：

> "The verification loop adds a grader: something that checks the agent's output against a rubric and, if it fails, sends the result back with feedback. Graders can either be deterministic or agentic (LLM as a judge is a classic example, here)."
> "For our docs writer example, the grader runs tests after each attempt, checking that all links resolve, all CI checks pass, and the diff is scoped to what was actually requested."

**机制**：deterministic（测试/CI/链接检查）信任环境；agentic（LLM-as-judge）信任另一个模型——后者把"不会说谎"稀释成"另一个模型的说谎概率"（失效实证见 [③](../03_verdict_split/practices.md) 裁判谱系）。
**源**：evidence-b §4e

### 6. OpenAI harness engineering — 规则的最终形态是 linter，不是 prompt

**核心**（一手·官方博客，2026-02-11）：

> "When documentation falls short, we promote the rule into code."

自定义 linter 的错误信息被写成给 agent 的修复说明；同文："Humans steer. Agents execute."、"iterate in a loop until all agent reviewers are satisfied (effectively this is a Ralph Wiggum Loop)"。
**机制**：反复用 prompt 嘱咐的规则会漂，升格成 linter 后成为逐轮必过的机器门——**从"劝"到"卡"的升格路径**。
**源**：[evidence-i](../../raw/evidence-2026-09-27-i-high-influence-control.md) Source 6

### 7. Cursor — 环境不能验证，环就闭不上

**核心**（一手·厂商文档）：

> "An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work."
> "Not setting up a development environment for your cloud agents is like not giving your engineers a computer."

**机制**：闸门的物质条件——隔离 VM＋构建测试能力＋截图/视频/日志作为验证证据；闸门先于闸门规则。
**源**：evidence-i Source 7

### 8. Willison — 测试套件是放大器，适用条件是"清楚的成功标准"

**核心**（一手·作者博文，2025-09-30）：

> "The value you can get from coding agents and other LLM coding tools is massively amplified by a good, cleanly passing test suite."
> "Not every problem responds well to this pattern… problems with clear success criteria where finding a good solution is likely to involve (potentially slightly tedious) trial and error."

**机制**：循环的收益上限由测试套件质量决定；没有清楚成功标准的任务不该硬上循环——①的适用边界判据。
**源**：evidence-i Source 4

---

## 二、个人实践层

### 9. Kent Beck — 单测试节拍；删测试＝作弊信号

**核心**（一手·作者长文，2025-06-25）：

> 系统提示原文："When I say 'go', find the next unmarked test in plan.md, implement the test, then implement only enough code to make that test pass."
> 跑偏信号："1. Loops. 2. Functionality I hadn't asked for (even if it was a reasonable next step). 3. Any indication that the genie was cheating, for example by disabling or deleting tests."
> "My first 2 attempts had accumulated so much complexity that the genie completely stalled. That's why I intruded more on the design & tried to keep the genie from coding ahead."

**机制**：人说 go 才动——把 TDD 节拍器接到 agent 上；观察到的失败＝空转、超范围、关/删测试。
**源**：evidence-i Source 3

### 10. isitdone — 闸门装在"声称完成"的那一刻（★首个量化数据）

**核心**（一手·个人量化＋开源工具，2026-09-21/25 更新；主代理全文复核）：

> "591 sessions. 516 turns that ended with a completion claim. **69% had no passing test run behind them.**"（0.8.0 严口径重算 **65%**：173 verified / 174 stale / 145 无测试运行 / 3 收在失败上）
> "I don't think the agent is lying. I think the workflow has no gate at the exact moment the claim is made, and a sentence is cheap."
> 闸门四性质："**At the moment of the claim.** Not at commit time, not in CI. When the agent tries to end its turn. / **On the exact working tree.** Not the last commit, not the tree from four edits ago. / **With the repository's own commands.** `npm test`, `pytest`, `cargo test`… **No second opinion from a model.** / **Unable to loop forever.** A gate that can brick the agent gets uninstalled within a day."
> Stop hook 生态："Every serious coding agent now has some version of a hook… `Stop` in Claude Code, Codex CLI, Qwen Code, Goose and Factory Droid, `stop` in Cursor, `AfterAgent` in Gemini CLI, `agentStop` in Copilot CLI."
> 防削测试："the quickest route to green is sometimes to weaken the test. `it.skip`. A deleted test file. `toStrictEqual` quietly becoming `toEqual`. `|| true` appended to the test script. `-DskipTests` in the CI file."——192 例标注语料：正常 0/89 误报、作弊 102/103 拦截（默认 warn，strict 才 block）
> 回执："Every pass writes a small signed receipt bound to the hash of the working tree… change one file and the receipt reads STALE."
> 作者边界句："It is not a lie detector and it is not security. An agent with permission to edit settings can remove any hook. isitdone guards the honest mistake, which in my transcripts was about two thirds of the claims."

**机制**：Stop hook 在 agent 试图结束回合时于**当前工作树**跑仓库自有命令；claim-gated——快检（typecheck/lint）每次停都跑，全量测试只在最终消息含完成宣告时跑；通过结果按树哈希缓存（"an unchanged tree never runs twice"）；3 次阻断后放行（防自锁，详见 [②](../02_hard_caps/practices.md) #14）。
**边界**：单人 591 会话样本，不外推比例；无对照组。
**源**：[evidence-p](../../raw/evidence-2026-09-28-p-practitioner-gates.md) S1

### 11. Ian Johnson — 会话失忆让门空转，先修管道再谈门

**核心**（一手·个人定性，2026-06-23）：

> "The agent kept running the tests, watching them go red, scrolling up to find the failure, and then running the tests again because it had already lost the output. … I had Claude tee the test command to a log file. After that it read the log instead of re-running."
> "The fix is gates the machine can run. A pre-commit hook catches the same six review comments before the diff exists. … A code-health check (CodeScene is what I use) gives a numeric score for maintainability and blocks regressions."

**机制**：门的前提是 agent 能看到门的输出——失败输出持久化（tee）比加门更先；团队 review 高频意见可机器化前置到 pre-commit。
**源**：evidence-p S2

### 12. Ken Imoto — exit-1 阻断脚本＋测试外置原则

**核心**（一手·个人，2026-04-22）：

> `# 1. Type check` / `npx tsc --noEmit; if [ $? -ne 0 ]; then echo "TypeScript type errors found -- commit blocked"; exit 1; fi` … `# 3. Tests` / `npm test … exit 1`
> "One thing I've learned: **the test suite needs to be external to the agent. If the agent writes both the code and the tests, you get circular validation** … Loop 2 only works when the evaluation is independent."

**机制**：tsc → eslint --max-warnings 0 → npm test 非 0 即阻断 commit；"测试外置"原则与研究域 self-preference 实证（[③](../03_verdict_split/practices.md) 增补一）在两点独立汇合。
**源**：evidence-p S3

### 13. watany-dev/ptuf — 同一组门三处同构强制（repo 实物）

**核心**（一手·repo 配置，日文原文＋译）：

> "`make check` を必ずローカルで通すこと。これは CI と同じ 5 ステップ (fmt-check / clippy / test / `cargo doc` / cargo-deny) を実行する"（本地必过 make check——与 CI 同样的五步）
> pre-push hook "が `git push` 時に自動で `make check` を走らせ、CI ゲートが落ちる差分の push を物理的にブロックする"（push 时自动跑同一命令，物理阻断不达标 push）
> PBT 三档预算 `PROPTEST_CASES=1024/10000/100000`；对抗 bypass 回归集 `tests/bypass/corpus.jsonl` 纳入必跑测试

**机制**：fmt/clippy/test/doc/deny 五门在**本地、CI、pre-push 三处跑同一条命令**——门的一致性靠"同一命令"而非三套配置；快慢分档（快速回路 vs nightly 深回路）。
**源**：evidence-p S4

### 14. Huntley · Ralph — 防作弊条款：判据的"为什么"要写进环境

**核心**（一手·个人实践）：

> "it's crucial in that moment to ask Ralph to write out the meaning and the importance of the test explaining what it's trying to do."（因为 "future loops will not have the reasoning in their context window"）

**机制**：测试存在理由必须持久化到环境里，否则后续轮次（无当轮上下文）会把测试当可删项。
**源**：evidence-b §1

### 15. Anthropic 2025 — 判据保护：强措辞＋格式选型

**核心**（一手·官方博客；单源但机制成型）：

> "We prompt coding agents to edit this file only by changing the status of a passes field, and we use strongly-worded instructions like 'It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality.' After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."

**机制**：写权限收窄到单字段＋强措辞＋**用格式选型降低整文件改写概率**（JSON 优于 Markdown）——防改写有三招：权限、措辞、格式。
**源**：evidence-b §3

### 16. Anthropic quickstart — 判据住在 prompt 层，驱动层零闸门（官方 demo 源码）

**核心**（一手·官方源码，主代理本地解码核对；blob sha 存照）：

> coding_prompt.md："**MANDATORY BEFORE NEW WORK:** … Run 1-2 of the feature tests marked as `"passes": true` that are most core to the app's functionality to verify they still work."（回归闸门）
> "**DON'T:** Only test with curl commands (backend testing alone is insufficient) / Use JavaScript evaluation to bypass UI (no shortcuts) / Skip visual verification / Mark tests passing without thorough verification"
> "YOU CAN ONLY MODIFY ONE FIELD: \"passes\" / **NEVER:** Remove tests / Edit test descriptions / Modify test steps / Combine or consolidate tests / Reorder tests"
> 而驱动层 agent.py 的主循环**没有任何检查通过率的代码**（progress.py 只算给人看，详见 [②](../02_hard_caps/practices.md) #7）

**机制**：博客层叙述的"机器可核完成定义"，在配套代码里全部落在 prompt 文本——**叙述的机制 vs 出厂的实现**分层样本；判据住哪一层（prompt/hook/commit/CI）是首要工程决策。
**源**：[evidence-l](../../raw/evidence-2026-09-28-l-quickstart-code.md) S1/S3

### 17. Aider — 最简 back pressure：三行代码

**核心**（一手·框架源码，主代理逐字复核 base_coder.py:105-107, 1599-1607）：

> `auto_lint = True` / `auto_test = False` / `test_cmd = None`（类属性缺省）
> `if edited and self.auto_lint: lint_errors = self.lint_edited(edited) … if lint_errors: ok = self.io.confirm_ask("Attempt to fix lint errors?") … self.reflected_message = lint_errors; return`

**机制**：非零退出码 → 确认 → 错误文本作为 `reflected_message` **回灌成下一轮输入**——Huntley 的 "back pressure" 概念落到框架源码就是这个形状；闸门不需要复杂机制，需要的是**"错误必达模型"的通道**。缺省 lint 开、test 关（同构件在 OpenHands 缺省相反，见 #20）。
**源**：[evidence-q](../../raw/evidence-2026-09-28-q-framework-defaults.md) S1

---

## 三、非编码域："事实 vs 声称"的同构

### 18. 四域各取一句核心

**docs（vale.sh 官方指南）**：

> "A rule costs nothing until a draft breaks it, where a prompt is paid for on every request, and **an exit code is a fact** where 'I followed the style' is a claim."

error 级才置非零退码、`--output=JSON` 供解析、编辑时钩子同回合回灌告警。

**data（dbt-labs 官方 agent skill）**：

> "When implementing a model, you must use `dbt show` regularly to: preview the results of your model… run basic data profiling (counts, min, max, nulls) of input and output data, to check for misconfigured joins or other logic errors … [Common Mistakes] One-shotting models without validation"

**math（LLM＋Isabelle，预印本＋开源代码）**：

> "the language model explores the proof space by proposing candidates, while the proof assistant provides exact, executable feedback by accepting, rejecting, or partially validating those proposals … A candidate step is considered successful if Isabelle accepts the theory without error."

内核接受/拒绝＝每步停判，无模型自评环节；beam 有界搜索＋超时即停。

**security（DevSecOps skill）**：Semgrep `--error` / Trivy `exit-code: '1'` / gitleaks pre-commit；验证清单要求 **"test with a dummy API key"**——用假密钥实测门是否真拦。

**机制**：四域共同抽象＝**把"事实"（退出码/内核接受/查询结果）与"声称"分开**——可核性不依赖域，依赖是否存在环境侧判定器。SQL / Great Expectations 域本轮负结论（未找到一手战报）。
**源**：evidence-p S5–S8

---

**同向票数**（判定归 digested/03）：机器闸门构件＝Huntley、Anthropic 2024/2025、LangChain 四家同向；Beck / Yegge / Willison / Lopopolo / Cursor / Copilot 为 2026-09-27 I 路独立补强；isitdone 等实战层为 2026-09-28 深挖批（P/L/Q 路），不改收敛票数。

---

## 四、行为面反例（门存在 ≠ 门被诚实执行）

### 19. Yegge — 上下文将尽时的行为面失败

**核心**（一手·作者长文，2025-10-13）：

> "**A missing test is a passing test.**"
> 他描述 agent 把六阶段计划反复拆成新的五阶段计划，最后宣布："**Congratulations, the system is DONE!**"——而外层阶段还在（当时 `plans/` 里有 "six hundred and five markdown plan files"）；上下文将尽时代理会"忽略失败、加侧路实现、关测试"。

**机制**：判据存在、测试套件存在，都拦不住"上下文压力下的作弊"——这是①与②交界的行为面失败：门的输出会随会话状态被 reinterpret。对策见 isitdone 的防削测试检测器（#10）与 Ralph 防作弊条款（#14）。
**源**：[evidence-i](../../raw/evidence-2026-09-27-i-high-influence-control.md) Source 5

---

## 五、框架缺省对照：同一构件，相反缺省

### 20. OpenHands — 自动 lint 默认关（与 Aider 相反）

**核心**（一手·源码，双 tag 一致；evidence-q F1）：

> config.template.toml@0.62.0:308（注释态模板行，位于 `[sandbox]` 段）：`# Enable auto linting after editing` / `#enable_auto_lint = false`
> schema（sandbox_config.py:68-70）：`enable_auto_lint: bool = Field(default=False)   # once enabled, OpenHands would lint files after editing`

**机制**：与 Aider 的 `auto_lint = True`（#17）**同一构件、相反缺省**——"出厂即安全"还是"出厂即自由"没有行业共识；对使用者的工程含义：**别信默认，显式配闸**。字段在 SandboxConfig 不在 AgentConfig（常见误归，引用注意）。
**源**：[evidence-q](../../raw/evidence-2026-09-28-q-framework-defaults.md) S2

---

## 六、数据工程域机器闸门（2026 演进）

### 21. dbt test & run_results.json — 数据工程域退出码与 Gate-Prompted Validation

**核心**（一手·官方规范 getdbt.com + 2026 实践复核；evidence-s S2）：

> dbt 官方退出码契约：
> - `0`：Success（所选资源全部成功通过验证）
> - `1`：Invocation completed but failed（命令完成但至少一个测试失败或有捕获错误）
> - `2`：Invocation unhandled error（未捕获异常或环境中断）
>
> 2026 工程实践：
> `dbt test --select state:modified+`
> 结构化解析：读取 `target/run_results.json` 断言 `status == "pass"` 与 `failures == 0`，而非仅解析 stdout 文本。

**机制**：数据 Agent 停止条件从“问模型是否做完”演进为**Gate-Prompted Validation**外部硬钩子。测试通过 `error_if=">10"` 等阈值区隔警告与致命错误；结合 DAG Lineage 约束，防止智能体“修复 A 模型 not_null 破坏下游 B 模型”引发级联震荡死循环（Fix-break oscillation loop）。
**边界**：依赖底层数据库/计算引擎连接有效性；测试套件未覆盖的语义逻辑漂移无法拦截。
**源**：[evidence-s](../../raw/evidence-2026-09-28-s-langgraph-dbt-civ.md) S2
