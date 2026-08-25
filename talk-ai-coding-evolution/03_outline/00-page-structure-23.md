# Talk 页面结构（现场版 · 23 页 · 45 min）

> **现场版**：P1–P23，目标 45 min、硬上限 50。每页只列**必讲要点**（1–2 个），完整素材在各幕内容文件里。
> 27 页版（`01-page-structure.md`）降为全素材索引。**无 demo。**

## 开场（3.5 min）

| 页 | 内容 | 时间 | 必讲要点 |
|---|---|---|---|
| P1 | 封面 | 0.5 | 题目 + 开场问题：一个人该把 AI Coding 掌握到多深？ |
| P2 | 钩子 | 1.5 | 你的角色一直在变：说话者→策展者→环境工程师→控制流作者→编排者；Cherny 金句"My job is to write loops"；"你不是在追新工具，是被往上推" |
| P3 | 路线图 | 1.5 | 四站：五层 → 为什么根本是 harness → 固定 vs 灵活 → DSH |

## 第一幕 · 五层演变（12 min）

| 页 | 内容 | 时间 | 必讲要点 |
|---|---|---|---|
| P4 | 发动机 | 2 | 一个原因五层结果：模型越强→杠杆点上移；METR 7 个月翻倍 + "prompt 措辞越来越不重要"；叠加不是替代 |
| P5 | Prompt + Context | 3 | 说话者→策展者；prompt 是行为控制面；context rot"塞得越多记得越差"；MCP/RAG 是生态事件 |
| P6 | Harness（埋雷） | 2.5 | Agent = Model + Harness；**埋雷：单次运行容器**（loop/graph 都实例化它） |
| P7 | Loop + Graph | 2.5 | 控制流作者 + 编排者；黄金法则；反转（blast radius / 不是新东西 / 术语先于发布）；叙事期 |
| P8 | 叠加观 + 成熟度 | 2 | 扳手/螺丝刀；成熟度标尺；今天重仓 1–3 层；引向"承重墙" |

## 第二幕 · 根本还是 harness（10 min）

| 页 | 内容 | 时间 | 必讲要点 |
|---|---|---|---|
| P9 | 转折 | 1 | 五层讲完，根本还是 harness；口径：我们的判断，三线撑（结构/哲学/风险） |
| P10 | 定义 | 1.5 | Agent = Model + Harness；"The agent has a prompt, a Bash Tool, and an Edit Tool." |
| P11 | 两套控制 + 确定/概率 | 3 | Guides/Sensors（教小孩做菜）；comp vs infer（npm test vs AI 说不错）；确定性优先 |
| P12 | 圈住 / 拦住 / 看清 | 2.5 | 模型给能力，harness 给可靠性；三个动词收束 |
| P13 | 承重墙 | 1 | 结构线（one floor above / engine & pilot）+ 哲学线（GraphARC 门禁）+ "假设下层正确是 bug 的来源" |
| P14 | 2026 CVE | 1 | 执行时授权缺失；authorize at execution；对一人公司的意义 |

## 第三幕 · 固定 vs 灵活（8.5 min）

| 页 | 内容 | 时间 | 必讲要点 |
|---|---|---|---|
| P15 | 抉择 | 1 | 不是"自己做 vs 现成"，是"固定 vs 灵活"；精装公寓比喻 |
| P16 | 固定的好 | 2 | 组件随产品交付（民主化）；沙箱/权限/观测开箱即用；Start with the simplest viable system |
| P17 | 固定的卡 | 3 | 想改 harness 本身：挂模型/工具/换后端/skill/knowledge map 受限；改不了内核只能等厂商；context rot 佐证 |
| P18 | 本质 | 2.5 | 不是别用现成，是别只能现成；装自己的 + 借现成的 |

## 第四幕 · DSH（5 min）

| 页 | 内容 | 时间 | 必讲要点 |
|---|---|---|---|
| P19 | DSH | 1 | 无特权内核："extend by mounting a plugin beside the others"；能改 harness 本身 |
| P20 | 双向灵活 | 2.5 | 装自己的（挂模型 ctx.llm / 挂工具 ctx.tools / 换后端 seam / skill / knowledge map，"都不必改 loop"）+ 借现成的（15 行 YAML 挂 vendor） |
| P21 | 哲学 | 1.5 | "Agents follow enforced gates far more reliably than prose conventions." + GraphARC 同套；自己定义门禁、机器执行 |

## 收尾（2 min）

| 页 | 内容 | 时间 | 必讲要点 |
|---|---|---|---|
| P22 | 回答 + 带走一句 | 2 | 角色表回扣（一人公司 = 被同一人承担五角色）；掌握到 harness 层，不用从零造但要能改；**装自己的，借现成的** |
| P23 | Q&A | 2 | 预埋三问：Loop/Graph 是炒作吗？现成何时够用？DSH 怎么上手？ |

## 时间账

```
开场 3.5 + 第一幕 12 + 第二幕 10 + 第三幕 8.5 + 第四幕 5 + 收尾 2 = 41 内容
+ Q&A 2 + 弹性 2 = 45（硬上限 50）
```

## 剪枝点（超时安全网）

- **必讲，不能砍**：P2 钩子 / P6 埋雷 / P9–P12 第二幕核心 / P15–P18 / P19–P21 / P22 slogan
- **可压可砍（砍了故事不断）**：P4 数字只留一句 / P5 细节 / P7 细节 / P8 压缩 / P14 CVE 压成一句 / P13 细节

## 素材来源

- 各幕内容文件：`02-act2-harness-content.md`（P9–P14）、`03-act3-flexibility-content.md`（P15–P18）、`04-act4-dsh-content.md`（P19–P23）、`05-opening-and-act1-content.md`（P1–P8）
- 素材/口径红线：`../02_evidence/00-absorption-plan.md`
