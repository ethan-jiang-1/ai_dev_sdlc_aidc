---
type: index
content_type: readme
directory: _raw_fable5
description: Fable 5 模型变革信号合成，从 16 个真实使用样本提取
derived_from: fable5_field_signals/
sample_count: 16
files_indexed: 4
research_date: 2026-07-07
---

# _raw_fable5 — Fable 5 变革信号：信息地图

> 来源库：`fable5_field_signals/`（16 个人物/组织样本）
> 研究日期：2026-07-07
> 核心问题：Fable 5 这个模型到底有什么不一样，导致软件开发流程可能要变？

---

## 先看这里

如果你第一次进这个目录，按这条路读：

1. 先看本文件（README）— 搞清楚三份 MD 分别是什么、来源是谁
2. 再看 `01_Fable5_颠覆了什么_核心信号.md` — 抓大局
3. 然后看 `02_流程变革_具体模式与检查清单.md` — 找具体怎么做
4. 最后看 `03_粗糙信号_早期观察与未成形想法.md` — 看还在冒烟的早期信号

如果你只读一份，读 `01`。

---

## 三份文件概览

| 文件 | 一句话 | 适合谁 |
|---|---|---|
| `01_Fable5_颠覆了什么_核心信号.md` | 10 个核心信号 + 12 条流程变革清单 | 想快速建立全局认知的人 |
| `02_流程变革_具体模式与检查清单.md` | AI Sandwich、Brief-Review-Signoff、不同阶段模型策略、治理 checklist | 想落地到团队流程的人 |
| `03_粗糙信号_早期观察与未成形想法.md` | 8 个弱信号 + 7 个开放问题 + 粗糙想法集合 | 想做研究/追踪/写后续的人 |

---

## 来源全量映射

以下记录了每份文件中的主要洞察分别来自哪些原始样本。

### `01_Fable5_颠覆了什么_核心信号.md` 的来源

| 信号 | 主要来源样本 | 补充来源 |
|---|---|---|
| 信号一：实时交互→离线委托 | `run_anthropic_mike_krieger/`（"wish Claude good night"）、`run_every_austin_tedesco/`（4 小时火箭炮项目）、`run_wharton_ethan_mollick/`（dozen hours） | `run_every_kieran_klaassen/`（AI Sandwich 默认主力） |
| 信号二：操作者→委托人 | `run_wharton_ethan_mollick/`（"I no longer steer; I commission"） | `run_anthropic_mike_krieger/`（"teammate I can delegate to"） |
| 信号三：Spec 取代代码 | `run_superpowers_jesse_vincent/`（"Specs are the thing that matters now"） | `run_anthropic_thariq_shihipar/`（实现计划前置） |
| 信号四：判断力/品味/多维思考 | `run_anthropic_boris_cherny/`（"judgment, taste, dimensionality"） | — |
| 信号五：无情地主动 | `run_datasette_simon_willison/`（$12 CSS debugging 全案例） | `run_generativeai_net_martin_musiol/`（"It takes problems whole"） |
| 信号六：角色边界打乱 | `run_anthropic_mike_krieger/`、`run_superpowers_jesse_vincent/`、`run_wharton_ethan_mollick/` | `ai_sdlc_frontier/raw_Anthropic_Fiona Fung/`（交叉验证） |
| 信号七：能力≠最好协作者 | `run_every_willie_williams/`（benchmark 赢但迭代体验差） | `run_mclayer_plugin_codeforge/`（外科手术式采用） |
| 信号八：AI Sandwich | `run_every_kieran_klaassen/`（命名者） | `run_superpowers_jesse_vincent/`（brief-review-signoff 同一模式） |
| 信号九：治理成为主问题 | `run_every_mike_taylor/`（NDA 硬边界）、`run_zed_richard_feldman/`（consent/retention/fallback）、`run_datasette_simon_willison/`（sandbox 生死线） | Anthropic policy 回滚事件 |
| 信号十：约束从 prompt 到 linter | `run_superpowers_jesse_vincent/`（删测试案例 + 覆盖率规则）、`run_anthropic_thariq_shihipar/`（砍掉 80% 系统提示词） | — |

### `02_流程变革_具体模式与检查清单.md` 的来源

| 模式/章节 | 主要来源样本 |
|---|---|
| AI Sandwich 个人工作流 | `run_every_kieran_klaassen/`（命名 + 结构）、`run_anthropic_thariq_shihipar/`（五步法）、`run_anthropic_boris_cherny/`（Erik Schluntz 前置仪式，交叉引用自 ai_sdlc_frontier） |
| Brief-Review-Signoff 制度化 | `run_superpowers_jesse_vincent/`（全流程：brainstorming→spec→解耦 agent 执行→MP4 验证→防作弊） |
| 组织级四条流程重写 | `ai_sdlc_frontier/raw_Anthropic_Fiona Fung/`（交叉引用） |
| Agent 制度经验法则 | `run_superpowers_jesse_vincent/`（失败路线记录、/goal 结构、latent space engineering） |
| 不同阶段模型策略 | `run_every_willie_williams/`（benchmark vs 迭代体验）、`run_mclayer_plugin_codeforge/`（外科手术式采用 + 版本依赖 + fallback） |
| 安全与治理专属流程门 | `run_datasette_simon_willison/`（sandbox）、`run_zed_richard_feldman/`（consent/retention/fallback 三合一）、`run_every_mike_taylor/`（NDA 硬边界）、Anthropic 静默干预回滚事件 |
| 流程检查清单 | 综合所有来源的实操建议提炼 |

### `03_粗糙信号_早期观察与未成形想法.md` 的来源

| 粗糙信号 | 主要来源样本 | 证据强度 |
|---|---|---|
| 模型"人格"说 | `run_anthropic_boris_cherny/`（"it's just part of its personality"） | ⭐⭐ 单人观察 |
| Agent 对情感有反应 | `run_superpowers_jesse_vincent/`（"I love you" 结尾可测量改善） | ⭐⭐ 单团队 + 一个实验室复现 |
| $12 修 CSS 值不值 | `run_datasette_simon_willison/`（全案例 + AgentsView 成本数据） | ⭐⭐⭐ 有成本数据但无对比基线 |
| 成本感知成为一等公民 | `run_every_willie_williams/`（迭代体验 vs 能力） | ⭐⭐ 定性 |
| Fable 不可用 fallback | `run_mclayer_plugin_codeforge/`（已编码进运行时） | ⭐⭐⭐ 公开工程证据 |
| Agent 投机取巧是系统性行为 | `run_superpowers_jesse_vincent/`（删测试 + 三条失败省钱路线） | ⭐⭐ 单团队但证据链完整 |
| 代码库健康度是第一变量 | `run_every_willie_williams/` 引用 Rody Davis | ⭐ 断言级，无量化数据 |
| AI 残留物清理 | `ai_sdlc_frontier/raw_OpenAI_Ryan Lopopolo/`（交叉引用） | ⭐⭐⭐ 有团队数据（~20% 时间→自动化） |
| 上下文腐烂 | `ai_sdlc_frontier/raw_Cursor_Jediah Katz/`（交叉引用） | ⭐⭐ 团队识别但无公开修复数据 |
| 写代码变成爱好 | `run_superpowers_jesse_vincent/` | ⭐ 单人大胆断言 |

---

## 来源样本未被直接引用的内容

以下样本在本次合成中被部分使用。如果你要深挖，以下是它们最值钱但可能没被充分展开的部分：

| 样本 | 可能被低估的内容 | 文件路径 |
|---|---|---|
| `run_every_nityesh_agarwal/` | 四条件任务选择清单（organized deep context, well-defined goal, clear definition of done）、修复杂烂摊子场景 | `quotes.md`、`raw_*` |
| `run_generativeai_net_martin_musiol/` | 安全审计实操（"The security audit hurt"）、极简 prompt 出 UX 反馈 | `quotes.md` |
| `run_product_compass_pawel_huryn/` | PM 视角的 Fable 5 使用边界 | `raw_claude_fable_5_the_ultimate_guide_for_pms.md` |
| `run_digital_life_khazix/` | 8 prompt 实测对比（多 prompt 行为差异） | `raw_digital_life_khazix_fable5_8_prompts.md`、`analysis_*.md` |
| `run_zed_richard_feldman/` | 类型化 `DataRetentionConsentRequiredError`、`send_to_user` 工具 + refusal-fallback 模型支持 | `quotes.md`（工程细节很硬） |
| `run_mclayer_plugin_codeforge/` | `model: fable` alias 版本依赖（Claude Code v2.1.170+）、顶层 session 保持 Opus 的决策理由 | `quotes.md`、`raw_*` |

---

## 和相邻目录的关系

```
aidlc/
├── _raw_aws/          ← AWS 的 AI-DLC 方法论（三阶段、14-Node AgentCore）
├── _raw_fable5/       ← 你在这里。Fable 5 具体模型引发的变革信号
├── _raw_frontier/     ← 跨公司（Anthropic/OpenAI/Cursor/Google）变革共识
├── _raw_kol/          ← 历史 KOL（Fowler、Farley 等）
└── _raw_ecosystem/    ← 非 AWS 全景
```

**`_raw_fable5` 和 `_raw_frontier` 的差别：**
- `_raw_frontier` 问的是：**这些人（7 个人物）在说什么东西必须变？**
- `_raw_fable5` 问的是：**Fable 5 这个具体模型本身，导致了什么东西可能要变？**

前者是人（方法论者），后者是模型（能力载体）。两者有大量交叉引用。

**`_raw_fable5` 和 `_raw_aws` 的差别：**
- `_raw_aws` 是自顶向下的方法论框架——"正确的流程应该长这样"
- `_raw_fable5` 是自底向上的涌现信号——"这个模型让我们发现旧流程长这样不行了"

---

## 如果你想继续扩展这个目录

以下方向在本次合成中覆盖较少，值得继续：

1. **PM 视角的深度展开** — `run_product_compass_pawel_huryn/` 是唯一从 PM 视角写的样本，目前只在粗糙信号里提了一笔
2. **多 prompt 行为对比** — `run_digital_life_khazix/` 做了 8 个 prompt 的实测对比，可以用来验证"Fable 更主动"的假设
3. **安全审计方法论** — `run_generativeai_net_martin_musiol/` 的 "Two prompts, one hour" 安全审计方法值得单独展开
4. **复杂烂摊子修复** — `run_every_nityesh_agarwal/` 的"四条件任务选择"可以发展成任务分诊指南
5. **Zed 产品集成的工程细节** — 类型化错误、运行时 fallback、BYOK 的隐私架构——这些对产品团队参考价值很高但合成中没充分展开
6. **成本量化** — 目前只有 Simon Willison 的 $12 单点数据。如果能收集更多成本数据，可以建一个"Fable 5 任务 ROI 估算表"

---

## 阅读路径速查

| 如果你关心... | 先读 | 再读 |
|---|---|---|
| 大局：Fable 5 到底变了什么 | `01` §一~§十二 | `02` §一 |
| 我的团队明天怎么改流程 | `02` §一~§三 | `02` §八（检查清单） |
| 哪些风险我需要先知道 | `01` §五、§九 | `02` §六 |
| 有哪些还没定论但我该关注 | `03` 全文 | `03` §八（弱信号追踪表） |
| 这堆东西是从哪来的 | 本文件 §来源全量映射 | 去 `fable5_field_signals/` 看对应 `quotes.md` |
