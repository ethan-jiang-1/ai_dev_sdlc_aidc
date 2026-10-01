# W1-04 Security and Governance Question List

## Must Answer

- Zero Trust 对 agent 来说到底意味着什么最小控制集：identity、policy decision point、policy enforcement point、tool scoping、runtime re-auth，还是别的？
- 在 agent coding / ops pipeline 里，blast radius 最现实的可计算代理指标是什么？
- 哪些风险最应该在 protocol 层解决，哪些必须在 runtime 或 governance 层解决？
- 如何给 non-human identities 做生命周期管理，避免 token creep、scope creep 和 secret leakage？
- agentic red teaming 应该如何进入研发节奏：pre-deploy gate、continuous simulation、incident replay，还是专门 exercise？
- 哪些安全控制必须平台默认强制，哪些控制适合团队自定义？
- 在软件交付主干链路里，哪些信号最适合进入统一 `release-risk gate`：immutable workflow dependency、short-lived credential、provenance attestation、deploy success、protected environment approval，还是别的？

## High-Value Follow-Ups

- attack-path simulation 能否和 code graph / service dependency graph / knowledge graph 结合，形成更接近业务 blast radius 的风险分数？
- MCP / A2A / tool runtime 的 credential model 最可能形成怎样的 industry baseline？
- 如何将 agent security 审计和 AI governance 审计统一成一套运行节奏？
- release-risk gate 能否统一 `merge gate + provenance gate + deploy gate + environment approval gate`，而不是让这些控制各自分散存在？
- 对 AI-heavy delivery 来说，哪些环境 tier 应该允许自动推进，哪些 tier 必须要求人工批准或独立 attestor？

## Current Gaps

- 软件交付事故与发布门控证据已经明显增强，但仍缺少更多真实 agent-specific pipeline incident case studies。
- provenance、deploy approval 和 protected environment 的公开实现已较强，但仍缺少直接面向 software diff 或 tool-call 的 blast-radius 公开实现。
- workload identity lifecycle 的公开工程细节已经补强，但 agent-specific non-human identity lifecycle 仍缺少更完整的 public pattern。
