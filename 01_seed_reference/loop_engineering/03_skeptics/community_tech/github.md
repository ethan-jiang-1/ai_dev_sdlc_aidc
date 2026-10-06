# github — community_tech（专业程序员群众）·怀疑向

> 非 KOL：一般开发者体感。派别判定权威：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。只收 2026-06 后。

## 二、GitHub：故障清单（官方仓库社区反馈）

> 观察：单个 issue 的 👍 普遍 ≤11——社区痛感体现在 issue 数量与复述里，而非表情反应；抽样 issue 厂商回复率极低（12 个仅 2 处）。

| Issue | 日期 / 状态 | 故障要点 |
|---|---|---|
| claude-code **#68619**（本批最高反应 👍11/34c） | 06-15 open | **"权限拒绝应停止分支，却成了继续繁殖的触发器"**："Permission denials trigger further agent spawning instead of stopping..."（"a permission denial appears to be acting as a spawn trigger rather than a stop condition. That's not really a tuning issue."—— hiwasham） |
| claude-code **#93744** | 09-11 open | /goal 停止条件评估器**读不到 goal 本体**（信息隔离）——无人值守会话被打断 9 次，末段产出为零 |
| claude-code **#98066** | 09-29 open | **/goal × auto mode 互锁**：Stop hook 被审批器拒绝后重触发 ~15 次死循环——推动派两大特性组合即锁死 |
| claude-code **#98708** | 10-01 open | 20 子代理＋/goal＋Stop hook 下**"停止"动词本身失效**（同一句 stop 发了几十次），唯一停法是关 VS Code 窗口；且停止后已调度脚本仍触达生产系统 |
| claude-code #90664 | 08-30 open | 普通用户视角：agent 自主扩大搜索规模→5 小时配额烧尽，"awful experience" |
| codex **#32389**（库内已知，实取核实） | 07-11 open | **假 stop 信号**：HTTP 200/stopReason 'stop' 但零文本——停止条件不止"停不下来"，还有"假停" |
| codex **#37304** | 08-06 open | Goal 恢复即死循环烧配额（隔月仍可复现）："Ideally Codex should detect loops like this to prevent wasting tokens!" |
| codex #48091 | 09-25 open | "sure to be sure" 自我确认空转循环（仅标题级） |

**厂商声音**（非社区情绪、非 KOL 证据）：
1. **anthropics/claude-code #73307**：COLLABORATOR bcherny（Boris Cherny）确认**尚无通用 loop-detection 权限门**，只列举局部护栏（子代理 spawn 上限、`--max-budget-usd` 硬预算）——厂商承认缺口存在。
2. **anomalyco/opencode #45379→#49866**：内置自主 /goal 命令 **23 天后被维护者 dax 整体 revert**（"Reverts 5464aa4... in full"，无公开理由；配套 #48239：stop 按钮停不下循环）——对"自主 loop 应内置于主流工具"最强的**行动级反证**。
