# R1 授权执行（正式阶）——交出单轮内的工具与命令执行权

> **交接面**：人不再逐句批准"能不能跑这条命令/改这个文件"，改为一次性划定**授权面**（允许哪些工具、哪些命令模式），
> 循环在面内自主、面外拒绝或升级。人保留的东西：授权面本身＋机器可核判据（测试门）。

## 一、定义（跨源最小交集）

循环在**一轮之内**可以自主调用工具、执行命令、读写文件；失败自动重试；人的介入点从"每次动作"后移到"授权规则"。

## 二、支撑条目（自说明）

**① Anthropic（deny-and-continue 授权语义）** ⏳ 逐字待补
- 出处：auto mode / Claude Code docs（已回源，锚 [evidence-b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) / evidence-c）
- 要点：面外动作不中断循环，拒绝并继续（deny-and-continue），拒绝计数累积触发熔断（3/20 口径，转述自台账 `anthropic_org` 行）
- 逐字摘录待补齐后此条才可外引。

**② Cursor 设置面（Run Mode / Auto review / Command Allowlist / File Deletion Protection）** ⏳ 官方一手待回源
- 现状：仅有中文传播层转述（[evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) §2，侦察级）：
  > "在Command Allowlist里添加NPM test、NPM run build ptest等常用命令，开启File Deletion Protection防止自动删文件。
  > 日常开发用Auto review或Allowlist with Sandbox就够了。Run Everything只在demo或小项目里用。"
- **回源队列 #2**：官方 docs 核实设置名与语义后升条目；顺带核销 evidence-t §1 讹变表。

**③ 本仓自证（DSH 授权面即此阶实现）**——指针：[evidence-g](../raw/evidence-2026-09-27-g-dsh-control-surface.md)（沙箱模式/审批策略即 R1 授权面的运行实例）。

## 三、反例位

- 授权面过大＝R1 直接升级成事故面：失控实录三案（practices ②，[stop_conditions](../stop_conditions/README.md)）里有命令级越权案例 ⏳ 引句待搬。
- "Run Everything 只在 demo 用"——中文传播层与 Anthropic 分档口径同构（evidence-t §3），升阶前先核对官方原文。

## 四、升 R2 的闸门

单轮授权跑顺后，瓶颈移到"每轮都要人来判停/续"——此时需要**可观察的完成条件**（机器闸门 ①）与
**验收分离**（③）才能把"判停权"交出去。停止条件三件的对应做法在
[`stop_conditions/01_machine_gates/`](../stop_conditions/01_machine_gates/README.md) 与 [`03_verdict_split/`](../stop_conditions/03_verdict_split/README.md)，不复制。
