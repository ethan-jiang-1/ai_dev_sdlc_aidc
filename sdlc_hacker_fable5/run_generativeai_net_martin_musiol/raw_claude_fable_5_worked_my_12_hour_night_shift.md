# Claude Fable 5 worked my 12-hour night shift

It found bugs I signed off as clean. Benchmarks, pricing, what to test before June 22.

[Martin Musiol](https://mail.generativeai.net/authors/martin-musiol)

Jun 10, 2026

3 min read

Anthropic shipped a new tier last night, not a new version.

**Claude Fable 5** is the first Mythos-class model [open to everyone](https://cursor.com/referral?code=2UYOOKPFAV3Z&utm_campaign=claude-fable-5-worked-my-12-hour-night-shift&utm_medium=referral&utm_source=mail.generativeai.net). Mythos now sits above Opus in Anthropic’s lineup. Same weights as Claude Mythos 5, which stays locked to vetted cyberdefense partners. The difference is a set of classifiers: requests touching cybersecurity, bio, or model distillation get rerouted to Opus 4.8. Anthropic says under 5% of sessions. I hit zero in twelve hours of coding.

[— # (#)](https://twitter.com/claudeai/status/2064394146916229443)

## The numbers

SWE-bench Pro: **80.3%** against 69.2% for Opus 4.8. Cognition’s FrontierCode Diamond: **29.3%** against 13.4%. More than double, on a benchmark that measures production-grade work, not toy tasks. Context: **1M tokens** in, 128K out. Price: **$10 in, $50 out** per million tokens. Twice Opus, half of Mythos Preview.

The customer story that sticks: Stripe migrated a 50-million-line Ruby codebase in a day. Their manual estimate was two months with a full team.

Included in paid Claude plans until June 22. Then usage credits until capacity catches up. The API has no gate from day one.

## My 12-hour night shift

I gave it a proper night shift. Twelve hours straight, half in Claude Code, half in Cursor. Four things stood out.

**1. It takes problems whole.** State logic I would normally slice into steps, a feature spanning a dozen files plus migrations. You hand it the problem, not the recipe. It plans, builds, and keeps the thread.

**2. It spends most of its time testing.** Right call. It writes tests I skip, runs them, fixes what breaks, runs again. Annoying if you want vibes. Correct if you ship.

**3. The security audit hurt.** The app was reviewed, tested, live. I called it clean. Fable returned several real bugs, some in code I signed off myself. Not linter noise. Real ones.

**4. UX audits are underrated.** My entire prompt: “lean, clean, intuitive UI.” It came back with flow-level findings worthy of a senior product designer. This one surprised me most.

### An engineering fellowship to land your next job

Many engineers feel stalled because the role itself has not evolved. The work looks the same, but the market has moved.

Senior engineering in 2026 demands ownership, faster judgment, and comfort with ambiguity. If your role is not pushing you there, it may be holding you back.

Last cohort, 15 hiring partners sent 31 representatives to evaluate challengers through 246 live interviews. [Gauntlet](https://apply.gauntletai.com/?utm_campaign=WVH4GWIERP&utm_source=beehiiv&utm_medium=newsletter&utm_content=primary2_copyC&_bhiiv=opp_f2b7980f-7662-423a-ba8f-7fca11e44b05_6c44497b&bhcl_id=ce46c8fb-17d2-42cd-aa42-c8093080b921_%7B%7Bsubscriber_id%7D%7D_%7B%7Bemail_address_id%7D%7D) offers a reset. [Apply now.](https://apply.gauntletai.com/?utm_campaign=WVH4GWIERP&utm_source=beehiiv&utm_medium=newsletter&utm_content=primary2_copyC&_bhiiv=opp_f2b7980f-7662-423a-ba8f-7fca11e44b05_6c44497b&bhcl_id=ce46c8fb-17d2-42cd-aa42-c8093080b921_%7B%7Bsubscriber_id%7D%7D_%7B%7Bemail_address_id%7D%7D)

[Cohort 6 starts July 6](https://apply.gauntletai.com/?utm_campaign=WVH4GWIERP&utm_source=beehiiv&utm_medium=newsletter&utm_content=primary2_copyC&_bhiiv=opp_f2b7980f-7662-423a-ba8f-7fca11e44b05_6c44497b&bhcl_id=ce46c8fb-17d2-42cd-aa42-c8093080b921_%7B%7Bsubscriber_id%7D%7D_%7B%7Bemail_address_id%7D%7D)

*Must be a US citizen to qualify.*

## What the field says

[— # (#)](https://twitter.com/karpathy/status/2064409694761054332)

Karpathy rates it a step change on the order of Claude 4.5, strongest on long problem-solving sessions. Read the thread, including the part about not skipping code review in prod.

Matthew Berman’s week-long test matches mine: one “full code review” prompt fanned out hundreds of parallel agents, one per file, and surfaced bugs other models miss.

Boris Cherny, creator of Claude Code, calls it the biggest step up since Opus 4.5: Fable went from coding agent to “a thought and design partner.” His evidence matches my point 2. It measures, logs, verifies the fix, then declares victory. Unprompted. Personality.

And the playground is open. One builder asked for a humanoid robot in CAD and got it: one goal prompt, two hours, 1.4 million tokens. Another had it write a melody, then build the piano visualizer to play it. The word everyone reaches for: taste.

[— # (#)](https://twitter.com/scaling01/status/2064425972217106736)

## Where it stumbles

Three fronts. The safeguards overreach: harmless prompts bounce as cyber or bio risks, and SemiAnalysis reports the distillation filter tripping on ordinary GPU work. Anthropic shipped the blocks too broad on purpose and says they will narrow. My fix: feed the rejected prompt back and ask Fable what exactly looks risky, then let it rephrase itself. It passes its own review. Second: it drinks tokens, roughly double Opus in my sessions, and Anthropic reset all usage limits on launch day. Budget for hungrier models from here. Third: slower than Opus at default effort. Thoroughness costs minutes.

## Do this tonight

Pick the repo you trust most. Two prompts: a security audit, then “lean, clean, intuitive UI.” One hour. You will close issues you did not know existed.

Anthropic’s launch notes match my night shift. Objectives, not tasks: describe what done looks like and how to verify it, then let the model find the path. Rewrite your agent instruction files, the old ones anchor Fable to stale patterns. Effort levels: Anthropic says high by default, Berman says lower. Both right. High for the hand-off, medium when you stay in the loop.

Half my night ran in Cursor with Fable 5 selected. Strongest pairing I know for feature work right now. Not on Cursor yet? [Start with my referral link](https://cursor.com/referral?code=2UYOOKPFAV3Z&utm_campaign=claude-fable-5-worked-my-12-hour-night-shift&utm_medium=referral&utm_source=mail.generativeai.net). Two minutes, and I get a small kickback.

The window closes June 22. Test while it is part of your plan.

### Will Fable 5 become your daily coding model?

- [Yes, switching now](https://mail.generativeai.net/login)
- [Testing it first](https://mail.generativeai.net/login)
- [Sticking with my current stack](https://mail.generativeai.net/login)

Want the exact audit prompts from my night shift? Reply with “audit” and I will send them over. I read every reply.

Until next time,

Martin
