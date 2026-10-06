---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# chawla_koul — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Tisha Chawla & Susheem Koul · AIEWF 2026《Your Agent Failed in Prod. Good Luck Reproducing It.》（视频上传 2026-06-29）

- URL：https://ai.engineer/talks/Lc8zRh9muoY-your-agent-failed-in-prod-good-luck （curl 实取全文）
- 身份：页面无机构字段（同场另有其二人《FinOps for AI Agents》议题）——**仅作会议层样本**。
- **挂钩**：验证回路（可复现性缺失）＋无人值守运行（失控后取证）。
- 逐字摘录：

> "Instead of doing the math, the agent sells the raw number one thousand and dumps it straight into the quantity field… it sells one thousand shares instead. At a hundred and ninety bucks a share, a thousand dollar intent will become a hundred and ninety thousand dollars disaster… The API returned a clean two hundred OK in thirty milliseconds. Zero exceptions, zero alerts."
>（无人值守错单实录：一切监控绿灯、错单已成。）

> "The reflex here is to just turn the model temperature down to absolute zero… But that's a complete misconception. Setting the temperature to zero doesn't fix a broken reasoning path… temperature zero isn't even truly deterministic on a hardware level… The real culprit is batch variance here, because your request gets grouped with whatever else hits the server that millisecond."
>（temperature=0 迷思的四点拆解——采样确定性≠系统确定性。）

> "We've been asking the wrong question all along… The wrong question is, how do I make the model deterministic?"
- **最小主张**：agent 生产事故不可复现是常态；应记录"语义边界/执行包络"并重放状态转移，而不是追逐模型层确定性。
- **派别适配**：**怀疑票（工程实证向）**。
