# AIDLC Figures · 20 files · ~3.4MB

所有文件均通过格式验证（magic bytes 匹配扩展名），SVG 已注入默认 CSS 样式。

## arXiv 论文原图

### 2604.26275 — Agentic AI in the SDLC (Bhati, Apr 2026)
| 文件 | 格式 | 大小 | 内容 |
|------|------|------|------|
| `arxiv_2604_26275_fig1.svg` | SVG | 18K | SWE-bench Verified 性能轨迹 |
| `arxiv_2604_26275_fig2.svg` | SVG | 17K | 六层 L0-L5 参考架构图 |
| `arxiv_2604_26275_fig3.svg` | SVG | 11K | Agentic vs Non-Agentic 系统对比 |
| `arxiv_2604_26275_fig5.svg` | SVG | 14K | 五大开放问题 |
| `arxiv_2604_26275_fig6.svg` | SVG | 20K | 组织采用率与成熟度分布 |

### 2505.05283 — CodeLLM Benchmark Survey (Wang et al., May 2025)
| 文件 | 格式 | 尺寸 | 内容 |
|------|------|------|------|
| `arxiv_2505_fig1.png` | PNG | 971×951 | 181 基准测试 SDLC 阶段分布全景 |
| `arxiv_2505_fig2.png` | PNG | 1079×226 | 基准发布时间线 |
| `arxiv_2505_fig3.png` | PNG | 1080×225 | 各 SDLC 阶段覆盖热力图 |
| `arxiv_2505_fig4.png` | PNG | 1078×1755 | 编程语言与任务类型分布 |
| `arxiv_2505_fig5.png` | PNG | 1080×771 | 基准评估维度对比 |
| `arxiv_2505_fig6.png` | PNG | 1080×1889 | 模型性能对标矩阵 |
| `arxiv_2505_fig7.png` | PNG | 1080×771 | 研究趋势与空白分析 |

## AWS AI-DLC

| 文件 | 格式 | 尺寸 | 内容 |
|------|------|------|------|
| `aws_aidlc_architecture.png` | PNG | 1960×1076 | 14-Node Bedrock AgentCore 平台架构全景 |
| `aws_blog_3phase_flow.png` | PNG | 374×401 | Inception→Construction→Operations 三阶段流程 |
| `aws_blog_adaptive_model.png` | PNG | 323×307 | 自适应执行模型 |
| `aws_blog_artifacts_flow.png` | PNG | 679×348 | 产物流与状态管理 |

## 第三方分析 + 行业报告

| 文件 | 格式 | 内容 | 来源 |
|------|------|------|------|
| `ttpsc_full_aidlc_diagram.webp` | WebP | AI-DLC 三阶段深度拆解 | TT PSC |
| `ttpsc_full_artifacts.webp` | WebP | 产物流与质量门控 | TT PSC |
| `ttpsc_full_operations.webp` | WebP | Operations 阶段完整示例 | TT PSC |
| `gartner_hype_cycle_ai_2025.jpg` | JPEG | Gartner 2025 AI Hype Cycle | testRigor |

---

## ⚠️ 已知问题

- **arXiv SVG**: 已注入默认 CSS，但 ar5iv 原始 SVG 严重依赖外部样式表。部分细节可能渲染不完美。替代方案：直接用浏览器打开 [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2604.26275) 截图。
- **AWS blog 图**: image01 (374×401) 和 image02 (323×307) 分辨率较低，来自博客内嵌。
- **缺少的图**: ELEKS/Forrester 成熟度模型、EPAM ADLC 阶段图、Stack Overflow 调查图表均为页面内嵌渲染（JS/D3.js），无法直接下载原始文件。
