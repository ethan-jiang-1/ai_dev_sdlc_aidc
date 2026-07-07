[

Modular acquires BentoML to deliver production AI in the cloud!  - Read more



](https://www.modular.com/blog/bentoml-joins-modular)

[

](https://www.modular.com/)

[

Back

](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

-   [
    
    Product
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    Resources
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    Customers
    
    
    
    ](https://www.modular.com/customers)
-   [
    
    Docs
    
    
    
    ](https://docs.modular.com/max/)
-   [
    
    Blog
    
    
    
    ](https://www.modular.com/blog)
-   [
    
    Company
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    Request Demo
    
    
    
    ](https://www.modular.com/request-demo)

[

](https://github.com/modular/modular)[

Get started

](https://docs.modular.com/max/get-started)

-   -   MODULAR PLATFORM
        
        -   [
            
            MAX Framework
            
            GenAI native modeling & serving
            
            ![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/690d3398ec2956898ed94e68_max-hero.png)
            
            ](https://www.modular.com/max)
        -   [
            
            Mojo Language
            
            The best GPU & CPU performance
            
            ](https://www.modular.com/mojo)
        -   [
            
            Mammoth
            
            Scale intelligently to any cluster
            
            ![Cartoon mammoth wearing futuristic blue visor and high-tech backpack with glowing elements.](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/68cd4d25c9c954cb1b845eb5_mammoth-hero.png)
            
            ](https://www.modular.com/mammoth)
    -   DEPLOYMENT OPTIONS
        
        -   [
            
            Deployment
            
            Modular cloud
            
            ](https://www.modular.com/deployment)
        -   [
            
            Editions
            
            All the ways you can use Modular
            
            ](https://www.modular.com/pricing)
-   -   [
        
        Docs
        
        Get up and running. Fast.
        
        ](https://docs.modular.com/)
    -   [
        
        Models
        
        500+ supported open models
        
        ](https://builds.modular.com/?category=models)
    -   [
        
        Tutorials
        
        Build amazing things
        
        ](https://docs.modular.com/max/tutorials)
    -   [
        
        Recipes
        
        Step-by-step guides
        
        ](https://builds.modular.com/?category=recipes)
    -   [
        
        GPU Puzzles
        
        Learn GPU Programming
        
        ](https://builds.modular.com/puzzles)
    -   [
        
        Community
        
        Build the future of AI together
        
        ](https://www.modular.com/community)
-   -   [
        
        About
        
        Build AI for anyone, anywhere.
        
        ](https://www.modular.com/company/about)
    -   [
        
        Careers
        
        We’re currently hiring!
        
        ](https://www.modular.com/company/careers)
    -   [
        
        Culture
        
        What we believe
        
        ](https://www.modular.com/company/culture)
    -   [
        
        Contact Us
        
        Request a demo
        
        ](https://www.modular.com/request-demo)

[

](https://github.com/modular/modular)[

Get started

](https://docs.modular.com/max/get-started)

close

February 18, 2026

# The Claude C Compiler: What It Reveals About the Future of Software

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1ab11_64078db03b0c891d0c658708_Chris.jpeg)

Chris Lattner

Engineering

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6996624ca950e0f8926d6f86_Option05.png)

Compilers occupy a special place in computer science. They're a canonical course in computer science education. Building one is a rite of passage. It forces you to confront how software actually works, by examining languages, abstractions, hardware, and the boundary between human intent and machine execution.

Compilers once helped humans speak to machines. Now machines are beginning to help humans build compilers.

I’ve spent a large part of my career working on compilers and programming languages, so when [Anthropic announced the](https://www.anthropic.com/engineering/building-c-compiler) [_Claude C Compiler_](https://www.anthropic.com/engineering/building-c-compiler) (CCC), I paid close attention. My basic take is simple: this is real progress, a milestone for the industry. We’re not in the end of times, but this also isn’t just hype, so take a deep breath, everyone.

AI building a C compiler is not truly revolutionary, but it does reveal how far AI coding has progressed and where it may be heading next.

Before diving in, here are my main take-aways:

-   AI has moved beyond writing small snippets of code and is beginning to participate in engineering large systems.
-   AI is crossing from local code generation into global engineering participation: CCC maintains architecture across subsystems, not just functions.
-   CCC has an “LLVM-like” design (as expected): training on decades of compiler engineering produces compiler architectures shaped by that history.
-   Our legal apparatus frequently lags behind technology progress, and AI is pushing legal boundaries. Is proprietary software cooked?
-   Good software depends on judgment, communication, and clear abstraction. AI has amplified this.
-   AI coding is automation of implementation, so design and stewardship become more important.
-   Manual rewrites and translation work are becoming AI-native tasks, automating a large category of engineering effort.
-   AI, used right, should produce better software, provided humans actually spend more energy on architecture, design, and innovation.
-   Architecture documentation has become infrastructure as AI systems amplify well-structured knowledge while punishing undocumented systems.

The implications for engineering teams are real and immediate. At the end, I share how I'm translating these insights into concrete expectations for my team at Modular.

## What are Compilers? Why do they matter as an AI Benchmark?

To understand why the Claude C Compiler matters, we must first understand why compilers themselves are such a revealing test of intelligence, whether human or artificial.

A compiler sits at the intersection of multiple difficult domains at once: formal language design, large-scale software architecture, deep performance constraints, and unforgiving correctness requirements.

Most applications can tolerate bugs, compilers cannot. A single incorrect transformation can silently produce wrong programs, disrupting the productivity of countless users. Every layer must maintain strict invariants while cooperating with every other layer.

Historically, this is why compilers became a rite of passage in [computer science education](https://www.amazon.com/Modern-Compiler-Implement-Andrew-Appel/dp/0521607647/ref=sr_1_1). They force engineers to think across abstraction layers: turning text into structure, structure into meaning, meaning into optimized machine behavior.

![From my previous piece on LLVM compiler design. ](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/6996624795e78de0713c65e0_image.png)

_From_ [_my previous piece_](https://aosabook.org/en/v1/llvm.html) _on LLVM compiler design._

That process mirrors something deeper, which is the process of translating human intent into precise execution, which is why compilers are a uniquely interesting benchmark for AI system integration.

Earlier generations of AI coding tools were impressive at local tasks, such as writing functions, generating scripts, or filling in missing pieces of code. Those tasks test pattern recognition and short-term reasoning.

The Claude C Compiler is a milestone, showing progress at a different level. It shows an AI system maintaining coherence across an entire engineering system that can coordinate multiple subsystems, preserve architectural structure, iterate toward correctness over time, and operate within a complex feedback loop of tests and failures. AI is beginning to move from _code completion_ toward _engineering participation_.

However, the deeper reason compilers align unusually well with modern AI systems is that compiler engineers build architectures that are highly legible and structured. Compilers have layered abstractions, consistent naming conventions, composable passes, and deterministic feedback (“it works” or “it doesn’t” - there is a clear success criteria). These properties make compilers unusually learnable for both humans _and_ machine learning systems trained on large amounts of source code.

Seen this way, CCC is validation of decades of software engineering practice. The abstractions developed by compiler engineers turned out to be structured enough that machines can now reason within them. That is a remarkable milestone. However, it also hints at an important limitation.

## **Looking Inside the Claude C Compiler**

One of the most interesting aspects of the Claude C Compiler is that Anthropic [released the full source history](https://github.com/anthropics/claudes-c-compiler). Unlike many AI demonstrations, this is an engineering artifact that anyone can inspect, not simply a polished result or benchmark score. The entire repository, including commit history, [design documents](https://github.com/anthropics/claudes-c-compiler/blob/main/src/backend/README.md), and [future plans](https://github.com/anthropics/claudes-c-compiler/tree/main/ideas), is available. That means we can actually study _how_ the system approached building a compiler. I spent some time doing exactly that.

The [first major commit](https://github.com/anthropics/claudes-c-compiler/commit/26f6f8b2c1db903cb718bd8d0496ccdbb9711294) effectively “one-shots” the basic architecture of the system. From the start, CCC follows a classic compiler structure. Major subsystems all have pretty amazing design docs too, including:

-   a frontend handling [preprocessing](https://github.com/anthropics/claudes-c-compiler/tree/main/src/frontend/preprocessor), [parsing](https://github.com/anthropics/claudes-c-compiler/tree/main/src/frontend/parser), and [semantic analysis](https://github.com/anthropics/claudes-c-compiler/tree/main/src/frontend/sema) (common to all compilers)

  

-   an [intermediate representation](https://github.com/anthropics/claudes-c-compiler/tree/main/src/ir) and [optimizations](https://github.com/anthropics/claudes-c-compiler/blob/main/src/ir/mem2reg/README.md) that are directly [inspired by LLVM](https://github.com/anthropics/claudes-c-compiler/issues/231)
-   and a [backend responsible for code generation](https://github.com/anthropics/claudes-c-compiler/tree/main/src/backend), with 4 architectures ([x86-32](https://github.com/anthropics/claudes-c-compiler/tree/main/src/backend/i686), [x86-64](https://github.com/anthropics/claudes-c-compiler/tree/main/src/backend/x86), [RISC-V](https://github.com/anthropics/claudes-c-compiler/tree/main/src/backend/riscv), and [AArch64](https://github.com/anthropics/claudes-c-compiler/tree/main/src/backend/arm))

The design choices throughout the repository consistently reflect well-established compiler practice - things taught in a university class and widely used by existing compilers like LLVM and GCC. The intermediate representation includes concepts that will look immediately familiar to LLVM developers, including [instructions like](https://github.com/anthropics/claudes-c-compiler/blob/main/src/ir/README.md#instruction-set) [`GetElementPtr`](https://github.com/anthropics/claudes-c-compiler/blob/main/src/ir/README.md#instruction-set), basic block “[terminators](https://github.com/anthropics/claudes-c-compiler/blob/main/src/ir/README.md#terminators)” and [Mem2Reg](https://github.com/anthropics/claudes-c-compiler/blob/main/src/ir/mem2reg/README.md). It appears to have [strong knowledge](https://github.com/anthropics/claudes-c-compiler/blob/main/ideas/high_use_def_chains.txt) of widely-used compiler design [techniques](https://github.com/anthropics/claudes-c-compiler/blob/main/src/ir/mem2reg/README.md#ssa-construction-algorithm).

![Example subsystem compiler architecture  ](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/69966247697f39cee3d8283b_image.png)

_E__xample subsystem compiler architecture_

LLVM and GCC code are clearly part of the training set - Claude effectively translated large swaths of them into Rust for CCC. The design docs show detailed knowledge of both systems, as well as [considered takes on its implementation approach](https://github.com/anthropics/claudes-c-compiler/tree/main/src/frontend/preprocessor#design-decisions). Some have criticized CCC for learning from this prior art, but I find that ridiculous - I certainly [learned from GCC when building Clang!](https://newsletter.pragmaticengineer.com/p/from-swift-to-mojo-and-high-performance)

Pushpendre Rastogi wrote a [great blog post about CCC and agent scaling laws](https://vizops.ai/blog/agent-scaling-laws/), showing how iterative agent workflows gradually expanded implementation and test coverage:

![Code archaeology timeline, by Pushpendre Rastogi (included with permission)](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/6996624a26163069e119a103_image1.png)

_Code archaeology timeline,_ [_by Pushpendre Rastogi_](https://vizops.ai/blog/agent-scaling-laws/) _(included with permission)_

Taken together, CCC looks less like an experimental research compiler and more like a competent textbook implementation, the sort of system a strong undergraduate team might build early in a project before years of refinement. That alone is remarkable.

### **What did the** Claude C Compiler **get wrong?**

The most revealing parts of CCC are its mistakes. Several design choices suggest optimization toward passing tests rather than building general abstractions like a human would. A few examples:

-   The code generator is “toy” and the optimizer [reparses assembly text](https://github.com/anthropics/claudes-c-compiler/blob/main/src/backend/x86/codegen/peephole/passes/local_patterns.rs#L410) instead of using an IR, and the code generators are poorly factored.
-   The parser appears to have [poor error recovery](https://github.com/anthropics/claudes-c-compiler/blob/main/src/frontend/lexer/README.md#no-separate-lexer-error-token) / usability and have some [incorrect corner cases](https://github.com/anthropics/claudes-c-compiler/blob/main/src/frontend/parser/README.md#cast-expression-ambiguity).
-   It appears that CCC doesn’t parse system headers (which are much more gnarly to deal with than application code) so it [hard codes in things](https://github.com/anthropics/claudes-c-compiler/blob/main/src/frontend/parser/parse.rs#L329) it needs for its tests.

This last issue is the big problem that indicates CCC won’t be able to generalize well beyond its test-suite, which appears to be [confirmed](https://github.com/anthropics/claudes-c-compiler/issues/74) by its [bug tracker](https://github.com/anthropics/claudes-c-compiler/issues/1). These flaws are informative rather than surprising, suggesting that current AI systems excel at assembling known techniques and optimizing toward measurable success criteria, while struggling with the open-ended generalization required for production-quality systems.

And that observation leads directly to the deeper question: what does this tell us about AI coding itself?

## What the Claude C Compiler Reveals About AI Coding

The most interesting lesson from the Claude C Compiler is not that AI can build a compiler. It’s _how_ it built one. CCC didn’t invent a new architecture or explore an unfamiliar design space. Instead, it reproduced something strikingly close to the accumulated consensus of decades of compiler engineering: structurally correct, familiar, and grounded in well-understood techniques.

Modern LLMs are extraordinarily powerful distribution followers. They learn patterns across vast bodies of existing work and generate solutions near the center of that collective experience. When trained on decades of compilers shaped by GCC, LLVM, and academic literature, it is entirely natural that the result reflects that lineage. This phenomenon closely aligns with Richard Sutton’s _Bitter Lesson_, where scalable methods [rediscover broadly successful structures](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).

An analogy helps. Training on English literature allows a model to produce Shakespearean prose: not because literature stopped evolving in the 1600s. Instead, it’s because Shakespeare occupies a dense region of the training distribution. Models learn what has been widely written and reinforced. The same dynamic appears here in compiler design (of all things, rawr! 🐉).

![Every course of human knowledge, absorbed at scale - but who writes the next curriculum?](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/6996624b6a3857739f87f9cb_Gemini_Generated_Image_bmzkqibmzkqibmzk.png)

Every course of human knowledge, absorbed at scale - but who writes the next curriculum?

CCC shows that AI systems can internalize the _textbook knowledge_ of a field and apply it coherently at scale. AI can now reliably operate within established engineering practice. This is a genuine milestone that removes much of the drudgery of repetition and allows engineers to start closer to the state of the art. But it also highlights an important limitation of this work:

Implementing known abstractions is not the same as inventing new ones. I see nothing novel in this implementation.

Historically, progress in compilers did not come from assembling standard components quickly. It came from conceptual leaps, e.g. new intermediate representations, new optimization models, new ways of structuring programs and hardware interaction. It came from getting groups of people to work together, which required inspiring and motivating engineers in new ways.

Current AI coding systems excel when success criteria are clear and verifiable: compile the program, pass the tests, improve performance. In these environments, iterative refinement works extremely well: [red/green TDD works](https://bookshop.org/p/books/test-driven-development-by-example-kent-beck/e44aeb44342499d9)! Innovation is different. When inventing a new abstraction, success is not yet measurable. There is no test suite for an idea that does not exist, and good design is hard to quantify.

> AI coding is therefore best understood as another step forward in automation. It dramatically lowers the cost of implementation, translation, and refinement. As those costs fall, the scarce resource shifts upward: deciding what systems should exist and how software should evolve.

As writing code is becoming easier, _designing software_ becomes more important than ever. As custom software becomes cheaper to create, the real challenge becomes choosing the right problems and managing the resulting complexity. I also see big open questions about who is going to maintain all this software.

## IP Law and Proprietary Software Moats

The Claude C Compiler also raises important yet uncomfortable questions about intellectual property. If AI systems trained on decades of publicly available code can reproduce familiar structures, patterns, and even specific implementations, where exactly is the boundary between learning and copying? Some observers have pointed out cases where CCC appears to regenerate artifacts strongly [resembling existing implementations](https://github.com/anthropics/claudes-c-compiler/issues/231), including [standard headers](https://github.com/anthropics/claudes-c-compiler/blob/main/include/arm_neon.h) and [utility code](https://x.com/devknoll/status/2019609090562093309?s=20), despite claims of [“clean room” development](https://www.anthropic.com/engineering/building-c-compiler). These examples highlight how [current legal frameworks](https://github.com/anthropics/claudes-c-compiler/issues/231#issuecomment-3873754810) struggle to describe systems that learn statistically from vast prior work rather than explicitly referencing source material.

At the same time, this situation is not new. Humans learn by studying existing systems, internalizing patterns, and reapplying ideas in new contexts. The difference is scale and automation. AI compresses decades of engineering knowledge into a generative model capable of reproducing solutions instantly. That challenges traditional assumptions about ownership when the underlying ideas are widely shared but specific expressions may still carry licenses.

We are facing a new era of automated reimplementation of proprietary software, but this doesn’t mean the paradigm is suddenly obsolete. AI lowers the cost of reproducing established designs, which will shift competitive advantage away from isolated codebases and toward execution, ecosystems, and continuous innovation. This will force legal and institutional norms to evolve, similar to when Linux and open source software first gained wide-spread adoption. Just as with those transitions, I am betting that we will see ecosystem gravity from human collaboration replace legacy ecosystems that cannot keep pace with rapidly changing times.

## Automation, Innovation, and the Future of Software

If AI coding primarily _automates implementation_, what happens next?

History gives us a clear pattern: when the cost of building something drops dramatically, we [don’t simply build the same things more cheaply](https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf). We build entirely new things.

Compilers themselves are a perfect example. Early programmers wrote assembly by hand, but once compilers became reliable, developers became vastly more ambitious and entire industries emerged because abstraction made complexity manageable. As writing code becomes easier, the likely outcome is not fewer programmers but more software. We will get more experimentation, more specialized tools, and solutions to problems that previously weren’t worth automating.

![Conducting aeronautical research with an IBM 704 in 1957 via NASA](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/6996624bb37cb6dd6a5f6413_image.png)

Conducting aeronautical research with an IBM 704 in 1957 via NASA

What changes is the economics of engineering work and particularly the large-scale elimination of mechanical tasks like rewrites, migrations, and boilerplate implementation. These activities are necessary but rarely innovative, and AI systems are unusually good at exactly this kind of work. Engineers move from typing implementations toward directing systems: specifying intent, validating outcomes, and shaping architecture.

As implementation becomes cheaper, the role of engineers shifts upward. The scarce skills become choosing the right abstractions, defining meaningful problems, and designing systems that humans and AI can evolve together. This will increasingly blur the boundary between software engineering and product thinking. The limiting factor is no longer whether software _can_ be built, but deciding what _should_ be built and how to manage the complexity that follows. AI amplifies both good and bad structure, so we can expect to see poorly managed code scale into incomprehensible nightmares.

That raises the next question: if programming is changing this fundamentally, what happens to software engineers themselves?

## The Evolving Role of Software Engineers

Every major shift in software development has changed what it means to be a programmer. Early engineers managed hardware directly, while later generations learned to trust compilers and higher-level languages. Each transition removed manual work while raising expectations for what engineers could accomplish, and AI coding represents the next step in that progression.

As implementation grows increasingly automated, the core skill of software engineering shifts away from writing code line-by-line and toward shaping systems. Engineers can focus on deciding what should exist, how components fit together, and how complexity remains understandable over time. Good software depends on judgment, communication, and clear abstraction. AI systems amplify these human qualities, rather than replacing them.

The most effective engineers will not compete with AI at producing code, but will learn to collaborate with it, by using AI to explore ideas faster, iterate more broadly, and focus human effort on direction and design. These tools are rapidly becoming part of the normal software development stack, much like compilers, version control, or continuous integration before them. Learning to work effectively with AI is quickly becoming a core professional skill. Ignoring AI today would be like refusing to adopt source control twenty years ago.

![Source: CircleCI State of Software Delivery Report, 2026 via Luca Rossi’s The Era of the Software Factory. The top teams are pulling away, fast.](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/6996624b6891368b4f0ad304_image.png)

Source: [CircleCI State of Software Delivery Report, 2026](https://circleci.com/software-delivery-data-explorer/) via Luca Rossi’s [The Era of the Software Factory](https://refactoring.fm/p/the-era-of-the-software-factory). The top teams are pulling away, fast.

The gap between teams successfully embracing AI tooling and those that aren't is already measurable and widening fast. According to [CircleCI's 2026 State of Software Delivery Report](https://circleci.com/software-delivery-data-explorer/), the top 5% of engineering teams nearly doubled their output year-over-year, while the bottom half stagnated. The most productive team in 2025 delivered roughly 10x the throughput of 2024's leader.

Which raises a practical question: how should teams adapt to be successful?

Here's how I'm translating this shift into concrete expectations for Modular.

## How I Expect Modular to Adapt to AI tools

Developments like the Claude C Compiler have changed how I think about engineering work and what I now ask from my team. Fully benefiting from AI tools requires a deliberate leap: habits formed over decades don’t change automatically, and organizations rarely transform just because better tools exist.

At the same time, we need to be pragmatic. AI systems are powerful but far from perfect. Progress comes from collaboration with AI, not abdication to it. The goal is not to remove humans from the loop, but to move humans into higher-leverage positions inside it.

That leads to three expectations:

### **1\. Aggressively** **adopt AI while s****taying accountable**

Every employee, from engineering to G&A and GTM, is expected to actively adopt AI tools to accelerate productivity and decision-making. The world is moving quickly, and we must lean into change.

Crucially, this does not transfer responsibility to the tool. For example, engineers building large-scale production software [remain accountable for correctness](https://llvm.org/docs/AIToolPolicy.html), design quality, and long-term maintainability. AI expands our capabilities, but it does not outsource judgment. Work produced with AI should be understood, validated, and owned just as deeply as work written by hand. Reputation is still built on outcomes, not prompts.

### **2\. Move human effort up the stack**

A large fraction of historical engineering effort has gone into mechanical work: rewriting code, adapting interfaces, migrating systems, and reproducing existing patterns in new environments. AI is rapidly becoming better at these tasks than humans. We should not compete with automation at mechanical work. Instead, engineers should clarify intent with rigor, validate outcomes with tests, and improve their design.

Human effort should concentrate where creativity and judgment matter most: and all engineers now have management responsibilities. As migration and implementation accelerate, architectural evolution is no longer limited by how fast humans can rewrite software, but by how clearly we can define where systems should go next.

### **3\. Invest in structure and community**

AI amplifies structure.

Well-documented systems become dramatically easier to extend and evolve, and poorly structured systems scale into confusion faster than ever. Documentation, clear interfaces, and explicit design intent are now operational leverage, not optional overhead.

As implementation costs approach zero, the scarce resource shifts from writing code to aligning people. The greatest opportunity lies in building communities of like-minded people that collaborate toward shared goals and ecosystems where developers can move forward together instead of repeatedly rebuilding the past.

For my team, that means focusing on tools and platforms that help other developers succeed: systems that move existing code forward, unlock modern compute, and enable collaboration between humans and AI. This aligns directly with Modular’s [mission to Democratize AI Compute](https://www.modular.com/democratizing-ai-compute) and expand what programmers everywhere can create.

### Closing Thoughts

The Claude C Compiler doesn’t mark the end of software or compiler engineering. If anything, it opens the door wider. The easier implementation gets, the more room there is for genuine innovation.

Lower barriers to implementation do not reduce the importance of engineers; instead, they elevate the importance of vision, judgment, and taste. When creation becomes easier, deciding _what is worth creating_ becomes the harder problem. AI accelerates execution, but meaning, direction, and responsibility remain fundamentally human.

**Writing code has never been the goal.** **Building meaningful software is****.** The future belongs to teams willing to embrace new tools, challenge assumptions, and design systems that help people create together.

That is the future that has driven Modular’s mission from the start, and the one I believe this new era of AI makes possible.

\- Chris Lattner

  

* * *

Want to build the AI future with us? [Modular is hiring](https://www.modular.com/company/careers#open-roles).

  

## Read more from Modular

[

View all blogs

](https://www.modular.com/blog)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6984f903eb465bf32916cf6d_Gemini_Generated_Image_egiucbegiucbegiu.jpeg)

The Five Eras of KVCache

February 5, 2026

[](https://www.modular.com/blog/the-five-eras-of-kvcache)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/695e4a43361ef1d3c7d32607_68f13b8008ac53405e7fa7ad_AMD2.jpeg)

Achieving State-of-the-Art Performance on AMD MI355 — in Just 14 Days

October 17, 2025

[](https://www.modular.com/blog/achieving-state-of-the-art-performance-on-amd-mi355----in-just-14-days)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/695e4a6b00399522dff8217e_685b3481a020b5d4b20a047a_685b347fe1ad1a2c1274bc16_34c4acd5c588d8420f0399d0b9c92330.webp)

Exploring Metaprogramming in Mojo

May 27, 2025

[](https://www.modular.com/blog/metaprogramming)

Build the future of AI with Modular

[

Get started - FREE

](https://docs.modular.com/max/get-started)

[

View Editions

](https://www.modular.com/pricing)

-   ![Person with blonde hair using a laptop with an Apple logo.](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/68cc733ff9050921bab7782c_emoji-dev.png)
    
    Get started guide
    
    Install MAX with a few commands and deploy a GenAI model locally.
    
    [
    
    Read Guide
    
    ](https://docs.modular.com/max/get-started)[](https://docs.modular.com/max/get-started)
-   ![Magnifying glass emoji with black handle and round clear lens.](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/68cc733fb111718bbd49ca31_emoji-zoom.png)
    
    Browse open models
    
    500+ models, many optimized for lightning-fast performance
    
    [
    
    Browse models
    
    ](https://builds.modular.com/?category=models)[](https://builds.modular.com/?category=models)

## Sign up for our newsletter

Get all our latest news, announcements and updates delivered directly to your inbox. Unsubscribe at anytime.

⚠️ This form requires JavaScript to function. Please enable JavaScript in your browser to continue.

Email\*

First Name

Last Name

Thanks for signing up to our newsletter! 🚀

Thank you,

Modular Sales Team

Oops! Something went wrong while submitting the form.

Latest from our blog:

[

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/698b3d9c1a2a7039840ceff8_image%20(1).png)

New

BentoML Joins Modular



](https://www.modular.com/blog/bentoml-joins-modular)

Get the latest news,  
announcements & updates:

[

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a81f/68cc76bcf732ee52e8efb9d9_icon-email.svg)

Join our Newsletter

](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

-   Product
    
    -   [
        
        Editions
        
        
        
        ](https://www.modular.com/pricing)
    -   [
        
        Install
        
        
        
        ](https://docs.modular.com/max/get-started/)
    -   [
        
        Mammoth
        
        
        
        ](https://www.modular.com/mammoth)
    -   [
        
        MAX
        
        
        
        ](https://www.modular.com/max)
    -   [
        
        Mojo
        
        
        
        ](https://www.modular.com/mojo)
-   Quick Start
    
    -   [
        
        Documentation
        
        ](https://docs.modular.com/max/)
    -   [
        
        GenAI models
        
        ](https://builds.modular.com/?category=models)
    -   [
        
        Run Gemma3
        
        ](https://builds.modular.com/models/gemma-3-it/1B)
-   Solutions
    
    [
    
    Batch inference
    
    ](https://www.modular.com/request-demo)
    
    [
    
    Code Generation
    
    ](https://www.modular.com/code-generation)
    
    [
    
    AI Agents
    
    ](https://www.modular.com/max/solutions/agent)
    
    [
    
    AI Inference
    
    ](https://www.modular.com/max/solutions/ai-inference)
    
    [
    
    Chatbots
    
    ](https://www.modular.com/max/solutions/chatbots)
    
    [
    
    RAG & CAG
    
    ](https://www.modular.com/max/solutions/rag-cag)
    
    [
    
    Research
    
    ](https://www.modular.com/max/solutions/research)
    
-   Developers
    
    -   [
        
        Docs
        
        ](https://docs.modular.com/max/)
    -   [
        
        Modular Help Forum
        
        ](https://forum.modular.com/)
    -   [
        
        MAX Changelog
        
        ](https://docs.modular.com/max/changelog)
    -   [
        
        Mojo🔥 Changelog
        
        ](https://docs.modular.com/mojo/changelog)
-   Connect
    
    -   [
        
        Blog
        
        ](https://www.modular.com/blog)
    -   [
        
        Community
        
        ](https://www.modular.com/community)
    -   [
        
        Report a security issue
        
        ](https://www.modular.com/company/report-issue)
-   Company
    
    -   [
        
        About Us
        
        ](https://www.modular.com/company/about)
    -   [
        
        Culture
        
        ](https://www.modular.com/company/culture)
    -   [
        
        Careers
        
        ](https://www.modular.com/company/careers)
    -   [
        
        Request a demo
        
        ](https://www.modular.com/request-demo)

-   [
    
    ](https://github.com/modular/modular)
-   [
    
    ](https://discord.gg/modular)
-   [
    
    ](https://x.com/modular)
-   [
    
    ](https://youtube.com/@modularinc)
-   [
    
    ](https://linkedin.com/company/modular-ai)
-   [
    
    ](https://www.modular.com/blog/rss.xml)

Copyright © 2026 Modular Inc

[Terms](https://www.modular.com/legal/terms), [Privacy](https://www.modular.com/legal/privacy) & [Acceptable Use](https://www.modular.com/legal/aup)

Join our newsletter

Get all our latest news, announcements and updates delivered directly to your inbox. Unsubscribe at anytime.

Email\*

First Name

Last Name

Thanks for signing up to our newsletter! 🚀

Thank you,

Modular Sales Team

Oops! Something went wrong while submitting the form.

Return to page

Modular Champions

X/X

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417ad2de85aa7c73eed_6923596dc4d3dc4a769cfda4_owen-hilyard.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417ad2de85aa7c73ee9_69235dd6654439019c9ccaf3_fire.jpeg)

Owen Hilyard

I'm a PhD student at the University of New Hampshire in the Cloud Computing Lab, where I conduct research on hardware acceleration of networking and distributed systems reliability. I'm also a former component maintainer for DPDK, the Data Plane Development Kit, which is where I got my start looking "under the hood" at networking before resigning to work in my PhD. All of this means I like making computers go fast, and Mojo + MAX is a great place to combine my love of hardware, high performance software, and my interest in programming languages. I also act as one of the community moderators for Modular on the Discord server and Discourse forum.

Connect with Owen Hilyard

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.linkedin.com/in/owen-hilyard-7ba8a7168/)
-   [
    
    ](https://github.com/owenhilyard)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4172ce608abed214612_69235996eaf244c8c1584940_seth-stadick.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4172ce608abed21460c_6924a25d0e1bcaded722ecb7_emoji-explode.png)

Seth Stadick

I'm a Bioinformatics Software Engineer passionate about building high-performance systems. For the past six years, I've developed in Rust across environments ranging from Raspberry Pi devices to full-scale HPC clusters in the cloud. I'm excited about Mojo's potential to reshape how we approach performance-critical computing.When I'm not coding, I’m usually spending time with my family — or trying to land new tricks on a skateboard (I just learned to Ollie)!

Connect with Seth Stadick

-   [
    
    ](https://bsky.app/profile/ducktapeprogrammer.bsky.social)
-   [
    
    ](https://www.linkedin.com/in/seth-stadick-ms-95b63151/)
-   [
    
    ](https://github.com/sstadick)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4177507f06c6a92ec1b_692359bc01147a2f4c3cfd1a_brian-grenier.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4177507f06c6a92ec17_6924a269769e4a94d866aa27_emoji-machevuoi.png)

Brian Grenier

I am C++ developer working for a cardiac image processing company. I've been a Mojo standard library contributor since 2024. I also actively maintain two libraries, EmberJSON, a JSON library written in pure Mojo, and Kelvin, a type safe dimensional analysis library. I often hang out in the Mojo discord and forum!

Connect with Brian Grenier

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.linkedin.com/in/brian-grenier-07a724162/)
-   [
    
    ](https://github.com/bgreni)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417d0370bc41829c918_69235a2d17b125834ba5d721_martin-vuyk.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417d0370bc41829c915_6924a274cb0a7c1a1952d336_emoji-q2.png)

Martin Vuyk

I'm a Mechatronics Engineer who pivoted into Software Development. I like tackling complex problems and building lasting solutions. I invest my time into things that I think will be impactful.

Connect with Martin Vuyk

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.linkedin.com/in/martin-vuyk-loperena-37181b230)
-   [
    
    ](https://github.com/martinvuyk)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4178e2aa2dbe4926c97_692359d23c0eb0b468eb85f7_sawyer-bergeron.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4178e2aa2dbe4926c9c_6924a281d231594a12889d97_emoji-q.png)

Sawyer Bergeron

Compiler, PL, and systems/performance engineering enthusiast with an eyebrow-raising amount of VAX assembly experience. Collector (of hobbies). Enjoys bagels just a bit too much.

Connect with Sawyer Bergeron

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.linkedin.com/in/sawyerbergeron/)
-   [
    
    ](https://github.com/szbergeron)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4184404f567d86c3fa0_692359d8e862996d6e873fd0_valentin-erokhin.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4184404f567d86c3faf_6924a2a54f7f4a53bc9d3e84_emoji-bee.png)

Valentin Erokhin

Author of Lightbug, a Mojo HTTP Framework (https://github.com/Lightbug-HQ/lightbug\_http)

Connect with Valentin Erokhin

-   [
    
    ](https://bsky.app/profile/a2svior.bsky.social)
-   [
    
    ](https://www.linkedin.com/in/valentin-erokhin-24969a14a/)
-   [
    
    ](https://github.com/saviorand)
-   [
    
    ](https://www.valentin.wiki/)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c418a0e1f9e5c50ed4ed_692359dc98d5de59b8ba0c44_sora.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c418a0e1f9e5c50ed4ea_6924a2b1c56b7843eca61fbf_emoji-upsidedown.png)

Sora

Connect with Sora

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://github.com/soraros)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417cd73c8fb08635a25_692359c79405151086edae43_maxim-zaks.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417cd73c8fb08635a2a_6924a2bfbcf7b7f70604b3d4_emoji-catscare.png)

Maxim Zaks

I tell computers how to waste electricity, hopefully in an efficient or at least useful way.

Connect with Maxim Zaks

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.linkedin.com/in/m-zaks)
-   [
    
    ](https://github.com/mzaks)
-   [
    
    ](https://mzaks.medium.com/)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4175a760300836082b5_6924a60ada600939ad5c5f18_IMG_20210929_110905618_HDR%2520-%2520Gabriel%2520de%2520Marmiesse.jpeg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c4175a760300836082b1_6924a691ca8d9f4a839c3826_emoji-cat.png)

Gabriel de Marmiesse

Former core dev of Keras, author of Python-on-whales, currently working at Kyutai to democratize AI through open science

Connect with Gabriel de Marmiesse

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.linkedin.com/in/gabriel-de-marmiesse-52146711b/)
-   [
    
    ](https://github.com/gabrieldemarmiesse)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6977d5022d2e3029ab1dbec8_MaxB-Profile.jpg)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c417da688b9ef16432e5_6924a2d7e11925ae81cd9348_emoji-sunflower.png)

Max Brylski

Explorer of the computational universe

Connect with Max Brylski

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://github.com/helehex)
-   [
    
    ](https://helehex.net/)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c418ca0bcd2d54f4a6fb_69262f1707de6d827b446673_avatar-max.png)![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/6926c418ca0bcd2d54f4a6f8_6924a2cf819ab6c2525890bf_emoji-monkey.png)

Tilli Fe

Connect with Tilli Fe

-   [
    
    ](https://x.com/tilli_fe)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://github.com/TilliFe)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

Return to page

Leadership team

X/X

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1b279_Chris.jpg)

Chris Lattner

[Distinguished Leader](http://www.nondot.org/sabre/) who founded and scaled critical infrastructure including [LLVM](https://llvm.org/), [Clang](https://clang.llvm.org/), [MLIR](https://mlir.llvm.org/), [Cloud TPUs](https://cloud.google.com/tpu) and the [Swift](https://swift.org/) programming language. Chris built AI and core systems at multiple world leading technology companies including Apple, Google, SiFive and Tesla.

Connect with Chris Lattner

-   [
    
    ](https://www.twitter.com/clattner_llvm)
-   [
    
    ](https://www.linkedin.com/in/chris-lattner-5664498a/)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1b267_Tim.jpg)

Tim Davis

[Repeat Entrepreneur](http://www.timdavis.com/about) and Product Leader. Tim helped build, found and scale large parts of Google's AI infrastructure at [Google Brain](https://research.google/teams/brain/) and Core Systems from APIs ([TensorFlow](http://www.tensorflow.org/)), Compilers ([XLA](https://www.tensorflow.org/xla) & [MLIR](https://www.blog.google/technology/ai/mlir-accelerating-ai-open-source-infrastructure/)) and runtimes for server (CPU/GPU/TPU) and [TF Lite](https://www.youtube.com/watch?v=Jjm7MT6W0Dc) (Mobile/Micro/Web), [Android ML](https://developers.google.com/ml-kit) & [NNAPI](https://source.android.com/devices/architecture/modular-system/nnapi), large model infrastructure & OSS for billions of users and devices. Loves running, building and scaling products to [help people](https://www.youtube.com/watch?v=o623TB-mY6A), and [the world](https://www.youtube.com/watch?v=UT2noVDFoaA).

Connect with Tim Davis

-   [
    
    ](https://twitter.com/iamtimdavis)
-   [
    
    ](https://www.linkedin.com/in/timdavisau/)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1b26c_Mostafa.jpg)

Mostafa Hagog

Mostafa is a seasoned engineering leader in high-performance computing. During his tenure at [NVIDIA](https://www.nvidia.com/en-us/), he served as Engineering Director and led teams to develop optimized deep learning libraries like cuDNN and CUTLASS, revolutionizing GPU-accelerated AI. At [SiFive](https://www.sifive.com/), as VP of Software, Mostafa assumed a leadership role guiding teams in the development of an MLIR/LLVM-based software stack for SiFive Intelligence & performance cores. His contributions also extend to optimizing [Intel](https://www.intel.com/content/www/us/en/homepage.html) GPU hardware/software features, playing a pivotal role in developing the AVX1/2 SIMD ISA for Intel CPUs, and contributing to the GNU C Compiler. Mostafa holds a Master of Science in Electrical Engineering from the [Technion](https://www.technion.ac.il/en/home-2/), with a specialization in compiler optimizations. His unwavering passion for innovation continues to drive advancements in the field of high-performance computing.

Connect with Mostafa Hagog

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1b26b_Kalor.jpg)

Kalor Lewis

Kalor is Modular's VP, Finance and leads all our Finance operations. Prior to Modular, Kalor was a VP, Finance at [Fivetran](https://fivetran.com/) where he was the first finance hire in 2018 and built out the companies entire finance function. Before Fivetran, Kalor was part of [Palantir Technologies](https://www.palantir.com/), where he scaled their strategic finance function.

Connect with Kalor Lewis

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1b268_Eric.jpg)

Eric Johnson

Product leader who has built and scaled AI applications and infrastructure. Eric led the TensorFlow API, Compiler, and Runtime teams at [Google Brain](https://research.google/teams/brain/) and Core Systems, including the founding of [TFRT](https://blog.tensorflow.org/2022/02/tfrt-progress-update.html) and the productionization of [JAX](https://github.com/google/jax). He holds an MBA from [Wharton](https://www.wharton.upenn.edu/) and Computer Science MS from Penn and loves soccer, fitness, and the great outdoors.

Connect with Eric Johnson

-   [
    
    ](https://twitter.com/theericajohnson)
-   [
    
    ](https://www.linkedin.com/in/ericallenjohnson/)

![](https://cdn.prod.website-files.com/68c9c3107effc2ea46e1a82c/68c9c3107effc2ea46e1b26a_Mike.jpg)

Mike Edwards

Mike has spent over 25 years working in the fields of IT, corporate operations, and software development - most recently at Apple. Mike volunteers his time serving as a Board member with the [LLVM Foundation](https://foundation.llvm.org/), focusing on finance and operations. Mike truly believes in the power of AI to help address some of the world’s greatest needs.

Connect with Mike Edwards

-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)
-   [
    
    ](https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software#)

Return to page

No items found.

