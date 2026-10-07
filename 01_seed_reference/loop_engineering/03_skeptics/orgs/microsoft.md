---
type: org_evidence
directory: 03_skeptics/orgs
observation_date: 2026-10-06
---

# microsoft — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Ornella Bahidika & Joel Allou（Microsoft）· AIEWF 2026《Don't Let the LLM Drive》（视频上传 2026-07-20）

- URL：https://ai.engineer/talks/m24UKZomm7k-dont-let-llm-drive （curl 实取全文）
- 身份：Microsoft 讲者（页面 title 带机构）——**仅作会议层样本**。
- **挂钩**：停止条件（控制权外移＝对"模型自主决定下一步"的否定）＋循环结构（状态机包住模型）。
- 逐字摘录：

> "The trick is LLM is not in charge… It nails the demo, then a real user gets in, and halfway through, the agent decides it's done, or skips a state or even loops… But reliability was never a prompting problem. It's a control problem. The model is the talent, and the harness is the director. The model is brilliant at delivering a line, but it's really terrible at remembering if it's on step three of six. So we stop asking it to."
>（**"可靠性不是提示问题而是控制问题"**；agent "even loops" 作为失败模式被点名。）

> "The model never decides where we are… It proposes, but ultimately it is the harness that decides."
>（与推动派"loops 自主跑"叙事正面对冲：推进权收回 harness。）

> "Instead of having a very heavy model like a 4.7, we're actually able to rely on something like a Haiku 4.5… saving money, saving time, and saving latency."
>（控制权外移的经济学红利。）
- **最小主张**：多步 agent 的可靠性来自把"何时结束/走向何方"从模型手里拿走，放进状态机；模型只出提案。
- **派别适配**：**怀疑票（控制权向）**——对 loop 自主化路线的工程学刹车。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：ai.engineer 讲稿页重取（官方逐字稿＋6 分节全列，fetch 成功）。本轮引句全部当日 fetch 逐字取得。

**官方分节名（全列）**："The lesson ends halfway through"／"Give each step a narrow contract"／"Smaller assignments enable a smaller model"／"Control the operations around the conversation"／"The model proposes; the harness decides"／"Move unreliable control flow into code"。

## 处方面（状态机收权的具体工程）

**逐字摘录（均为仓库新引句）**：

> "A lesson is a small state machine with intro, teach, check, grade, advance, and wrap. Each steps hands the model a narrow contract. Do this one thing, return it."
（**六态小状态机**：每步给模型一个窄契约——只做一件事、交回结果。）

> "The harness validates what comes back, advance the state, and decide what's next. The model never decide where we are. That's the design."
（**harness 三职能**：校验返回／推进状态／决定下一步——"模型永远不知道自己在哪一步"。）

> "Like when is the lesson done is one, right? Did the student actually get it right? … And what comes next, right? And so everything that comes within those three categories… we have engineered that outside of the model, right?"
（**三类决策全收出模型**：何时完成／对错判定／下一步——页面表格化为 Own the completion decision／Own the decision about correctness／Select the next step。）

> "If it's somewhat of a coin flip, then you wanna take the control flow out of the model. You want the model to not make as many decisions as it could, and instead build those decisions around the model and simply feed an easy input so that the model can easily produce an output, right?"
（**迁移诊断启发式（本轮最重处方）**：某步决策接近掷硬币＝把控制流从模型里拿出来的信号——围绕模型建决策，模型只收简单输入出输出。）

> "we see that there is harnessing for a section which provides input to the model about exactly what to speak about, what to do. We have harnessing about drawing on the whiteboard. We have harnessing that deals with clearing the queue. … everything that would allow us to actually build the lesson in a way that is reliable, even if there's a new scenario that comes in, we try to incorporate that in our state machine."
（**运营性步骤也纳入状态机**：白板、清队列、收尾——不只管"内容"，还管流程可靠。）

> "So don't let the model talk, right? Or actually let it talk, but don't let it drive."
（**收尾金句**：让它说话，别让它开车。）

- **成本红利（诚实注记）**：换 Haiku 4.5 级小模型省钱省时省延迟是**宣称非量化**（页面明示 "supplies no measurements or controlled tutoring comparison"）；内容校验规则未在讲中详述。

## 本轮推荐面小结（一句）

替代方案＝**控制权收归确定性层**：六态小状态机＋每步窄契约＋harness 独占"完成/对错/下一步"三类决策＋coin-flip 收权判据＋运营步骤全入状态机——模型只提案（原有主节引句），代价是成本红利尚无量化。
