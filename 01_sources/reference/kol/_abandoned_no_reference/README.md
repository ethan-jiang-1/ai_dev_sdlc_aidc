---
type: index
content_type: readme
directory: _abandoned_no_reference
description: 无源可溯的内容收容所——所有文件因违反来源铁律或时间铁律被移入
---

# _abandoned_no_reference — 内容收容所

> **铁律**：本库所有材料必须有可验证的来源 URL + 必须在 2026 年 1 月之后。
> 以下文件因不满足此要求被移入此地。若日后找到可靠来源，可恢复。

---

## 文件清单

| 文件 | 原始位置 | 移入日期 | 原因 | 恢复条件 |
|---|---|---|---|---|
| `from_raw_kol_06_synthesis.md` | `_raw_kol/` | 2026-07 早期 | 综合文件，缺乏可验证来源 | 找到每条声明的原始 URL |
| `from_raw_kol_11_pragmatic_summit_2026.md` | `_raw_kol/` | 2026-07 早期 | Pragmatic Summit 报道，缺乏可验证来源 | 找到每条声明的原始 URL |
| `from_frontier_04_技术深水区.md` | `_raw_frontier/` | Round 3 | 核心内容（四层压缩、marble_origami、cache_edits）基于 Claude Code 源码逆向，非 Anthropic 官方公开文档 | Anthropic 公开发布相关技术文档 |
| `from_engelberg_08_practical_workflow.md` | `_raw_engelberg_2026/` | Round 2 | 7步工作流来自匿名参会者，经由第三方转述，无法溯源 | 找到具名来源的公开 URL |
| `from_corp_ecosystem_02_evolution_timeline.md` | `aidlc_reference_corp/_raw_ecosystem/` | Round 7 | 190行仅1个pre-2026 URL，大部分声明无来源 | 逐条补 URL |
| `from_corp_ecosystem_03_community_reactions.md` | `aidlc_reference_corp/_raw_ecosystem/` | Round 7 | 163行零URL，含"130名专业人士"幽灵调查 | 找到每条声明的原始 URL |
| `from_corp_ecosystem_05_core_drivers.md` | `aidlc_reference_corp/_raw_ecosystem/` | Round 7 | 202行零URL，市场数据/经济声明全无来源 | 逐条补 URL |
| `from_corp_ecosystem_07_synthesis.md` | `aidlc_reference_corp/_raw_ecosystem/` | Round 7 | 168行零URL，综合文件无来源链接 | 逐条补 URL |

---

## 恢复流程

1. 找到每条核心声明的**可验证公开 URL**
2. 补入文件 frontmatter 的 `source_urls`
3. 确认所有 URL 可访问（curl 200）
4. 确认所有来源在 2026 年 1 月之后
5. 移回对应目录，更新目录 README 的文件计数
