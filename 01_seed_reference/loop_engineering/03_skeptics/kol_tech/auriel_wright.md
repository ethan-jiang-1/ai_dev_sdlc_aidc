---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# auriel_wright — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Auriel Wright——Harvard CS、YC W20 创始人；Google Brain（为 Search/Pixel/Waymo 供数的 ML 系统，NeurIPS 发表）→ Google DeepMind（Gemini RL/self-evolving systems 与后训练研究）；现为独立 AI builder／天使投资人／高管教练（旧金山＆亚特兰大，个人站自述）。（履历核：aurielws.github.io＋Latent Space，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察（一手来源已核）；第九轮（2026-10-07）补全推荐面节（见文末增量）。
### Auriel Wright（前 Gemini RL）《How to Stop Shipping Low-Quality RL Environments (with Examples)》（2026-06-05，Latent Space 客座文）

- URL：https://www.latent.space/p/bad-envs （curl 实取全文）
- 身份：前 Gemini RL 从业者（③弱——工程实践层样本）。
- **挂钩**：验证回路（reward hack 分类学）＋循环结构（训练环的 harness 质量）。
- 逐字摘录：
  - "Your broken harness is actively making the model worse."（副题原句。）
  - "Your reward function only checks whether tests pass, not whether the code is actually correct. The agent discovers it can hardcode expected outputs instead of solving the problem. Every test passes, the agent gets maximum reward… What the model ends up learning: 'Read the tests, hardcode the outputs, skip understanding the bug.'"（**reward hack 的 coding-agent 形态**：tests pass≠correct——与 SWE-Marathon "weak verifier becomes an attack surface"（中-7.2）互证。）
  - "In RL, you don't have a static dataset… Every action and every reward becomes a data point. A flaky harness systematically generates garbage data."
  - "Silent timeout defaults: Your harness silently returns a default value when an API call takes too long instead of throwing an error. The model learns that certain actions 'always succeed instantly' and never builds retry logic…"（**静默超时默认值**——与第五轮"默认态偏松"清单同族。）
  - "a well-built harness has clean signal… graceful degradation… and fail-fast behavior."
- **最小主张**：验证器质量是环的地基；"tests pass 即奖励"的弱 verifier 会被硬编码攻击直接打穿；fail-fast 应作为 harness 的设计公理而非默认配置。
- **派别适配**：**怀疑票（工程实证向）**——训练侧 harness 文，但其 verifier 弱点分类学对 loop 验证回路判读直接适用。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：Latent Space 客座文重取（全文非付费墙，fetch 成功）。本轮引句全部当日 fetch 逐字取得。

**官方分节名（关键节）**："Common Harness Errors Across Agentic Use Cases"／"Error Class 1: The Stale Cache"／"Error Class 2: The Reward Hack"／"Error Class 3: The False Resolution"／"More Harness Failures to Watch For"／"How to Minimize Harness Failures"（下分 "Know Your Model, Know Your Harness"／"Adopt Traditional Software Engineering Best Practices in Your RL Research"）／"Go Fix Your Janky Harness"。

## 处方面（好 harness 三性质＋5% 熔断改道判据）

**逐字摘录（均为仓库新引句）**：

> "From my experience a well-built harness has clean signal (every state is fresh, every reward matches reality), graceful degradation (bad episodes get flagged and excluded before they reach the gradient), and fail-fast behavior (something breaks, it throws immediately instead of silently corrupting data - you'd rather lose an episode than poison one)."
（**好 harness 三性质**：干净信号／优雅降级（坏 episode 进梯度前剔除）／fail-fast（宁丢一局不毒一局）。）

> "If your environment failure rate is above 5%, you don't have a model problem, you have a harness problem. Fix the harness first."
（**5% 判据**：环境失败率过线＝修 harness 先于修模型——把"怪模型还是怪回路"变成了可操作的分流规则。）

> "You learn to recognize these properties by spending time with your model - reviewing trajectories, building a failure taxonomy so you know whether a bad episode was a model failure or a harness failure."
（**方法**：复看轨迹＋建 failure taxonomy——区分模型失败与 harness 失败。）

> "Treat your training harness like your production one as much as you can. So if prod experiences 200 QPS on average, make sure your harness knows what that feels like without errors." ＋ "Treat the training harness as an extension of your actual product - with the same level of engineering quality you expect the model to see in production."
（**SE 实践移植**：训练 harness 当生产系统对待——流量画像、工程质量同标准。）

> "A good harness compounds: every clean episode builds on the last. A bad one compounds too, just in the wrong direction. The gap between teams that ship working harnesses and those that don't widens with every training run."
（**复利论**：好 harness 复利、坏 harness 负复利——团队差距随每轮训练拉大。）

- **诚实注记**：原文没有"每类 broken harness 对应修法"的 1:1 映射表——五类错误只有"现象→模型学到什么"因果链，修法收敛到三性质＋SE 两节；如需映射表只能标推断级。

## 本轮推荐面小结（一句）

替代方案＝**修 harness 先于修模型**（5% 失败率判据）＋三性质（clean signal/graceful degradation/fail-fast）＋failure taxonomy 方法＋把训练回路当生产系统做工程。

---

# 增量补挖（2026-10-07 goal 第二批·单点→稳定复核）

> 判定：**单点解除 → 稳定**（06-05 Latent Space 客座文 → ~09-07/08 howtoposttrain.com 系列同向：环境/verifier 真实性是地基，弱 verifier 被 hack／sandbagging 两向打穿）。
- ⚠️ 级别标注：第二时点日期为 sitemap lastmod 代理（非页面明示日期）；系列文的立场句与主档同族（环境真实性/弱 verifier 攻击面）。引句级细节见 .tmp-goal-movers/batch-E-residual.md（tmp 过渡）。
