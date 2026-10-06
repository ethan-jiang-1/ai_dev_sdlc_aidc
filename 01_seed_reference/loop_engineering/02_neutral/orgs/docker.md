# docker — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第六轮挖掘（2026-10-06）：播客层第二轮）**

### 中-14 · Mark Cavage（Docker President/COO）· Software Engineering Daily #1952《Docker and Sandboxing AI Agents》（2026-07-30，官方 transcript .txt 实取）＋ Andrew Barba & Shar Dara（Vercel）#1967《Scaling Agent Workloads at Vercel》（2026-09-17，官方 transcript .txt 实取）

- URL：https://softwareengineeringdaily.com/podcasts/docker-and-sandboxing-ai-agents/ ；transcript https://softwareengineeringdaily.com/wp-content/uploads/2026/07/SED1952-Docker-2026.txt ｜ https://softwareengineeringdaily.com/podcasts/scaling-agent-workloads-at-vercel/ ；transcript https://softwareengineeringdaily.com/wp-content/uploads/2026/09/SED1967-Shar-Dara-Andrew-Barba.txt （均 curl 实取）
- **挂钩**：循环结构（环境层：沙箱与多租 harness 基建）。
- 逐字摘录：
  - Cavage："the most useful coding agents can mutate their environments by downloading packages, writing files, and connecting to services across the network. However, that freedom also presents dangers… Docker Sandboxes, which gives each agent its own isolated microVM… A standard container shares the host's kernel, but a microVM emulates hardware and runs its own kernel, giving a stronger security boundary around code that cannot be trusted."（**"agent 打破容器不可变性假设"**——环境层对循环自治的响应。）
  - Cavage："agents break the immutability assumptions containers were built on"（官方简介层原句实录。）
  - Barba："EVE on Vercel… will scale out horizontally to meet that demand. We can spin up these harnesses very, very quickly. In parallel, we can isolate these sessions. They're durable. A whole bunch of mechanics behind it for recovery and retries and error handling…"
  - Barba："EVE is a framework that basically stitches together with very good defaults, all of those types of products to give you a very robust out-of-the-box harness that lives in the cloud."
- **最小主张**：harness 的环境层已商品化（microVM 沙箱、durable session、retry/recovery 默认件）；"多 agent 同时打进来"正成为 harness 的设计基准而非例外。
- **派别适配**：**中性票**。
