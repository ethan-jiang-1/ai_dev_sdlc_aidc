# 需求工程 Topics Deep Research 一轮 执行状态（Progress / State）
> 状态：本轮已收口（completed / closed_for_current_round）。过程件仅作回溯，修改 final/ 勿据本文，以 final/ 现状为准。

> 对应计划：`requirements_engineering/plan/dr-round-1.plan.md`
> 对应执行队列：`requirements_engineering/plan/dr-round-1.queue.md`
> 本文件只记录运行态状态、阻塞、恢复上下文与分支处置；连续动作回读 `requirements_engineering/plan/dr-round-1.queue.md`。

## 🚩 Resume Protocol（接手此轮 DR 的 Agent 第一眼读这里）

> **如果你是新接手的 Agent / 新会话**：按以下 5 步顺序读；任何顺序偏差都会导致误判状态或重复劳动。

1. **读 plan（设计态 SoR，只读不改）**：`requirements_engineering/plan/dr-round-1.plan.md` — 6 条研究线注册表 + Source Tier Policy + Hard Gates + 输出契约。设计态由人类决定，执行态不得修改它。
2. **读本文件（运行态 SoR）**：
   - 先看「当前执行快照」确认 `current_wave` / `current_gate` / `required_next_step`
   - 再看「Wave 0 Foundation Sufficiency Check」和「Wave 1 各研究线」块，确认每条线的 `shared_support` + `gap` + `status`
   - 最后看「Resume Checkpoint」取得 `last_completed_step` + `resume_precheck` + `do_not_forget`
3. **读 queue（连续动作 SoR）**：`requirements_engineering/plan/dr-round-1.queue.md` → `Active Queue.current_task`，这是**唯一**你要立即执行的动作；其 `done_condition` 是完成判据，`writes_to` 是要改哪些文件。**不要跳到 `next_task` 之后，除非 current 已达 done_condition**。
4. **核对硬盘实情与 SoR 对齐**（3 项快检，应全部通过；若有任何一项失败，**先修对齐再动手做新工作**）：
   - `ls requirements_engineering/deep_research_topics/_reference/00-shared-*.md | wc -l` 输出应等于 `Wave 0.docs_landed`（当前为 12）
   - `_reference/_INDEX.md` 快速计数总和应等于上条
   - 每份 Worklog 登记的文件路径都应真实存在
5. **启动当前 task**：按 `queue.current_task.writes_to` 顺序写入；每完成一份 AC（authoritative copy）要同步刷新 `_reference/_INDEX.md` + 本文件 `Worklog` + 相关研究线 `doc_count/primary_count/status` + `Gate State.last_gap_reduction`。**每次 tool batch 结束都保证三份 SoR 与硬盘一致**。

### Handoff-Safe 操作规则

- **不改 plan**：plan 是设计态 SoR；若真有必要变拓扑（加/删研究线），先在 `Topology Delta / Formalization State.pending_topic_candidates` 登记，请求用户确认后再改。
- **不跳 gate**：当前 gate = `wave0_complete`；下一个 gate = `wave1_primary_saturated`（需 ≥ 3/6 研究线跨过 primary_saturated 阈值）。不满足 gate 条件不要写 Wave 2 综合。
- **每动一步都过 No-Empty-Queue Rule**：完成 `current_task` 前先把 `next_task` 提升到 `current_task`、把 `next_after_next` 提升到 `next_task`、从 Refill Pool 补一个新的 `next_after_next`，再真正把新的 `current_task` 走 done_condition。
- **paywall / 抓取失败的显式降级**：INCOSE GtWR v4 官方 PDF 被 Cloudflare 挡、ISO 直站 403、IEEE Xplore 付费 —— 当前策略是二次重述 + 风险登记；任何需要逐字原文才能成立的主张，必须在 `_artifacts/*-evidence-summary.md` 里显式标注"待 Tier-A 原文升级"。
- **任何断言都要挂具体 `_reference/*.md` 路径**；没有本地 AC 的主张视为 Tier-E（叙事），不进入综合。

### Cold-start 必读最少文件集

```
requirements_engineering/plan/dr-round-1.plan.md                (design SoR)
requirements_engineering/plan/dr-round-1.status.md              (this file — runtime SoR)
requirements_engineering/plan/dr-round-1.queue.md               (action SoR)
requirements_engineering/deep_research_topics/_reference/_INDEX.md   (30-second evidence index)
requirements_engineering/deep_research_topics/_reference/README.md   (naming + required-fields schema)
requirements_engineering/deep_research_topics/_artifacts/README.md   (artifact cadence + naming)
requirements_engineering/deep_research_topics/claims-audit.md        (原文 10 条断言的证据强度初版)
```

读完以上 7 份（总量 < 1000 行）就可以开始做 `queue.current_task`。**不需要**读 `_reference/00-shared-*.md` 的 12 份 AC 原文，除非你要展开当前 task 的证据链。

---

## 当前执行快照（Current Execution Snapshot）

- state: `closed_for_current_round`
- current_mode: `execution`
- current_wave: `Current round formally closed after packaging completion on top of the frozen evidence base; deliverable surface is handoff-ready`
- blocking_issue: `not_applicable`
- required_next_step: `no further action is required for this round; only reopen if the user explicitly wants a deferred-gap continuation`
- largest_gap_if_stop_now: `no packaging gap remains; only explicit deferred evidence-upgrade gaps remain on Topics 01/02/03/04/05/06`

## Queue Pointer

- queue_path: `requirements_engineering/plan/dr-round-1.queue.md`
- last_queue_refill: `2026-04-18 after formal round closeout — active queue parked on user-directed deferred-gap reopen while the round remains handoff-ready`

When `QUEUE_PATH.Active Queue.queue_health = blocked`, sync `state = blocked`, `blocking_issue`, and `Resume Checkpoint.safe_to_interrupt` with `QUEUE_PATH.Blocked State`.

## Gate State

- current_gate: `closed_for_current_round`
- next_gate: `user_directed_deferred_gap_reopen`
- next_scoring_action: `none for this round`
- stalled_scoring_actions_since_last_gap_reduction: `0`
- last_gap_reduction: `Topic 06 formal scaffold-aware benchmark upgraded 2026-04-18 via OctoBench; exact cross-tool AGENTS.md semantic conformance suite remains explicitly deferred. _INDEX.md total = 74`

## Plan / Status Sync

- plan_placeholders_cleared: `yes`
- topology_sync_state: `synced`

## 目录与集成状态（Directory / Integration State）

- seed_readme_ready: `yes`
- reference_readme_ready: `yes`
- artifact_readme_ready: `yes`
- reference_index_ready: `yes`
- seed_backfill_status: `complete (all 6 topic seed files now preserve historical sections and expose this-round evidence / mechanism / trends / current-judgment packaging sections aligned with the frozen evidence base as of 2026-04-18)`
- artifact_status: `round_closed_final_surface`（01/02/03/04/05/06 evidence-summary + question-list pairs exist; W2 cross-topic / selection matrix / claims audit have been promoted to round-closed status as of 2026-04-18）

## Topology Delta / Formalization State

当前有效 topic 数量始终由 plan 中的 `topic registry` 派生；此处只记录拓扑增量、推进中的结构变化与最近一次正式化说明。plan/status 哪一侧尚待同步，不写在这里，统一写入上面的 `Plan / Status Sync.topology_sync_state`。

- new_topics: `none`（06 agent-format 的 seed 文件 requirements_engineering/deep_research_topics/topic-06-agent-format.md 已在 execution entry 中创建；README / references-by-topic / claims-audit 已登记）
- pending_topic_candidates: `none`
- recent_change: `Wave 0 completed 2026-04-17: 12 shared authoritative copies landed in _reference/; _INDEX.md populated to 12/12; Foundation Sufficiency Check passed; queue rewritten for Wave 1; gate advanced to wave0_complete`
- formalization_sync_note: `not_applicable`

## Wave 0：共享 Ground Truth 地基

- target_floor: `12`
- docs_landed: `12`
- completion_status: `complete`
- foundation_sufficiency_check: `passed 2026-04-17 — see Foundation Sufficiency Check block below`
- gap: `none at floor level; Wave 1 per-topic primary sources still to be landed`
- coverage_by_tier: `tier-A: 5 (GtWR v4, 29148, Mavin 2009 EARS, Cohn Stories Applied, Patton Story Mapping) / tier-B: 6 (Cursor Rules, Claude Code, AGENTS.md spec, Fowler UserStory, Fowler GivenWhenThen, Gherkin reference) / tier-C: 1 (ISO 26262-8 Part 8 via industry primer)`
- limitation_source_coverage: `3 landed (ISO 26262-8 Part 8 Clause 6 + 11 compliance constraints; Anthropic Claude Code best practices on context rot; AGENTS.md spec scope-neutrality / overlap caveats) — floor ≥ 2 satisfied`

### Foundation Sufficiency Check 2026-04-17

- floor_reached: `yes (12/12)`
- tier_A_min_3: `yes (5 landed)`
- limitation_source_min_2: `yes (26262-8 + Claude Code context-rot + AGENTS.md scope-neutrality caveats)`
- cross_topic_bridge_built: `yes — shared anchors cross-reference ≥ 2 topics each (see _INDEX.md related_topic column)`
- paradigm_landscape_core_terms_locked: `yes — requirement (29148) / user story (Fowler + Cohn) / story map (Patton) / EARS five modes (Mavin) / BDD GWT (Fowler) / Gherkin keywords (Cucumber) / agent format (Cursor + Claude + AGENTS.md) / safety-requirement (26262-8 Clause 6) — 8 working definitions locked across shared foundation`
- outstanding_risks: `ISO 26262-8 Part 8 still only captured via industry primer (tier C). INCOSE GtWR v4 has now been upgraded from reqi-only to official webinar-presentation level, but full technical product PDF / summary-sheet verbatim capture is still pending. ISO/IEC/IEEE 29148:2018 remains at official scope/catalog level; clause-level wording is still paywalled and pending full-text access for stronger Topic 03 / 05 / Wave 2 assertions.`
- decision: `wave0_complete → open Wave 1 with Topic 03 EARS as first branch (highest leverage: single primary author + cleanest empirical pattern set + most directly bridging to Topic 05 + Topic 06)`

## Wave 1：按研究线深挖

### 研究线 01：re-landscape

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 01/re-landscape`
- topic_id: `01`
- topic_slug: `re-landscape`
- doc_count: `10`（topic-scoped；shared 层已提供 29148 + GtWR v4 + Mavin 2009 EARS + Fowler UserStory + Cohn + Patton 共 6 份跨范式锚点）
- shared_support: `6 shared anchors provide paradigm coverage: 00-shared-iso-iec-ieee-29148-2018.md, 00-shared-incose-gtwr-v4-summary.md, 00-shared-mavin-2009-ears-re09.md, 00-shared-fowler-user-story-bliki.md, 00-shared-cohn-user-stories-primer.md, 00-shared-patton-story-mapping-primer.md`
- primary_count: `6`
- primary_source_coverage: `primary_saturated_for_gate — systems-engineering frame + lifecycle standard + Use-Case 2.0 contrast + OMG SysML v2 official anchor + official tools ecosystem + DoD transition guidance + Collins industrial signal adequately support the current paradigm-map backbone, and INCOSE automotive metadata adds a bounded non-defense signal; continue for formal-method / decision-table / broader multi-industry implementation maturity completion`
- secondary_count: `3`
- recent_count: `4`
- limitation_count: `1`
- topic_stop_decision: `continue`
- early_saturation_reason: `not_applicable`
- evidence_summary: `round_closed`
- question_list: `round_closed`
- status: `closed_for_current_round`
- gap: `starter pack plus MBSE official anchor, tools ecosystem, DoD external transition guidance, Collins defense-industry signal, INCOSE automotive metadata signal, INCOSE/OMG multi-org end-user participation signal, and Productive4.0 non-defense validation use-case landed via SEBoK requirements-engineering anchor + ISO/IEC/IEEE 15288 overview + Use-Case 2.0 official contrast + OMG SysML v2 official source + OMG tools ecosystem page + DoD transition guidance + Collins PROVERS signal + INCOSE IS 2025 automotive case metadata + INCOSE/OMG update deck + Productive4.0 Arrowhead validation use-case; continue because production/outcome maturity, formal methods, decision tables / DMN, and stronger 29148 ↔ GtWR ↔ EARS synthesis would still improve the final paradigm map`

### 研究线 02：user-story

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 02/user-story`
- topic_id: `02`
- topic_slug: `user-story`
- doc_count: `12`（topic-scoped 计数，不含 shared；shared 已覆盖 Fowler UserStory + Cohn primer + Patton story mapping 三份）
- shared_support: `3 shared anchors already landed: 00-shared-fowler-user-story-bliki.md, 00-shared-cohn-user-stories-primer.md, 00-shared-patton-story-mapping-primer.md`
- primary_count: `2`
- primary_source_coverage: `starter_covered — one book-level anchor + one original method source + one recent KOL revisit landed; not yet primary_saturated because Cockburn / Beck / boundary taxonomy remain open`
- secondary_count: `10`
- recent_count: `2`
- limitation_count: `2`
- topic_stop_decision: `continue`
- early_saturation_reason: `not_applicable`
- evidence_summary: `round_closed`
- question_list: `round_closed`
- status: `closed_for_current_round`
- gap: `starter pack plus XP-roots/use-case-boundary anchor, subtype starter pack, Beck preview-level anchor, Cohn direct anti-pattern boundary, O'Reilly Story Smells preview, InformIT publisher-level taxonomy TOC, Cohn 2024 overly-small story discussion, Mountain Goat common-problems taxonomy, and Seb Rose Beck/BDD origin-boundary article landed via Cohn book-level anchor + Wake original INVEST + Mike Cohn AI-era revisit + XP/C3/Cockburn boundary support + Job Story/Spike/Enabler starter boundaries + Beck/Fowler XP previews + Cohn 2004 slides + O'Reilly preview extracts + InformIT TOC + Cohn 2024 blog + Mountain Goat curriculum + ACCU Overload / Seb Rose; Chapter 14 full discussion and Beck verbatim full text remain deferred rather than treated as solved`

### 研究线 03：ears

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 03/ears`
- topic_id: `03`
- topic_slug: `ears`
- doc_count: `4`（topic-scoped；shared 已覆盖 Mavin 2009 RE'09 + GtWR v4 + 29148 三份锚点）
- shared_support: `3 shared anchors already landed: 00-shared-mavin-2009-ears-re09.md (primary), 00-shared-incose-gtwr-v4-summary.md, 00-shared-iso-iec-ieee-29148-2018.md`
- primary_count: `2`
- primary_source_coverage: `starter_covered — one academic empirical anchor + two official/practitioner guides landed; software-scope applicability is now supported, but SaaS empirical evidence and rule-by-rule GtWR mapping remain open`
- secondary_count: `2`
- recent_count: `3`
- limitation_count: `2`
- topic_stop_decision: `continue`
- early_saturation_reason: `not_applicable`
- evidence_summary: `round_closed`
- question_list: `round_closed`
- status: `closed_for_current_round`
- gap: `starter pack plus software-scope guidance landed via Uusitalo 2023 PLC empirical study + Mavin official guide / RE2016 bibliographic trace + Jama industrial primer + QRA software-scope guidance; continue because EARS↔GtWR rule mapping and SaaS/non-safety empirical cases remain high-value gaps`

### 研究线 04：future-trends

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 04/future-trends`
- topic_id: `04`
- topic_slug: `future-trends`
- doc_count: `15`（topic-scoped；shared 层已提供 Cursor + Claude + AGENTS.md 三基线，Wave 1 starter pack 已补 spec-driven / governance / trend signals，并补 multimodal / graph starter signals、BMW graph case、v0 multimodal workflow、hosted outcome、independent design-study outcome、AI4UI enterprise benchmark、UX Tools independent adoption census 与 Figma/Findable named deployment case）
- shared_support: `3 shared anchors support agent-era trend framing: 00-shared-cursor-rules-official.md, 00-shared-claude-code-official.md, 00-shared-codex-agents-md-spec.md`
- primary_count: `10`
- primary_source_coverage: `primary_saturated_for_gate — spec-driven / governance / IDE-native axes now have enough grounding to enter cross-topic synthesis; multimodal axis now has both Figma and v0 official workflow signals plus hosted outcome, independent-study outcome, enterprise-benchmark outcome, independent adoption census, and a named vendor-hosted deployment case; graph axis has requirements-engineering-specific research signal, enterprise customer-requirements signal, and a BMW broader product-development case; continue only for independently verified production outcome or ISO 42001 completion if needed`
- secondary_count: `3`
- recent_count: `9`
- limitation_count: `2`
- topic_stop_decision: `continue`
- early_saturation_reason: `not_applicable`
- evidence_summary: `round_closed`
- question_list: `round_closed`
- status: `closed_for_current_round`
- gap: `starter pack plus multimodal/graph starter signals, one hosted multimodal outcome, one independent design-study outcome, one enterprise-grade benchmark, one independent adoption census, and one named vendor-hosted deployment case landed via GitHub Spec Kit official + Kiro official + NIST AI RMF / EU AI Act + Thoughtworks trend signal + Figma Make multimodal signal + Figma/Findable app-shell deployment case + Vercel v0 multimodal/PRD workflow + Vercel/Stripe hosted outcome + Personagram study + AI4UI benchmark + UX Tools State of Prototyping survey + W3C RDF/SHACL graph-constraint substrate + KG-EmpiRE RE knowledge graph + IBM enterprise customer-requirements KG + BMW virtual product-development KG case; remaining multimodal gap narrowed to independently verified production outcome and ISO/IEC 42001 completion`

### 研究线 05：integration-bdd

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 05/integration-bdd`
- topic_id: `05`
- topic_slug: `integration-bdd`
- doc_count: `6`（topic-scoped；shared 已覆盖 Fowler GWT + Gherkin official reference + ISO 26262-8 限制面）
- shared_support: `3 shared anchors already landed: 00-shared-fowler-given-when-then-bliki.md (primary for GWT concept), 00-shared-gherkin-official-reference.md, 00-shared-iso-26262-part8-overview.md (limitation face)`
- primary_count: `4`
- primary_source_coverage: `primary_saturated_for_gate — examples-layer / discovery-formulation pipeline / enterprise-signal plus OMG DMN decision-model boundary, FlowForge same-prototype Story/DMN/Gherkin chain, and ISTQB acceptance-governance framework are sufficiently anchored for cross-topic synthesis; continue only for EARS-inclusive high-compliance same-project case and original BDD-history completion if needed`
- secondary_count: `2`
- recent_count: `2`
- limitation_count: `2`
- topic_stop_decision: `continue`
- early_saturation_reason: `not_applicable`
- evidence_summary: `round_closed`
- question_list: `round_closed`
- status: `closed_for_current_round`
- gap: `starter pack plus OMG DMN boundary anchor, FlowForge same-prototype BPMN/DMN -> User Story/Gherkin chain, and ISTQB acceptance-governance framework landed via Adzic book-level anchor + Matt Wynne/Cucumber Book method framing + Cucumber official discovery/formulation/case + OMG DMN official positioning + FlowForge prototype study + ISTQB Acceptance Testing syllabus; remaining gap narrowed to EARS-inclusive high-compliance same-project governance case and Dan North original BDD-history completion`

### 研究线 06：agent-format

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 06/agent-format`
- topic_id: `06`
- topic_slug: `agent-format`
- doc_count: `15`（topic-scoped；Wave 0 三份基线已全部落在 shared 组，Wave 1 starter pack 已落 adopter / failure / comparison / format-convergence / public OSS usage / GitHub Copilot support，并补 Stripe enterprise-internal usage、GitHub-scale adoption study、OpenSpec direct comparison、Cline/Continue/Aider semantic comparison、rule-effect study、AGENTbench multi-agent context-file evaluation、OctoBench scaffold-aware compliance benchmark 与 Umans AI practical cross-tool instruction-following experiment 共 15 份）
- shared_support: `3 Wave-0 baselines already landed: 00-shared-cursor-rules-official.md, 00-shared-claude-code-official.md, 00-shared-codex-agents-md-spec.md (all 2026-04-17)`
- primary_count: `14`
- primary_source_coverage: `primary_saturated_for_gate — the layered-structure question is now strongly anchored by fifteen topic references plus three shared baselines; non-OpenAI format-adoption is partially closed via Amp / Sourcegraph, GitHub Copilot broadens ecosystem support, public OSS usage is visible, Stripe adds non-tool-vendor enterprise-internal support, a GitHub-scale study strengthens broader diversity, OpenSpec adds a direct workflow/config comparison anchor, Cline/Continue/Aider show semantic divergence, Zhang et al. gives empirical rule-effect evidence, Gloaguen et al. / AGENTbench gives multi-agent context-file evaluation evidence, Umans AI gives same-repo practical cross-tool instruction-following evidence, and OctoBench adds formal scaffold-aware coding compliance benchmark evidence; continue only if an exact cross-tool AGENTS.md semantic conformance suite appears`
- secondary_count: `0`
- recent_count: `18`（shared 三基线 + topic-scoped 十五份均在 2024Q3–2026Q1 时间窗内）
- limitation_count: `3`（shared 中 AGENTS.md scope-neutrality / Claude context-bloat + topic-scoped one big AGENTS.md failure mode）
- topic_stop_decision: `continue`
- early_saturation_reason: `not_applicable`
- evidence_summary: `round_closed`
- question_list: `round_closed`
- status: `closed_for_current_round`
- gap: `starter pack plus enterprise-internal usage, adoption breadth, direct workflow/config comparison, semantic divergence evidence, empirical rule-effect/failure evidence, multi-agent context-file evaluation, formal scaffold-aware compliance benchmark evidence, and practical cross-tool instruction-following experiment landed via OpenAI Codex adopter case + OpenAI harness engineering failure/mechanism article + GitHub Spec Kit official + GitHub Copilot AGENTS.md support + Kiro official workflow + Amp / Sourcegraph AGENTS.md format-convergence case + OpenWork OSS public usage + Stripe Minions enterprise-internal case + GitHub-scale adoption study + OpenSpec direct comparison + Cline/Continue/Aider rule-loading semantics comparison + Zhang et al. 2026 rule-effect study + Gloaguen et al. 2026 AGENTbench evaluation + OctoBench scaffold-aware coding benchmark + Umans AI same-repo AGENTS.md following experiment; exact cross-tool AGENTS.md semantic conformance suite remains explicitly deferred after targeted search`

When `topic_stop_decision = suspend / archive / redirect`, add or update the matching record in `Suspended Branches`. When `topic_stop_decision = early_saturation`, keep `early_saturation_reason` explicit even if no separate branch record is needed.

## Wave 2：跨主题综合

- synthesis_file: `round-closed at requirements_engineering/deep_research_topics/_artifacts/W2-cross-topic-synthesis.md`
- cross_checks_done: `9 pre-defined checks filled with evidence pointers, final labels, and residual risk notes for the closed current round`
- unresolved_conflicts: `closed-round conflict register: story ambiguity vs GtWR precision; spec-driven promise vs hard-to-review risk; AGENTS adoption vs semantic consistency; standards full-text paywall; model-layer official positioning vs tool/adoption maturity`
- status: `closed_for_current_round`

## Readiness Check

- 30_second_local_evidence_retrieval: `pass`（_INDEX.md total = 74；12 条 shared authoritative copies + 62 条 topic-scoped AC 可检索；related_topic 列支持跨主题查找）
- mechanism_trend_difficulty_check: `pass_with_deferred_gaps`（机制层已覆盖 Story / EARS / BDD / agent-format / Spec Kit-Kiro / OpenSpec direct comparison / rule-loading semantic divergence / rule-effect study / multi-agent context-file evaluation / formal scaffold-aware coding compliance benchmark / practical cross-tool instruction-following experiment / acceptance-governance framework / same-prototype Story-DMN-Gherkin chain / independent design-to-code adoption census / governance / SysML v2 model layer；趋势与难度仍有 Topic 01 production/outcome maturity、Topic 02 Chapter 14 full discussion / Beck verbatim full text、Topic 03 SaaS empirical EARS、Topic 04 independent production outcome verification、Topic 05 EARS-inclusive high-compliance same-project governance case、Topic 06 exact cross-tool AGENTS.md semantic conformance suite 等 deferred upgrade gaps）
- cross_topic_synthesis_check: `pass_round_closed`
- topology_stability_check: `pass`（6 条研究线稳定，topology_sync_state = synced）
- handoff_continuity_check: `pass`（plan/status/queue + 74 份 AC + 6 evidence summaries + 6 question lists + 3 W2 artifacts + 6 packaged topic seeds 可交接；queue 当前停在 user-directed deferred-gap reopen，恢复时回读 _INDEX.md + queue 即可继续）
- overall_status: `closed_for_current_round_with_deferred_gap_register_frozen`

## Suspended Branches

记录所有非主线分支处置，不只包含 `suspended`。

- none_recorded_yet: `yes`

When first real disposition appears, delete `none_recorded_yet` and add exactly these fields: `branch / state / why / confirmed_so_far / still_missing / reopen_trigger`.

## Failed Explorations

只记录有代表性的失败探索，避免后续重复无效路径。

- exploration: `Topic 03 post-RE09 primary upgrade — attempted direct retrieval of RE2016 "Listens learned (8 lessons learned applying EARS)" and adjacent official mirrors`
- why_tried: `queue.current_task expected a post-2009 / around-2016 Mavin guideline or lessons-learned source stronger than the shared RE'09 anchor`
- what_found: `ResearchGate direct PDF returned 403 (Cloudflare); INCOSE RWG Jan-2022 PDF returned 403 challenge; public web did yield a 2019 official "Definitive Guide" PDF and the 2023 MDU paper reference list explicitly citing the 2016 IEEE RE paper`
- why_failed: `public mirrors for the 2016 conference paper are challenge-protected or not openly accessible from this environment`
- lesson: `use the accessible 2019 official guide as an interim Tier-B post-RE09 anchor, keep explicit risk notes that RE2016 full text is still upgrade-pending, and avoid claiming verbatim 2016 lessons without the paper body`

- exploration: `Topic 03 SaaS / non-safety empirical case pass — attempted retrieval of credible public software / web / SaaS EARS cases`
- why_tried: `queue.current_task required either landing a SaaS/software empirical case or explicitly deferring the gap after a documented search pass`
- what_found: `search results yielded official software-scope guidance, academic/privacy-adjacent papers, teaching artifacts, and vendor/blog examples, but no sufficiently strong public non-vendor SaaS empirical case that clearly documents EARS use in production software requirements`
- why_failed: `available public results were either off-domain, too weak, too indirect, or lacked reliable case specificity for this round's evidence threshold`
- lesson: `keep Topic 03 at software-scope-supported / saas-empirical-pending; do not promote blog-level or teaching-level examples into authoritative-copy evidence just to satisfy the queue`

- exploration: `Topic 03 SaaS / non-safety empirical recheck after Topic 06 continuation`
- why_tried: `queue.current_task was re-promoted after Topic 06 enterprise-internal closure; needed one more targeted academic/official search pass before rolling forward`
- what_found: `repeat targeted searches again surfaced software-scope guidance, PLC/industrial papers, academic index pages, and weak vendor/teaching examples, but still no sufficiently strong public non-vendor SaaS/software production case`
- why_failed: `the publicly accessible evidence base remains too weak or too indirect for this round's authoritative-copy threshold`
- lesson: `retain the same boundary: software-scope-supported; saas-empirical-pending; avoid cycling on the same weak search space unless a new primary lead appears`

- exploration: `Topic 01 SysML v2 production/outcome maturity pass after validation-use upgrade`
- why_tried: `queue.current_task required either landing a stronger production/outcome source or explicitly deferring after search; Topic 01 already had official positioning, tool ecosystem, participation, metadata, and Productive4.0 validation-use evidence`
- what_found: `search surfaced OMG final-adoption vendor/tool availability signals, SysML v2 case-study metadata, collaborative MBSE investigations, and academic/prototype validation papers, but no sufficiently strong public non-defense production rollout or quantified outcome source beyond validation/prototype level`
- why_failed: `available public sources were mainly tool-availability, participation, vendor positioning, or validation/prototype signals; none met this round's threshold for production/outcome maturity`
- lesson: `retain Topic 01 as official-positioning/tool-ecosystem/participation/validation-supported; production-outcome-maturity-pending. Do not inflate final-adoption press quotes or tool availability into outcome evidence.`

- exploration: `Topic 04 independent multimodal production adoption census after AI4UI enterprise benchmark`
- why_tried: `queue.current_task required either landing an independent production adoption census / real deployment case or explicitly deferring after search; Topic 04 already had official workflow, hosted case, independent design study, and enterprise benchmark evidence`
- what_found: `search surfaced Figma AI report/sponsored studies, general enterprise AI coding adoption studies, design-to-code benchmarks, production-grade frontend framework papers, and weak market-stat pages, but no sufficiently strong independent adoption census specifically for multimodal requirements/design-to-production workflows`
- why_failed: `available sources were either vendor-sponsored/survey-level, generic coding-agent adoption rather than multimodal design/spec-to-code, or benchmark/framework studies rather than real deployment/adoption census`
- lesson: `retain Topic 04 as workflow/hosted-outcome/independent-study/enterprise-benchmark-supported; independent production adoption census pending. Do not substitute generic AI coding adoption for multimodal requirements/design-to-code adoption.`

- exploration: `Topic 02 Chapter 14 full discussion / Beck full-text revisit`
- why_tried: `queue.current_task required either landing a stronger Chapter 14 discussion or Beck full-text-adjacent source, or explicitly deferring after search; Topic 02 already had O'Reilly preview, InformIT taxonomy TOC, Beck/Fowler preview anchors, Cohn 2024 one-smell discussion, and Mountain Goat common-problems taxonomy`
- what_found: `targeted searches surfaced existing official publisher previews, official TOC pages, weak search snippets, non-official mirrors, and generic summaries, but no stronger legal/open official or high-trust source that captured Chapter 14 full discussion or Beck original text beyond current ACs`
- why_failed: `available stronger-looking materials were either paywalled, preview-limited, non-official mirrors, or not sufficiently attributable for this round's authoritative-copy threshold`
- lesson: `retain Topic 02 as preview/taxonomy/one-smell/common-problems supported; Chapter 14 full discussion and Beck full-text remain deferred. Do not promote non-official mirrors or snippets into AC evidence.`

- exploration: `Topic 06 formal cross-tool semantic conformance suite revisit`
- why_tried: `queue.current_task required either landing one formal cross-tool semantic conformance suite for agent rules/instruction files or explicitly deferring after search; Topic 06 already had OpenSpec workflow comparison, Cline/Continue/Aider semantic divergence, Zhang et al. rule-effect evidence, and AGENTbench multi-agent context-file evaluation`
- what_found: `targeted searches surfaced no formal conformance suite or semantic oracle for same instruction artifacts across multiple coding agents; the strongest additional source found was Umans AI's same-repo / same-task / same-rules practitioner experiment comparing AGENTS.md / CLAUDE.md following across Codex CLI, Claude Code, Gemini CLI, and Cursor`
- why_failed: `the Umans AI experiment is conformance-adjacent but not formal: it is a practitioner blog, one codebase/task family, limited configurations, and no reusable semantic suite or formal oracle`
- lesson: `retain Topic 06 as practical-cross-tool-instruction-following-experiment-supported and formal-cross-tool-conformance-suite-pending. Do not inflate AGENTbench or practitioner same-repo experiments into formal semantic conformance.`

- exploration: `Topic 05 EARS-inclusive high-compliance same-project governance case revisit`
- why_tried: `queue.current_task required either landing one stronger EARS-inclusive high-compliance same-project governance case or explicitly deferring after search; Topic 05 already had OMG DMN official boundary, FlowForge same-prototype BPMN/DMN -> User Story/Gherkin evidence, and ISTQB acceptance-governance framework`
- what_found: `targeted searches surfaced weak wiki/vendor/tool pages, generic EARS/Gherkin mentions, and already-covered adjacent evidence, but no public strong source that documents EARS plus Story/Example/Gherkin/DMN governance in one high-compliance project`
- why_failed: `available materials were either too generic, not same-project, not EARS-inclusive, not governance/compliance oriented, or below this round's authoritative-copy threshold`
- lesson: `retain Topic 05 as DMN-boundary-supported / same-prototype-story-dmn-gherkin-supported / acceptance-governance-framework-supported, with EARS-inclusive-high-compliance-same-project-case-pending. Do not inflate tool docs or generic mapping articles into same-project governance evidence.`

- exploration: `Topic 03 SaaS / non-safety EARS empirical case revisit`
- why_tried: `queue.current_task required either landing one stronger non-safety software / SaaS empirical EARS source or explicitly deferring after search; Topic 03 already had software-scope guidance plus PLC/industrial empirical evidence`
- what_found: `targeted searches surfaced general software-scope pages, PLC/industrial studies, EARS template identification / detection papers, vendor pages, wiki pages, and teaching examples, but no qualified public SaaS or non-safety software production case that documents EARS adoption in real requirements work`
- why_failed: `available materials were either not empirical production cases, not SaaS/non-safety software, too generic, or below this round's authoritative-copy threshold`
- lesson: `retain Topic 03 as software-scope-supported / saas-empirical-pending. Do not substitute EARS classifier papers, vendor documentation, or teaching examples for production SaaS empirical evidence.`

- exploration: `Topic 01 SysML v2 production/outcome maturity revisit`
- why_tried: `queue.current_task required either landing one stronger public production rollout or quantified outcome source or explicitly deferring after search; Topic 01 already had official SysML v2 positioning, tools ecosystem, DoD transition guidance, Collins industrial signal, automotive metadata, end-user organization participation, and Productive4.0 validation use-case`
- what_found: `targeted searches again surfaced official/tool ecosystem pages, transition and vendor/tool availability signals, SysML v2 case metadata, pilot/prototype/validation projects, and active-development / not-production-ready caveats, but no qualified public production rollout or quantified outcome case`
- why_failed: `available public materials remained tool availability, participation, transition, validation, or pilot evidence rather than public production/outcome maturity evidence`
- lesson: `retain Topic 01 as official-positioning/tool-ecosystem/transition/participation/validation-supported with production-outcome-maturity-pending. Do not inflate SysML v2 final-adoption, tool lists, or validation pilots into production maturity.`

- exploration: `Topic 06 formal conformance-suite periodic recheck after Topic 01 deferral`
- why_tried: `queue.current_task was re-promoted after Topic 01 production/outcome maturity revisit; needed one later search pass before round closeout`
- what_found: `later targeted searches still found no exact cross-tool AGENTS.md / CLAUDE.md semantic conformance suite, but did surface OctoBench, a 2026 academic benchmark for scaffold-aware instruction following in repository-grounded agentic coding with objective checklists, full trajectory capture, and automated scoring`
- why_failed: `OctoBench is a formal scaffold-aware compliance benchmark, not a semantic-conformance oracle for the same instruction artifacts across multiple coding agents/tools`
- lesson: `upgrade Topic 06 to formal-scaffold-aware-coding-compliance-benchmark-supported while retaining cross-tool-AGENTS-md-semantic-conformance-suite-pending`

When first representative miss appears, delete `none_recorded_yet` and add exactly these fields: `exploration / why_tried / what_found / why_failed / lesson`.

## Resume Checkpoint

这里记录恢复上下文；下一步动作一律回读 `requirements_engineering/plan/dr-round-1.queue.md`，不要在此处复制第二份 active queue。

- last_completed_step: `Formal round closeout completed 2026-04-18: packaged deliverables, W2 artifacts, evidence summaries, question lists, and source-of-record files were all advanced to closed-for-current-round state without reopening evidence collection.`
- last_verified_result: `docs_landed = 74 total (12 shared + 62 topic-scoped); artifacts = 6 evidence summaries + 6 question lists + 3 W2 round-closed files; six topic seeds are packaged and handoff-ready; queue is parked on user-directed deferred-gap reopen.`
- safe_to_interrupt: `yes`
- queue_resume_entry: `read requirements_engineering/plan/dr-round-1.queue.md -> Active Queue`
- resume_precheck: `Confirm _INDEX.md total = 74, six evidence-summaries + six question-lists + three W2 round-closed artifacts exist, all six topic seeds contain packaged current-judgment sections, queue.current_task = user-directed deferred-gap reopen, and deferred gaps are frozen rather than silently treated as solved.`
- do_not_forget: `This round is formally closed, not merely packaging-complete. Deferred gaps remain explicit. Treat GtWR as upgraded-to-official-presentation level, not full-PDF verbatim capture; treat 29148 as scope-level official anchor, not clause-level text; treat OctoBench as formal scaffold-aware benchmark evidence, not exact AGENTS.md semantic conformance.`

## Worklog

- instantiation completed in previous turn
- execution entry initiated 2026-04-17: created `_reference/README.md` + `_reference/_INDEX.md` + `_artifacts/README.md` + `topic-06-agent-format.md` seed stub
- navigation surfaces updated 2026-04-17: `deep_research_topics/README.md` (6-topic structure + execution-round pointers), `references-by-topic.md` (Topic 6 section), `claims-audit.md` (topic-06 cross-reference)
- gate advanced 2026-04-17: `instantiation_complete -> setup_ready`; current_mode flipped to execution; Wave 0 status = in_progress
- Wave 0 first Tier A landed 2026-04-17: `_reference/00-shared-incose-gtwr-v4-summary.md` — INCOSE GtWR v4 (INCOSE-TP-2010-006-04, 2023-06) summary with 15 characteristics + 42 rules + cross-product alignment; `_INDEX.md` total 1 / tier-A 1
- Wave 0 second Tier A landed 2026-04-17: `_reference/00-shared-iso-iec-ieee-29148-2018.md` — ISO/IEC/IEEE 29148:2018 scope + construct-of-good-requirement + characteristics + cross-standard alignment captured from IEEE SA/ISO catalog pages (full text paywalled)
- Wave 0 third Tier A landed 2026-04-17: `_reference/00-shared-mavin-2009-ears-re09.md` — Mavin 2009 RE'09 EARS paper + author official guide: five patterns (Ubiquitous / State-driven / Event-driven / Optional Feature / Unwanted Behaviour) + Complex pattern + ruleset + industrial adoption
- Wave 0 Topic 06 baseline 1/3 landed 2026-04-17: `_reference/00-shared-cursor-rules-official.md` — Cursor Rules official docs: Project/User/Team/AGENTS.md four-tier model, .mdc schema, Always/AutoAttached/AgentRequested/Manual activation modes, nesting rules, limitations
- Wave 0 Topic 06 baseline 2/3 landed 2026-04-17: `_reference/00-shared-claude-code-official.md` — Anthropic Claude Code best practices + CLAUDE.md memory guidance + Skills/Subagents/Plugins/Hooks architecture + context-rot caveat as limitation anchor
- Wave 0 Topic 06 baseline 3/3 landed 2026-04-17: `_reference/00-shared-codex-agents-md-spec.md` — AGENTS.md open format spec (Linux Foundation Agentic AI Foundation stewardship, 20,000+ GitHub repos adoption as of 2025-09) + OpenAI Codex CLI integration (global/project/override discovery, byte limits)
- Wave 0 KOL anchors landed 2026-04-17: `_reference/00-shared-fowler-user-story-bliki.md` (XP origin, INVEST via Wake, As-a/I-want/So-that, Cohn book locked as standard) + `_reference/00-shared-fowler-given-when-then-bliki.md` (GWT = Dan North & Chris Matts BDD, equivalence to Four-Phase Test / Arrange-Act-Assert, Gherkin distinction)
- Wave 0 BDD syntax anchor landed 2026-04-17: `_reference/00-shared-gherkin-official-reference.md` — Cucumber official Gherkin reference: Feature/Rule/Example/Background/Scenario Outline + Given/When/Then/And/But/* + DocStrings / DataTables + 70+ language localisation + "1922 rule" for When steps
- Wave 0 story-method anchors landed 2026-04-17: `_reference/00-shared-cohn-user-stories-primer.md` (Mountain Goat primer + *User Stories Applied* 2004 standard book; 3C credited to Jeffries 2001; "story is not a requirements document"); `_reference/00-shared-patton-story-mapping-primer.md` (2008 "New User Story Backlog is a Map" + 2014 O'Reilly book; backbone / walking skeleton / car-MVP metaphor; "bag of context-free mulch" critique of flat backlogs)
- Wave 0 safety/limitation anchor landed 2026-04-17: `_reference/00-shared-iso-26262-part8-overview.md` — ISO 26262-8:2018 Part 8 Supporting Processes overview: Clause 6 (4 hard requirements: completeness/consistency/verifiability/unambiguity + bidirectional traceability) + Clause 11 (Tool Confidence Level TCL1/2/3, TI×TD matrix, why AI coding agents currently cannot be sole RM tool at ASIL-B+). Tier C due to ISO paywall; industry primer used for excerpt-level evidence only.
- Wave 0 Foundation Sufficiency Check passed 2026-04-17: floor 12/12, tier-A ≥ 3 (actual 5), limitation-source ≥ 2 (actual 3), 8 core working definitions locked, cross-topic bridges built via _INDEX.md related_topic column. Gate advanced: `setup_ready → wave0_complete → wave1_ready`. Next branch: Topic 03 (EARS) deep-dive.
- Wave 1 Topic 03 primary anchor landed 2026-04-18: `_reference/03-ears-uusitalo-2023-plc-empirical.md` — 2023 conference/workshop paper from MDU on EARS-based requirement formalization and PLC testing; key findings captured: different authors choose different patterns, completeness is the most common problem, and EARS-based PLC testing is applicable.
- Wave 1 Topic 03 post-RE09 guide landed 2026-04-18: `_reference/03-ears-mavin-2016-ears-guidelines.md` — accessible 2019 official EARS guide plus explicit bibliographic trace to RE2016 "Listens learned"; captured training/coaching advice, "when not to use EARS", and over-complexity / >3 preconditions boundaries; full RE2016 text remains pending.
- Wave 1 Topic 03 industrial primer landed 2026-04-18: `_reference/03-ears-jama-industrial-primer.md` — Jama official webinar deck with Mav; captured EARS patterns, `gently constrains` framing, and tooling signal that Requirements Advisor analyzes both EARS patterns and INCOSE rules.
- Wave 1 Topic 03 artifact seeded 2026-04-18: `_artifacts/03-ears-evidence-summary.md` created with scope, landed evidence, current judgments, remaining must-answer gaps, and next deep-dive questions. `_reference/_INDEX.md` refreshed to total 15 with topic-03 quick-count = 3. Queue promoted: Topic 06 current / Topic 02 next / Topic 05 next_after_next.
- Wave 1 Topic 06 adopter case landed 2026-04-18: `_reference/06-agent-format-openai-codex-adoption.md` — OpenAI "How OpenAI uses Codex" case study; captured internal-adoption signal that engineers paste `user request or spec` to Codex, use Ask Mode -> Code Mode, and let background agent work continue through meetings.
- Wave 1 Topic 06 failure/mechanism anchor landed 2026-04-18: `_reference/06-agent-format-openai-harness-engineering.md` — OpenAI harness engineering article; captured `one big AGENTS.md` failure, `AGENTS.md as table of contents`, docs-as-system-of-record, and `plans are treated as first-class artifacts`.
- Wave 1 Topic 06 feature-workflow anchors landed 2026-04-18: `_reference/06-agent-format-github-spec-kit-official.md` + `_reference/06-agent-format-kiro-spec-workflow-official.md` — official evidence that feature-level workflows are carried by `spec/plan/tasks` or `requirements/design/tasks`, not by bloated team-level instruction files; Kiro explicitly places EARS in requirements phase.
- Wave 1 Topic 06 artifact seeded 2026-04-18: `_artifacts/06-agent-format-evidence-summary.md` created with layered-structure judgment (`team/repo contract` vs `scoped rules` vs `feature-level workflow`), remaining gaps, and next deep-dive questions. `_reference/_INDEX.md` refreshed to total 19 with topic-06 quick-count = 4. Queue promoted: Topic 02 current / Topic 05 next / Topic 01 next_after_next.
- Wave 1 Topic 02 book-level anchor landed 2026-04-18: `_reference/02-user-story-cohn-book-excerpts.md` — official `User Stories Applied` book page + sample chapter; captured canonical chapter topology (`Writing Stories`, `Acceptance Testing User Stories`, `What Stories Are Not`, `Story Smells`) and explicit INVEST adoption.
- Wave 1 Topic 02 original INVEST anchor landed 2026-04-18: `_reference/02-user-story-wake-invest-original.md` — Bill Wake 2003 original article; captured `Cards / Conversation / Confirmation`, INVEST original authorship, and story-as-pidgin-language framing.
- Wave 1 Topic 02 recent KOL revisit landed 2026-04-18: `_reference/02-user-story-mike-cohn-ai-era.md` — 2024 revisiting-user-stories podcast + 2026 AI story writing post; captured `meaningful conversations`, details-moving-to-acceptance-criteria, and AI-as-partner-not-replacement stance.
- Wave 1 Topic 02 artifact seeded 2026-04-18: `_artifacts/02-user-story-evidence-summary.md` created with story-method boundary judgment, remaining must-answer gaps, and next deep-dive questions. `_reference/_INDEX.md` refreshed to total 22 with topic-02 quick-count = 3. Queue promoted: Topic 05 current / Topic 01 next / Topic 04 next_after_next.
- Wave 1 Topic 05 method anchor landed 2026-04-18: `_reference/05-integration-bdd-adzic-specification-by-example.md` — Gojko official book page + 10-year follow-up; captured `over 50 projects`, `bridge the communication gap`, living documents, and examples-as-source-of-truth framing.
- Wave 1 Topic 05 family-boundary anchor landed 2026-04-18: `_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md` — Matt Wynne official books page + Cucumber example-guided-development post; captured `The Cucumber Book` metadata and xDD-family convergence around examples.
- Wave 1 Topic 05 workflow/case anchor landed 2026-04-18: `_reference/05-integration-bdd-cucumber-discovery-formulation-case.md` — Cucumber official BDD docs + Example Mapping docs + collaboration article + global investment bank case; captured `Discovery / Formulation / Automation`, yellow-blue-green-red card structure, and PO-written acceptance tests translated to Gherkin.
- Wave 1 Topic 05 artifact seeded 2026-04-18: `_artifacts/05-integration-bdd-evidence-summary.md` created with examples-layer judgment, remaining gaps, and next deep-dive questions. `_reference/_INDEX.md` refreshed to total 25 with topic-05 quick-count = 3. Queue promoted: Topic 01 current / Topic 04 next / Topic 03-upgrade next_after_next.
- Wave 1 Topic 01 systems-engineering anchor landed 2026-04-18: `_reference/01-re-landscape-sebok-system-requirements-definition.md` — SEBoK pages on Business or Mission Analysis, System Requirements Definition, and Requirements Management; captured mission/problem framing, stakeholder-to-technical transformation, and traceability lifecycle.
- Wave 1 Topic 01 lifecycle anchor landed 2026-04-18: `_reference/01-re-landscape-iso-iec-ieee-15288-2023-overview.md` — ISO/IEC/IEEE 15288:2023 official overview; captured full life-cycle coverage, process-framework positioning, and method-neutral stance.
- Wave 1 Topic 01 use-case contrast anchor landed 2026-04-18: `_reference/01-re-landscape-use-case-2-0-official.md` — Ivar Jacobson International Use-Case 2.0 official pages; captured `use-case slices`, the boundary with user stories, and large-scale/regulated-domain applicability.
- Wave 1 Topic 01 artifact seeded 2026-04-18: `_artifacts/01-re-landscape-evidence-summary.md` created with map-structure judgment, remaining gaps, and next deep-dive questions. `_reference/_INDEX.md` refreshed to total 28 with topic-01 quick-count = 3. Queue promoted: Topic 04 current / Topic 03-upgrade next / Topic 05-upgrade next_after_next.
- Wave 1 Topic 04 workflow-signal anchors landed 2026-04-18: `_reference/04-future-trends-github-spec-kit-official.md` + `_reference/04-future-trends-kiro-spec-workflow-official.md` — official signals that spec-driven / IDE-native specs are now explicit workflows rather than pure conjecture.
- Wave 1 Topic 04 governance anchor landed 2026-04-18: `_reference/04-future-trends-ai-governance-nist-eu-ai-act.md` — official NIST AI RMF 1.0 + EU AI Act signals; captured technical documentation, logs, traceability, and human oversight obligations that strengthen the case for structured specification artifacts.
- Wave 1 Topic 04 trend-signal anchor landed 2026-04-18: `_reference/04-future-trends-thoughtworks-spec-driven-development-signal.md` — Technology Radar Vol.33 placed spec-driven development in Assess, while also recording elaborate/opinionated/hard-to-review limitations.
- Wave 1 Topic 04 artifact seeded 2026-04-18: `_artifacts/04-future-trends-evidence-summary.md` created with spec-driven / governance / IDE-native trend judgments, remaining gaps, and next deep-dive questions. `_reference/_INDEX.md` refreshed to total 32 with topic-04 quick-count = 4. Queue promoted: Topic 03-upgrade current / Topic 05-upgrade next / Wave 2 scaffold next_after_next.
- Shared-risk upgrade on GtWR completed 2026-04-18: `00-shared-incose-gtwr-v4-summary.md` upgraded from reqi-only dependency to `official webinar presentation + reqi detail fill` level; explicit decision recorded that Wave 1 / Wave 2 may proceed with primer-level official anchor while preserving `full technical product PDF pending` risk note.
- Shared-risk decision on 29148 completed 2026-04-18: `00-shared-iso-iec-ieee-29148-2018.md` remains at official scope/catalog level; explicit acceptance recorded that clause-level text is still paywalled and pending, so strong clause-by-clause assertions remain risk-noted rather than blocked.
- Wave 1 question-list seeding completed 2026-04-18: `_artifacts/01-re-landscape-question-list.md`, `_artifacts/02-user-story-question-list.md`, `_artifacts/03-ears-question-list.md`, `_artifacts/04-future-trends-question-list.md`, `_artifacts/05-integration-bdd-question-list.md`, `_artifacts/06-agent-format-question-list.md` all created; all six research lines now have evidence-summary + question-list pairs.
- Wave 1 stop-assessment pass completed 2026-04-18: all six lines explicitly dispositioned as `continue`; 01 / 04 / 05 / 06 marked `primary_saturated_for_gate`; 02 / 03 remain `starter_covered` with high-value gaps.
- Wave 2 scaffold seeded 2026-04-18: `_artifacts/W2-cross-topic-synthesis.md`, `_artifacts/W2-claims-audit-v2.md`, `_artifacts/W2-selection-matrix-v2.md` created as skeletons; Wave 2 status set to `seeded`, not complete.
- Wave 2 first-pass synthesis drafted 2026-04-18: `W2-cross-topic-synthesis.md` X1-X9 filled with judgments/risk labels; `W2-selection-matrix-v2.md` first-pass decision rules and evidence pointers added; `W2-claims-audit-v2.md` first-pass audit decisions added.
- Wave 2 second-pass / seed backfill completed 2026-04-18: `W2-selection-matrix-v2.md` got weighting guidance, scenario recommendations, and residual risk labels; `W2-claims-audit-v2.md` got final-use recommendations; `topic-04-future-trends-and-evidence.md` §4.6 and `topic-06-agent-format.md` backfill sections updated.
- Topic 01 high-value gap closed 2026-04-18: `_reference/01-re-landscape-omg-sysml-v2-official.md` added; MBSE / SysML v2 official positioning now starter-covered, leaving tool maturity / industrial adoption as the remaining upgrade axis. `_reference/_INDEX.md` total = 33 at that step.
- Topic 06 high-value gap closed 2026-04-18: `_reference/06-agent-format-amp-agents-md-adoption.md` added; non-OpenAI AGENTS.md format-adoption now partially covered via Amp / Sourcegraph, leaving non-tool-vendor enterprise usage as the remaining adopter-diversity upgrade. `_reference/_INDEX.md` total = 34.
- Wave 2 final-candidate and readiness pass completed 2026-04-18: `W2-cross-topic-synthesis.md` status moved to `final_candidate`; selection matrix and claims audit residual-risk labels updated for SysML v2 / Amp additions; Readiness Check passed for current round with explicit deferred-gap register.
- Topic 05 deferred gap upgraded 2026-04-18: `_reference/05-integration-bdd-omg-dmn-decision-boundary.md` added; decision-table / DMN ↔ EARS object boundary is now starter-covered via OMG official positioning plus EARS official “when not to use” guidance. `_reference/_INDEX.md` total = 35.
- Topic 03 deferred gap narrowed 2026-04-18: `_reference/03-ears-software-scope-guidance.md` added; EARS software applicability is now officially supported for low-level software / IT textual requirements, leaving SaaS empirical evidence as the remaining domain-extension gap. `_reference/_INDEX.md` total = 36.
- Topic 02 deferred gap narrowed 2026-04-18: `_reference/02-user-story-xp-origins-cockburn-boundary.md` added; XP/C3 roots and Cockburn use-case boundary are now starter-covered, leaving Beck original text and story subtype boundaries as the remaining Topic 02 upgrade gaps. `_reference/_INDEX.md` total = 37.
- Topic 04 deferred trend axes upgraded 2026-04-18: `_reference/04-future-trends-figma-make-multimodal-signal.md` + `_reference/04-future-trends-w3c-shacl-graph-constraints.md` added; multimodal input and graph/constraint substrate are now starter-covered, leaving requirements-specific adoption cases as the remaining Topic 04 upgrade gap. `_reference/_INDEX.md` total = 39.
- Topic 06 deferred gap narrowed 2026-04-18: `_reference/06-agent-format-openwork-oss-usage.md` added; AGENTS.md is now supported not only by tool-vendor announcements but also by a public OSS usage case with separate PRD workflow, leaving non-tool-vendor enterprise-internal usage as the remaining adoption gap. `_reference/_INDEX.md` total = 40.
- Topic 02 subtype boundary upgraded 2026-04-18: `_reference/02-user-story-subtypes-job-spike-enabler.md` added; Job Story / Spike / Enabler are now starter-covered as adjacent work-item types, leaving Beck original text and deeper Story Smells / What Stories Are Not extracts as the main Topic 02 upgrade gaps. `_reference/_INDEX.md` total = 41.
- Topic 01 maturity gap narrowed 2026-04-18: `_reference/01-re-landscape-omg-sysml-v2-tools-ecosystem.md` added; SysML v2 now has not only official positioning but also official tool-ecosystem support, leaving broad industrial adoption maturity as the remaining Topic 01 gap. `_reference/_INDEX.md` total = 42.
- Topic 02 deeper-text gap narrowed 2026-04-18: `_reference/02-user-story-beck-planning-xp-previews.md` added; Beck/Fowler XP planning literature now has preview-level local anchors for `Writing Stories` and `task cards`, leaving full-text Beck excerpts and deeper Story Smells / What Stories Are Not content as the remaining Topic 02 gap. `_reference/_INDEX.md` total = 43.
- Topic 04 graph axis upgraded 2026-04-18: `_reference/04-future-trends-kg-empire-re-knowledge-graph.md` added; graph/knowledge-graph trend is now supported not only by W3C substrate but also by a requirements-engineering-specific research artifact, leaving industrial/product-side adoption as the remaining Topic 04 gap. `_reference/_INDEX.md` total = 44.
- Topic 04 enterprise graph signal upgraded 2026-04-18: `_reference/04-future-trends-ibm-enterprise-requirements-kg.md` added; graph/knowledge-graph trend is now supported not only by substrate and RE research artifacts but also by an enterprise customer-requirements use case, leaving broader product-development adoption as the remaining Topic 04 gap. `_reference/_INDEX.md` total = 45.
- Topic 06 ecosystem breadth upgraded 2026-04-18: `_reference/06-agent-format-github-copilot-agents-md-support.md` added; AGENTS.md is now supported across a broader tool ecosystem, leaving non-tool-vendor enterprise-internal usage as the main remaining Topic 06 gap. `_reference/_INDEX.md` total = 46.
- Topic 06 enterprise-internal usage upgraded 2026-04-18: `_reference/06-agent-format-stripe-minions-enterprise-usage.md` added; non-tool-vendor enterprise-internal coding-agent usage is now publicly supported via Stripe's Minions case, leaving broader enterprise-diversity / tool-comparison hardening as the remaining Topic 06 gap. `_reference/_INDEX.md` total = 47.
- Topic 03 SaaS empirical pass deferred 2026-04-18: no sufficiently strong public non-vendor SaaS/software EARS case was found in this pass; gap retained as `software-scope-supported; saas-empirical-pending` rather than weakened with low-quality evidence. Queue promoted to Topic 02 deeper-text gap.
- Topic 03 SaaS empirical recheck deferred 2026-04-18: another targeted academic/official search pass still found no sufficiently strong public non-vendor SaaS/software EARS case; gap remains `software-scope-supported; saas-empirical-pending` and queue rolled forward to Topic 01 broad adoption maturity.
- Topic 01 broad-adoption maturity upgraded 2026-04-18: `_reference/01-re-landscape-dod-sysml-v2-transition-guidance.md` added; SysML v2 now has not only OMG official positioning and tools ecosystem signal, but also external official transition guidance from DoD, leaving second-source broad industrial adoption maturity as the remaining Topic 01 gap. `_reference/_INDEX.md` total = 48.
- Topic 04 broader product-development graph adoption upgraded 2026-04-18: `_reference/04-future-trends-bmw-virtual-product-development-kg.md` added; graph/knowledge-graph trend is now supported not only by substrate, RE research, and enterprise customer-requirements matching, but also by a BMW virtual product-development collaboration case, leaving broader multimodal adoption as the more prominent Topic 04 gap. `_reference/_INDEX.md` total = 49.
- Topic 06 broader diversity upgraded 2026-04-18: `_reference/06-agent-format-github-adoption-study-2026.md` added; coding-agent adoption is now supported not only by OpenAI/Stripe/OpenWork cases but also by a GitHub-scale study spanning project maturity, established organizations, and diverse languages/topics, leaving direct cross-tool workflow/config comparison as the stronger remaining Topic 06 gap. `_reference/_INDEX.md` total = 50.
- Topic 02 anti-pattern boundary upgraded 2026-04-18: `_reference/02-user-story-cohn-2004-intro-slides.md` added; user story is now supported not only by book-structure inference but also by Cohn's direct wording that stories are placeholders for future conversations, not written contracts, not fixed requirements, and not use cases, leaving Story Smells detail and Beck full-text as the stronger remaining Topic 02 gaps. `_reference/_INDEX.md` total = 51.
- Topic 01 second-source adoption signal upgraded 2026-04-18: `_reference/01-re-landscape-collins-sysml-v2-provers.md` added; SysML v2 now has not only government transition guidance but also a defense-industry implementation/adoption signal from Collins Aerospace / DARPA PROVERS, leaving non-defense broad industrial maturity as the remaining Topic 01 gap. `_reference/_INDEX.md` total = 52.
- Topic 04 broader multimodal adoption upgraded 2026-04-18: `_reference/04-future-trends-vercel-v0-multimodal-prd-workflow.md` added; multimodal requirement/spec workflow is now supported not only by Figma Make but also by Vercel v0 screenshots/files/images/videos plus PRD-to-spec workflow, leaving adoption-outcome evidence as the more prominent Topic 04 multimodal gap. `_reference/_INDEX.md` total = 53.
- Topic 06 direct comparison upgraded 2026-04-18: `_reference/06-agent-format-openspec-cross-tool-comparison.md` added; Topic 06 now has an official cross-tool workflow/config comparison anchor spanning Spec Kit, Kiro, and 25+ tools, leaving semantic-consistency / precedence as the stronger remaining gap. `_reference/_INDEX.md` total = 54.
- Topic 02 Story Smells preview upgraded 2026-04-18: `_reference/02-user-story-cohn-story-smells-preview.md` added; Topic 02 now has direct preview-level support for `What Stories Are Not` and one concrete `Story Smells` item, leaving fuller taxonomy and Beck full-text as the stronger remaining gaps. `_reference/_INDEX.md` total = 55.
- Topic 01 non-defense adoption signal upgraded 2026-04-18: `_reference/01-re-landscape-incose-automotive-sysml-v2-case-metadata.md` added; SysML v2 now has a bounded non-defense commercial/industrial automotive signal, leaving implementation-detail and broader industrial maturity as the remaining Topic 01 gaps. `_reference/_INDEX.md` total = 56.
- Topic 04 multimodal hosted outcome upgraded 2026-04-18: `_reference/04-future-trends-vercel-v0-stripe-outcomes.md` added; Topic 04 now has one named adoption/outcome case for app-building AI workflow, leaving broader non-hosted multimodal maturity as the stronger remaining gap. `_reference/_INDEX.md` total = 57.
- Topic 02 taxonomy visibility upgraded 2026-04-18: `_reference/02-user-story-cohn-story-smells-informit-toc.md` added; Topic 02 now has publisher-level visibility of the broader Story Smells taxonomy and Chapter 12 negative-boundary substructure, leaving fuller smell discussion and Beck full-text as the stronger remaining gaps. `_reference/_INDEX.md` total = 58.
- Topic 01 multi-org non-defense participation upgraded 2026-04-18: `_reference/01-re-landscape-sysml-v2-update-end-user-orgs.md` added; Topic 01 now has named non-defense end-user organizations beyond a single automotive metadata point, leaving implementation/outcome evidence as the stronger remaining maturity gap. `_reference/_INDEX.md` total = 59.
- Topic 04 independent multimodal outcome upgraded 2026-04-18: `_reference/04-future-trends-personagram-multimodal-design-study.md` added; Topic 04 now has an independent academic design-study outcome in addition to official workflow and hosted customer outcome, leaving enterprise production maturity as the stronger multimodal gap. `_reference/_INDEX.md` total = 60.
- Topic 06 semantic divergence upgraded 2026-04-18: `_reference/06-agent-format-rule-loading-semantics-comparison.md` added; Topic 06 now has official Cline/Continue/Aider evidence that rule-loading and precedence semantics differ across tools, leaving conformance/failure evidence as the stronger remaining gap. `_reference/_INDEX.md` total = 61.
- Topic 02 story-smell discussion upgraded 2026-04-18: `_reference/02-user-story-cohn-too-small-stories-2024.md` added; Topic 02 now has practical discussion-level support for the overly-small-stories smell, leaving multi-smell discussion and Beck full-text as the stronger remaining gaps. `_reference/_INDEX.md` total = 62.
- Topic 01 implementation-validation upgraded 2026-04-18: `_reference/01-re-landscape-productive40-sysml-v2-validation-use-case.md` added; Topic 01 now has a non-defense Industry 4.0 / chemical / IIoT SysML v2 validation use-case, leaving production/outcome maturity as the stronger remaining gap. `_reference/_INDEX.md` total = 63.
- Topic 04 enterprise benchmark upgraded 2026-04-18: `_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md` added; Topic 04 now has enterprise-grade multimodal design/spec-to-code benchmark evidence, leaving independent production adoption census as the stronger remaining gap. `_reference/_INDEX.md` total = 64.
- Topic 06 rule-effect/failure evidence upgraded 2026-04-18: `_reference/06-agent-format-rules-shape-or-distort-2026.md` added; Topic 06 now has a large empirical rule-file study showing both benefits and harmful rule types, leaving cross-tool conformance suite / multi-tool replication as the stronger remaining gap. `_reference/_INDEX.md` total = 65.
- Topic 02 common-problems taxonomy upgraded 2026-04-18: `_reference/02-user-story-mountain-goat-common-problems-taxonomy.md` added; Topic 02 now has practice-facing coverage of multiple story problems and non-story item boundaries, leaving Chapter 14 full discussion and Beck full-text as the stronger remaining gaps. `_reference/_INDEX.md` total = 66.
- Topic 01 production/outcome maturity deferred 2026-04-18: targeted search did not find a sufficiently strong public production rollout or quantified outcome source beyond tool-availability / validation evidence; gap remains `production-outcome-maturity-pending` and queue promoted to Topic 04 independent production adoption census. `_reference/_INDEX.md` total remains 66.
- Topic 04 independent production adoption census deferred 2026-04-18: targeted search did not find a sufficiently strong independent adoption census or real deployment case specifically for multimodal requirements/design-to-code workflows beyond hosted case / benchmark / generic coding-AI adoption evidence; gap remains `independent-production-adoption-pending` and queue promoted to Topic 06 conformance suite. `_reference/_INDEX.md` total remains 66.
- Topic 06 multi-agent context-file evaluation upgraded 2026-04-18: `_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md` added; Topic 06 now has AGENTbench / Evaluating AGENTS.md evidence across Claude Code, Codex, and Qwen Code showing repository-level context files are not automatically beneficial and can increase cost, leaving formal cross-tool semantic conformance suite as the remaining narrower gap. `_reference/_INDEX.md` total = 67.
- Topic 02 Chapter 14 / Beck full-text revisit deferred 2026-04-18: targeted search did not find a stronger legal/open official or high-trust Chapter 14 full-discussion or Beck full-text-adjacent source beyond current O'Reilly preview, InformIT taxonomy TOC, Beck/Fowler preview anchors, Cohn 2024 discussion, and Mountain Goat common-problems taxonomy; gap remains `chapter-14-full-discussion-pending; beck-full-text-pending` and queue promoted to Topic 05 same-project governance case. `_reference/_INDEX.md` total remains 67.
- Topic 05 same-project governance narrowed 2026-04-18: `_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md` + `_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md` added; Topic 05 now has same-prototype BPMN/DMN -> User Story/Gherkin evidence plus official acceptance-governance framework evidence, leaving EARS-inclusive high-compliance same-project case as the narrower residual gap. `_reference/_INDEX.md` total = 69.
- Topic 04 independent adoption census upgraded 2026-04-18: `_reference/04-future-trends-state-of-prototyping-2026.md` added; Topic 04 now has an independent open-data survey covering AI prototyping / design-to-code adoption across 1,478 designers/builders, leaving named real production deployment case or independently verified production outcome as the narrower multimodal residual gap. `_reference/_INDEX.md` total = 70.
- Topic 06 formal conformance-suite revisit completed 2026-04-18: targeted search did not find a formal cross-tool semantic conformance suite for agent rules/instruction files; `_reference/06-agent-format-umans-agents-md-following-experiment.md` added as conformance-adjacent practitioner evidence comparing same-repo `AGENTS.md` / `CLAUDE.md` following across Codex CLI, Claude Code, Gemini CLI, and Cursor; gap remains `formal-cross-tool-conformance-suite-pending` and queue promoted to Topic 02 Chapter 14 / Beck full-text revisit. `_reference/_INDEX.md` total = 71.
- Topic 02 Beck-adjacent origin/boundary upgraded 2026-04-18: `_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md` added; Topic 02 now has Seb Rose / ACCU Overload support for Beck 2004 Planning Game story origins, user-story terminology evolution, and Story-vs-BDD feature boundary, while Chapter 14 full discussion and Beck verbatim full text remain explicitly deferred. `_reference/_INDEX.md` total = 72.
- Topic 05 EARS-inclusive same-project governance revisit deferred 2026-04-18: targeted search did not find a qualified public EARS-inclusive high-compliance same-project governance case beyond current FlowForge prototype, ISTQB governance framework, OMG DMN boundary, and Cucumber/BDD evidence; gap remains `ears-inclusive-high-compliance-same-project-case-pending` and queue promoted to Topic 04 real production deployment case. `_reference/_INDEX.md` total remains 72.
- Topic 04 named real deployment case upgraded 2026-04-18: `_reference/04-future-trends-figma-make-findable-production-case.md` added; Topic 04 now has a Figma / Findable vendor-hosted app-shell deployment case with reported 50% faster delivery and 90%+ final product code from Figma Make, leaving independently verified production outcome as the narrower residual gap. `_reference/_INDEX.md` total = 73.
- Topic 03 SaaS / non-safety EARS empirical revisit deferred 2026-04-18: targeted search again did not find a qualified public SaaS or non-safety software production EARS case beyond existing software-scope guidance and PLC/industrial evidence; gap remains `saas-empirical-pending` and queue promoted to Topic 01 production/outcome maturity. `_reference/_INDEX.md` total remains 73.
- Topic 01 production/outcome maturity revisit deferred 2026-04-18: targeted search again did not find a qualified public SysML v2 production rollout or quantified outcome source beyond existing official positioning, tools ecosystem, transition guidance, participation, and validation/pilot evidence; gap remains `production-outcome-maturity-pending` and queue promoted to Topic 06 formal conformance-suite periodic recheck. `_reference/_INDEX.md` total remains 73.
- Topic 06 formal scaffold-aware benchmark upgraded 2026-04-18: `_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md` added; Topic 06 now has formal benchmark evidence for scaffold-aware coding compliance, leaving exact cross-tool `AGENTS.md` semantic conformance as the narrower residual gap. `_reference/_INDEX.md` total = 74.
- Readiness closeout / deferred-gap register freeze completed 2026-04-18: `_reference/_INDEX.md`, Topic 06 artifacts, W2 synthesis/matrix/claims audit, status, and queue were synchronized to 74 authoritative copies; current round is now stoppable with explicit deferred gaps on Topics 01/02/03/04/05/06.
- Final-deliverable packaging / cross-file polish completed 2026-04-18: all six topic seed files now expose the output-contract sections on top of the frozen evidence base, Topic 05 tail ordering and residual labels were normalized, and status/queue were advanced to `packaging_complete_for_current_round` with optional deferred-gap reopen parked as the next action.
- Formal round closeout completed 2026-04-18: current-state fields across status, queue, W2 artifacts, evidence summaries, and question lists were synchronized to `closed_for_current_round`; the round now ends cleanly with explicit deferred gaps and no remaining mandatory action.
