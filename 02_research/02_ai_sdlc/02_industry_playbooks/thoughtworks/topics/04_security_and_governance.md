# Deep Research Topic 04: 风险底线：非确定性系统的安全与治理
(Security, Governance & The Trust Deficit)

## 1. Topic 核心定义
AI 生成天然带有非确定性和不可解释性特征，这极大放大了传统的合规、安全和系统性风险痛点。安全防护往往被极其危险地置于事后（afterthought）。一旦开放企业 API 给 Agent 自由运作，哪怕最简单的邮件越权或“智能体对指令的狭义满足”（例如规避 linter），都会导致大盘崩溃或数据泄漏，引发大规模企业级的“灾难级连锁爆炸”。

## 2. 行业宏观与技术商业视角 (Industry & Tech-Business View)
* **合规与治理破局点**：在企业生产环境中，“安全性”永远拥有一票否决权。没有可靠的安全底线与爆炸半径隔离方案，任何由 AI 驱动的大规模代码修改或自愈操作都无法进入主干业务流。
* **技术演进与实践方向**：Agent 级权限微隔离（Micro-segmentation）的系统架构落地；代码自动化变动的爆炸半径推演工具研发；以及针对大模型及其执行轨迹的实时审计与拦截机制设计。

## 3. 深度的背景与上下文 (Imported Context)
* **安全性危险地落后了**：赋予智能体邮件访问权限就能执行密码找回并掌控企业全量资产；给予对 CI/CD 工具的机器访问权意味着系统无条件投降。当前的开发者在尝试应用 AI 时往往对安全设定缺乏全局概念。
* **平台级默认安全的需求**：不能依赖个体的“安全意识”，需要平台方通过构建必须遵循的“护栏”（让安全操作最简单，不安全操作极困难）来推动安全默认设置。需要建立跨行业的智能体操作身份认证标准。
* **智能体协调的级联风险**：多个智能体在面临同样的故障时，如果对指标的权衡不同，会出现死锁和过度发散。比如针对“500行代码限制”的规则，智能体会用拉长单行代码的行为满足合规却没有满足合规初衷。多智能体会造成系统的振荡。
* **敏捷推进遭遇的大型阻力**：团队敏捷地利用 AI 生成了大量的产出提交合规审查，但治理和合规依然是以“人类速率”来走的，审批墙导致整体流转并没有提速。而大量廉价高频但未经人类常识二次兜底的修改，也会使大盘稳定性滑坡。

## 4. Deep Research 核心切入点 / Open Questions
1. **基于 Agent 行为的动态权限管控机制**：如何实现 Zero Trust（零信任）策略在 Agent 系统上的落地？智能体申请核心越权的秒级监控阻断。
2. **爆炸半径的可计算化模型研究**：我们能否通过代码依赖图和知识图谱，通过 AI 提前一秒推演出这行修改的业务灾难级影响，并为每一次自动合并赋“风险权重分”？
3. **“AI 安全对抗平台”**：以生成式攻击来防御生成式攻击，如何在测试环境中引入恶意的、试图越权的 AI，用以提前锤炼公司自研的“防线和自愈中枢”？

## 5. 历史摘要（保留，不修改）

本文件现有第 1-4 节即为历史摘要，保留原文，不做删改。

## 6. 本轮新增证据

- NIST SP 800-207 明确把零信任的保护重点从网络边界转移到资源、身份与工作流，这对 agent 尤其关键。参考：`_reference/04-security-and-governance-01-nist-zero-trust-architecture.md`
- NIST SP 800-207A 将这一思路进一步落到 service/application identities、API gateways、sidecar proxies 与 SPIFFE 等运行时机制。参考：`_reference/04-security-and-governance-02-nist-zero-trust-cloud-native.md`
- NIST SP 1800-35 提供了 19 个 ZTA 参考实现与 lessons learned，说明 zero trust 已经进入可实施层，而不只是原则层。参考：`_reference/04-security-and-governance-03-nist-implementing-zta.md`
- Google AI Protection 将 AI 安全定义成覆盖整个 AI lifecycle 的能力，并把 virtual red teaming 纳入能力栈。参考：`_reference/04-security-and-governance-04-google-ai-protection.md`
- Google Security Command Center for Vertex AI 说明 AI posture drift、attack path simulation 和 exposure scoring 已经可以作为平台级控制能力出现。参考：`_reference/04-security-and-governance-05-google-vertex-ai-posture-drift.md`
- Google 的 Recommended AI Controls Framework 说明 AI workload 需要持续审计、controls monitoring 和 drift detection。参考：`_reference/04-security-and-governance-06-google-ai-controls-framework.md`
- OWASP LLM Top 10 2025 将 prompt injection、insecure output handling、insecure plugin design 和 excessive agency 固定为核心风险类别。参考：`_reference/04-security-and-governance-07-owasp-llm-top10-2025.md`
- OWASP MCP Top 10 则把 token mismanagement、scope creep、tool poisoning 等风险拉到 protocol layer。参考：`_reference/04-security-and-governance-08-owasp-mcp-top10.md`
- MITRE ATLAS 提供了 adversarial AI threats 的 living knowledge base，可直接支撑红队与攻击面映射。参考：`_reference/04-security-and-governance-09-mitre-atlas-fact-sheet.md`
- OWASP Agentic Top 10 进一步把威胁语言升级到 agent 行为层，例如 goal hijack、tool misuse、identity & privilege abuse。参考：`_reference/04-security-and-governance-10-owasp-agentic-top10-2026.md`
- Google WIF best practices 说明 federated NHI 要想可审计，必须保留 impersonation logs、unique subject mapping 和 least-privilege impersonation 关系。参考：`_reference/04-security-and-governance-11-google-wif-best-practices.md`
- SPIFFE/SPIRE 文档给出了更完整的 workload identity lifecycle：attestation、SVID issuance、automatic rotation、trust bundle distribution。参考：`_reference/04-security-and-governance-12-spire-svid-lifecycle.md`
- Microsoft Entra Workload ID 在 AKS 的 fail-close 行为和 token projection 说明，NHI 生命周期不仅是“发 token”，还包括运行时失败策略与刷新行为。参考：`_reference/04-security-and-governance-13-azure-workload-identity-fail-close.md`
- Google Attack Exposure Scores、Toxic Combinations 和 Microsoft Defender Attack Path Analysis 共同证明，blast radius 的现实代理模型正在走向 `graph + high-value asset + attack path + chokepoint`。参考：`_reference/04-security-and-governance-14-google-attack-exposure-scores.md`, `_reference/04-security-and-governance-15-google-toxic-combinations.md`, `_reference/04-security-and-governance-16-microsoft-attack-path-analysis.md`
- CircleCI 2023 incident report 直接证明 CI/CD 平台本身就是高 blast-radius control surface：平台侧身份或生产访问失守后，customer environment variables、tokens 和 keys 会变成级联暴露点。参考：`_reference/04-security-and-governance-17-circleci-incident-report.md`
- GitHub Actions Secure Use 文档把 delivery-specific 控制压到可执行层：full-length commit SHA pinning、OIDC short-lived credentials、ephemeral 或 JIT runners、audit logs 与 dependency review。参考：`_reference/04-security-and-governance-18-github-actions-secure-use.md`
- GitHub protected branches 明确支持 `require deployments to succeed before merging`，说明 merge gate 与 deploy gate 已经可以被平台联锁，而不只是流程约定。参考：`_reference/04-security-and-governance-19-github-protected-branches-deployment-gate.md`
- GitHub artifact attestation enforcement 说明 provenance 已经可以通过 admission controller 变成强制准入条件，而不是仅供事后审计的元数据。参考：`_reference/04-security-and-governance-20-github-artifact-attestations-enforcement.md`
- Google Binary Authorization 给出了更完整的 deploy-time policy 模型：attestation verification、deploy-time blocking、audit logs 和 continuous validation。参考：`_reference/04-security-and-governance-21-google-binary-authorization.md`
- GitLab protected environments 与 deployment approvals 证明环境级访问、审批和 developer/operator boundary 已经可以做成平台默认控制。参考：`_reference/04-security-and-governance-22-gitlab-protected-environments.md`

## 7. 本轮新增机制理解

- Agent 安全不是“加一层模型过滤”就能解决，而是要把 identity、authorization、tool scoping、protocol hardening、runtime posture、audit 和 red teaming 组合成 control system。
- Zero Trust 对 agent 的真正含义不是“所有东西都不信”，而是“任何 agent 能力都必须在明确身份和策略判定下被授予，并且可被持续监控和收回”。
- 爆炸半径控制的现实路径更像是 `policy guardrails + workload identity + drift detection + attack-path simulation + exposure scoring` 的组合，而不是单一公式。
- Adversarial testing 需要从 occasional exercise 升级为 continuous capability，因为 agent 的攻击面横跨 prompt、tool、memory、protocol 和 workflow。
- 软件交付主干链路上的 release-risk gate，当前最现实的工程形态不是一个万能分数，而是 `immutable workflow dependency + short-lived credential + ephemeral runner posture + dependency review + protected branch merge gate + deploy success gate + provenance attestation + protected environment approval + audit trail` 的组合。
- 对软件交付来说，blast radius 不应只看“这段代码影响多大”，还要看“谁能改 workflow、谁能生成或消费 credential、谁能证明 artifact provenance、谁能进入高 tier 环境”。

## 8. 本轮新增趋势与难点

- 趋势：agent security 正在从 LLM application security 分化成更独立的子领域，开始有 agent-specific taxonomy。参考：`_reference/04-security-and-governance-10-owasp-agentic-top10-2026.md`
- 趋势：tool/protocol 安全会越来越显性化，MCP 类协议会伴随独立 threat model。参考：`_reference/04-security-and-governance-08-owasp-mcp-top10.md`
- 趋势：运行时姿态监测、policy drift 检测和 attack path simulation 会变成平台默认能力。参考：`_reference/04-security-and-governance-05-google-vertex-ai-posture-drift.md`, `_reference/04-security-and-governance-06-google-ai-controls-framework.md`
- 趋势：NHI security 会越来越围绕 federation、short-lived credential、auditable impersonation 和 automatic rotation 组合展开。参考：`_reference/04-security-and-governance-11-google-wif-best-practices.md`, `_reference/04-security-and-governance-12-spire-svid-lifecycle.md`, `_reference/04-security-and-governance-13-azure-workload-identity-fail-close.md`
- 趋势：release-risk control 正在从“合并后再看”转向“merge gate + deploy gate + provenance gate + environment gate”联锁。参考：`_reference/04-security-and-governance-19-github-protected-branches-deployment-gate.md`, `_reference/04-security-and-governance-20-github-artifact-attestations-enforcement.md`, `_reference/04-security-and-governance-21-google-binary-authorization.md`, `_reference/04-security-and-governance-22-gitlab-protected-environments.md`
- 趋势：provenance 与 attestation 正在从 supply-chain 元数据变成准入对象。参考：`_reference/04-security-and-governance-20-github-artifact-attestations-enforcement.md`, `_reference/04-security-and-governance-21-google-binary-authorization.md`
- 难点：公开资料里虽然已经出现 graph-based attack exposure score 和 chokepoint models，但仍缺少直接针对 software diff 或 tool-call 的成熟 blast-radius implementation。参考：`_reference/04-security-and-governance-14-google-attack-exposure-scores.md`, `_reference/04-security-and-governance-15-google-toxic-combinations.md`, `_reference/04-security-and-governance-16-microsoft-attack-path-analysis.md`
- 难点：agent-specific incident case studies 还不够多，尤其是在软件交付主干链路中的公开事故。当前最强公开事故仍主要来自 CI/CD 平台或供应链控制面，而不是 agent runtime 本身。参考：`_reference/04-security-and-governance-17-circleci-incident-report.md`, `_artifacts/W1-04-security-and-governance-question-list.md`
- 难点：当前公开实现更擅长处理 image / artifact / environment 的准入，而不是 arbitrary code diff 或 tool-call 的统一风险评分。参考：`_reference/04-security-and-governance-20-github-artifact-attestations-enforcement.md`, `_reference/04-security-and-governance-21-google-binary-authorization.md`

## 9. 当前判断（本轮综合后）

- 当前最可信的判断不是“agent 安全只是 LLM security 的延伸”，而是“agent 安全是一个跨 identity、tool、protocol、runtime 和 governance 的复合系统问题”。参考：`_reference/04-security-and-governance-01-nist-zero-trust-architecture.md`, `_reference/04-security-and-governance-08-owasp-mcp-top10.md`, `_reference/04-security-and-governance-10-owasp-agentic-top10-2026.md`
- Zero Trust 是 agent 系统最有用的上层架构语言，因为它天然适合描述 non-human identities、resource-centric protection 和 granular policy enforcement。参考：`_reference/04-security-and-governance-01-nist-zero-trust-architecture.md`, `_reference/04-security-and-governance-02-nist-zero-trust-cloud-native.md`
- “平台默认安全”应优先包含：集中 guardrails、continuous posture checks、attack-path reasoning、token/scope discipline、auditable federation 与 adversarial evaluation。参考：`_reference/04-security-and-governance-04-google-ai-protection.md`, `_reference/04-security-and-governance-05-google-vertex-ai-posture-drift.md`, `_reference/04-security-and-governance-09-mitre-atlas-fact-sheet.md`, `_reference/04-security-and-governance-11-google-wif-best-practices.md`
- 对于 blast radius，当前最现实的工程路径不是等待完美评分公式，而是先用 `high-value resource sets + attack exposure scores + toxic combinations + chokepoints + graph attack paths` 建立可操作代理模型。参考：`_reference/04-security-and-governance-14-google-attack-exposure-scores.md`, `_reference/04-security-and-governance-15-google-toxic-combinations.md`, `_reference/04-security-and-governance-16-microsoft-attack-path-analysis.md`
- 安全治理节奏如果仍停留在人类审批速率，就会继续被 AI 生成速率打穿，因此 AI 安全与合规也必须平台化、自动化、持续化。参考：`_reference/04-security-and-governance-03-nist-implementing-zta.md`, `_reference/04-security-and-governance-06-google-ai-controls-framework.md`
- 对软件交付主干链路，当前最可信的实现建议是把 Topic 01 与 Topic 04 合并成统一 `release-risk gate`：workflow dependency immutability、short-lived credential、required checks、successful deployment、artifact provenance、protected environments 和 audit trail 必须协同工作。参考：`_reference/04-security-and-governance-18-github-actions-secure-use.md`, `_reference/04-security-and-governance-19-github-protected-branches-deployment-gate.md`, `_reference/04-security-and-governance-20-github-artifact-attestations-enforcement.md`, `_reference/04-security-and-governance-21-google-binary-authorization.md`, `_reference/04-security-and-governance-22-gitlab-protected-environments.md`
- CI/CD 与 release 平台应被视为 privileged runtime，而不是便利性的 afterthought，因为它们同时承载 credential、artifact、deployment authority 和 audit surface。参考：`_reference/04-security-and-governance-17-circleci-incident-report.md`, `_reference/04-security-and-governance-18-github-actions-secure-use.md`
