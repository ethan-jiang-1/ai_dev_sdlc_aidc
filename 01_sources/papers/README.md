# AI SDLC Papers

围绕 AI-driven SDLC 主题的论文收集、转换、消化。

## 目录约定

```text
ai_sdlc_papers/
├── README.md                          # 本文件
├── raw_{arxiv_id}_{short_title}/      # 每篇论文一个目录（原始 PDF + 转换产物）
│   ├── {arxiv_id}.pdf                 #   下载的 PDF
│   ├── {arxiv_id}_paper.md            #   正文（不含 References）
│   ├── {arxiv_id}_references.md       #   参考文献（单独存放）
│   └── figures/                       #   提取的图表
├── digested/                          # 消化后的笔记/摘要（一篇一个文件）
└── result/                            # 最终合成产出
```

命名规范：
- 目录名：`raw_{arxiv_id}_{short_title}`，如 `raw_2606.05608_agentic_software`
- 方便按 ID 检索、按标题快速识别主题

## 已有论文

| 论文 | ID | 标题 |
|---|---|---|
| [正文](raw_2606.05608_agentic_software/2606.05608_paper.md) / [引用](raw_2606.05608_agentic_software/2606.05608_references.md) | 2606.05608 | Agentic Software: How AI Agents Are Restructuring the Software Paradigm |

## 依赖

```bash
uv add pymupdf pymupdf4llm pillow
```

核心工具链：
- **PyMuPDF (fitz)** — PDF 底层操作、矢量图形渲染
- **pymupdf4llm** — PyMuPDF 官方的 LLM 专用 PDF→Markdown 转换器
- **Pillow** — 图片处理

## 工作流

### 1. 下载论文

```bash
# arXiv 直链较慢，用 export 镜像 + 长超时
ARXIV_ID="2606.05608"
SHORT_NAME="agentic_software"

mkdir -p raw_${ARXIV_ID}_${SHORT_NAME}

curl -L --connect-timeout 15 --max-time 180 \
  -o raw_${ARXIV_ID}_${SHORT_NAME}/${ARXIV_ID}.pdf \
  "https://export.arxiv.org/pdf/${ARXIV_ID}"
```

### 2. PDF → Markdown

```bash
uv run python scripts/pdf_to_md.py raw_${ARXIV_ID}_${SHORT_NAME}/${ARXIV_ID}.pdf
```

脚本位置：项目根 `scripts/pdf_to_md.py`。

产物：
- `{arxiv_id}.md` — 完整 Markdown，含章节结构、表格、图表引用
- `figures/` — 提取的图表 PNG（200 DPI）

### 3. 消化（待定）

将 MD 喂给 LLM 做摘要、翻译、QA 等，产出放 `digested/`。

---

## 经验总结

### 为什么选 pymupdf4llm

最初尝试用 PyMuPDF 手写解析（spans → 段落拼接、word-position → 表格聚类、font-size → 章节检测），遇到一堆边界情况：

| 问题 | 原因 |
|---|---|
| 文字粘连（`AbstractForoverhalfacentury`） | PDF 的空格是独立 span，容易被过滤掉 |
| 章节检测不准 | 标题用大字号而非粗体，阈值难以通用 |
| 表格难以重建 | PDF 里的表格是定位文字，不是标准 table 对象；列宽窄导致跨行断词 |
| 正文和表格区域混杂 | 字号相同，难以用 font-size 区分 |

**pymupdf4llm** 是 PyMuPDF 团队专门为 LLM 场景写的转换器，内部做了布局分析、表格检测、OCR 回退，开箱即用效果好很多。

### 脚本只需要做轻量后处理

`scripts/pdf_to_md.py` 现在的职责：

1. 调 `pymupdf4llm.to_markdown()` 做重活
2. 修复图片路径（绝对 → 相对）
3. 去掉页码残留
4. 去掉标题里多余的 `**`（pymupdf4llm 把 heading 文字也套了粗体标记）
5. 用 PyMuPDF 额外渲染矢量图形的裁剪版（比整页渲染更干净）

### 已知局限

- **表格跨行断词**：原始 PDF 列太窄，单词被迫断成 `mecha-` + `nism` 两行。pymupdf4llm 能还原成 Markdown 表格，但 cell 内容保留了断词。如需完美表格，可加一层 LLM 后处理（把表格区域的文字发给 LLM 重新整理）。
- **OCR 乱序**：部分页面的文字区域走了 Tesseract OCR，偶尔出现词序颠倒。这是 PDF 本身嵌入字体/编码的问题，换任何工具都会有。
- **矢量图裁剪**：只有检测到矢量 drawing 的页面才会额外渲染裁剪版；纯栅格图片直接用 pymupdf4llm 提取的结果。

### 不要重复造轮子

PDF 解析是个深坑——布局分析、字体编码、表格检测、RTL 语言、OCR 回退……每个都够写一篇论文。**先用成熟工具，只在确实不够用时再针对性补丁**，这条经验适用于所有文档处理场景。
