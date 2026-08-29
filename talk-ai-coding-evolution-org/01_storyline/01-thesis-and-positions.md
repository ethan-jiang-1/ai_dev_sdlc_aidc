# 核心论点与立场（v0.5 摘要）

> 详细论证见 [`00-storyline-map.md`](./00-storyline-map.md)。对象 = 研发整体组织，独立成篇。

1. **代码不再是瓶颈**：AI 把 build 压到小时级，慢的是 plan/review/test/deploy 这些「人的速度」的环节。
2. **所以转型对象是整条 SDLC，不是编码**：六阶段（Plan→Design→Build→Test→Deploy→Maintain）是主轴，全要重写。
3. **五层是引子，不强扭成章节**：Prompt→Context→Harness→Loop→Graph 各在自然接点点破 SDLC 某一阶段——Plan=Prompt、Design=Context、Build/Test/Deploy=Harness、Test/Maintain=Loop、跨阶段编排=Graph。
4. **harness 是临界点**（开场先立住）：模型给能力，harness 给可靠性；harness 是组织唯一该集中建设的一层。
5. **工件链 = 审计链**：`intent → spec → plan → diff → PR → incident` 的 commit 链就是审计记录。
6. **人守 gate，不逐行**：human judgment at gates；确定性优先（computational > inferential）。
7. **DSH = 可组合 harness runtime（给不同环节定制）**：registry / adapter / capability seam / enforced gate / append-only session log = 准入/替换/放行/重建事实；组织用它「组装」而非「从零造」。
8. **带走原则**：代码不再是瓶颈，流程才是。

## 一句话主线（源自 00-storyline-map）

代码不再是瓶颈；组织要转型的是整条 SDLC——沿六阶段把五层一一落地，DSH 作为可组合 runtime 收束。
