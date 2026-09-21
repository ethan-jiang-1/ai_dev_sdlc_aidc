# 维度 08 · 漂移治理（SDD）

> 角色：加权维。**v1.1 新增维**。形态适用：A+B，**漂移是两形态共同的敌人，但守护对象不同**（见 §A/B 子族）。

## 核心问题

规格、契约、实现、文档声明之间的一致性，是否被机器守护？

## 为什么独立成维

SDD 在 2026 年成为主流实践后，"漂移"是它的一号工程问题：spec 写了、代码改了、两者渐行渐远。社区已把 drift detection 做成 SDD 工具链的一等公民（[spec-driven-development-skill](https://github.com/mariano-aguero/spec-driven-development-skill)：constitution → specify → plan → tasks → implement → validate，带漂移检测与质量门禁）；SDD 的适用边界也在被认真讨论（[InfoQ: When Spec-Driven Development Pays Off](https://www.infoq.com/articles/when-spec-driven-development-pays-off/)）。对 agent 的特殊意义：**agent 是最忠实的规格执行者，也是最忠实的漂移放大者**——规格过时时，人类会感知到违和，agent 会照着错规格继续生成。原五维没有一维回答"仓库工件之间的一致性由谁守护"。

## 边界声明

- 归此维：**仓库工件之间**的一致性——spec 与实现、契约文件与两端代码、文档声明与实际行为、schema 与序列化。判据形态：一致性有没有被**测试/脚本/CI** 守护（机器守护 vs 仅文档声明）。
- 归他维：契约有没有显式存在（静态面）归 04——04 管"契约可见"，08 管"契约不破"；指引文件自身旧了没人删归 07（分界口诀见 07 文件）；规格质量本身（写得好好不好）不是本体系对象，本体系只问一致性守护机制。

## 判据族（草案）

1. **契约钉子**：跨组件契约进了测试/一致性脚本，违反即红（不是只写在文档里）。
2. **漂移检测门禁**：lockfile/基线/schema/生成物有机器化的漂移检查，且在 CI 阻断。
3. **spec 单一事实源**：同一行为只有一处权威声明；其他位置指针引用。
4. **变更同步义务**：改实现必须同步改 spec/契约的规则成文，且有机器或流程强制。
5. **声明可判定**：文档中的行为性声明（"X 不会发生 Y"）可追溯到测试或显式标注为"设计意图未强制"。
6. **agent 对漂移的可见性**：仓库向 agent 声明"哪里是权威、哪里可能过时"（如 spec 状态标记），agent 能区分现行规则与历史文档。

## A/B 子族（v1.2）

漂移是 A/B 共同的敌人，分型依据不是"谁怕漂移"，而是守护对象与手段不同：

**A 子族 · 断言机制下的规格漂移**：
- 守护对象：spec/契约 ↔ 确定性实现。错误会被测试/运行结果戳穿，所以 tier-0/1（契约测试、CI 漂移检查）即完整答案。
- 条件判据：未采用 SDD 的 A 仓库不因"无 spec"扣分；**采用了 SDD 则漂移守护判据加严**（模型会拿着过时 spec 高保真地继续生成——比没有 spec 更糟）。

**B 子族 · 统计机制下的行为漂移**：
- 守护对象：行为定义/提示/SKILL ↔ 预期行为。错误不表现为"测试红了"，表现为"行为不对"；且模型被厂商更新即引入第三方漂移源（[arXiv 2606.28791](https://ar5iv.labs.arxiv.org/html/2606.28791) §5.5：agent 无终态，须 TEVV 永久看护）。
- 判据形态：行为基线/evals 存在、模型版本变更触发重跑、漂移监控自动化。
- **成熟度标注：探索**。

## 依据

- [mariano-aguero/spec-driven-development-skill](https://github.com/mariano-aguero/spec-driven-development-skill)（drift detection 作为 SDD 管道环节，2026）。
- [InfoQ: When Spec-Driven Development Pays Off](https://www.infoq.com/articles/when-spec-driven-development-pays-off/)（2026，SDD 适用边界）。
- raw 04 §8.1（约束下沉到确定性最强的一层——本维的原理基础：一致性守护应下沉到测试/CI，不是祈使句）。
- raw 05 §6.1（lockfile/基线漂移由机器守护的案例模式）、raw 06 案例 1/2（codex bazel-lock 漂移规则、airflow 架构边界判断句）。

## 泛化注意

- 本维判据**大部分可用 tier-0/1** 采证（grep 契约测试存在、CI 配置含漂移检查），是九维里自动化潜力最高的——checklist-v1 落条时优先 tier-0 化。
- 与 `03_practice/spec_driven_development/`、`harness_governance/` 是兄弟主题：本维只做**判据**，方法论归实践层；届时互加指针（单一事实源，不复制正文）。

## 开放问题

- "spec 单一事实源"与多目标规格（人读的 PRD + agent 读的 spec）并存时如何判 ✅——需要"声明主从关系"式的判据写法。
- 仓库无显式 spec 时本维如何打分：按"一致性守护机制缺失"计 ❌ 过重？还是判 ⚠️ 并要求契约钉子兜底？待 checklist-v1 定。
