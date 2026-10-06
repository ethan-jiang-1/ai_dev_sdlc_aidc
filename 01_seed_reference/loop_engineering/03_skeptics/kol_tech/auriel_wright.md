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

**状态**：单点观察——待补挖。
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
