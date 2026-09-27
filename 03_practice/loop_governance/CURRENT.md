# 当前状态（热区）

> 最近一次更新：**2026-09-27（deck 两场收口）**：backbone 与 manual 的确认不变。deck 两场——`intro/`（入门场 19 页）与 `advanced/`（技术产品场 27 页）——经四轮反馈打磨（三档格式、场别命名、难点页 callout、术语中英对照）后，2026-09-27 用户收口。原统一稿已迁入两场并按用户决定移除。没有回改本目录正文。

## 一句话

**立题初稿已确认通过**：backbone 与 manual 可用。研究层 [`landscape.md`](../../02_research/ai_loop_engineering/result/landscape.md) 已入层。deck 只写叙事：大纲与文稿主张句已对齐，画面与 PPTX 已删除。

## 状态

| 件 | 状态 |
|---|---|
| `README.md` | ✅ 定位 / 命名理由 / 分工边界 / 信息流 / 核心结论速览 |
| `result/backbone.md` | ✅ §0–§6 七节——**2026-09-27 用户确认通过** |
| `result/README.md` | ✅ 入层判据 |
| `result/manual.md` | ✅ 12 节——**2026-09-27 用户确认通过** |
| 证据层 | ✅ 循环机制见 [`ai_loop_engineering`](../../02_research/ai_loop_engineering/README.md)；控制接口见 [`agent_goal_eval`](../../02_research/agent_goal_eval/digested/README.md) |
| deck | 两场分稿已收口（2026-09-27）：`intro/` 入门场 19 页、`advanced/` 技术产品场 27 页，主张句与各自大纲对齐，每页三档上屏＋难点页 callout＋术语中英对照；原统一稿已迁入两场并移除。画面与 PPTX 已删除 |

## 下一步

1. **deck 两场已收口（2026-09-27）。** 入门场 `intro/` 19 页、技术产品场 `advanced/` 27 页，主张句与各自文稿对齐，四轴与红线自查通过。内容冻结：后续只按用户明确要求改。做片交由下游 agent（读各场 manuscript-*.md）。改动未提交，提交与否由用户定。
2. 研究层遗留（不阻塞 deck，登记在研究层 CURRENT）：Unrolling 候选 403 / 归属修正 / Morris 四级。

## 缺口（backbone 登记的两项开放缺口 + 两项附加）

1. **量化自主度分档＝0 一手来源**（backbone §3 登记的开放缺口①）——只能给位置不给刻度；若后续出现轮次判据的一手源，回研究层补档再升主干。
2. **跨 feature 在途可见性**（backbone §2 开放缺口②）——手册 §5 给出受限工作行试点，但已复核材料没有证明统一控制面成型；先观察交接漏项与维护成本，再决定是否推广。
3. **行为面与外部结果仍有盲区**：§4/手册 §10 的删测、越界功能、未解释失败核对不能证明“该做的事都做了”；外部业务结果无观测时保留待人判/待观测，不把产出完成伪装为业务成功。两类操作分流都没有效果对照。
4. DSH 侧的 goal/plan 机制是本主题控制轴的一个**第一方实例候选**（姊妹仓 FAQ 15 的 owner 四仓案例），但那是外部研究——若要引用须走本仓研究层回源流程。

## 铁律速记

- **证据权威在对应研究主题**：循环机制来自 [`ai_loop_engineering`](../../02_research/ai_loop_engineering/README.md)；goal/eval 条件和裁判分歧来自 [`agent_goal_eval`](../../02_research/agent_goal_eval/README.md)。F 的未合并 PR/单用户报告只作反例，I 的个人案例不作效果证据，I2 侦察与 K 候选不入规程；goal/eval 的单人观察与单源 FAQ 不作通用效果结论。
- **result 层语义命名、无序号**；主干结论改动 → 反向同步研究层 digested。
- **未回源的东西不上主干**（`⏳ 待回源` 只能出现在研究层的线索区）。
