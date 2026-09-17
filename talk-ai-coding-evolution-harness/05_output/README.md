# 05_output —— PPTX 交付物

本目录放**版本化交付**：`vN/` 子目录 + 该版 PPTX + slide 源文件 + 视觉规格。

## 版本约定

- **只有当前版本与视觉基准留在目录里。** 被取代的版本一律移出，归档到仓库根
  `.tmp-harness-talk-archive-YYYYMMDD/`（不入库，仅供回查）。
  理由：旧版本的页码、页序留在旁边，是下一轮改错稿的主要来源。
- 版本编号连续 `v0.x`；只有完整稿通过文字与视觉 REVIEW、被明确认定为首个正式发布版时，
  才允许用 `v1.0`。
- **唯一 REVIEW 对象**写进 `../CURRENT.md`。

## 每版的必做项

1. 全量渲染 + 逐页检查（层级、对齐、留白、溢出、模板保真）。
2. **文字 REVIEW**：主张、口径、来源、转场；外部数字的证据强度标注是否同屏。
3. **视觉 REVIEW**：纸白画布是否统一；语义色是否只作强调；终端构件是否风格一致。
4. speaker notes 保留 `[Sources]` 块；不得出现本地绝对路径。
5. 发布前删掉对应的 `.tmp-harness-talk-vN*` 中间目录。

## 状态

### v0.1 —— 视觉样片（2026-09-16）· 仍有效

`v0.1/visual-samples.html`，4 张——

| # | 样片 | 验证什么 |
|---|---|---|
| 1 | 封面 | 标题层级、路线条、终端母题 |
| 2 | 机制页（两套控制） | 信息浓度够不够撑 2.5 分钟；三栏结构图 + 下方两档判定 |
| 3 | 数据页 | **证据强度横幅与数字同屏**——"当场降档"有没有真做进版面 |
| 4 | **呼吸页** | 留白 ≥60%、只有一句大字、不显示页码——"呼吸"能不能成立 |

**用户已认可（2026-09-16）。这 4 张是后续全套的视觉基准（D29）。**

### v0.4 —— 42 张 PPTX（2026-09-17，★ 当前唯一 REVIEW 对象）

`v0.4/AI Coding 演变指南/AI Coding 演变指南.pptx`，**36 页正文 + 呼吸页 B1–B6 = 42 张**，
对应 `04_drafts/ppt-text-v3.md` 与 `03_outline/00-page-structure-v3.md`。

| 项 | 位置 |
|---|---|
| PPTX | `v0.4/AI Coding 演变指南/AI Coding 演变指南.pptx` |
| slide 源（42 个） | `v0.4/AI Coding 演变指南/slides/NN.slide` |
| 视觉规格 | `v0.4/AI Coding 演变指南/DESIGN.md` |
| 生成器 | `.tmp-harness-talk-deck-v3/build_slides_v3.py`（不入库） |
| 预览总览 | `.tmp-harness-talk-deck-v3/preview/all.html` |
| 渲染图 | `.tmp-harness-talk-deck-v3/shots/sNN.png`（0 基，s00 = P1） |

**编译方式**（`slidep` CLI：`~/.workbuddy/binaries/node/versions/22.22.2-3/bin/slidep`）：

```bash
slidep create "<deck>.pptx"                                    # 建空本
slidep upsert-dsl "<deck>.pptx" --dsl-file NN.slide --page-index -1   # 追加
slidep upsert-dsl "<deck>.pptx" --dsl-file NN.slide --page-index N    # 替换第 N+1 页
slidep screenshot "<deck>.pptx" --page-index N --out sNN.png   # 出图检查
```

**改稿流程**：改生成器 → 重跑生成 `.slide` → 只 `upsert-dsl` 受影响的那一页 → 出图检查。
不要手改 PPTX。

**两个已知坑**：
- DSL 里 Text 节点**不吃 height**，行高要压在 Box 上（`minHeight`），否则版面会塌。
- 批量 upsert 被中断时，用 `ls ppt/slides/*.xml | wc -l` 核页数，
  **不要**用 `ls ppt/slides/`（会把 `_rels` 目录数进去）。

**REVIEW 要点**：P25–P28 两类程序 / P29–P33 DSH 展开 / P18 现场走查（现为示意 trace）/ 呼吸页 B1–B6。

### 已归档（不在本目录）

| 版本 | 内容 | 归档位置 |
|---|---|---|
| v0.2 | `deck.html`，v2 结构 49 张 HTML 稿 | `.tmp-harness-talk-archive-20260917/v0.2/` |
| v0.3 | v2 结构 49 页 PPTX + 49 个 .slide + STORY.md | `.tmp-harness-talk-archive-20260917/v0.3/` |
| — | v0.4 里曾有一份从 v0.3 复制的 `STORY.md`（v2 叙事，与 v3 冲突） | `.tmp-harness-talk-archive-20260917/v0.4-STORY-v2叙事.md` |

### v1.0 —— 完整 PPTX：**未开始**

内容与视觉定稿后再转。转换时视觉方向服从本目录，不套第三方模板。
