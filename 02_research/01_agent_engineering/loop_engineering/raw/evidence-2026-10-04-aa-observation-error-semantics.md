---
type: evidence_archive
collected_by: 委派回源子代理（AA 路 · 反馈路径问题 T1「真实观察与错误语义」）
collected_at: 2026-10-04
serves: digested/09-feedback-harness-interface.md（新判读，主代理撰写；本档案只出证据）
status: 一手文档 5 页（lint-test / commands / options / tips / faq，站点渲染页逐字核验）＋ 官方源码 4 文件（commands.py / base_coder.py / linter.py / prompts.py，作机制证据、非实际执行）；含通道备注 1 条与待核 5 条
quality_bar: 一手官方文档（aider.chat 站点渲染页，curl 直取并逐字核验）与官方源码；仓库文档源作交叉印证；web_fetch 工具层 DNS 异常不影响取证（curl 先例见 evidence-z）
---

# 回源档案 AA：反馈接口 T1——真实观察与错误语义（观测 2026-10-04）

> **任务**：查清 Aider 的 lint/test 退出码语义与自动修复循环；「检查未执行」与「执行了但失败」是否可区分；观察的真实性与局限声明；工具/环境异常与目标失败（goal failure）的区分。
> **访问通道说明（重要）**：web_fetch 工具访问 aider.chat 报 "URL hostname resolves to a non-public IP address"（**工具层 DNS 异常**，同 evidence-z 先例）；`curl -sL` 直取均 HTTP 200。本档案全部引句先取官方渲染页（aider.chat 站点），再取官方仓库文档源文件交叉核对：lint-test / commands / options 三页的站点渲染文本已用脚本对关键句逐一匹配通过（含 `dotnet build && dotnet test`、`--lint "language: cmd"` 等；差异仅 `<code>` 反引号被 HTML 剥离，正文一致）。
> **版本锚**：文档页无单页发布日期（活文档）。各文件取 main 分支最近提交日期：lint-test.md 2025-05-02（sha fdc7be1）、commands.md 2026-03-03、options.md 2025-06-25、commands.py 2026-02-26、base_coder.py 2025-11-30、linter.py 2025-05-08、prompts.py 2025-07-04。观测日期统一 2026-10-04。
> **源码使用纪律**：源码段全部标注「机制依源码、非实际执行」——只证明机制存在与形态，不冒充实际 run 的观察。判定级结论归 digested/09。

---

## Source 1 · 官方文档《Linting and testing》（lint-test.md）

- URL：https://aider.chat/docs/usage/lint-test.html （文本源：https://raw.githubusercontent.com/Aider-AI/aider/main/aider/website/docs/usage/lint-test.md ，lint-test.md 最近提交 2025-05-02）
- 作者：Aider 官方（Paul Gauthier 项目文档站）
- 发布日期：页面无标注（活文档）；访问日期：2026-10-04

### 1a. 机制总纲与退出码契约（lint）

- 逐字引句：
  > "Aider can automatically lint and test your code every time it makes changes. This helps identify and repair any problems introduced by the AI edits."
  > "Aider comes with built in linters for most popular languages and will automatically lint code in these languages. Or you can specify your favorite linter with the `--lint-cmd <cmd>` switch. The lint command should accept the filenames of the files to lint. **If there are linting errors, aider expects the command to print them on stdout/stderr and return a non-zero exit code. This is how most linters normally operate.**"
  > "By default, aider will lint any files which it edits. You can disable this with the `--no-auto-lint` switch."
  > （per-language）"To specify different linters based on the code language, use `--lint \"language: cmd\"`."
- 事实：观察的**唯一通信契约是「退出码＋stdout/stderr 输出」**——aider 不解析错误内容，只依赖非零退出码这个布尔信号＋原始文本。未声明超时、截断、输出上限等语义（文档未写 → 见待核）。

### 1b. 官方自曝退出码通道的歧义（formatter 反例）

- 逐字引句：
  > "Many people use code formatters as linters, to format and pretty their code. These tools sometimes return non-zero exit codes if they make changes, **which will confuse aider into thinking there's an actual lint error that needs to be fixed.**"
  > （对策）"You can use formatters by wrapping them in a shell script like this and setting the script as your linter."（配套脚本：跑两次 pre-commit，第一次允许改文件非零退出、第二次才反映真实问题，即把「改了文件」与「真错误」的区分**外包给用户自己的脚本**）
- 事实：官方承认**退出码通道无法区分「检查器自身改动了环境」与「目标失败」**，并把这层区分责任下放给用户脚本。这是 Aider 文档里最接近「异常 vs 失败」议题的一句，但它只处理 formatter 这个特例，不一般化。

### 1c. test 的退出码语义与自动修复循环

- 逐字引句：
  > "You can run tests with `/test <test-command>`. Aider will run the test command **without any arguments**. If there are test errors, aider expects the command to print them on stdout/stderr and return a non-zero exit code."
  > "**Aider will try and fix any errors if the command returns a non-zero exit code.**"
  > "You can configure aider to run your test suite after each time the AI edits your code using the `--test-cmd <test-command>` and `--auto-test` switch."
- 事实：自动修复的触发条件被官方写成**且仅写成**非零退出码；错误文本原样进 chat。文档没有写「输出为空但退出码非零」「退出码非零但命令根本没跑起来」等边界。

### 1d. 编译语言复用同一对通道

- 逐字引句：
  > "If you want to have aider compile code after each edit, you can use the lint and test commands to achieve this."（lint-cmd 兼做逐文件编译检查；"provide a `--test-cmd` which both builds and tests the project"，或 "`--test-cmd \"dotnet build && dotnet test\"`"）
- 事实：build 失败与 test 失败共用同一退出码通道——通道语义按设计就是**不区分失败种类**。

### 1e. /run：观察的第三条入口（人决定是否喂给模型）

- 逐字引句：
  > "You can use the `/run` command in the chat to run your code and optionally share the output with aider. This can be useful to share error messages or to show aider the code's output before asking for changes or corrections."
- 事实：与 /test 的「非零才自动喂」不同，/run 的输出进不进 chat 由**人逐次确认**（见 Source 4 源码）。观察到达下一轮的三条通道：自动 lint（默认开）、自动/手动 test（默认关）、人确认的 /run。

---

## Source 2 · 官方命令表《In-chat commands》（commands.md）

- URL：https://aider.chat/docs/usage/commands.html （文本源同仓库；commands.md 最近提交 2026-03-03）；访问日期：2026-10-04
- 说明：表格由源码 cog 自动生成（页面内 `get_help_md()` 标记），即**命令描述逐字来自源码 docstring**，是文档与源码的交叉点。
- 逐字引句（表格行）：
  > "**/test** | Run a shell command and add the output to the chat **on non-zero exit code**"
  > "**/run** | Run a shell command and optionally add the output to the chat (alias: !)"
  > "**/lint** | Lint and fix in-chat files or all dirty files if none in chat"
- 事实（观察可用性的关键句）：**exit 0 时输出不进 chat**——通过事件在对话里不留观察记录；失败事件才以消息形式落地。命令表层面已经写死了「观察=失败侧单向」的语义。

---

## Source 3 · 官方配置默认值《Configuration options》（options.md）

- URL：https://aider.chat/docs/config/options.html （文本源同仓库；options.md 最近提交 2025-06-25）；访问日期：2026-10-04
- 逐字引句（各条目的 Description/Default 行）：
  > "`--lint-cmd` | Specify lint commands to run for different languages, eg: \"python: flake8 --select=...\" (can be used multiple times) | Default: []"
  > "`--auto-lint` | Enable/disable automatic linting after changes (default: True) | Default: True"
  > "`--test-cmd VALUE` | Specify command to run tests | Default: []"
  > "`--auto-test` | Enable/disable automatic testing after changes (default: False) | Default: False"
  > "`--test` | Run tests, fix problems found and then exit | Default: False"
- 事实：
  - **「未配置」是出厂默认态**：test-cmd 默认空、auto-test 默认关（lint 默认开但用内建 linter）。所以「检查根本没执行」是 Aider 用户的**默认状态**，不是罕见边角。
  - 文档对 `--test`（无头模式："Run tests, fix problems found and then exit"）声明了一个**命令行级修复循环**：跑测试→修→退出——循环的驱动条件仍是退出码。
  - 「auto-test 开了但 test-cmd 没配」的行为，文档全部五页均未写（→ Source 4 源码给出机制，登记待核）。

---

## Source 4 · 官方源码机制（标注：机制依源码、非实际执行）

以下四文件均为官方仓库 main 分支（观测 2026-10-04；commit 日期锚见文件头）。只证明机制形态，不证明某次实际运行发生了什么。

### 4a. cmd_test：未配置时静默不执行（commands.py L993–1011）

```python
def cmd_test(self, args):
    "Run a shell command and add the output to the chat on non-zero exit code"
    if not args and self.coder.test_cmd:
        args = self.coder.test_cmd

    if not args:
        return
    ...
    return self.cmd_run(args, True)
```

- 机制：`/test` 不带参数且 `--test-cmd` 未配置 → **静默 return**：不执行、不报错、不进 chat。模型与用户都得不到「没执行」的信号（用户侧也无提示）。
- 注：docstring 即 Source 2 表格里的那句话，两处逐字一致。

### 4b. cmd_run：非零才喂、喂的格式固定（commands.py L1013–1048 ＋ prompts.py run_output）

```python
exit_status, combined_output = run_cmd(args, verbose=self.verbose,
    error_print=self.io.tool_error, cwd=self.coder.root)
...
if add_on_nonzero_exit:
    add = exit_status != 0
else:
    add = self.io.confirm_ask(f"Add {k_tokens:.1f}k tokens of command output to the chat?")
```

- 机制：`/test` 路径 `add = exit_status != 0`——布尔开关，无第三态。喂给模型时用固定模板（aider/prompts.py L36–43，逐字）：
  > "I ran this command:\n\n{command}\n\nAnd got this output:\n\n{output}"
  该模板以 user 消息追加进 `cur_messages`（即作为下一轮输入）。退出码本身**不进模板**——模型看到的只有命令＋输出文本，退出码是隐藏的（非零这个事实由「消息出现了」隐式传达）。
- 机制：`/run` 路径由人确认，且 exit≠0 时把 placeholder 设为 "What's wrong? Fix"（引导下一轮）。

### 4c. 修复回环与 3 次上限（base_coder.py L101、L932–944、L1598–1622）

```python
max_reflections = 3            # L101，类常量
...
if edited and self.auto_lint:
    lint_errors = self.lint_edited(edited)
    self.auto_commit(edited, context="Ran the linter")
    self.lint_outcome = not lint_errors          # 布尔 outcome
    if lint_errors:
        ok = self.io.confirm_ask("Attempt to fix lint errors?")
        if ok:
            self.reflected_message = lint_errors
            return
...
if edited and self.auto_test:
    test_errors = self.commands.cmd_test(self.test_cmd)
    self.test_outcome = not test_errors
    if test_errors:
        ok = self.io.confirm_ask("Attempt to fix test errors?")
        if ok:
            self.reflected_message = test_errors
            return
```

```python
# run_one 的回环（L932–944）
while message:
    self.reflected_message = None
    list(self.send_message(message))
    if not self.reflected_message:
        break
    if self.num_reflections >= self.max_reflections:
        self.io.tool_warning(f"Only {self.max_reflections} reflections allowed, stopping.")
        return
    self.num_reflections += 1
    message = self.reflected_message
```

- 机制事实：
  - **自动修复循环的完整链**：编辑 → lint/test → 非空错误 → 人确认 "Attempt to fix …?" → 错误文本成为 reflected_message（下一轮输入）→ 再编辑。循环上限 **3 次反射**（类常量，文档未暴露配置口——待核），超限提示 "Only 3 reflections allowed, stopping." 后**带着未解决错误退出循环**（错误留在 chat 历史，但循环停了）。
  - `lint_outcome` / `test_outcome` 只是一个**布尔**（`not errors`）——outcome 通道只有「有错/没错」两态，见 4d/4e 的混淆后果。
  - **自动 test 路径没有 test_cmd 前置检查**：`self.auto_test` 为真即调用 `cmd_test(self.test_cmd)`；test_cmd 为 None 时按 4a 静默 return → `test_outcome = not None = True`——**「没执行」在 outcome 通道里与「通过了」记录成同一个值**。
  - 人确认环节（confirm_ask）意味着默认配置下**修复循环不是全自动**——拒绝确认即停止回环（观察不再到达下一轮）。

### 4d. linter 的工具异常处理：OSError 被当成「无错误」（linter.py L45–69）

```python
def run_cmd(self, cmd, rel_fname, code):
    cmd += " " + oslex.quote(rel_fname)
    returncode = 0
    stdout = ""
    try:
        returncode, stdout = run_cmd_subprocess(cmd, cwd=self.root, encoding=self.encoding)
    except OSError as err:
        print(f"Unable to execute lint command: {err}")
        return                      # → 无 LintResult → lint_outcome=True
    errors = stdout
    if returncode == 0:
        return  # zero exit status
    res = f"## Running: {cmd}\n\n"
    res += errors
    return self.errors_to_lint_result(rel_fname, res)
```

- 机制事实：
  - lint 命令**进程拉不起**（OSError）→ 打印到用户控制台、返回 None → 被上层记为「无 lint 错误」→ `lint_outcome=True`。**工具异常在 outcome 通道里被记成通过**。
  - shell 层的「命令不存在」（退出码 127）走另一条路：非零退出 → 被当成 lint 错误喂给模型。同一类「工具坏了」，在 lint 侧随故障层次不同分别被记成**通过**或**失败**。
  - 模型收到的错误文本带前缀头部 `## Running: {cmd}` 和 `# Fix any errors below, if possible.`（linter.lint 内），输出附 tree_context 行号上下文。
  - 读不了文件（OSError on read）同样返回 None → 记为无错误。

### 4e. 环境向模型声明「检查由谁跑」（base_coder.py L1149–1170，平台提示文本）

```python
if self.lint_cmds:
    if self.auto_lint:
        platform_text += "- The user's pre-commit runs these lint commands, don't suggest running them:\n"
    else:
        platform_text += "- The user prefers these lint commands:\n"
...
if self.test_cmd:
    if self.auto_test:
        platform_text += "- The user's pre-commit runs this test command, don't suggest running them: "
    else:
        platform_text += "- The user prefers this test command: "
```

- 机制事实：配置了检查命令后，aider 会把检查的存在**写进系统提示**并按 auto 与否换措辞——auto 时告诉模型「pre-commit 会跑，别再建议跑」。即模型被明确告知观察通道的存在与归属；但该文本**没有任何「结果如何获知」的说明**，模型不知道检查是过了还是挂了，只会在错误文本作为 user 消息到达时才知道。

---

## 观察「最多支持何种声明」——三例雏形（档案级最小主张，判定归 digested/09）

依据上述文档＋源码机制（未做实际 run）。每例分「能声称／不能声称」。

### 例 1 · 正常通过（exit 0）

- **能声称**：「配置的检查命令以退出码 0 结束」（auto-lint/auto-test 或 /test 路径机制上会执行到这一步）。这是退出码契约能支撑的全部——lint-test.md 原文把观察定义为退出码＋stdout/stderr，没有任何更多语义。
- **不能声称**：
  - 「功能正确/端到端可用」——文档通篇无「测试通过≠正确」类声明（已核 lint-test/tips/faq/commands/options 五页，均无），但也没有任何一句把 exit 0 升格为正确性背书；升级属于使用者的越权解读。
  - 「检查真的跑了」在**对话里不可见**——exit 0 时输出不进 chat（Source 2/4b 机制），chat 转录里没有通过事件；可见性只剩 git 侧的 auto_commit（"Ran the linter"）与 outcome 布尔（内部字段）。
  - 「测试覆盖了本次改动」——test-cmd 是单一全局命令且无参数运行，与改动内容无结构化关联。

### 例 2 · 未执行

- **能声称**：「这是出厂默认态的一部分」——test-cmd 默认空、auto-test 默认关（Source 3）；`/test` 无参数且未配置时静默返回（Source 4a 机制）。
- **不能声称**：
  - 「检查做了」——机制上什么都没发生。
  - **在 outcome 通道里区分它与例 1**：auto-test 开而 test-cmd 未配时，`test_outcome` 被记为 True，与真实通过同值（Source 4c 机制）；chat 里也无「未执行」信号。即 Aider 现有观察通道（chat 消息＋outcome 布尔）**不能可靠区分「通过」与「没跑」**——「未执行」只在用户读文档＋源码、且检查配置方式特定的条件下才可推断。
  - 文档层面：该行为五页均未写明（待核 2）。

### 例 3 · 执行了但失败（exit ≠ 0）

- **能声称**：「命令退出非零，且其 stdout/stderr 原文以固定模板作为 user 消息进入对话（"I ran this command… And got this output…"），Aider 在人确认后以它为下一轮输入发起修复，回环上限 3 次」。失败侧观察是**可达、有界、带原文**的——这是 Aider 观察语义里最强的一条。
- **不能声称**：
  - 「这是目标失败（goal failure）」——退出码通道不区分失败种类：formatter 改文件的非零退出会被「confuse aider into thinking there's an actual lint error」（官方原话，Source 1b）；shell 命令不存在（127）与测试真失败走同一分支（Source 4d 机制）。**文档未区分工具异常与目标失败**；源码层面三种异常（formatter 非零 / OSError 拉不起 / 127）分别被记成失败、通过、失败，互相不可分辨。
  - 「失败信号一定会到达下一轮」——修复要过人确认（confirm_ask），拒绝即断链；3 次回环耗尽后循环停止、错误悬置。

---

## 工具/环境异常 vs 目标失败：Aider 与既有证据的对照

- **Aider（本档案）**：**文档未区分**（五页均无一般化表述）；唯一官方承认的歧义是 formatter 特例（Source 1b），处理方式是把它外包给用户脚本；源码层面的 outcome 布尔（4c）与 OSError→通过（4d）表明通道设计上就未做区分。
- **对照 [evidence-2026-09-26-b-stop-and-scheduling.md](evidence-2026-09-26-b-stop-and-scheduling.md)**（指针，不复制正文）：
  - Claude Code `/goal`：三值判定（Not yet met / Met / **Impossible**）＋四类不可恢复错误**清空目标**与普通错误三次重试暂停分开处理——错误种类进入停止语义（该档案 §问题1 4a）。
  - Claude Code auto mode：拒绝带理由回灌、单次拒绝不停循环、3/20 阈值熔断——把「边界拒绝」从「工具错误」里分出独立处理路径（§问题1 4b）。
  - 即 B 路一手材料里存在**显式的错误分类机制**，Aider 文档没有同级机制（不推断 Aider 能力，只记录文档与源码现状）。
- **对照 [evidence-2026-09-28-p-practitioner-gates.md](evidence-2026-09-28-p-practitioner-gates.md)**（指针）：
  - vale.sh："an exit code is a fact where 'I followed the style' is a claim"——与 Aider 同以退出码为事实底座，但 P 路素材把「事实 vs 声称」的分离当卖点写出来，Aider 文档未做此声明。
  - isitdone：闸门装在声称时刻、树哈希签名回执（STALE 检测）、防削测试——针对的正是 Aider 语义里缺的两件事：「观察是新鲜的/对得上当前工作树」与「观察没被执行者自己伪造」；Aider 无任何等价机制见诸文档。
  - Ian Johnson：agent 丢测试输出导致重复跑——Aider 的镜像事实：exit 0 观察不进 chat（4b），通过事件本就不留痕。
- **分账（供 digested/09 用）**：Aider 提供的是「失败侧单向、有界（3 次）、需人确认、原文直灌」的最小观察语义；异常/失败区分、观察新鲜性、防伪造均不在其文档承诺内（后两者由 evidence-p 的工具层补）。

---

## 复用证据指针（不复制正文）

- [evidence-2026-09-26-b-stop-and-scheduling.md](evidence-2026-09-26-b-stop-and-scheduling.md)：机器闸门与停止条件骨架（back pressure / feature_list passes / `/goal` 三值判定 / auto mode 3·20 熔断 / `/loop` 硬过期 / auto-review 拒绝恢复）；其中「负结论与限制」节与本档案的待核纪律同型。
- [evidence-2026-09-28-p-practitioner-gates.md](evidence-2026-09-28-p-practitioner-gates.md)：实战闸门（isitdone 声称时刻闸门与签名回执 / tee 日志防输出丢失 / 退出码即事实的 docs 域 / 内核即裁判的 math 域）；其中 Source 1 的四性质（时点/工作树/仓库自有命令/无第二意见）可与本档案三例雏形直接对接。

## 负结论与待核清单

1. **负结论（已解决→降级为通道备注）：aider.chat 经 web_fetch 不可达、经 curl 可达**。web_fetch 两次报 "URL hostname \"aider.chat\" resolves to a non-public IP address"，属**工具层 DNS 异常而非网络不可达**（同 evidence-z 先例）；`curl -sL` 直取 aider.chat / raw.githubusercontent.com 均 HTTP 200。所有引句均已在 **aider.chat 站点渲染页**逐字核验（lint-test / commands / options 三页脚本匹配通过），仓库文档源仅作交叉印证。不再登记为访问失败待核。
2. **待核：「auto-test 开而 test-cmd 未配」与「/test 未配置静默返回」**——机制依源码（4a/4c），文档五页未写；未做实际运行验证（遵守「只读源码不冒充实际发生」）。
3. **待核：「测试通过≠正确」类局限声明**——已核 lint-test / tips / faq / commands / options 五页未见；其余文档页（languages、conventions、scripting 等）未逐页排查。
4. **待核：max_reflections=3 是否可配置**——源码为类常量（base_coder.py L101），文档未见暴露开关。
5. **待核：run_cmd / run_cmd_subprocess 的失败分层细节**——aider/run_cmd.py 未回源全文；「OSError vs shell 127」的分界按 linter.py 与 commands.py 的调用面推断（已标注机制来源，未读 run_cmd.py 本体）。
6. **待核：timeout/输出截断语义**——lint/test 命令有无超时、输出上限、编码处理（io.encoding 出现在调用面），文档与已读源码段均未写。
