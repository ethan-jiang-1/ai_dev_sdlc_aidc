---
type: evidence_archive
collected_by: 委派回源子代理（P 路 · 实践者战报＋非编码域"每轮机器可核闸门"）＋ 主代理抽验（isitdone 全文逐字复核）
collected_at: 2026-09-28
serves: stop_conditions/01_machine_gates/practices.md ＋ insights.md
status: 8 条新来源（4 个人实践一手、2 厂商一手规格、1 论文预印本、1 社区 skill 产物）；含 5 条负结论
quality_bar: 一手作者本人内容优先；厂商规格注明非中立；同温层风险（dev.to harness 圈）已标注
---

# 回源档案 P：实战闸门战报＋非编码域"环境当裁判"（观测 2026-09-28）

> **任务**：为①补两类素材——(a) 实践者在真实项目里的闸门战报（带命令与踩坑）；(b) 编码域之外的可核判据形态（docs/data/math/security）。

## Source 1 · isitdone — 把闸门装在"声称完成"的那一刻（★主代理全文复核）

- URL：https://dev.to/raimondasl/69-of-my-coding-agents-done-claims-werent-here-is-the-gate-i-put-in-front-of-them-lho ；2026-09-21（09-25 更新重算）；工具 github.com/raimondasl/isitdone（MIT、零依赖）；访问：2026-09-28
- 摘录（复核原句）：
  > "591 sessions. 516 turns that ended with a completion claim. **69% had no passing test run behind them.**"（0.8.0 严口径重算：495 claims，**65%**——173 verified / 174 stale / 145 无测试运行 / 3 收在失败上）
  > "I don't think the agent is lying. I think the workflow has no gate at the exact moment the claim is made, and a sentence is cheap."
  > 闸门四性质："**At the moment of the claim.** Not at commit time, not in CI… / **On the exact working tree.**… / **With the repository's own commands.** `npm test`, `pytest`, `cargo test`… **No second opinion from a model.** / **Unable to loop forever.** A gate that can brick the agent gets uninstalled within a day."
  > Stop hook 生态："Every serious coding agent now has some version of a hook… `Stop` in Claude Code, Codex CLI, Qwen Code, Goose and Factory Droid, `stop` in Cursor, `AfterAgent` in Gemini CLI, `agentStop` in Copilot CLI."
  > claim-gated："Fast checks (typecheck, lint) run on every stop. The full suite runs only when the final message contains a completion claim… A passing tree is cached by a hash of the working tree."
  > 防"削测试转绿"："the quickest route to green is sometimes to weaken the test. `it.skip`. A deleted test file. `toStrictEqual` quietly becoming `toEqual`. `|| true`… 192 例标注语料：legitimate 0/89 误报；tampering 102/103 拦截"（默认 warn，strict 才 block）
  > 回执："Every pass writes a small signed receipt bound to the hash of the working tree… change one file and the receipt reads STALE."
  > 边界（作者原话）："It is not a lie detector and it is not security. An agent with permission to edit settings can remove any hook. isitdone guards the honest mistake, which in my transcripts was about two thirds of the claims."
- 最小主张：**首个量化的"完成宣告无测试背书"比例**（单人 591 会话 65%）；Stop-hook 闸门的完整工程规格（时点/工作树/仓库自有命令/防死锁 3 次放行）；削弱测试检测器带公开基准；签名回执防 stale。
- 不支持：单人样本不可推广；无对照组证明 hook 后比例下降；工具由 Claude 代写（作者自述并 owns 发布）。
- 强度：high（一手、量化、工具与语料公开可复核）。

## Source 2 · Ian Johnson — 会话失忆导致重复跑测试的坑

- URL：https://dev.to/tacoda/what-breaks-when-you-skip-the-harness-3237 ；2026-06-23 首发；访问：2026-09-28
- 摘录："The agent kept running the tests, watching them go red, scrolling up to find the failure, and then running the tests again because it had already lost the output. … I had Claude tee the test command to a log file. After that it read the log instead of re-running."；"The fix is gates the machine can run. A pre-commit hook catches the same six review comments before the diff exists. … A code-health check (CodeScene…) gives a numeric score for maintainability and blocks regressions."
- 最小主张：实战坑——agent 会丢失自己的测试输出而重复跑（tee 进日志修）；团队 review 高频意见可转成 pre-commit 机器门；可维护性数值分数可阻挡回归。
- 不支持：无量化；作者自认无 clean benchmark（有出书动机）。
- 强度：medium-high（一手定性）。

## Source 3 · Ken Imoto — 硬闸门脚本与"测试必须外置"

- URL：https://dev.to/kenimo49/almost-every-time-vs-every-time-why-hooks-beat-instructions-for-ai-agents-28bf ；2026-04-22；访问：2026-09-28
- 摘录：
  > "# 1. Type check / `npx tsc --noEmit; if [ $? -ne 0 ]; then echo \"TypeScript type errors found -- commit blocked\"; exit 1; fi` … # 3. Tests / `npm test` … exit 1"
  > "One thing I've learned: **the test suite needs to be external to the agent. If the agent writes both the code and the tests, you get circular validation** … Loop 2 only works when the evaluation is independent."
- 最小主张：带具体命令的 commit 阻断脚本（tsc→eslint --max-warnings 0→npm test）；**测试外置于 agent**的原则表述（自写自测＝循环自证）；四层反馈循环分层（秒级 lint／任务级测试／会话级 AGENTS.md／战略级重构）。
- 不支持：执行率图为示意；无前后对比。
- 强度：medium。

## Source 4 · watany-dev/ptuf — 同一命令三处强制的 repo 实物

- URL：https://github.com/watany-dev/ptuf/blob/main/CLAUDE.md （Rust CLI，Apache-2.0，2026-05 起活跃）；访问：2026-09-28
- 摘录（日文原文，翻译摘录）："`make check` を必ずローカルで通すこと。これは CI と同じ 5 ステップ (fmt-check / clippy / test / cargo doc / cargo-deny) を実行する"；pre-push hook "が `git push` 時に自動で `make check` を走らせ、CI ゲートが落ちる差分の push を物理的にブロックする"；PBT 三档预算 `PROPTEST_CASES=1024/10000/100000`；对抗性 bypass 回归集 `tests/bypass/corpus.jsonl` 纳入必跑。
- 最小主张：同一组门（fmt/clippy/test/doc/deny）在本地、CI、pre-push **三处同构强制**；测试预算分档（快回路 vs nightly 深回路）；对抗语料进必跑测试。
- 不支持：纯配置无效果叙述；单人小 repo。
- 强度：medium（存在性＋活跃维护）。

## Source 5 · vale.sh agents 指南 — docs 域"退出码即事实"

- URL：https://docs.vale.sh/guides/agents ；v3.20/3.21 时点；访问：2026-09-28
- 摘录："A rule costs nothing until a draft breaks it, where a prompt is paid for on every request, and **an exit code is a fact** where 'I followed the style' is a claim."；only `error` 置非零退码、`--output=JSON` 供解析；编辑时钩子"lints each prose file as the assistant writes it and hands back the alerts, so a mistake is fixed in the same turn it was made."
- 最小主张：docs 域完整机器闭环规格：退出码=事实 vs 口头承诺=claim；同回合回灌告警；CI 门失败构建。
- 不支持：厂商自述（产品叙事）；无第三方实测。
- 强度：medium。

## Source 6 · dbt-labs 官方 agent skill — data 域验证回路

- URL：https://github.com/dbt-labs/dbt-agent-skills/blob/main/skills/dbt/skills/using-dbt-for-analytics-engineering/SKILL.md （官方 org，727 stars，2026-01 起活跃）；访问：2026-09-28
- 摘录："When implementing a model, you must use `dbt show` regularly to: preview the results of your model… run basic data profiling (counts, min, max, nulls) of input and output data, to check for misconfigured joins…"；"[Common Mistakes] One-shotting models without validation"。
- 最小主张：data 域官方把**执行结果预览**（dbt show）设为 agent 的逐轮验证回路，并把"不验证的一次成型"列为头号错误；allowed-tools 限定 Bash(dbt *)。
- 不支持：skill 规格非会话实证；dbt build/test 退出码在此文件未写成停判。
- 强度：medium。

## Source 7 · LLM+Isabelle — math 域内核即裁判（proof-check 即停判）

- URL：https://arxiv.org/abs/2601.04653 （Griffith Univ.，2026-01 预印本；代码 github.com/zhehou/llm-isabelle）；访问：2026-09-28
- 摘录："the language model explores the proof space by proposing candidates, while the proof assistant provides exact, executable feedback by accepting, rejecting, or partially validating those proposals … A candidate step is considered successful if Isabelle accepts the theory without error."；验证器结局直接作 reranker/RL 训练信号。
- 最小主张：math 域的①完全体：内核接受/拒绝＝每步停判，无"模型自评"环节；beam 有界搜索＋超时即停（②同场出现）；且系统本身由 LLM 写成（自举样本）。
- 不支持：未同行评审；单人自测无外部复现。
- 强度：medium-high。

## Source 8 · DevSecOps security-gate skill — 安全域的门配置＋"测门本身"

- URL：https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/skills/implementing-devsecops-security-scanning/SKILL.md ；访问：2026-09-28
- 摘录：`semgrep scan --config p/security-audit --severity ERROR --error`；Trivy `exit-code: '1'`；汇总 job "BLOCKED: Secrets detected in repository / exit 1"；Verification 清单："Gitleaks blocks commits and PRs containing hardcoded secrets (**test with a dummy API key**)"。
- 最小主张：security 域把机器门配置写成 agent 可部署的 skill；且验证清单要求**实测门是否真拦**（假 API key）——"测闸门本身"的工程意识样本。
- 不支持：个人仓库无采用度；纯指南产物非战报。
- 强度：low-medium。

## 判读

- **观察**：①在实战层的形态远比厂商文档细：闸门**装在声称时刻**（Stop hook）而非 commit/CI；**快慢分离**（每停快检、claim 才跑全量、树哈希缓存）；**防死锁**（3 次放行——闸门自己也要有停止条件）；**防削测试**（检测器＋基准语料）；**回执防 stale**（树哈希签名）。非编码域四例（docs 退出码、data 执行预览、math 内核判定、security 退出码门）共同点：**把"事实"（exit code/内核接受/查询结果）与"声称"分开**——与编码域同构。
- **推断（候选）**：①的工程要领清单可从实战层重写：时点（claim 处）、命令（仓库自有，无第二意见）、快慢分档、防削测试、防自锁、回执化。Ken Imoto 的"测试外置于 agent"与 M 档 self-preference 实证在两点独立汇合——**同源自评失效**是跨域共识。
- **与现有材料关系**：与 evidence-b 的 back pressure/grader 是同一构件的实战细化；isitdone 的 65% 数字为 digested/03"提前宣告完成"目标敌人提供**首个个体量化的行为面数据**（单人样本，不外推）。

## 负结论与限制

- SQL/分析域未收口（候选源超时/二手聚合未用）；Great Expectations 无一手战报（负结论）。
- Lean 域两条线索未及核（MIT CSAIL talk、reservoir.lean-lang.org）；Isabelle 已覆盖。
- dev.to 三源（isitdone/Ian Johnson/Ken Imoto）同属 harness 主题圈——**同温层风险**，独立性按作者分开计但不视为三家机构。
- 检索基础设施故障两次（端点报错/60s 超时）影响覆盖。
