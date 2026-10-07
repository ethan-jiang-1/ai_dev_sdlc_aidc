---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# paul_bakaus — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Paul Bakaus——jQuery UI 创建者（2007，后成 jQuery 核心团队）；Aves 游戏引擎（公司被 Zynga 收购）；Google 2013–2021（Chrome DevTools → AMP/Web Stories DevRel 负责人——非 AMP 创造者；创办 Google for Creators）；后 Koji → Spotter EVP → 独立顾问；2026-07 创办 Renaissance Geek（a16z 领投；Impeccable 即其开源设计 skills 系统）。（履历核：paulbakaus.com/about＋ai.engineer，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察（一手来源已核）；第九轮（2026-10-07）补全推荐面节（见文末增量）。
### Paul Bakaus（Impeccable 作者，前 Google DevRel）· Latent Space 访谈《Skill engineering and the case against one-shot AI design》（2026-07-02）

- URL：https://www.latent.space/p/skill-engineering-design （curl 实取全文；同日 AIEWF 现场报道 aiewf-daily-dispatch-agency 互证，https://www.latent.space/p/aiewf-daily-dispatch-agency 全文实取）
- 身份：Impeccable（开源设计 skills 系统）作者（③＋④弱中）。
- **挂钩**：停止条件（人审位作为产品原则）＋循环产品化机制（对"循环即终局"的正面反驳）。
- 逐字摘录：
  - "He sees two dominant camps: people trying to preserve the traditional Figma-centered workflow, and on the other side advocates of 'loopmaxxing' who want agents to work with as little human intervention as possible. 'The truth is somewhere in the middle,' he said."（**"loopmaxxing"作为贬义标签进入访谈层**——与 "tokenmaxxing"/"benchmaxxing" 同族词。）
  - "There is no auto," he said, "and there will be no auto."（**产品化拒绝 auto**——与 Microsoft《Don't Let the LLM Drive》（疑-6）跨场互证。）
  - "Asked about the language of software factories and other visions that appear to remove people from engineering altogether, his response was unambiguous. 'I'm squarely against that.'"
  - 现场报道档实录："His goal is to let agents handle the laborious first 80% of the work, before bringing the human back in 'for the last 20% to make it a unique thing — to really put in your taste, your point of view.'"（80/20 分工＝停止条件的具体化。）
  - "It's never going to be a tool for one-shot design. That's not the intent."
- **最小主张**：工具作者开始把"拒绝全自动"写成产品原则（no auto as a feature）；对 software factory 叙事出现阵营内明确的立场反对。
- **派别适配**：**怀疑票（立场向）**——注意其承认前 80% 交 agent，判读时与全盘否定区分。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：Latent Space 访谈页重取（fetch 成功）。**形态注意**：记者文（Richard MacManus）——带引号句为直接引语可逐字；其余为记者转述，引用须标〔转述〕。

## 处方面（skill engineering 的替代路径）

**逐字摘录（新增，均为仓库新引句）**：

> "The point is to give you a way to steer what you want to end up with… It's never going to be a tool for one-shot design. That's not the intent."
（工具目的＝**steering** 而非 one-shot——skill 是给人插进控制点用的。）

> "An adjective with nothing behind it is just a nice apostrophe," Bakaus said. "You really have to tell the agent what you mean."
（**skill 灌义处方**：形容词背后没有可操作定义就只是撇号——必须把"你到底要什么"灌进 skill。）

> "People need purpose, and they want to play a role in whatever they create… When you work with the agent, then you feel more ownership of the product."
（**为什么人必须留在环内**：目的感与所有权——替代方案的动机层。）

> "Designers are moving into code, engineers are moving into design, and vice versa… These worlds are all colliding." ＋ "Designers all have to move one layer up the stack to think more about the what."
（**角色上移**：设计者进码、工程师进设计——人往上走一层管"what"。）

> "One of the interesting topics was that most skills — [and] most models — are not very creative. They converge in one direction, and if everybody uses the same skill to do frontend design work or something like that, everything ends up looking the same."
（**反创造性收敛**：同 skill 全员用＝万物趋同——"no auto"的审美论据。）

**〔转述〕处方面（须标注非逐字）**：80/20 分工（AI 前 80%，人拥有 taste/context 的后 20%）；"insert the person at the point where their judgment is most valuable"（把人插在判断最值钱处）；skill 内 MoE 式路由（省 token 提效果）；跨 harness skill "cannot assume they all provide identical capabilities"；live mode＝chat＋直接视觉操纵之间的 "design harness"。

## 本轮推荐面小结（一句）

替代方案＝**skill engineering 路线**：专家词汇灌义进 skill＋skill 内路由＋跨 harness 不假设等能力＋人插在判断最值钱的那一步（先 80 后 20）＋永不做 auto。
