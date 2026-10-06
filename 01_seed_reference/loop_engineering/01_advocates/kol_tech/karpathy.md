---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# karpathy — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：前 OpenAI/Tesla AI 总监
> **号召力**：④＋① 教育领袖
> **人物全景**：[_raw_people/07_andrej_karpathy.md]()
> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：稳定推动（agent 管理视角持续）
**起点**：推动·管理层（interns 隐喻）
**终点**：推动·管理层（remove yourself as the bottleneck，但该句仍仅存转引）
**弧线**：04-30 bearblog（'agents are like interns. You still have to be in charge of aesthetics, judgment, taste, and oversight'）→ autoresearch README（bottleneck 自我定位）
**关键转折**：无转折——一致认为人应管判断/品味，agent 管执行
## Andrej Karpathy · autoresearch / "remove yourself as the bottleneck"（2026，一手未取得）

- URL：GitHub https://github.com/karpathy/autoresearch（未直接取得）；演讲稿 https://karpathy.bearblog.dev/sequoia-ascent-2026/ （Cloudflare 拦截，403 未取得）；其言论经两路转引：swyx loopcraft 原文（S1 镜像，逐字转录其 Autoresearch 视频言论）与 All Things Open 文（转述 autoresearch 规模：约 630 行 Python、单 GPU 过夜跑 50 个实验、"数周内积累 59,000 stars"）｜ 作者身份：Andrej Karpathy，Eureka Labs 创始人、前 OpenAI/Tesla AI 总监
- 来源类型：**一手未取得**；两条独立二手（swyx 逐字转录＋ATO 转述）
- 号召力口径：①＋④（autoresearch 被广泛当作 system loop/自改循环的 canonical 例——Voss 分类学、ATO 教程文均引用）

**逐字摘录**（经 swyx loopcraft 原文转录其视频言论——**经转录，非本人页面**）：

> "To get the most out of the tools that have become available now you have to remove yourself as the bottleneck. You cant be there to prompt the next thing. You need to take yourself outside. You have to arrange things such that theyre completely autonomous… the name of the game now is to increase your leverage. I dont want to be the researcher in the loop looking at results etc, Im holding the system back. So the question is how do I refactor all the abstractions so that Im not… I have to arrange it once and hit go."
>（"把自己移出瓶颈、安排成完全自主、安排一次就按 go"——Karpathy 版的循环纲领，比 Osmani 教程口径更彻底。）

- LangChain 官方博客亦将其 YouTube（kwSVtQ7dziU）与 Steipete、Boris 并列为 "AI leaders… have all arrived at the same conclusion: the potential in agents is in the loops you build around them"——**Karpathy 被多方计为同结论领袖**。

**该条支持的最小主张**：Karpathy 2026 年以 autoresearch 实践与"移出瓶颈"言论被多方（LangChain、swyx、ATO）计为循环运动同路人；其本人一手页面在本环境均不可达。
**派别适配**：**推动票候选（降级）**——言论经两路独立转引一致，但本人一手未取得；入册建议标"经转引"，或待 bearblog/GitHub 再回源后升格。

---

## Andrej Karpathy —— 部分解决·强（bearblog＋autoresearch README 两个本人一手载体全文取得）

- URL/日期：① https://karpathy.bearblog.dev/sequoia-ascent-2026/ 《Sequoia Ascent 2026 summary》（curl＋浏览器 UA 实取全文——上轮 403 系 fetch 代理层问题），帖子日期 **2026-04-30**；② https://raw.githubusercontent.com/karpathy/autoresearch/228791fb499afffb54b46200aca536f79142f117/README.md （curl 实取，8KB；github.com/karpathy/autoresearch 的固定 commit）。
- ①的性质（本人声明，逐字）："I fed an LLM all of my recent blog posts and tweets, then I had it read this video's transcript and produce 1) a summary and 2) a cleaned up transcript… AI generated content below for this talk follows."——**本人发布、LLM 清理的本人讲座文本**（Sequoia Ascent 2026 对谈 Stephanie Zhan；按"本人一手·AI 清理转写"计，引用注明）。
- 逐字摘录（①，Edited transcript 部分为其讲话）：

> "Right now the agents are like interns. You still have to be in charge of aesthetics, judgment, taste, and oversight."

> "People have to be in charge of the spec and plan. … You are in charge of oversight and the top-level categories. The agents do much of the work underneath."

> "Vibe coding raises the floor. Agentic engineering is about extrapolating the ceiling."（summary 部分同义展开："Agentic engineering raises the ceiling. It is the professional discipline of coordinating fallible agents while preserving correctness, security, taste, and maintainability."）

> "I am becoming the bottleneck of even knowing what we are trying to build, why it is worth doing, and how to direct my agents."＋"Understanding is still the bottleneck because you cannot be a good director if you do not understand."

- 逐字摘录（②README，autoresearch 本体）：

> "give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved, keeps or discards, and repeats. You wake up in the morning to a log of experiments and (hopefully) a better model."

> "you're not touching any of the Python files like you normally would as a researcher. Instead, you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org."

> "you can expect approx 12 experiments/hour and approx 100 experiments while you sleep."

- 附带：README 文内挂本人两条 X 帖 ID（`x.com/karpathy/status/2029701092347630069` 与 `…/2031135152349524125`，X 本体不可达，ID 已登记供后续回源）。
- 边界如实记录：**"remove yourself as the bottleneck" 逐字句本身仍未在本人一手载体中出现**——它仍只存在于 swyx loopcraft 的视频转录（S1，经转录标注不变）；本轮到手的是语义同构但措辞不同的一手表述（"I am becoming the bottleneck…"/"arrange it once and hit go" 语族的近邻）。
- 状态：**部分解决·强**（上轮 bearblog 403＋GitHub 未取得 → 本轮两个一手载体全文到手）。
- **派别适配**：**推动票（实践者）升格**——不再纯"降级候选"；其一手文本同时把"spec/oversight/品味不可外包"写入，判派按推动派＋理解/品味 nuance 照记。
