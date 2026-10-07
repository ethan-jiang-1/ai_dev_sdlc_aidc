---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# dex_horthy — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：HumanLayer CEO；12-factor agents 作者
> **背景**：Dex Horthy——物理本科出身；Sprout Social 早期工程师 → Replicated 约 7 年（容器编排/产品/GTM）→ Metalytics（SQL 数仓 agent 实验，HumanLayer 前身）→ 创办 HumanLayer（YC）；《12-factor agents》作者（2025，agent 工程方法论）；bio 自称 “context engineering” 造词人；以“反对自由 loop until goal、在工具选定与执行之间打断”著称（evidence-i Source 2）。（履历核：YC 页＋humanlayer GitHub，2026-10-07）
> **号召力**：①＋②
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Source C · Dex Horthy（HumanLayer CEO）· AIEWF "great loops debate" 反方＋播客长访谈（2026-07-02 / 08-13）

- C1（经现场稿转述）：https://www.latent.space/p/aiewf-daily-dispatch-locomotives （Richard MacManus，07-03，curl 实取）：
  > "The basic take here is not whether loops are good or bad…Kubernetes is actually built on loops — built on control loops. But they're deterministic loops."
  > "the hype is outrunning the discipline."
  > "I haven't seen proof that we are at a point where we can just step up an abstraction level…I actually think we need to step down an abstraction level, if anything."
  > （软件工厂段落）"you never touch the problem"——建议"build up intuition"、从小 loop 迭代起步而非端到端自动化。
- C2（主持人页内 pull quotes＋全 transcript 在页）：The Weekly Dev's Brew Ep21《What Actually Gets You 2-3x With AI Coding》（2026-08-13，https://www.wordman.dev/podcast/dex-horthy-what-actually-gets-you-2-3x-with-ai-coding/ ，curl 实取）：
  > "You can get 99% of human-quality code, like very good code as if you had written every character by hand, but two to three times faster. You can't get 10x. It can't be done. Not today."
  > "I don't give two damns how your spec is shaped. It should give you leverage."
  > "I think abandoning code quality and system quality, giving engineers permission to ship slop, I don't think that's correct. I think that's going to collapse your codebase into ash much faster than you think."
  > "If you're a manager and you are not trying to help your people adopt AI, you are failing them."
  - 章节含 **"1:14:01 · Vibe coding vs production loops"**；官方 Key Takeaways 含 "Kill a session when the model starts flailing on tests."；Mentioned 清单含 **"Addy Osmani on Loop Engineering"**（其单集官方页面即在引用在册 KOL 的 loop engineering 内容——传播链证据）。
- 身份：HumanLayer CEO/联创；页面 bio 称其 "coined 'context engineering'"，12-Factor Agents 作者。
- 号召力口径：②＋③＋④（AIEWF 主舞台辩手＋头部 newsletter 生态人物）。
- **最小主张**：反的是"无纪律 loop 的 hyper"，不是 loop 本身；生产语境天花板 2-3x；review 是瓶颈、人的时间应花在设计与拆解上。
- **派别适配**：**中性**（辩论反方席但自述 "not anti-loops"——教科书式中性席位）。

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核）

> 判定：**单点解除 → 稳定**——四个窗口内时点同向；07-23 演讲把论证升级到新层。

## AI Engineer 演讲《Why coding agents keep making your codebase worse》（2026-07-23；⚠️ 引句为 ai-wiki 时间戳摘要转引，非官方逐字稿）

- URL：https://podcasts.apple.com/ca/podcast/why-coding-agents-keep-making-your-codebase-worse/id1572440477?i=1000792424627
- 转引（⚠️ 标注）：

> "no amount of harness engineering or loops maxing can solve what is fundamentally a model training issue"
（**论证升级**：从"反自由循环"到 RL reward shape 根因论——同时自曝 HumanLayer lights-off 实跑失败。）

## Beyond Coding ep270（2026-09-30，官方页章节题同向）

- 章节题："Why 2-4x productivity beats chasing 100x"／"dark factories"
（**2-4x 现实主义**——与怀疑派 Arcolano 的衰减曲线同向的推动侧口径。）
