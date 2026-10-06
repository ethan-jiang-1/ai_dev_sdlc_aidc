---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# dan_abramov — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：React 核心贡献者（Redux 创建者）
> **号召力**：④ 大分发＋① 框架定义者
> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：实践反思（过程叙事）
**起点**：实践者（Conway 猜想 vibe 证明）
**终点**：过程反思者（process theater 命名）
**弧线**：09-18《How I Vibed a Proof of Conway's Conjecture》——harness running for days、'process theater'、'nontechnical engineering manager rallying a talented but terribly distractable team'
**关键转折**：单点深观察——把 agent 协作比作非技术经理带天才团队，角色可被项目管理 agent 替代
### Source B · Dan Abramov ·《How I Vibed a Proof of Conway's Conjecture》（overreacted.io，2026-09-18）

- URL：https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/ （curl 实取，全文 117 段；页内日期 September 18, 2026）
- 身份：React 核心前成员，前端圈最高分发技术博客之一。
- 号召力口径：④。
- 逐字摘录（全部实取）：

> "It took me an entire month of my free time and a boatload of tokens, but I believe I've obtained a Lean proof of this conjecture posed by John Conway 50 years ago"
>（外行用 agent 一个月拿下 Conway 猜想 Lean 证明——"无人值守"叙事的极限案例；同文自我设限："My proof has not been independently verified by mathematicians."）

> "This let me keep the harness running for days. I didn't understand the math so I limited my involvement to poking the agents, asking what they were doing, and experimenting with their workflows."

> "I set up a 'cafeteria' agent that relayed every message it received to every other agent (emulating a group chat)."

> "I also kept an eye so they don't introduce 'process theater' with audits, as they liked to replace work with bureaucracy."
>（对多 agent 自组织的一手负样本：审计倾向滑向官僚化。）

> "In a sense, I felt like I'm a nontechnical engineering manager rallying a talented but terribly distractable team around a plan that they've promised me would work."

> "However, the models would repeatedly drift and fail to structure the engineering work, so in that sense the answer is no. That said, I believe my role could have been (better?) fulfilled by a dedicated agent that is taught to project-manage other agents, watch out for when they're spiraling or need to be poked."
>（对"人该不该在环上"的双向答案：既证明人可被替代，又实录 drift 失控——本项目"停止条件/外层调度"议题的一手民间数据点。）

- **最小主张**：无人值守多 agent 实验的完整一手复盘——可行性（存在性证明）与失控面（drift/官僚化/需人当"非技术工程经理"）同时入档。
- **派别适配**：**中性**（两面向全；"角色可被项目管理 agent 替代"半句同时是推动派引句）。

---

# 增量补挖（2026-10-07 第二轮：06-29/07-02 产品侧姿态＋10 月无新文确认）

> 通道：overreacted.io RSS＋HN（gaearon 作者检索，窗口内零提交零评论）＋arctic-shift Reddit（u/gaearon，React core team flair）＋nextjs.org 公告页全文。overreacted.io 09-18 Conway 猜想后**无新博文**（feed 全量核对）。X 连接失败＋登录墙、Bluesky API 两次超时，如实记录。增量发现：他未点名 loop engineering 运动，但在命名事件与 Claude Code 团队定义（06-30）之间，以 Next.js 团队成员身份转发推广 next-dev-loop Skill——以产品侧姿态实质接入同一实践方向。

## Next.js 16.3: AI Improvements —— Abramov 转发推广 next-dev-loop Skill（2026-06-29）

- URL：https://www.reddit.com/r/nextjs/comments/1uj3v4y/nextjs_163_ai_improvements/ （arctic-shift 存档确认其 r/nextjs 提交 2026-06-29T20:25:20Z；公告本体 https://nextjs.org/blog/next-16-3-ai-improvements 全文实取，缓存 abramov-nextjs-163-ai-improvements.txt）
- **与 loop engineering 的挂钩**：验证回路＋循环产品化机制——把"编辑→编译→浏览器运行时验证"的开发反馈回路做成给 coding agent 的一方 Skill；示例 prompt 即 Steinberger 式"设计 loop 驱动 agent"的粘贴即用形态。
- 逐字摘录（公告正文，原帖由 Aurora Scharff 与 Jude Gao 撰写——他的角色是放大推广而非亲笔，如实标注）：

> "The next-dev-loop Skill gives your coding agent access to the full development feedback loop. It can drive the browser, read the console, follow network requests, and inspect the React tree as it iterates."

> "After every edit, verify the page still works at runtime using the next-dev-loop skill."

> "The fix isn't verified until you've reloaded the route and looked at what renders."

> "The per-feature loop is the same in both: the Skill reads the actionable error, fetches the per-error docs page it links to, applies that fix to the route, then drives the browser through next-dev-loop to confirm the static shell renders the right content."
（"isn't verified until…"——修复的完成判据被写进 loop 本身：停止条件的产品化表述。）

- 立场：**支持（验证回路产品化，限自家产品语境）**。

## r/nextjs 评论：亲述以 Claude Code + Opus 4.8 试用官方 agent skills 成功（2026-07-02）

- URL：https://www.reddit.com/r/nextjs/comments/1ul9vt3/anyone_uses_cache_components/ov35bg8/ （arctic-shift 整帖评论检索实取，含父评论上下文，逐字核对；缓存 abramov-cc-thread.txt）
- **与 loop engineering 的挂钩**：循环产品化机制——把 agent 工具链（含 dev-loop skill 体系）当可诊断、可调优的工程对象。
- 逐字摘录：

> "I've tried our skills on a couple of projects and they worked fine, but it was with Opus 4.8 in Claude Code."

> "Which harness did you use and what was migrated incorrectly?"
（父评论抱怨"喂了全部 Next 文档链接 agent 仍迁移出错"，他回应亲试成功并追问 harness 与失败点——本人使用者立场锚点。）

- 立场：**支持（一线使用者证言）**。
