

[![a3545c3562712af1-e4a7e37bbc032a73](https://d24ovhgu8s7341.cloudfront.net/uploads/publication/logo/97/ai_and_i_cover_1.png)AI & I](https://every.to/podcast)

# Transcript: ‘How Anthropic Uses Claude Fable 5 With Mike Krieger’

‘AI & I’ with Mike Krieger

[![6fd98b0a90128f4a-3047de73d5495145](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/2743/EVENT.to_SJH_FINALS_-15.jpg)Dan Shipper](https://every.to/@danshipper)

Jun 10, 2026

Listen

**The transcript of *<u>[AI & I](https://every.to/podcast)</u>* with Mike Krieger is below. Watch on [X](https://x.com/danshipper/status/2064761654789681281) or** **<u>[YouTube](https://www.youtube.com/watch?v=XWpTgCvgYaE)</u>, or listen on [Spotify](https://open.spotify.com/show/5qX1nRTaFsfWdmdj5JWO1G) or [Apple Podcasts](https://podcasts.apple.com/us/podcast/how-anthropic-uses-claude-fable-5-with-mike-krieger/id1719789201?i=1000772067637).**

#### Timestamps

1. Introduction: 00:00:03

2. How Fable completely reshaped Mike’s workflow: 00:01:48

3. When to use Sonnet versus Fable: 00:04:48

4. What the media tracker Mike built over a weekend reveals about agent-native architecture: 00:10:06

5. The cost to build has collapsed: 00:15:00

6. Is software engineering over?: 00:19:03

7. How Anthropic’s engineering teams work today: 00:21:48

8. The mechanics of verification: 00:38:39

9. Dynamic workflows: 00:47:24

10. What people should use the model to build: 00:44:39

#### Transcript

**Dan Shipper**

Mike, welcome to the show.

**Mike Krieger**

Great to be here, Dan. Good to see you.

**Dan Shipper**

For people who don’t know you, you’re the head of Anthropic Labs and the co-founder of Instagram. What I want to talk about today is Fable 5. It’s dropping tomorrow—we’re recording this the day before, and this will come out after it drops. I really wanted to bring you on the show to tell me what it’s like to use this model beyond the first day. When a model this powerful drops, it’s so useful to have someone who’s using it day in and day out tell you, “This is where it’s powerful. This is what it actually changes. This is what it doesn’t change”—so you can think clearly about how it fits into your life.

**Mike Krieger**

Absolutely. It’s also just been interesting—we’ve had some models in this Mythos class leading up to the Fable release for a couple of months now. I think it’s very exciting to see how people will build with this externally. But you’re right that day-one impressions really come from getting to use it over a couple of weeks.

We’ve seen that even with previous models. The December-into-January usage with Opus 4.5 or 4.6 was really important because people spent extended time with the model and figured out, “I wasn’t pushing it hard enough. I need to go further and rethink what’s even possible with this generation.”

**Dan Shipper**

Totally. There are people internally at Every who have been using it and said, “I think I need a whole new set of skills to use this model.” You can especially see it with people who are more non-technical and on the knowledge-work side—they’re like, “I don’t even know what I would use this for.” And the people who are orchestrating agents are like, “There are so many new things I need to learn.” So tell me about the difference between your impression when you first tried it and now.

**Mike Krieger**

Your point about adopting new workflows is a really good one—and I mean that quite literally, in terms of actual workflows, but also just how I think about usage. At first, the timing was interesting because it coincided with me transitioning from CPO into Labs and going back into builder mode. It was about a month and a half or two months into that when we first had one of these models available internally. I sat there and thought, “I feel like a total newbie again,” because the way I was prompting—or even thinking about decomposing a task—was really out of date with this model.

The time horizon and the interactivity model have to evolve. Early on I’d be like, “I have an idea for this feature. Can we start by doing—” absolutely not. It evolved to: let me express more of the intent, and then just go. I remember in March and April being amazed that on the one shot it was already incredibly impressive, but it also understood the intent around how we’d evolve things and the global context as well.

That evolution has continued. I was talking to somebody this morning, and I think about doing work—I had a flight, and I was like, “I can do most of this work remotely.” I don’t even worry about the Wi-Fi dropping out because if I set up the right context instructions—like a loop command—it’ll see things through.

My last two months have been full of moments where I’ll wish Claude a good night, set it off on a complex task, and wake up to find it’s done—usually by around 2 a.m., and it just fiddles with loose ends for the next four hours. What’s really impressive is its ability to complete the swing: “Mike asked me to do this complex task overnight. I got stuck because this remote service went down. I’ll write a scaffolded backend for now, document that, go all the way through, keep track of that fact, and fix it when it comes back online.” The most impressive thing for me is just being able to delegate that kind of task and trust that the right thing will happen by the end.

Of course you review the result—there’s still a whole verification thing we should talk about, because that’s an important part of completing the swing. But it’s really forced me to rethink what being productive with one of these models looks like. We’ve talked for a while about what it’s like when these models are more of a companion or coworker. It really feels now like a teammate I can delegate a lot of work to.

**Dan Shipper**

What is your day-to-day flow like right now? One thing I notice is that if you give it a big task and monologue into it and let it go for a few hours or overnight, it’s the most impressive model I’ve ever tried. But it’s so slow and expensive that I feel like I don’t want to use it for day-to-day tasks. What is your actual flow in terms of how you use it day to day, and where does it slot in versus other models?

**Mike Krieger**

I’ve ended up having a lot more architectural planning conversations up front with it. That’s been another interesting change. It’s an area where all models still need to continue to improve, and I’m really grateful for the Instagram experience—having to start from our initial version duct-taped on a server in LA, to scaling it and eventually integrating it with all of the Facebook infrastructure—because you develop a sense of what infra abstractions and complexity are appropriate for each stage.

I still go back and forth with Fable sometimes. It’ll come up with what looks like a good implementation, and I’ll say, “I do plan on shipping this fairly soon—we should probably think about more than one server.” That back and forth is important. But for architectural planning, I’ll often ask it to just make an HTML page that represents what we talked about so I can share it with the team. Even just a markdown document works, but I like having diagrams.

So that’s been an interesting use pattern: let’s plan with it, think it through, and then have some document we can align the team on. You can build a lot very quickly now, and forcing more of that early alignment—even if you do an initial prototype and then back it out into a more planned architecture—is really key. It ends up being the place where human-to-human interaction still stays very much part of the process.

From there, whether overnight or during the day, having it execute on chunks of tasks means having a lot more concurrent sessions than before. I go back and forth between liking a single long-running Claude Code session where I ask it to do everything in background forked sub-agents so the main thread stays responsive, and other times just embracing having five or six tabs tackling long comprehensive work.

There’s something to this long-horizon, “don’t worry, I’m on it, it’ll take me a while” modality. We’ll have to figure out how to support that in our products too—you want to preserve both modes, and they interact with each other in interesting ways. My preference is usually to have at least one Claude that’s high-context but also very fast to respond, with the instinct of, “I’ll answer you and kick something off if I need to, otherwise I’ll hang tight.”

You’re right that for fine-grained interaction questions, Fable will go off and think very hard. Fable is actually the first model where I’ve played more with the effort levels, where I’ve thought, “I just need to tweak some UI—I’ll put it to medium and see how that plays out.” I didn’t find myself doing that as much with Opus, maybe because the range felt less wide. With Fable it can feel quite wide.

**Dan Shipper**

What about a quick question? You’re on the go—are you asking Fable random questions as they come to you? It feels like using a rocket launcher to kill a mosquito, or are you flipping back and forth?

**Mike Krieger**

It’s funny you ask that. I had been using Fable for everything, and you’re right—you’d watch it thinking, thinking really hard. Then this last week I was asking it something I actually felt embarrassed about. It was something NBA Finals related, and I switched my iOS app to Sonnet. “Oh yeah, I used to use this all the time for fast questions.” It’s order-of-magnitude different in feel, and it’s not even really about tokens per second—it’s about how much thinking goes into the answer. Sometimes the answer does not need to be fully thought through.

This is a good product question for us too. In general, you don’t want people to have to think so much about these choices. Ideally what we can coalesce around longer term is some more bucketable use cases that are really grokable. Or it varies by surface—it’s actually probably unlikely that most of the time on the iOS app I’m doing Fable-type tasks. Having a sticky model selection per surface might be the way to do that. We’ll have to explore what that means from a product perspective. But I’ve definitely had the feeling of, “This is not a Fable-worthy question. I should ask Sonnet this.”

**(00:10:00)**

**Dan Shipper**

Can you show us something you’ve built with it?

**Mike Krieger**

One of the things we did this go-around was encourage personal account usage, especially on the weekends. It was really fun because we have a lot of Anthropic-specific tooling, so it was good to step back and say, “I’m just going to use pure Claude Code and work on something over the weekend.”

**Dan Shipper**

Are you in the terminal app or the desktop app?

**Mike Krieger**

That’s a great question. I’m mostly still in the terminal app. It’s been interesting watching my wife—not a professional engineer, more of a UX designer/PM—really fall in love with Claude Code via the desktop app. I think it’s simplified some of the abstractions for her. But for this one I was still in Ghostty and the terminal app.

Everybody has some bespoke need. I wanted a good media tracker experience—I’m playing games, watching TV shows, getting all these recommendations, and I wanted to build something personal that fit my use cases. My two biggest criteria were: one, really easy to add things, where you can just talk to Claude and it does agentic search over everything and puts the right things in. And two, proactively surfacing things, like when there’s a new season or a sequel to a game it could go research.

Most of the UI was Fable one-shot, which was already impressive. But the thread I’ve been pulling on a lot in Labs this year is: how do you bring the software team—which is Claude these days—closer to the software itself?

This was a Saturday morning with a full weekend of kid stuff, so a lot of it was kick-off work: go for a hike with the kids, come back, continue. Sometimes check in on the work during the hike—I probably shouldn’t, but it was nice to pop into remote mode and see what was going on.

The idea I had was: could we do a spike on what if you could actually modify the software from within itself? I built both a React Native version and this web version. I already had a chat-type thing where you could ask Claude to add things by URL. I want every piece of software to have this—I should never have to navigate a menu to do anything again.

In many ways, Dan, I was trying to distill agent-native architecture to its fullest degree, which is: also have the agent be able to modify the app. Phase one of agent-native architecture is that every single thing in the product is accessible from the agent and has tool calls. That’s hopefully becoming table stakes, although sadly not in a lot of software. I had a great example—somebody had recommended a Brazilian show about radioactive stuff in Goiânia. I couldn’t remember the name, and Claude was able to figure it out. So much better than me trying to figure it out intuitively.

But the next step I was interested in was: what would it mean to actually modify the software from itself on the go? If you long-press the little chat button, what I built—or really what Claude built—was a way to use our managed agents to take on edit requests, and then you can preview them. I used the Vercel live-preview thing. This whole feature was also one-shot, which was really cool, and I just added to it over time. It does a little diff view if you want, and you can go into the managed-agent conversation and see what it did—though I almost never do, because I genuinely don’t care about the long-term maintainability of this personal project.

It’s been really fun. I’ll be using it on the go and say, “The floating action button was too low on native iOS.” It went off and fixed it. And with some of the Expo tooling now it actually live-reloaded on my phone, which was a really cool feeling. Does this thing need to be a production-level thing going to a million users? No. But it felt good to have something where it didn’t have to stop at just the weekend—I could keep working on it just by using it, with this kind of end-to-end closed loop. This was a good manifestation of both Fable’s building ability and a lot of what both of us have been thinking about: how does Claude embed itself into software beyond just the usage side?

**Dan Shipper**

This is really cool. I want people to understand—you could have built something like this, maybe not the self-modifying part, but something like this, 10 or 20 years ago. But the cost to build has gotten dramatically lower. Think about how much it would have cost to do this in the Instagram days versus now. Can you help us understand how that has changed?

**Mike Krieger**

I think about this a lot when I look back at that time. I thought of myself as a very productive programmer in the early Instagram days—really into mobile development, good clarity on things. The gap from idea to fully realized product was still looking at roughly four or five days of all-nighters, which was just my natural state. Up until 4 a.m., sleep until noon—not conducive to family life, but that was my building mode.

**(00:20:00)**

Instagram V1, which probably had more features than what I built this weekend but not by an order of magnitude, was about five days of all-nighters—me on the front end and back end, Kevin working on the initial filters. And this was built on many years of iOS experience. The iteration was also gated: after the launch went well, we had all these ideas but were just trying to keep the site up or add the one incremental feature. Hashtags take a week to build, and then there are all the things you want to keep doing on top of that.

So it’s both that shortening of time—there’s still the time required for the idea, the concept, the iteration—and the other piece, which is how you can then iterate on what you have in a really fun, in-the-flow kind of way. And then beyond what I could do as a professional software engineer and startup founder: if you had that idea but couldn’t build it yourself, the options used to be find a consultancy, which is a really lossy process,