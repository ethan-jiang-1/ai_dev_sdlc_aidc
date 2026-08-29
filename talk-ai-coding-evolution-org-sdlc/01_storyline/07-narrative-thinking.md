# 叙事思路笔记（v0.6 内容 REVIEW）

> 本文件是**叙事推敲的上下文记忆**：记录「看了什么、被什么启发、叙事思路怎么演化的、关键决策为什么这样下」。
> 不是内容文件，是给下一次进来的 agent / 自己看「为什么会这样想」的。当前主线以 [`00-storyline-map.md`](./00-storyline-map.md) 为准，本文件是它的**来路与理由**。

## 一、看了什么（输入源）

| 源 | 是什么 | 提供了什么 |
|---|---|---|
| `_reference/rawdata_anthropic-ai-native-sdlc-playbook.md` | Anthropic「The AI-Native SDLC playbook」全文 | 六阶段 + 15 play + 「代码不再是瓶颈」+ 工件链 + loop + 治理 |
| `_reference/rawdata_ai-coding-evolution-final/` | 五层演变最终报告（`-opc` 同源） | Prompt→Context→Harness→Loop→Graph + Böckeler + 成熟度标尺 |
| `_reference/rawdata_dsh-digested/` | DSH 源码消化（harness-idea / session-and-loop / capability-seams / composition） | 插件图 + 事件流 + loop + seam 三角色 + 参与阶梯 |
| `_reference/rawdata_dsh-faq-on-digested/` | 二次研究问答（07/08/09 为主） | **三条腿**（知识外置/正确路径/可执行反馈）+ 可替换率 39.3% + 敢放手/省手/可复用 |
| `_reference/rawdata_dsh-plugin-*` | 插件收益阶梯 / 生态分布 / seam 成熟度 | 生态证据、价值阶梯、饱和 vs 缺口 |
| `04_output/deck_ai_sdlc_keynote/` | 既有主 Keynote（信息加工链隐喻） | **只看了一眼**——确认它听众不同（软件+业务混合）、本 talk 独立成篇不承接 |

## 二、被什么启发（关键触点）

1. **「Code is no longer the bottleneck」**（Anthropic）——组织级钩子：代码产出翻倍、交付没快，因为慢在流程与治理。这句成为开场钩子 + 收尾 slogan 的来源。
2. **「Agents follow enforced gates far more reliably than prose conventions」**（DSH FAQ 07）——确定性优先的最硬表达，焊死了整场的「人守 gate / 确定性优先」。
3. **DSH 的三条腿**（知识外置 / 正确路径 / 可执行反馈）——这是「DSH 怎么帮流程」的钥匙，也成为整场的**统一命题**（见下）。
4. **「工件链 = 审计链」**（playbook 的 committed artifact chain）——`intent→spec→plan→diff→PR→incident` 的 commit 链就是审计记录，成为贯穿主线。
5. **五层 = 深度，六阶段 = 宽度**——两套素材本来正交，但反复试下来，**不能让任何一轴吞掉另一轴**（见演化史）。

## 三、叙事思路的演化（v0.1 → v0.5，为什么最后是「主轴 + 引子」）

| 版 | 思路 | 问题（用户反馈） |
|---|---|---|
| v0.1 | harness 单焦点：「组织唯一该集中建设的是 harness」+ 23 页 | 被 playbook 重定调：对象扩为「软件研发与交付组织，从产品到实施」 |
| v0.2 | 全 SDLC：六阶段做主轴，五层挤成「深轴」 | **harness 出现太晚**；**Loop/Graph/DSH 关系不大**——五层被边缘化 |
| v0.3 | 五层各成一幕 + 三层（任务/平台/治理）概括 | **Prompt/Context 被吞进「任务层」**——五层变三层，前两层不见了 |
| v0.4 | 五层各成一幕（谁都不并） | **强扭**——SDLC 这个好轴被放弃了，五层硬凑成章 |
| **v0.5** | **SDLC 六阶段是主轴，五层 + DSH 各在自然接点作「引子」插入** | 定调，不再反复 |
| **v0.6** | **在固定 50 页内收紧因果：起始诊断 → 可执行 SDLC → 四问贯穿六阶段 → 共享控制面** | 不改主轴，解决「三套素材并列」和过强口径 |

**v0.5 为什么对**：SDLC 六阶段是「组织从产品到实施」最自然的轴（宽度）；五层提供深度镜头；DSH 提供参考实现。三者各司其职，谁也不吞谁。

**v0.6 收紧了什么**：

1. 「代码不再是瓶颈」从普适事实改成起始诊断，由听众用自己数据验证。
2. 中心命题收到「可执行 SDLC」：工件可交接、gate 可执行、owner 可问责、feedback 可回流。
3. 六阶段不再以 play 清单并列，每阶段都回答「工件 / gate / owner / feedback」四问。
4. 五层不再声称是某一阶段的「本质」，只负责解释外置与控制深度。
5. DSH 从答案改为参考实现；第三幕的任务是解释共享控制面如何工程化。

## 四、关键决策与理由

1. **对象 = 软件研发与交付组织**（CTO/平台/产品/QA/安全/发布/运维），不是 OPC、不是混合听众——每页落「组织该建什么/谁负责/怎么治理/怎么度量」。
2. **A 档单场加长**（75–90 min，**50 页已定**）——总页数作为稳定边界，内容 REVIEW 只在边界内调整页面职责。
3. **独立成篇**——不依赖、不承接 `deck_ai_sdlc_keynote`（听众不同：那边是战略隐喻，这边是操作级转型）。
4. **题目**：AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道；**slogan**：代码不再是瓶颈，流程才是。
5. **harness 开场先立住（P5）**，Build/Test/Deploy 再展开——它是临界点，不能晚出。
6. **DSH 三条腿保留在第三幕**（P41–P47）——它是「知识外置 / 正确路径 / 可执行反馈」的参考实现，不是唯一选型；所有机制必须回指第二幕的组织问题。
7. **工具不可知命名**：`CLAUDE.md` → `AGENTS.md`、`.claude/skills` → skills 目录、`.claude/agents` → subagents——随大流，不绑定 Claude Code。

## 五、统一命题（一句话焊点）

> 当 Build 不再是瓶颈，组织要把整条 SDLC 重建成可执行交付系统：工件可交接、gate 可执行、owner 可问责、feedback 可回流；
> 五层说明控制深度，DSH 作为共享 harness 控制面的参考实现。

这一句把「六阶段（在哪发生）× 五层（有多深）× DSH（怎么做成运行时）」焊成一条线。三条腿（知识外置=工件链、正确路径=归属、可执行反馈=gate）正是它。

## 六、当前状态

- 50 页总页数、六阶段主轴与三幕结构已锁定。
- 当前正在固定 50 页内做内容 REVIEW：收紧页面职责、四问贯穿、口径与转场；通过内容锁定后才写 `04_drafts/` 生产事实稿、选模板与产 PPTX。
