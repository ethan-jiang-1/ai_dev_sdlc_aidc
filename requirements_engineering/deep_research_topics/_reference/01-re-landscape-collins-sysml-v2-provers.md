# Collins Aerospace / DARPA PROVERS 2025 — SysML v2 industrial adoption signal in high-assurance engineering toolchain

- source_url: `https://sos-vo.org/system/files/2025-05/David_Hardin-hcss-25.pdf`
- source_type: `official industry presentation`
- accessed_at: `2026-04-18`
- related_topic: `01 re-landscape (primary), 04 future-trends`
- trust_level: `official industry`
- tier: `B`
- why_it_matters: Topic 01 在 DoD transition guidance 之后，仍缺第二个非-OMG adoption/maturity signal，避免把 SysML v2 的外部支持只写成政府 guidance 单点。该 2025 Collins Aerospace / DARPA PROVERS presentation 明确把 SysML v2 放进真实高保证工程 toolchain，写明它由 major tool vendors 支持，并称其对 `mass adoption by the Defense Industrial Base` 是必要条件。这不是 broad industrial census，但足以把 Topic 01 从“单一外部官方过渡信号”推进到“government + defense-industry program signal supported”。
- captured_excerpt: `yes`
- claims_supported: `SysML v2 is being integrated into an industrial high-assurance engineering pipeline; major tool vendors support SysML v2; Collins Aerospace and partner teams are using SysML v2 alongside AADL, contracts, DevOps, verification, and Rust code generation; SysML v2 is framed as necessary for mass adoption by the Defense Industrial Base.`
- date_scope: `presentation dated 2025`
- related_entities: `Collins Aerospace; DARPA PROVERS; INSPECTA; SysML v2; AADL; Rust; HAMR; GUMBO; Defense Industrial Base`

## 关键事实

1. 该 PDF 是 2025 年 Collins Aerospace 在 DARPA PROVERS / HCSS 场合的公开 presentation。
2. 文中明确写到 SysML v2:
   - is the second major version of the Systems Modeling Language
   - has a standard textual form in addition to graphical form
   - promotes third party tool interaction
   - is supported by major tool vendors: Siemens, The Mathworks, etc.
3. 最关键的一句是：SysML v2 is `necessary for mass adoption by the Defense Industrial Base`。
4. 同一份材料还展示了实际工程链：
   - `System Architecture Modeling (SysML v2/AADL)`
   - `Requirements`
   - `Component API Synthesis (HAMR)`
   - `Application Component Synthesis (Rust)`
   - proof engineering / ProofOps / DevOps integration
5. 这说明 SysML v2 已不只是标准文本，而是被放入真实高保证工程和生成式工具链里讨论和实践。

## 核心内容摘录

### 这是一条 industry-side adoption signal

- 与 DoD transition guidance 相比，这份材料来自 defense-industry 侧的实际项目/团队。
- 因而它能把 Topic 01 从“government guidance”进一步推进到“industry-side implementation signal”。

### SysML v2 被写进真实工程管线

- presentation 中的 pipeline 不是单纯概念图，而是把 SysML v2 与 AADL、contracts、Rust、verified synthesis、DevOps、ProofOps 串联起来。
- 这说明在高保证系统工程场景中，SysML v2 正被视为可接入 formal / code-gen / assurance toolchain 的模型层。

### 正确的结论边界

- 这份材料可以支持：
  - `major-tool-vendor-support-signaled`
  - `defense-industry-adoption-signal-supported`
  - `second-source-external-adoption-signal-supported`
- 但不能支持：
  - 全行业广泛成熟普及
  - 普通 SaaS 团队已经普遍使用 SysML v2

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 01 `re-landscape` | 把 SysML v2 的外部 adoption/maturity signal 从 DoD 单点升级到 government + defense-industry 双点 |
| Topic 04 `future-trends` | 支撑 requirements/model artifacts 与 formal verification / code generation / AI assistance 的组合趋势 |

## 可直接引用的术语 / 概念

- `supported by major tool vendors`
- `necessary for mass adoption by the Defense Industrial Base`
- `System Architecture Modeling (SysML v2/AADL)`
- `third party tool interaction`
- `standard textual form`

## 风险与局限

1. 这是 defense-industry / high-assurance domain signal，不代表所有行业。
2. 这是 presentation 级 adoption/maturity evidence，不是大规模市场调查。
3. 它更适合支持“外部 adoption signal strengthened”，而不是“broad industrial maturity solved”。

## 交叉引用

- Topic 01 evidence summary：[`../_artifacts/01-re-landscape-evidence-summary.md`](../_artifacts/01-re-landscape-evidence-summary.md)
- DoD transition guidance：[`01-re-landscape-dod-sysml-v2-transition-guidance.md`](01-re-landscape-dod-sysml-v2-transition-guidance.md)
- OMG tools ecosystem：[`01-re-landscape-omg-sysml-v2-tools-ecosystem.md`](01-re-landscape-omg-sysml-v2-tools-ecosystem.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
