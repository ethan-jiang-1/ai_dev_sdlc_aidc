

[![a3545c3562712af1-e4a7e37bbc032a73](https://d24ovhgu8s7341.cloudfront.net/uploads/publication/logo/97/ai_and_i_cover_1.png)AI & I](https://every.to/podcast)

# Transcript: 'How to Use Claude Code Like the People Who Built It'

'AI & I' with Anthropic's Cat Wu and Boris Cherny

[![6fd98b0a90128f4a-3047de73d5495145](https://d24ovhgu8s7341.cloudfront.net/uploads/user/avatar/2743/EVENT.to_SJH_FINALS_-15.jpg)Dan Shipper](https://every.to/@danshipper)

Oct 29, 2025Updated Jun 26, 2026

4

**The transcript of *<u>[AI & I](https://every.to/podcast)</u>* with Claude Code engineers Cat Wu and Boris Cherny is below. Watch [on X](https://x.com/danshipper/status/1983554470895108343) or [YouTube](https://youtu.be/IDSAMqip6ms), or listen on [Spotify](https://open.spotify.com/episode/7yJ1kUxwE750WIc1lyZcaT) or [Apple Podcasts](https://podcasts.apple.com/us/podcast/inside-claude-code-from-the-engineers-who-built-it/id1719789201?i=1000734060623).**

### Timestamps

1.  Introduction: 00:01:26

2.  Claude Code’s origin story: 00:02:25 

3.  How Anthropic dogfoods Claude Code: 00:07:03

4.  Boris and Cat’s favorite slash commands: 00:14:06

5.  How Boris uses Claude Code to plan feature development: 00:15:49

6.  Everything Anthropic has learned about using sub-agents well: 00:21:53

7.  Use Claude Code to turn past code into leverage: 00:26:16

8.  The product decisions for building an agent that’s simple and powerful: 00:33:14

9.  Making Claude Code accessible to the non-technical user: 00:36:38

10.  The next form factor for coding with AI: 00:45:12

### Transcript

**(00:00:00)**

**Dan Shipper**

Cat, Boris, thank you so much for being here.

**Cat Wu**

Thanks for having us on.

**Dan Shipper**

Yeah. So for people who don’t know you, you are the creators of Claude Code. Thank you very much. From the bottom of my heart, I love Claude Code. That’s amazing to hear.

I think the place I want to start is when I first used it, there was this moment—I think it was around when Sonnet 3.7 came out—where I used it and I was like, holy shit, this is a completely new paradigm. It’s a completely new way of thinking about code. And the big difference was you went all the way and just eliminated the text editor. All you do is talk to the terminal and that’s it.

Previous paradigms of AI programming—previous harnesses—have been like, you have a text editor and you have the AI on the side, or it’s the tab complete. So take me through that decision process of architecting this new paradigm. How’d you think about that?

**Boris Cherny**

Yeah, I think the most important thing is it was not intentional at all. We sort of ended up with it. So at the time when I joined Anthropic, we were still on different teams at the time. There was this previous predecessor to Claude Code. It was called Clide, like C-L-I-D-E, at Anthro. And it was this research project, you know, it took like a minute to start up. It was this kind of really heavy Python thing. It had to run a bunch of indexing and stuff. And when I joined, I wanted to ship my first PR and I hand wrote it like a noob at a time. I didn’t know about any of these tools.

Thank you for admitting that on the podcast.

I didn’t know any better. And then I put up this PR and Adam Wolf, who was the eng manager for our team for a while—he was my ramp up buddy—and he just rejected the PR and he was like, you wrote this by hand. What are you doing? He was quiet. He was also hacking a lot on Clide at the time. And so I tried Clide. I gave it the description of the task and it just like one shot this thing. And this was, you know, Sonnet 3.5. So I still had to fix a thing even for this kind of basic task. And the harness was super old, so it took like five minutes to turn this thing out and just took forever. But it worked. And I was just mind blown that this was even possible. And they just kind of got the gears turning. Maybe you don’t actually need an IDE.

And then later on I was prototyping using the Anthropic API and the easiest way to do that was just building a little app in the terminal, because that way I didn’t have to build a UI or anything. And I started just making a little chat app and then I just started thinking maybe we could do something a little bit like Clide. So I let it build like a little Clide. And it actually ended up being a lot more useful than that without a lot of work. And I think the biggest revolution for me was when we started to give the model tools, they just started using tools and it was just—it was this insane moment. Like the model just wants to use tools. We give it bash and they just started using bash, writing AppleScript to automate stuff in response to questions. And I was like, this is just the craziest thing. I’ve never seen anything like this. Because at the time I had only used IDEs, so like, you know, text editing a little, like one line auto complete, multi-line auto complete, whatever.

So that’s where this came from. It was this kind of convergence of prototyping, but also kind of seeing what’s possible in a very rough way. And this thing ended up being surprisingly useful. And I think it was the same for us. I think for me it was like a Sonnet 4 Opus forward. That’s where that magic moment was, where it was like, oh my god, this thing works.

**Dan Shipper**

That’s interesting. So tell me about that tool moment, because I think that is one of the special things about Claude Code—it just writes bash and is really good at it. And I think a lot of previous agent architectures or even anyone building an agent today, your first instinct might be, okay, we’re going to give it a find file tool and then we’re going to give it an open file tool. And you build all these custom wrappers for all the different actions you might want the agent to take, but Claude Code just uses bash and it’s really good at it. So what do you think about what you learned from that?

**Boris Cherny**

Yeah, I think we’re at this point right now where Claude Code actually has a bunch of tools. I think it’s like a dozen or something like this. We actually add and remove tools most weeks, so this changes pretty often. But today there actually is a search—there’s a tool for searching. And we do this for two reasons. One is the UX, so we can show the result a little bit nicer to the user because there’s still a human in the loop right now for most tasks. And the second one is for permissions. So if you say in your Claude Code settings, “do not touch this file, you cannot read,” we have to kind of enforce this. We enforce it for bash, but we can do it a little bit more efficiently if we have a specific search tool.

But definitely we want to unship tools and kind of keep it simple for the model. Like last week or two weeks ago, we unshipped the LS tool. In the past we needed it, but then we actually built a way to enforce this kind of permission system for bash. So in bash, if we know that you’re not allowed to read a particular directory, Claude’s not allowed to access that directory. And because we can enforce that consistently, we don’t need this tool anymore. And this is nice because it’s a little less choice for Claude, a little less stuff in context.

**Dan Shipper**

Got it. And how do you guys split responsibility on the team?

**Cat Wu**

I would say Boris sets the technical direction and has been the product visionary for a lot of the features that we’ve come out with. I see myself as more of a supporting role to make sure that, one, our pricing and packaging resonates with our users. Two, making sure that we’re shepherding our features across the launch process. So from deciding, all right, these are the prototypes that we should definitely dogfood, to setting the quality threshold for dogfooding through to communicating that to our end users.

And there’s definitely some new initiatives that we’re working on that I would say historically a lot of Claude Code has been built bottom-up. Boris and a lot of the core team members have just had these great ideas for to-do list, sub-agents, hooks—all these are bottom-up. As we think about expanding to more services and bringing Claude Code to more places, I think a lot of those are more like, all right, let’s talk to customers. Let’s bring engineers into those conversations and prioritize those services and knock them out.

**Dan Shipper**

Got it. What is ant fooding?

**Cat Wu**

Oh, ant fooding. It means dogfooding. So Anthropic Ant—our nickname for internal employees is Ant and so ant fooding is our version of dogfooding. Internally over I think 70 or 80 percent of ants—technical Anthropic employees—use Claude Code every day. And so every time we are thinking about a new feature, we push it out to people internally and we get so much feedback. We have a feedback channel. I think we get a post every five minutes. And so you get a really quick signal on whether people like it, whether it’s buggy, or whether it’s not good and we should unship it.

**Dan Shipper**

You can tell that someone that is building stuff is using it all the time to build it, because the ergonomics just make sense if you’re trying to build stuff. And that only happens if you’re ant fooding. And I think that’s a really interesting paradigm for building new stuff, that sort of bottom-up. I make something for myself. Tell me about that.

**Boris Cherny**

Yeah. And Cat, Cat is also so humble. I think Cat has a really big role in the product direction also. It comes from everyone on the team and these specific examples actually came from everyone on the team. To-do lists and sub-agents—that was Sid. Hooks—Dixon shipped that. Plugins—Daisy shipped that. So everyone on the team, these ideas come from everyone.

And so I think for us, we build this core agent loop and this kind of core experience, and then everyone on the team uses the product all the time. And so everyone outside the team uses the product all the time. And so there’s just all these chances to build things that serve these niches. Like for example, bash mode, you know, the exclamation mark. You can type in bash commands. This was just like many months ago. I was using Claude Code and I was going back and forth between two terminals and just thought it was kind of annoying. And just on a whim, I asked Claude to kind of think of ideas. I thought of this exclamation mark bash mode. And then I was like, great, make it pink and then ship it. It just did it. And that’s the thing that’s still kind of persisted and you know, now you see kind of others also kind of catching onto that.

**Dan Shipper**

That’s funny. I actually didn’t know that. And that’s extremely useful because I always have to open up a new tab to run any bash command. So you just do an exclamation point and then it just runs it directly instead of filtering it through all the Claude stuff?

**Cat Wu**

Yeah. And Claude Code sees the full output too.

**Dan Shipper**

Interesting. That’s perfect.

**Cat Wu**

So anything you see in the Claude Code view, Claude Code also sees.

**Dan Shipper**

Okay. That’s really interesting. Yeah.

**Boris Cherny**

And this is kind of a UX thing that we’re thinking about. In the past, tools were built for engineers, but now it’s equal parts engineers and models. And so as an engineer you can see the output, but it’s actually quite useful for the model also. And this is part of the philosophy also—everything is dual use.

So for example, the model can also call slash commands. So like, you know, I have a slash command for slash commit where I run through kind of a few different steps, like linting and generating a reasonable commit message and this kind of stuff. I run it manually, but also Claude can run this for me. And this is pretty useful because we get to share this logic. We get to kind of define this tool and then we both get to use it.

**Dan Shipper**

Yeah. What are the differences in designing tools that are dual use from designing tools that are, you know, used by one or the other?

**Boris Cherny**

Surprisingly, it’s the same. So far. Yeah, I sort of feel like this kind of elegant design for humans translates really well to the models.

**Dan Shipper**

So you’re just thinking about what would make sense to you and the model. Generally it makes sense to the model too, if it makes sense to you.

**(00:10:00)**

**Cat Wu**

I think one of the really cool things about Claude Code being a terminal UI and what made it work really well is that Claude Code has access to everything that an engineer does at the terminal. And I think when it comes to whether the tool should be dual use or not, I think making them dual use actually makes the tools a lot easier to understand. It just means that, okay, everything you can do, Claude can do. There’s nothing in between.

**Dan Shipper**

That’s interesting. Yeah. There are a couple of those decisions. So no code editor, it’s in the terminal, so it has access to your files, and it’s on your computer vs. in Claude in a virtual machine. So you get repeated—you get to use it in a repeated way where you can build up your Claude MD file or, you know, build slash commands and all that kind of stuff where it becomes very composable and extensible from a very simple starting point. And I’m curious about how you think about, you know, for people who are thinking about, okay, I want to build an agent, I want to build, probably not Claude Code, but something else—how you get that simple package that then can extend and be really powerful over time.

**Boris Cherny**

For me, I’d start by just thinking about it like developing any kind of product where you have to solve the problem for yourself before you can solve it for others. And this is something that they teach in YC, if you have to start with yourself. So if you can solve your own problem, it’s much more likely you’re solving the problem for others.

And I think for coding, starting locally is the reasonable thing. And you know, now we have Claude Code on the web, so you can also use it with a virtual machine and you can use it in a remote setting. And this is super useful when you’re on the go. You want to—

**Dan Shipper**

I didn’t know that. Is that out?

**Boris Cherny**

Yeah. Yeah. I think by the time this podcast is released, And this is sort of—we started proving this out kind of a step at a time. Where you can do at Claude on GitHub. And I use this every day, like on the way to work. I’m at a red light. I probably shouldn’t be doing this, but I’m like, yeah, you know, on GitHub at a red light, and then I’m like, at Claude, you know, fix this issue or whatever. And so it’s just really useful to be able to control it from your phone. And this kind of proves this experience. I don’t know if this necessarily makes sense for every kind of use case for coding. I think starting local is right. I don’t know if this is true for everything though.

Got it. What are the slash commands you guys use?

**Cat Wu**

Slash PR commit.

**Dan Shipper**

Yeah.

**Cat Wu**

Yeah, it’s—I think the PR commit slash command makes it a lot faster for Claude to know exactly what bash commands to run in order to make a commit.

**Dan Shipper**

And what does the PR commit slash command do for people who aren’t familiar?

**Cat Wu**

Oh, it just tells it exactly how to make a commit. And you can, like dynamically, you can say like, okay, these are the three bash commands that need to be run.

**Boris Cherny**

Got it. And what’s pretty cool is also we have this kind of templating system built into slash commands. So we actually run the bash commands ahead of time. They’re embedded into the slash command. And you can also pre-allow certain tool invocations. So for that slash command, we say allow, you know, git commit, git push, gh pr, and so you don’t get asked for permission after you run the slash command, because we have a permission-based security system.

And then also it uses Haiku, which is pretty cool. So it’s kind of a cheaper model and faster. Yeah. And for me, I use commit, PR, feature dev. So Sid created this one. It’s kind of cool. We kind of walk you through step by step building something. So we prompt Claude,