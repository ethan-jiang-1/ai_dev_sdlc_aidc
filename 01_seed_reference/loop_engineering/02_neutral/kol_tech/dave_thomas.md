---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-07
---

# dave_thomas — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：《Pragmatic Programmer》共同作者；Pragmatic Bookshelf 创始人
> **背景**：Dave Thomas——agile 元老（Agile 宣言签署人）；pragdave.me 自建博客已停更（末篇 2024-09-26），活跃阵地在 Substack（articles.pragdave.me）。**本档为 2026-10-07 agile 元老专项新建**。（履历核：pragdave.me＋articles.pragdave.me，2026-10-07）
> **号召力**：①＋②＋④（agile 元老·行业级作者）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)
> 人群类型：**专业技术 KOL**（程序员/工程师出身）
> 词表注记：窗口内未用 "loop engineering" 一词——直接以"loop/无人值守"为批评对象。

## 态度轨迹

**方向**：个人乐趣正面 → **无人值守 loop 强警告** → 组织层面条件推动（**滑动者**）
**起点**：+1 偏推动（06-02 "Coding with AI is fun"）
**终点**：−1 偏怀疑（07-21 "Be a Luddite" 点名否定无人值守长循环）
**弧线**：06-02 Castles In The Air → 07-02 Clean Code is Good For AIs → 07-21 Be a Luddite
**关键转折**：07-21——逐字点名"36 小时 loop 产出 200 万行"流派并要求"回到现实"

## 《Castles In The Air》（articles.pragdave.me，2026-06-02）

- URL：https://articles.pragdave.me/p/castles-in-the-air ｜ fetch 成功
- **挂钩**：循环结构（反馈回路）＋验证回路（约束 hack 倾向）。

**逐字摘录**：

> "I was expecting to hate using Claude... I was wrong. Coding with AI is fun."＋"AI shortens the feedback loop: dramatically."

> "When it does, I know I need to be strict to stop it just hacking solutions, but that's way less effort than rolling back a week."
（起点即带纪律——验证回路雏形。）

## 《Be a Luddite》（2026-07-21）——本批最重：点名否定无人值守长循环

- URL：https://articles.pragdave.me/p/be-a-luddite ｜ fetch 成功
- **挂钩**：无人值守运行（点名）＋循环结构/停止条件（人在环）。

**逐字摘录**：

> "if you're in the 'my loop ran for 36 hours and produced 2 million lines of working code' school, then I'd ask you to come back to reality."
（**逐字点名无人值守长循环流派**——要求"回到现实"。）

> "Your role with AI is not to give it a goal and then get on with something else; that's exactly why Big Design Up Fact never really worked. Code isn't written from a spec, it evolves as we learn stuff along the way."
（**直接否定 goal-and-leave 式循环**：把 BDUF 失败史类推到"给目标就走人"——人必须在环。）

> "No AI is currently capable of keeping even a medium sized application all in context... the AIs will become increasingly less effective at maintaining it."
（TCO 陷阱——审慎的量化理由。）

- 副题："Successful organizations know that developer experience is an essential factor when AIs write code, and structure their teams accordingly."（组织层面条件推动）
- 辅证：07-02《Clean Code is Good For AIs, Too》（索引级，全文未取）。
- 谱系背景（窗口外）：Dev Life S5 E13 播客 2026-02-16（Orient-Step-Learn 框架）。
- 交叉：Fowler Fragments 06-16 转述其"乐趣"帖（martin_fowler.md）。

**判定**：**弧线（+1→−1）**——从"乐趣＋反馈回路缩短"滑到"无人值守长循环回到现实"；方向＝**对无人值守的清醒，不是对 agent 的拒绝**（组织层面仍条件推动）。滑动归因：概念的产品化叙事（36h/2M 行）与他的一线体感相撞。
**派别适配**：**滑动票（终点偏怀疑·无人值守轴）**——camp 归中性派（条件推动整体框架），跨带滑动按 DHH 先例保留轨迹。
