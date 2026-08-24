# mclayer / plugin-codeforge：洞察摘录

## 关键言辞

> capability 상승이 2배 비용을 정당화하는 **chief-author / 장기 agentic 코딩 / 적대적 심판** 역할에만 surgical 적용.

- 这句最关键，因为它把“最强模型默认全上”的直觉掰开了。
- 对资料库来说，真正有价值的不是赞美，而是这种明确的角色边界。

> `model: fable` alias 는 **Claude Code v2.1.170+** 필수.

- 这句说明他们不是把 Fable 5 当成抽象能力，而是当成一个有运行时版本依赖的系统部件。
- 一旦出现版本 floor，采用就从“试试看”进入了“需要治理”的阶段。

> 최상위 세션 = 현행 `opus` 유지 (CLAUDE.md 정책, 별도 결정 사안).

- 这句很值钱，因为它明确表明连 orchestrator 都不是自动切到最强模型。
- 这是一种非常成熟的约束意识：高能力模型不等于默认控制层模型。

> fable model-unavailable → opus **fresh re-spawn** 1회 자동 fallback

- 这句来自后续状态更新，说明他们已经把“Fable 不可用怎么办”纳入运行时恢复路径。
- 这让这条样本不再只是 adoption proposal，而更像真实生产编排的演进记录。

## 总结判断

- `plugin-codeforge` 这条线很适合补在 `fable5_field_signals/` 里，因为它给出了公开、硬核、可复核的采用制度。
- 它和 `Every` 样本形成互补：`Every` 更像组织中的 workflow 口述，这条线更像 repo 里的治理与角色编排证据。
