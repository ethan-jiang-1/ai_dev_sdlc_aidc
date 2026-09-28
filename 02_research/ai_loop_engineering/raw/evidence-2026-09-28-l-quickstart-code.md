---
type: evidence_archive
collected_by: 主代理直采（L 路 · Anthropic 官方 quickstart 源码，服务 stop_conditions 三点深挖）
collected_at: 2026-09-28
serves: stop_conditions/{01_machine_gates,02_hard_caps,03_verdict_split}/practices.md
status: 一手源码全文取得（api.github.com blob API，raw.githubusercontent.com 本环境不可达见负结论）；四个文件内容以 blob sha 存照
quality_bar: 官方配套代码＝机构一手；但定位是 demo，不能代 Anthropic 内部生产做法
---

# 回源档案 L：Anthropic claude-quickstarts/autonomous-coding 源码直采（观测 2026-09-28）

> **任务**：把《Effective harnesses for long-running agents》（2025-11-26，已档于 [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md) §3）
> 的**配套代码**取到源码层，回答三个工程问题：判据住在哪一层？上限默认值是什么？完成判定由谁执行？
> 博客讲了机制，代码显示实现粒度——两者的落差本身是发现。
>
> **取材方式**：raw.githubusercontent.com 直连超时（同 09-26 负结论）；改走
> `api.github.com/repos/anthropics/claude-quickstarts/git/blobs/<sha>`，main 分支，观测日 2026-09-28。
> 内容存照（blob sha）：`agent.py@8856d40`、`progress.py@aebee82`、`README.md@6a3ac47`、
> `prompts/coding_prompt.md@2af09ad`、`prompts/initializer_prompt.md@41a792`。
> 许可证标注 "Internal Anthropic use"。

## Source 1 · agent.py（主循环驱动）

- URL：https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/agent.py
- 发布日期：无单文件日期（main，观测 2026-09-28）；访问日期：2026-09-28
- 来源类型：官方源码（一手）

**逐字摘录（代码）**：

- 上限默认与语义：
  > `async def run_autonomous_agent(project_dir: Path, model: str, max_iterations: Optional[int] = None) -> None:`
  > docstring: `max_iterations: Maximum number of iterations (None for unlimited)`
  > `print("Max iterations: Unlimited (will run until completion)")`（未传参时）
- 主循环唯一退出路径（除异常外）：
  > `while True:` / `iteration += 1` / `if max_iterations and iteration > max_iterations:` →
  > `print(f"\nReached max iterations ({max_iterations})")` / `print("To continue, run the script again without --max-iterations")` / `break`
- **循环内没有完成检查**：`run_agent_session` 成功时恒返回 `("continue", response)`；驱动层不读通过率、不判 "全部 passes"。每轮 `client = create_client(project_dir, model)`（注释 "Create client (fresh context)"）。
- 节拍与重试：`AUTO_CONTINUE_DELAY_SECONDS = 3`；status == "continue" → 打印进度摘要后 sleep 3s；status == "error" → "Will retry with a fresh session..." 再 sleep 3s（**错误也不停循环**）。

**该摘录支持的最小主张**：官方配套驱动里，**硬上限是 opt-in（默认 None＝无限）**；循环退出只有两条路——可选的 `--max_iterations` 和用户中断；错误按可恢复处理（换新会话重试），不熔断。

**不支持什么**：demo 代码不能代表 Anthropic 内部生产 harness；"will run until completion" 是打印文案，代码层没有 completion 检查实现它。

## Source 2 · progress.py（进度＝显示，不是闸门）

- URL：https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/progress.py
- 访问日期：2026-09-28；来源类型：官方源码（一手）

**逐字摘录（代码）**：

> `def count_passing_tests(project_dir: Path) -> tuple[int, int]:` 读取 `feature_list.json`，
> `passing = sum(1 for test in tests if test.get("passes", False))`，返回 `(passing, total)`；
> `print_progress_summary` 打印 `f"\nProgress: {passing}/{total} tests passing ({percentage:.1f}%)"`。

**该摘录支持的最小主张**：通过率只被**算给人看**（每轮结束打印）；没有任何代码路径以 `passing == total` 作为停止条件。evidence-b §3 里"全真即完成"的可核定义，在配套代码的**驱动层没有落地**。

**不支持什么**：不能说 Anthropic 主张"不需要机器完成检查"——这是 demo 的实现选择，博客叙述的是另一层。

## Source 3 · prompts/coding_prompt.md（判据实际住处：prompt 层）

- URL：https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/prompts/coding_prompt.md
- 访问日期：2026-09-28；来源类型：官方源码模板（一手）

**逐字摘录（关键段）**：

- 回归闸门（STEP 3，"VERIFICATION TEST (CRITICAL!)" / "MANDATORY BEFORE NEW WORK"）：
  > "The previous session may have introduced bugs. Before implementing anything new, you MUST run verification tests."
  > "Run 1-2 of the feature tests marked as `\"passes\": true` that are most core to the app's functionality to verify they still work."
  > "**If you find ANY issues (functional or visual):** Mark that feature as \"passes\": false immediately … Fix all issues BEFORE moving to new features"
- 端到端验证（STEP 6，"VERIFY WITH BROWSER AUTOMATION" / "CRITICAL: You MUST verify features through the actual UI"）：
  > "**DON'T:** Only test with curl commands (backend testing alone is insufficient) / Use JavaScript evaluation to bypass UI (no shortcuts) / Skip visual verification / Mark tests passing without thorough verification"
- 判据保护（STEP 7，"UPDATE feature_list.json (CAREFULLY!)"）：
  > "**YOU CAN ONLY MODIFY ONE FIELD: \"passes\"**" / "**NEVER:** Remove tests / Edit test descriptions / Modify test steps / Combine or consolidate tests / Reorder tests"
  > "ONLY CHANGE \"passes\" FIELD AFTER VERIFICATION WITH SCREENSHOTS."
- 完成定义与时间观（IMPORTANT REMINDERS）：
  > "**Your Goal:** Production-quality application with all 200+ tests passing"
  > "**You have unlimited time.** Take as long as needed to get it right."

**该摘录支持的最小主张**：判据的**全部强制力都在 prompt 文本里**——回归验证、browser 自验、只许改 `passes`、判据不可删改，全是给干活 agent 的指令；没有一行驱动代码校验这些约束被遵守。完成定义（"all 200+ tests passing"）也只写在 prompt 的 Goal 里。

**不支持什么**：prompt 约束的实际遵从率未测；不能据此外推生产系统同样如此。

## Source 4 · README.md（官方对"何时停"的口径）

- URL：https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/README.md
- 访问日期：2026-09-28；来源类型：官方文档（一手）

**逐字摘录**：

- 停止方式："The agent auto-continues between sessions (3 second delay)" + "**Press Ctrl+C to pause**; run the same command to resume"
- CLI 表：`--max-iterations` | Max agent iterations | **Unlimited**（默认）
- 量级预期："First session … generates a `feature_list.json` with 200 test cases. This takes several minutes"; "Full app: Building all 200 features typically requires **many hours** of total runtime across multiple sessions."
- 安全模型（旁注，属 harness 环境轴）："Commands not in the allowlist are blocked by the security hook."（bash 白名单：ls/cat/head/tail/wc/grep、npm/node、git、ps/lsfg/sleep/pkill）

**该摘录支持的最小主张**：官方 README 明示的暂停方式是 **Ctrl+C**；上限默认 Unlimited；官方预期该 demo 跑"many hours"。

## 判读

- **观察**：判据（feature_list 逐条 passes）、上限（max_iterations）、完成判定（all passing）三者在**博客层都有机器化叙述**，在配套代码里分别落在三个不同层：判据住 prompt、上限 opt-in、完成判定＝干活 agent 自判＋人中断＋进度条给人看。这是"叙述的机制 vs 出厂的实现"之间的真实落差样本。
- **推断（限定 demo）**：即便在最先讲"机器可核完成定义"的机构自己的 demo 里，驱动层的机器闸门也是可选件——工程实践中 Ctrl+C 仍是兜底停止方式。此条为 ②（官方 demo 默认无上限）与 ③（完成判定退化为自判＋人盯）提供一手反例侧样本；为 ① 提供"判据住哪一层"的分层样本。
- **与现有材料关系**：对 evidence-b §3（同机构博客）是**实现粒度补强**，不推翻其机制叙述；机构链同源（Anthropic），不新增独立机构票。

## 负结论与限制

- raw.githubusercontent.com 直连：web_fetch 30s 超时（2026-09-28 复测，与 evidence-b 09-26 负结论一致）；改走 api.github.com blob API 成功。
- swyx《loopcraft》（latent.space）：直连 fetch failed；O'Reilly 疑似转载版导航过重截断——**正文未取得**，仅存在性线索（沿 evidence-b 旧负结论状态不变）。
- 未取 HEAD commit sha 存照（blob sha 已可钉住内容）；init.sh 生成逻辑、security.py 全文（10KB）未逐行审。
- 本档案所有代码引文经本地解码核对（.tmp-loop-research-batch1/，收口后清理）。
