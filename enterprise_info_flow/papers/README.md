---
title: Papers — 关键学术文献
stage: research
type: reference
---

# Papers

```
papers/
├── README.md
└── apm-manifesto/                  ← Agentic BPM 研究 manifesto
    ├── apm_manifesto.pdf           ← 原始 34 页
    ├── apm_manifesto_content.pdf   ← 1-25 页（内容）
    ├── apm_manifesto_refs.pdf      ← 26-34 页（参考文献）
    └── apm_manifesto.md            ← 结构化全文
```

---

## 1. Agentic Business Process Management: A Research Manifesto

- **目录**: `apm-manifesto/`
- **来源**: [arXiv:2603.18916](https://arxiv.org/abs/2603.18916)
- **发表**: *Information Systems*, Vol. 140, Aug-Sep 2026
- **日期**: 提交 2026-03-19，修订 2026-04-12
- **出处**: Dagstuhl Seminar #25192 (AUTOBIZ) + PMAI'25 Workshop (ECAI)

---

## 权威性评估

### 期刊：Information Systems (Elsevier)

| 指标 | 值 |
|------|-----|
| **创刊** | 1975 年（50 年历史） |
| **影响因子 (IF)** | **4.0**（2026，上升中） |
| **CiteScore** | **11.8** |
| **Scopus 分区** | **Q1**（Software 84%、IS 84%、Hardware 84%） |
| **WoS 分区** | Q2（IS 62%） |
| **h-index** | ~96-100 |
| **出版商** | Elsevier (Pergamon) |

**定位**：IS 领域的老牌技术期刊——不是 AIS "Basket of 8" 那种最高荣耀级别（那是 *MIS Quarterly*、*ISR* 那档），但在技术 IS/BPM 子领域是公认的强刊。Q1 在 Scopus 三个分类里都进了前 16%。影响因子每年在涨（3.0→3.4→4.0）。

### 作者群：BPM 领域的"全明星队"

18 位作者，来自 15 个机构，覆盖学术界 + 工业界：

| 作者 | 机构 | 分量 |
|------|------|------|
| **Marlon Dumas** | Univ. of Tartu | **BPM 领域最权威的学者之一**。h-index **95**、43,000+ 引用、爱沙尼亚 CS #1。合著 *Fundamentals of BPM*（全球标准教材）。Apromore 联合创始人 |
| **Giuseppe De Giacomo** | Univ. of Oxford | AI/MAS 领域顶级学者，牛津教授 |
| **Marco Montali** | Free Univ. of Bozen-Bolzano | BPM + 知识表示顶级学者 |
| **Stefanie Rinderle-Ma** | TU Munich | BPM 领域顶级学者，流程挖掘 |
| **Barbara Weber** | Univ. of St. Gallen | BPM + 软件工程 |
| **Fabiana Fournier** | IBM Research (Haifa) | 工业界 BPM 研究 |
| **Lior Limonad** | IBM Research (Haifa) | 工业界 BPM + AI |
| **Timotheus Kampik** | SAP + Umeå Univ. | 学术 + 工业双栖 |
| **Niek Tax** | Meta (London) | 流程挖掘 + 工业界 |
| **Andrea Marrella** | Sapienza Univ. of Rome | AI-augmented BPM |
| **Sebastian Sardiña** | RMIT Univ. | AI/MAS |
| **Andreas Metzger** | Univ. of Duisburg Essen | 自适应系统 |
| **Daniel Amyot** | Univ. of Ottawa | 需求工程 + BPM |
| **Peter Fettke** | DFKI / Saarland Univ. | 流程挖掘 + AI |
| **Artem Polyvyanyy** | Univ. of Melbourne | 流程挖掘 |
| **Angelo Casciani** | Sapienza Univ. of Rome | BPM + 形式化方法 |
| **Emanuele La Malfa** | Univ. of Oxford | AI 安全 / XAI |
| **Diego Calvanese** | Free Univ. of Bozen-Bolzano | 知识表示顶级学者 |

**关键人物 Marlon Dumas 的量化影响力**：
- 论文 "QoS-aware middleware for Web services composition" (2004)：~2,972 引用
- "Process Mining Manifesto" (2011)：~1,130 引用
- 教科书 *Fundamentals of BPM*：全球 BPM 课程的标准教材
- 创建了 Apromore（领先的流程挖掘平台）——学术成果商业化

### 事件：Dagstuhl Seminar

**Schloss Dagstuhl** 是计算机科学领域**最负盛名的邀请制研讨会**。Dagstuhl Seminar 不是谁都能去的——由领域顶级学者召集，参与者全部邀请制。产出通常定义一个子领域未来 5-10 年的研究议程。

**Seminar #25192 AUTOBIZ** (May 4-9, 2025)：
- 由 Giuseppe De Giacomo (Oxford)、Marlon Dumas (Tartu)、Fabiana Fournier (IBM)、Timotheus Kampik (SAP) 和 Lior Limonad (IBM) 联合召集
- **BPM 和 AI 社区首次在 Dagstuhl 层面正式碰撞**
- 四个工作组：Framed Autonomy、Situation-Aware Explainability、Automated Process Adaptation、Actionable Conversations
- 产出了四篇 PMAI@ECAI 2025 论文 + 本 manifesto

### 论文的学术谱系

这篇 2026 年的 APM Manifesto 不是凭空出现——它有一个清晰的学术演进：

```
AI-Augmented BPM Systems: A Research Manifesto (2023, Dumas et al.)
        ↓
Dagstuhl Seminar #25192 AUTOBIZ (May 2025)
        ↓
PMAI'25 Workshop @ ECAI 2025 — four position papers
        ↓
APM Manifesto (Mar 2026, Information Systems)
```

**从 "AI-Augmented BPM" 到 "Agentic BPM"**——名字的变化本身就反映了领域共识的演进。2023 年还在说"用 AI 增强 BPM"，2026 年已经在说"BPM 本身必须变成 Agentic 的"。

---

## 影响力评估

### 学术影响力

| 信号 | 判断 |
|------|------|
| **18 位作者跨 15 机构** | 大阵容 = 领域共识，不是单人观点 |
| **Dagstuhl 背书** | 最高级别的学术合法性 |
| **发表在 Information Systems** | 强刊但非最顶（IF 4.0, Q1 Scopus）。选择这而不是 *MIS Quarterly* 说明定位偏技术 IS 而非管理 IS |
| **arXiv 预印本** | 正在被广泛传播。arXiv 版本已有 3 次修订（v1 Mar 19, v3 Apr 12） |
| **覆盖 BPM + AI + MAS 三社区** | manifesto 明确说目标是"桥接三个社区"——跨学科影响力 |

### 工业影响力

| 信号 | 判断 |
|------|------|
| **IBM + SAP + Meta 作者** | 三大工业实验室参与——不是纯学术自娱自乐 |
| **概念已被工业界采纳** | Camunda ProcessOS 的架构、Forrester 的 APO 分类、ServiceNow 的 Blueprint——都在说 Framed Autonomy 的同一件事（只是用了不同的词） |
| **BPM Pulse Survey 2026** | 42% 用 GenAI，16% 部署自主 agent——manifesto 描述的未来已经有早期采用者 |

### 对 SDLC 研究的影响

这篇论文是 BPM 世界的" **AIDLC Manifesto** "——18 位学者联名宣布旧范式不够用，新范式叫 **Agentic BPM**，核心是 **Framed Autonomy**。它跟 SDLC 领域的 AI-SDLC 探索（Deer Valley → Engelberg、AI Sandwich、操作者→委托人）是完全平行的——**两边在说同一件事，用了不同的术语。**

**权威性总结**：这不是一篇普通的学术论文。这是一份**由 BPM 领域最权威的学者群 + 三大工业实验室 + Dagstuhl 背书的研究 manifesto**。它定义了 Agentic BPM 的概念基础、架构、四大能力和研究挑战。在 BPM 的 AI 转型这个子领域，它是目前**最高权威级别的文献**。
