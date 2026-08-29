# 故事线总图（v0.5 · AI-Native 研发组织 · SDLC 主轴 + 五层/DSH 引子）

> **对象**：研发整体组织——从产品一路到底到实施、再到运维。**题目已定**：AI-Native 研发组织：从产品到实施的 SDLC 转型之道。**slogan**：代码不再是瓶颈，流程才是。
> **篇幅档位 A**：单场加长 Keynote（75–90 min，~50 页）。**独立成篇**（不承接 `deck_ai_sdlc_keynote`）。
> **v0.5 定调（不再反复）**：**SDLC 六阶段是主轴**；**五层（Prompt→Context→Harness→Loop→Graph）+ DSH 不强扭成独立章节**，
> 而是各自在自然接点作「引子」插进 SDLC。harness 在开场先立住，Build/Test/Deploy 再展开；DSH 作为「给不同视角/环节定制」的可组合 runtime。

## 一句话主线

代码不再是瓶颈。组织真正缺的，不是更强的模型，而是**把「怎么正确参与」外置成系统**——工件链（要什么 / 为什么 / 怎么做）、
gate（对错怎么判）、归属（改哪里 / 谁负责）。沿着六阶段走一遍：Plan 是 Prompt（把意图外置成 `intent.md`），
Design 是 Context（把政策策展成 `spec.md`），Build/Test/Deploy 是 Harness（把可靠性外置成 hooks/evals/gates），
Test/Maintain 是 Loop（把反馈连成闭环），跨阶段编排是 Graph（多节点 + 门禁）。**DSH 是把这条原则做成的可组合 runtime**——
知识外置、正确路径、可执行反馈，三条腿一个不落。

## 主轴 + 引子（一张表看全）

| SDLC 主轴 | 引子（五层） | 落在本 talk 的机制/工件 |
|---|---|---|
| **Plan** | **Prompt**：组织怎么把意图一次说清楚 | `intent.md`（originator 自己的话 + 产品 owner 审批） |
| **Design** | **Context**：组织策展模型看到什么、知道什么 | `spec.md` + skills（政策在写 spec 时就施加） |
| **Build** | **Harness**（主战场）：圈住/拦住/看清 | plan mode / `AGENTS.md` / skills / hooks / 并行会话 |
| **Test** | **Harness 的 Sensors + Loop 起点**：会话自己验证 | feedback loop / continuous evals |
| **Deploy** | **Harness 的拦住/看清**：authorize at execution | PR review / hooks as gates / managed settings / CI-CD |
| **Maintain** | **Loop 收口 + Graph 编排**：linear→loop 关环 | 关 loop / scans / on-call（Claude Tag） |
| （收束） | **DSH**：给各环节定制的可组合 runtime | registry / adapter / capability seam / enforced gate / session log |

> 五层各作各阶段的引子单独点破，不并、不吞、不硬凑；它们共同的落点是「**把怎么正确参与外置成系统**」——工件链（外置要什么）、gate（外置对错）、归属（外置谁负责）。

## 故事弧线（开场 + 三幕）

| 幕 | 内容 | 作用 | 时间(约) |
|---|---|---|---|
| 开场 | 钩子 + 五层预告 + harness 引子先立住 | 让组织对号入座 | 0–6 |
| 第一幕 | 为什么整条 SDLC 要转型 | 论点 | 6–16 |
| 第二幕 | 六阶段转型（每阶段一个引子） | 主体（主轴） | 16–64 |
| 第三幕 | DSH + 治理收束 | harness runtime + 落地 | 64–84 |
| 收尾 | 带走一句 | 收束 | 84–90 |

## 每一幕的要点

### 开场（钩子 + 五层预告 + harness 引子先立住）
- 问题：组织已经让工程师用上 AI coding，代码产出翻了几倍，交付却没快——为什么？
- 钩子：**Code is no longer the bottleneck**（Anthropic，标注来源）。
- **P4 五层预告**：人机互动一直在变（Prompt→Context→Harness→Loop→Graph），这五层会沿着 SDLC 逐一亮相——不展开，只预告。
- **P5 harness 引子（先立住）**：模型给能力，harness 给可靠性——五层里组织最该握住的是 harness，后面 Build/Test/Deploy 展开。

### 第一幕：为什么整条 SDLC 要转型
- 代码不再是瓶颈 → 三个后果（瓶颈左移右移 / 旧控制失效 / 治理成本上升）。
- 传统 SDLC 的控制假设：每一步都是人做的；逐行 review、阶段闸门跟不上 agent 产出。
- 转型的本质：从「人执行 + 人工闸」→「harness 执行 + 人守 gate」。
- 贯穿主线早埋：**工件链 = 审计链**（intent→spec→plan→diff→PR→incident）。
- 六阶段 shifts 总表（传统 vs AI-native）。

### 第二幕：六阶段转型（每个阶段一个引子）
- **Plan（引子=Prompt）**：意图一次捕获 `intent.md`；originator 自己的话 + AI 头脑风暴，产品 owner 审批。治理=merge，度量=存活率 + 多周→小时。
- **Design（引子=Context）**：需求+设计合一 `spec.md`；skills 施加 brand/security/compliance/UX 政策；`AGENTS.md`/skills 把制度知识外置。治理=spec+prompt+skill 版本全进库，风险项路由 policy owner。
- **Build（引子=Harness 主战场）**：圈住（沙箱/权限）、拦住（hooks/门禁）、看清（观测/provenance）。plan mode 出 `plan.md`、`AGENTS.md`、skills、hooks、并行会话/子 agent（点出 Graph 雏形）。
- **Test（引子=Harness 的 Sensors + Loop 起点）**：feedback loop（会话自己验证）+ continuous evals（对 harness 配置的回归测试）。确定性优先。
- **Deploy（引子=Harness 的拦住/看清 + authorize at execution）**：PR review（职责分离）、hooks as gates、managed settings、CI/CD。提议权给模型，执行权留治理。
- **Maintain（引子=Loop 收口 + Graph 编排）**：关 loop（control-band breach → `intent.md` 重新入环）、scans、on-call。检测确定性、越界才调 agent。

### 第三幕：DSH + 治理收束（加厚）
- 工件链 = 审计链（谁要的 / agent 产出了什么 / 谁批的）；人守 gate，不逐行；确定性优先。
- **DSH 如何帮助流程 = 三条腿**：知识外置（一个事实一个 owner、负知识外置）、正确路径（参与阶梯、改哪里先问归属）、可执行反馈（门禁本身被测试、invariant）。
- **DSH = 可组合 harness runtime**：插件图（现在由什么组成）+ 事件流（刚才做过什么，append-only）+ loop（两者间取能力、写事实）；capability seam 三角色让「换后端 Consumer 不改」。
- 审计 = append-only + 审批成对 asked/decided + fail-closed；诚实标尺 = 可替换率 39.3%（饱和区 vs 缺口区）。
- 四项治理决定（准入/替换/放行/重建事实）各对应一个机制；组织落地顺序：先工件链 → 再 gate → 再关 loop。

### 收尾
- 带走一句：**代码不再是瓶颈，流程才是。**
- 回到开场：快的只是编码，慢的是整条链的流程与治理；组织要做的不是让工程师写得更快，而是沿 SDLC 把五层一一落地。

## 口径红线

- 前三层成熟，Loop / Graph 新兴（沿用 `-opc`，本 talk 里 Loop/Graph 是「组织责任的承担者」，不讲成既定生产范式）。
- 「代码不再是瓶颈」是 Anthropic 论点，引用标注来源；playbook 是 Claude 视角，机制讲透、产品名不唯一。
- DSH 原生机制不是 MCP；说 `ctx.llm`、`ctx.tools`、capability seam、plugin。
- DSH 命名随大流：`CLAUDE.md` 概念 → `AGENTS.md`；`.claude/skills` → skills 目录；`.claude/agents` → subagents。机制讲透，不绑定 Claude Code。

## 素材索引

- 六阶段 + 15 play：`../_reference/rawdata_anthropic-ai-native-sdlc-playbook.md`
- 五层结构：`../_reference/rawdata_ai-coding-evolution-final/final_v4.md` + `final_v4/`
- Böckeler（Guides/Sensors）：`../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`
- DSH 机制：`../_reference/rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md`、`../_reference/rawdata_dsh-digested/`
