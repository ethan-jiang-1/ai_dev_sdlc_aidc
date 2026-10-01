---
type: evidence_archive
collected_by: 委派回源子代理（O 路 · agent 循环失控实录与事后处置）＋ 主代理抽验（cline#3418 / claude-code#46787 / OpenHands PR#11799 三条 GitHub API 逐字复核）
collected_at: 2026-09-28
serves: stop_conditions/02_hard_caps/practices.md ＋ insights.md
status: 5 条新来源（2 GitHub 一手 issue、1 Reddit 一手经媒体链转述、2 厂商闸门文档/PR）；含 6 条负结论
quality_bar: 事故记录以一手过程细节为准；媒体转述明示并只取多源一致骨架；热度帖剔除
---

# 回源档案 O：agent 循环失控实录与事后处置（观测 2026-09-28）

> **任务**：为②硬上限补"失控真实发生吗、怎么发现、怎么停、事后加了什么"——②的存在理由档案。

## Source 1 · cline/cline#3418 — 交互式 agent 无限循环烧钱

- URL：https://github.com/cline/cline/issues/3418 ；2025-05-09（05-12 维护者关闭，not_planned）；访问：2026-09-28（**主代理已复核标题/状态/正文开头**）
- 摘录：
  > "I am getting a constant infinite loop on cline - it doesn't matter what model I choose... It's burning credits like crazy... It is stuck constantly reading files. It never does the work... I have burned an excessive amount of cash trying to resolve this."
  > 跟帖："I did 'exit' on all my terminals and it finally started working again. Burned probably $50…"
  > 维护者（2025-05-12）："models getting confused when working on very large tasks and looping endlessly is a known issue, and unfortunately there isn't a simple fix. What tends to happen is the context fills up with too much instruction or intermediate output, and the model ends up repeating steps without forward progress..."
- 最小主张：交互式 agent 无限循环真实存在（约 $50 级损失）；**发现＝人盯着；停止＝手动杀终端**；维护者给出机制解释（上下文塞满→重复无前进）且当时无产品级修复。
- 不支持：金额为用户自报；not_planned 关闭，未见 cap 落地（2026-09-28 复查 auto-approve 文档仍只有按类别开关）。
- failure_mode: runaway-loop ＋ bill-shock；remediation: 无产品闸门，建议＝拆任务。

## Source 2 · claude-code#46787 — 僵尸循环穿透"关闭"动作（canonical）

- URL：https://github.com/anthropics/claude-code/issues/46787 ；2026-04-11（06-11 stale 关闭 not_planned；#57910 归并）；访问：2026-09-28（**主代理已复核标题与 31% 段**）
- 摘录：
  > "…a period during which I was asleep for 14 of those 25 hours… my account consumed **31% of my weekly usage limit** and **12% of the current 5-hour rate limit session** before I even opened a new terminal."
  > 根因自诊断："2 'ralph' automation loops (tmux sessions…) — I had explicitly turned these off days earlier, **but the kill did not propagate to the actual tmux sessions**"；"1 stuck --resume session... running since Thursday"；"53 orphaned headless Chromium browser processes... The oldest were 194 hours old (8+ days)"
  > "There is no built-in mechanism in Claude Code to detect or alert users about orphaned processes that are silently consuming their usage quota."
  > 自建补救："Built a session-start audit hook (process-audit.sh)… alerts me about stale Claude processes (>2h), tmux sessions, ralph loops, orphaned browsers (>6h), and stuck --resume sessions (>4h)"
- 最小主张：**zombie 循环能穿透用户的显式关闭**（kill 未传导到 tmux）；发现＝事后查用量面板；停止＝手动全杀；用户自建审计钩子兜底并向厂商要孤儿清理/心跳/超时。
- 不支持：Anthropic 未文字确认根因（仅 triage 标签 bug+area:cost）；#57910 的"清理后配额仍掉 ~2%"是另一用户的推断。
- failure_mode: zombie-cron；remediation: 用户侧审计钩子（阈值 2h/4h/6h 分级报警）。

## Source 3 · Reddit $6,000 帖（一手 403，媒体链转述）— 定时循环×缓存经济

- URL：https://www.reddit.com/r/ClaudeAI/comments/1t11mmy/...（403 不可达）；转述链 MakeUseOf→quasa.io；约 2026-05；访问：2026-09-28
- 摘录（转述，两源一致骨架）：30 分钟一次的 Claude Code 定时循环；上下文滚到 ~800k token；prompt cache TTL 5 分钟 < 循环间隔 → 每次全价重建缓存；"Anthropic's usage dashboard updates with a delay of several days... The first sign of trouble was the angry email about exceeded limits."
- 事后闸门（转述）：循环间隔 ≤ cache TTL；或每迭代开全新无状态会话。
- 最小主张：**调度式循环的费用失控机制**＝间隔×上下文增长×缓存计费的交互；发现通道是超限邮件（面板延迟数天被点名放大损失）。
- 不支持：$6,000、46/48 次等数字仅媒体级；两转述在任务内容上冲突（查更新 vs 扫 PR）。**引用只取骨架，不引具体金额**。
- failure_mode: bill-shock（机制性，非模型行为）；remediation: 间隔对齐缓存 TTL / 无状态会话 / 实时计数器。

## Source 4 · OpenRouter Doom-Loop Detection — 失控闸门的产品化梯子

- URL：https://openrouter.ai/docs/agent-sdk/call-model/doom-loop-detection ；living doc；访问：2026-09-28
- 摘录：
  > "It tries the same tool call, gets the same result, and tries again anyway… That's a doom loop: **the run keeps spending money without getting anywhere.**"
  > "It's off by default. Turn it on with doomLoop: true, // recommended defaults: observe@2, block@3, stop@6"
  > escalate 档："run the next turn on a stronger model... maxEscalations: 2, // spend cap for the whole conversation"
  > 边界自述："What this doesn't catch: Loops with changing inputs... Saying the same thing in different words"
- 最小主张：失控闸门已产品化为**五级动作梯子**（observe→steer→escalate→block→stop），阈值按重复次数计，动机明写"防止花钱无进展"；且诚实记录检测边界（变输入循环、同义复述漏检）。
- 不支持：非事故记录；默认关闭，不能证明普遍部署。
- 注：与②既有"拒绝计数熔断"（auto mode 3/20）同族但判据不同——这个按**重复动作模式**计，不按拒绝计。

## Source 5 · OpenHands PR#11799 — 默认开启的 stuck detector 与误报史

- URL：https://github.com/OpenHands/OpenHands/pull/11799 （2025-11-21 合并，维护者 Graham Neubig）＋ https://docs.openhands.dev/sdk/guides/agent-stuck-detector ；访问：2026-09-28（**主代理已复核 PR 标题与描述**）
- 摘录（PR）："This PR adds a new configuration option `enable_stuck_detection` to allow users to disable automatic loop/stuck detection... **defaults to True** for backward compatibility... In cases where the stuck detection is triggering false positives"
- 摘录（docs）："Repeating Action-Observation Cycles: The same action produces the same observation repeatedly (4+ times)… Agent Monologue: …(3+ messages)… Alternating Patterns: Two different action-observation pairs alternate in a ping-pong pattern (6+ cycles)… can automatically halt execution…"
- 最小主张：开源框架**默认开启**量化阈值的 stuck detector（4+/3+/6+），可自动 halt；后因长任务合法重复误报改为可配置——**闸门自身会误伤，需要调参**。
- 不支持：无事故回放数据；stuck detector 立项 issue 未追到。

## 判读

- **观察**：失控实录覆盖三种 failure_mode——runaway-loop（cline）、zombie-cron（#46787，穿透显式关闭）、bill-shock（$6k 帖，机制性）。**发现通道全是事后**（人盯着/面板延迟/超限邮件）；**停止全靠人肉**（杀终端/杀进程）；事后补的闸门两个层次：用户侧审计钩子（进程年龄阈值）与厂商侧重复模式检测（次数阈值＋动作梯子）。
- **推断（候选）**：②的工程要领不止"设个上限"——至少四件套：资源上限（已有档案）、**失控模式检测**（重复模式≠拒绝计数）、**孤儿清理/心跳**（进程层，防穿透关闭）、**花费可见性**（实时计数；面板延迟被点名放大事故）。闸门本身有误报率，需要调参与逃生口（isitdone 的 3 次放行、OpenHands 的可配置开关、OpenRouter 的 detect 边界自述同构）。
- **与现有材料关系**：给②补"存在理由"层（为什么要有上限）；OpenRouter/OpenHands 两家独立得出"重复模式检测＋分级动作"，与 auto mode 拒绝熔断（按拒绝计）互补不重复。

## 负结论与限制

- Anthropic 状态页 retry 风暴机制：只有镜像站错误率时间线，无机制文字（负结论）。
- Reddit 原帖全通道 403（old.reddit/.json、代理均拦）——数字不引。
- 独立"AI cron 忘关数周"一手博客未找到；aider#3614（本地小模型循环）无成本维度不计。
- Uber CTO 烧预算（Forbes 二转）：采用量超支≠循环失控，仅线索。
- Cline 事后按任务请求数上限：2026-09-28 查文档不存在，未确认。
