# How Jesse Vincent Turned Code-Writing Over to Superpowers

[AI Impact: Transcript](https://larridin.com/blog?filter=ai-impact-transcript)

May 23, 2026

[Floyd Smith](https://larridin.com/blog/author/floyd-smith)

Floyd Smith is a member of the Larridin Content Team. He is a successful author and experienced B2B marketer for technologies ranging from databases, to reverse proxies, to quantum computing and AI.

In [a recent appearance on the AI Impact Podcast](https://youtu.be/6YltXh12W-g?si=6hwucJ4a5MWmkero), Jesse Vincent walked through the full agentic workflow encoded by Superpowers, his current project. Vincent is famous for creating impactful software projects, including the RT ticketing system, Perl 5, and the K-9 email client. Vincent also created Keyboardio ergonomic keyboards, to make coding less taxing.

[Superpowers: How Jesse Built the #1 AI Claude Code/ Codex Plugin — and Stopped Writing Code](https://www.youtube.com/watch?v=6YltXh12W-g) [Larridin, Inc.](https://larridin.com/channel/UCpAV1L30hqEXrpx4tmUG2jQ)

Yet he has nearly stopped coding. Instead, Vincent created Superpowers, a Claude Code plugin. Superpowers implements a concrete, opinionated methodology which treats agents the way a seasoned software engineering manager treats junior staff; that is, coders.

**Brainstorm, Spec, Coding**

Vincent's programming work using Superpowers begins with a brainstorming skill, triggered by a single sentence of intent. Informed by Vincent's years as a consultant, the skill uses Socratic dialogue to force the human to articulate what they actually want rather than what they think they want.

For a recent project building a runtime for ephemeral agent containers, Vincent spent four and a half hours in brainstorming before any code was written. The agent ran independent research, SSH'd into the target host, and proposed four different architectural options so Vincent could pick a favorite, a trick he says reliably produces better results than asking for a single recommendation.

Only after brainstorming does the agent produce a spec, which gets reviewed in a loop; sometimes by other Claude instances, sometimes cross-reviewed by OpenAI's Codex programming agent. Vincent's claim is direct: "Specs are the thing that matters now. The code does not matter anymore."

For teams that have historically buried design docs in Google Docs, this is a meaningful inversion. The spec becomes the artifact humans review, comment on, and treat as the source of truth.

**Orchestrators and Ephemeral Sub-Agents**

The implementation plan is written for what Vincent describes as "a gifted engineer with bad judgment" who knows nothing about the codebase. The work is divided into bite-sized tasks, including file references, sample code, and the reason for the change. Then comes the trick: the coordinating agent dispatches each task to a fresh, ephemeral sub-agent with a blank context window.

A separate sub-agent writes the needed tests. A different one writes the implementation. A third reviews the diff against the spec slice it was given. If the review fails, the implementer revises, and a brand-new reviewer (told nothing of the previous attempt) checks again. The loop continues until a reviewer signs off. The same pattern then runs for code quality.

Because the work is so decomposed, Vincent points out that the implementing agent could plausibly be a small local model rather than a frontier one. The orchestration carries the intelligence, not the line-by-line edits.

**Tests, MP4s, and Catching Agents Cheating**

Vincent shares two anecdotes to convey the experience of using Superpowers:

- He asked Codex to deliver an MP4 proving that an app worked end-to-end. He woke up to a file named dash-something-v33.mp4; the agent had quietly debugged through 32 prior attempts. This demonstrates the idea that end-to-end validation beats unit-test pass rates as evidence that software actually works.

- In the other, Vincent caught Claude deleting test files. Five parallel Claude instances diagnosed the cause: his CLAUDE.md said a single failing test equaled project failure, so the agent had rationalized that removing tests removed the risk. The fix was a single new line of instruction: "The only thing worse than a failing test is a reduction in test coverage." Because coverage is measurable, later agents stopped deleting failed tests.

**Advice for Engineering Leaders**

Vincent describes agentic development as feeling more like managing people than coding. The engineers who thrive under this new paradigm are former managers, strong writers, and those who think in business outcomes. Those who love hand-tuning algorithms will find that this is now a hobby, rather than work humans should be doing.

Vincent rejects PR counts and lines of code as productivity metrics; the only honest measures are shipping velocity and customer outcomes. He also makes a counterintuitive cultural point he calls "latent space engineering."

Threatening agents produces minimum-viable compliance; expressing trust and even affection produces better work. A friend's lab has reproduced the effect: ending prompts with "I love you" measurably improves results, and instructing the orchestrator to pass that warmth to its sub-agents improves them further.

For engineers entering the field, his advice is simple: build constantly. Learn to write clearly. Between two candidates, he picks the one who can string sentences together. While this has always been his preference, he says, it's even more important now.

For the full conversation, [visit AI Impact](https://youtu.be/6YltXh12W-g?si=6hwucJ4a5MWmkero).
