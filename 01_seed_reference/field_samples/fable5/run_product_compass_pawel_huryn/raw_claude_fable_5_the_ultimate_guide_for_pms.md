# Claude Fable 5: The Ultimate Guide for PMs

### Fable 5 dropped 36 hours ago. 6 experiments later: what changed, when your model silently swaps, and the first prompt you should run.



[Paweł Huryn](https://substack.com/@huryn)

Jun 11, 2026

∙ Paid

42

1

Fable 5 is the first model that’s **made me feel audited** .

Yesterday, mid-task, it read my CLAUDE.md and caught it teaching the exact pattern my own quality gate bans. I hadn’t asked for a review. It hit the contradiction and flagged it on its own.

That file is 320 lines. The knowledge layer behind it is 166 files, around 300k words of rules my agents follow every day. Every one of those rules was written by and for a weaker model.

This guide is what I did about that, plus everything else from six experiments (effort dial, speed head-to-head, time-to-first-token, depth chain, recursive workflows, nesting cost) in Fable 5’s first 36 hours.

**We’ll cover:**

- What changed, what it costs, and what the benchmark chart won’t tell you

- The effort dial and the “Fable is slow” complaint, measured

- When your model silently swaps mid-conversation, and the safeguards behind it

- Why “agentic judgment” is the real headline, with receipts from my own repo

- The audit prompt to run before giving Fable real work, and the migration workflow behind the paywall

- Objectives, not tasks: /goal patterns (paid)

- My nesting and workflow depth experiments, the costs, the decision rule (paid)

**We won’t cover:**  API migration fine print, benchmark-by-benchmark analysis, or anything I haven’t run myself.

## 1. What Actually Changed

According to Anthropic, Fable 5 is “*a Mythos-class model that we’ve made safe for general use. Its capabilities exceed those of any model we’ve ever made generally available*.”

They built a model they don’t fully release. **Mythos 5 stays limited-access** , available to trusted partners. **Fable 5**  is the version of it you’re **allowed to have** . That framing matters more than any spec row, and we’ll come back to it in Section 2.

Fable plugs in wherever Opus 4.7/4.8 did, with a few breaks that will bite you if you migrate blind:



The row that matters isn't price. It's the thinking row: you lost the off switch.

Three migration gotchas hiding in that table:

1. **You can’t turn thinking off.**  Pipelines that set thinking: disabled for speed get a 400 error. The effort dial survives; zero doesn’t.

2. **Temperature is gone.**  If your eval suite sweeps sampling settings, those configs fail on Fable.

3. **Until June 22, your API keys can’t reach it.**  Subscription surfaces only (Claude Code, Cowork, the apps). Plan your team’s testing window accordingly.

### 1.1 Fable 5 effort dial, measured

Instead of taking the docs' word for it, I ran 5 rounds of experiments and measured mean times:



The results:

- **Easy question, no tools** : below max the dial barely moves; thinking is adaptive and the model ignores budget it doesn’t need. Max triples the time and swings wildly between runs.

- **Realistic task, read two files and reconcile an apparent contradiction** : here the dial bites from xhigh up; max costs double low.

- **Hard math puzzle with a checkable answer:**  every effort level got it right, with the same method. The extra seconds bought re-verification and caveats, not correctness. Same on the realistic task: identical verdicts at every level, max just showed more work.

The practical setting based on my experiments so far: **default to high** . Dialing down buys back a few seconds, not different answers. Max should be a rare exception.

### 1.2 Fable 5 speed question, measured

The loudest day-one complaint after the classifiers: **“Fable is slow.”**  One widely shared review called it a crawl, "*even on simple tasks*." I couldn't find numbers, so here are mine. I ran two tests: 3-round checks on the startup pause and in-flight token use, and a bigger 50-answer sweep (5 questions, 5 rounds each) aimed at the simple-tasks complaint. Both used stream-level timestamps and exact token counts:



Based on my experiments:

- **Fable starts about 3 seconds later.**  First visible model activity on the same prompt: Opus in 4.7 to 5.3 seconds, Fable in 7.4 to 8.2, no overlap. You stare at a blank line for three extra seconds before anything moves, and that pause is my bet for where the “it crawls” feeling comes from.

- **In flight it’s denser, not slower.**  Same math problem, both models correct every time: Fable used about 40% fewer output tokens than Opus and finished 5 to 9 seconds sooner. It’s not thinking less. It’s saying the same thing in half the words.

- **On trivial one-shot questions, a real but modest tax.**  Fable averaged 1.4x Opus wall-clock (the round-by-round ratio ranged 1.2 to 1.7), every answer correct from both models. The single slowest answer in all fifty runs came from Opus, not Fable. And on a heavier multi-file audit the gap vanished entirely: 59 vs 63 seconds, and Fable caught a third more issues. Tighter per point, more points.

So the verdict is narrower than what social media says: you can budget a bit of patience at the start of every exchange, and stop worrying about the rest.

### 1.3 The benchmarks

Anthropic's official chart covers these better than any table I'd retype:



Source: [@claudeai on X](https://x.com/claudeai/status/2064394151441863006)

Two things the official chart won't tell you:

- The row that tells you what tier this is: **FrontierCode Diamond** , the hardest unseen problems in the set, where Fable more than doubles Opus 4.8 (29.3 vs 13.4) and runs 5x GPT-5.5:


Source: [@ChrissGPT on X](https://x.com/ChrissGPT/status/2064404270607134792)

- And one honest footnote from the [system card](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf): Fable's published scores already include its production safeguards, which is why some rows run slightly below Mythos.

## 2. The Safeguard Layer Most Coverage Missed

### 2.1 The visible layer: routing



Fable 5 ships with classifiers that screen for high-risk domains. When a query trips one, the session is routed to Opus 4.8 instead, and you get a notification that it happened. Anthropic puts it at \~5% of sessions.

My own experiments with subagents got capped, too:



It doesn't fail the query. It hands it to a different model, on purpose, and tells you. The capability ceiling and the safeguard layer are different things, and knowing which one you hit changes what you do next.

According to Anthropic, “*Mythos-class models have **reached a threshold where they present significant risks** .*” The example they give: these models “*excel at discovering and exploiting software vulnerabilities,*” enough to make cyberattacks “*substantially easier and cheaper to commit.*” 

There’s also a second, invisible layer: per the system card’s Section 1.5, requests targeting frontier LLM development itself don’t reroute, they get quietly degraded, with no notification, on \~0.03% of traffic. Unless your team pretrains models, you’ll never hit it. Researchers are furious anyway (Elie Bakouch’s “[very very sad for the research community](https://x.com/eliebakouch/status/2064399902684139852?s=20)”), and the precedent is: the model you bought can be tuned down by topic, silently.

### 2.2 What this means for your team

Two practical notes from the first 36 hours:

- **Expect occasional routing, especially if your work touches security, healthcare, or biotech:**  Anthropic admits it (Claude Code’s Boris Cherny: “We know the classifiers are trigger-happy, and are working on improving it”). The notification is your signal: you did nothing wrong, and the answer quality drops to “merely Opus 4.8.” For security audits, the supported path is the built-in /security-review command. Also see my [/security-review-static](https://github.com/phuryn/pm-skills) which inspects the full solution, not just the diff.

- **The API behaves differently:**  When per-token access opens June 22, there is no automatic fallback by default: a tripped classifier **blocks the request**  and returns a structured refusal category. Server-side fallback to Opus is opt-in. If your team is planning eval pipelines, budget for retry logic now.

The safeguard is worth copying: it swaps your model mid-session for safety. You can swap on purpose, for cost. Keep a cheaper model as your default and bring in Fable 5 only for the one call that needs it. Section 7 has what that costs.

## 3. Judgment Is the Feature

The benchmarks got their chart in Section 1. The interesting part of this launch is a behavior change.

One disclosure before the quotes: Every voice quoted in praise here works at Anthropic. Read them as insider testimony, not independent validation, then check them against my receipts.

Karpathy called it “*a major-version-bump-deserving step change forward,*” strongest “*for long problem-solving sessions on very difficult problems*”:



The people building Claude Code describe the same thing. Cherny, from his launch post: Fable “*has judgement, taste, and dimensionality in a way that previous models didn’t*”: 



He asked it to debug something, and it took measurements, added logs, and verified the fix before declaring victory. Then the line that stuck with me: “*There’s nothing in claude code’s prompting telling the model to do that, it’s just part of its personality.*” 

Thariq Shihipar compressed it to six words:



The closest thing to an outside read, two days in, is the shape of the criticism. Researchers are **angry about the invisible safeguards**  (Section 2), and Dylan Patel of SemiAnalysis reports power users defecting to Codex after “*[refusals for nonsensical reasons](https://x.com/dylan522p/status/2064727949274955953).*” Both complaints are about **access to the capability** . Neither questions the capability.

My version of that moment is the one this guide opened with. Fable read my instruction files and **started surfacing contradictions instead of executing them** . Previous models followed my rules. This one evaluated them.

## 4. Your Knowledge Layer Was Built for a Weaker Model

Fable flagged the first contradiction on its own, mid-task, before I’d read anyone’s tips. So I gave it the full job: read everything my agents follow and report what’s wrong.

That conclusion is consistent with voices inside Anthropic. Alex Albert’s launch tips name the same mechanism: instructions written for old models keep Fable behaving like those old models. Rework your skills and CLAUDE.md files; let the model use its own judgment first.

### 4.1 What Fable found in my repo

My agents maintain those files, not me. I trust Opus to keep them clean enough. Still, five finds:

- **A hardcoded date telling the model what day it is.**  One strategy file contains “*(today is 2026-05-24)*”, written during a May session and never noticed again. Every session since has been told the wrong date by its own instructions. A latent risk that didn’t materialize.

- **A rule documented with the pattern it bans.**  My writing system now bans em dashes in published content. The file that documents the ban is written with em dashes. Instructions teach by example as much as by rule, and the example contradicted the rule.

- **Calibration constants that drifted.**  An X voice rule still gates on an audience under 50K followers. That number was true when the rule was written. It isn’t two months later (75K).

- **Guardrails for failure modes the new model doesn’t have.**  Rules like “*never delegate judgment-heavy work to cheaper models*” and complex self-check procedures exist because earlier models needed them. Each one now eats context and pulls the model toward old habits without buying the safety it used to.

- **The same rule stated in three files.**  Three maintenance surfaces, three chances to drift apart.

Two were plain mistakes. The rest were right for the model they were written for. That’s exactly the problem. The better your system was for the last model, the more it holds back this one.

### 4.2 Written by a weaker model

The pushback I got within hours of [posting my first thoughts on X](https://x.com/PawelHuryn/status/2064447192212127937?s=20): if your files contradict each other, isn't that just sloppy housekeeping? Fair question, wrong model of the system.

This knowledge layer isn't a config file a human writes once. It's self-improving: agents file evidence as they work, turn evidence into working rules, and edit their own CLAUDE.md (the system from [Three CLAUDE.md Blocks](https://www.productcompass.pm/p/claude-md-snippets)). 166 files, maintained partly by the things that read them.

In a system like that, contradictions aren't carelessness. They're drift, the same drift every wiki and every org's process docs accumulate, except here it accumulates as fast as the agents write.

That creates the real trap: a knowledge layer written by a weaker model has a flaw no amount of review can fix. Every line an agent added passed review by the model that added it, by definition. **A system maintained by model N tends to preserve the errors model N can't see.**

I review these files every day and didn't catch it. Neither did Codex, which [reviews my knowledge files as a second pair of eyes](https://www.productcompass.pm/p/codex-setup-for-pms). And no automated check could: a rule in one file conflicting with a teaching example in another is a conflict in meaning, not in text. It sat there until the first reader arrived that was stronger than the system's own authors.

### 4.3 The audit prompt

So the first prompt I ran with Fable 5 wasn't a task. It's the prompt I'd now run before giving any new model real work,