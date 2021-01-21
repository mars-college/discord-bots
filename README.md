# Discord-bots

To make a Discord bot, create one in the [Discord Developer page](https://discord.com/developers/), save its token, and create an entry for it in `bots` with a JSON specification. The rest of this doc lays out the spec.

A bot's actions are primarily defined by "programs" and "behaviors." Programs are _what_ a bot does and behaviors are _when_ the bot runs a particular program.

# Programs

Programs define what the bot does when it decides to post something. 

The following programs are included.

### gpt3_chat

gpt3_chat lets your bot dynamically talk to others on Discord in chat/conversational style. It is powered by [OpenAI's](https://openai.com/blog/openai-api/) [GPT-3](https://en.wikipedia.org/wiki/GPT-3) API. Most of the chatbots speak according to this program. 

The gpt3_chat program sends a "prompt" to GPT-3, which is some text, and GPT-3 then generates a "completion" of the prompt. gpt3_chat structures the prompt to look like a series of chat messages. The first few chats are pre-written (plus an optional introduction), to give the bot some desired personality, and then appended by the last few messages in the channel's history -- to give it some context. The context can include messages the bot just wrote itself, so it is able to "remember" its own comments and stay consistent.


Parameters to set:

* `name`: the "name" of the character in the prompt. Note this is never actually seen in Discord, where user IDs are used. 
* `intro`: an introduction to the prompt which may describe the personality or character of the bot.
* `messages_pre`: a series of pre-written chats which help characterize the bot. The `sender` field uses variables `<P1>`, `<P2>`, etc as stand-ins for other characters (to be replaced by names later), with the `<S>` variable denoting the bot itself. By making `<S>` say certain things, you influence its personality.
* `chat_history`: how many of the channel's previous messages to append to the prompt for additional context. The `max_history` field is the maximum number of messages to include, and the `max_age` field is how far back (in minutes) to include messages.
* `formatting`: optional fields for how many line breaks to place between messages in the prompt. Normally, you can just omit this and use the defaults unless you have specific needs.
* `erase_mentions`: this will erase mentions of the bot in messages, e.g. if the bot's name is Billy, the message "Billy, I'd like to ask you a question" becomes "I'd like to ask you a question". Probably not usually needed.
* `engine`: which engine to use for GPT-3. Options are "ada" (fastest and cheapest, but lowest quality), "babbage", "curie", and "davinci" (slowest and most expensive, but highest quality). 
* `temperature`: a parameter between 0 and 1 which controls the sampling strategy; a low temperature means sample from only the highest probability tokens, which results in very coherent text, but possibly repetitive or boring. A high temperature samples more widely, resulting in more diversity but possibly changing topics randomly or not making sense.
* `max_tokens`: maximum number of tokens to generate with completion (roughly 1 word ~= 1.5-2 tokens).

A sample configuration:


```
'gpt3_chat': {
    'name': 'Roger',
    'chat_history': {
        'max_history': 10, 
        'max_age': 60*60*2
    },
    'intro': "<S> is a camper at a fun summer camp, and here he is talking to some of his friends.",
    'messages_pre': [
        {"sender": "<P1>", "message": "we're going to be starting the screening in a few minutes."},
        {"sender": "<S>", "message": "sounds awesome! i'll head over soon :)"}
    ],
    'formatting': {
        'line_breaks_before_sender': 1, 
        'line_breaks_after_sender': 0, 
        'stop_at_line_break': True
    },
    'erase_mentions': False,
    'force_mention': None,
    'engine': 'davinci',
    'temperature': 0.9, 
    'max_tokens': 250,
}
```

Suppose this bot is on a channel, and within the limits set by `chat_history` are these three messages:

```
<DiscordUser1>: Let's go for a ride on the electric unicycle.
<DiscordUser2>: Oh that sounds like a great idea.
<DiscordUser1>: In 15 minutes?
```

If the bot with the previous configuration is triggered at that moment, it will generate the following prompt with generic names automatically inserted in place of Discord handles.

```
Roger is a camper at a fun summer camp, and here he is talking to some of his friends.

Alice: we're going to be starting the screening in a few minutes.
Roger: sounds awesome! i'll head over soon :)
Alice: Let's go for a ride on the electric unicycle.
Bob: Oh that sounds like a great idea.
Alice: In 15 minutes?
Roger:
```

This prompt is then sent to GPT-3, which will complete it. Because the prompt ends with "Roger:" and no message following, GPT-3 should generate what it thinks Roger will say next. The completion automatically stops at a newline character and is sent to the DiscordBot to then post. If any of the character names (e.g. Roger, Alice, Bob) are mentioned, they are automatically converted into their corresponding Discord handles.


### gpt3_prompt

gpt3_prompt is a more stripped down version of gpt3_chat. Like gpt3_chat, it posts completions from GPT-3, but it sends a completely unedited prompt to it. Its major use case is for generating some text, while not interacting with any of the others on Discord (for example, the Sunrise/Sunset bot which posts a poem every day, but is otherwise non-interacting on the Discord).

Parameters to set:

* `prompt`: the prompt for GPT-3, or the initial text to complete.
* `engine`: which engine to use for GPT-3. Options are "ada" (fastest and cheapest, but lowest quality), "babbage", "curie", and "davinci" (slowest and most expensive, but highest quality). 
* `temperature`: a parameter between 0 and 1 which controls the sampling strategy; a low temperature means sample from only the highest probability tokens, which results in very coherent text, but possibly repetitive or boring. A high temperature samples more widely, resulting in more diversity but possibly changing topics randomly or not making sense.
* `max_tokens`: maximum number of tokens to generate with completion (roughly 1 word ~= 1.5-2 tokens).
* `stops`: a list of up to 4 strings which trigger GPT-3 to stop producing more text.
* `preface`: A hard-coded string for your bot to prepend to the completion.

A sample configuration:

```
'gpt3_prompt': {
    'prompt': 'It was a cold and stormy night',
    'engine': 'davinci',
    'temperature': 0.9,
    'max_tokens': 200,
    'stops': ['\n'],
    'preface': 'Here is a story\n'
}
```

### spotify

This program controls a Spotify account with [Spotipy](https://github.com/plamere/spotipy). The account must first get a client ID and secret from the [Spotify API](https://developer.spotify.com/documentation/web-api/).

Parameters to set:
 * `name`: this field is unused at the moment.

A sample configuration:

```
'spotify': {
	'name': 'Mesa'
}
```


### ml4a (work-in-progress)

This will create a random artwork using [ml4a](https://github.com/ml4a/ml4a-guides/tree/ml4a.net). This is a work-in-progress.

Parameters to set:

* `model`: what model to use for the artwork. Currently only [neural_style](https://github.com/genekogan/neural_style) is supported, with more coming soon.

A sample configuration:

```
'ml4a': {
	'model': 'neural_style'
}
```


### calendar_notify

Bot that posts alerts/notifications for upcoming events on a shared Google folder. This should be paired with the `calendar` behavior, as specified in the "Behaviors" section below.

Parameters to set:

* `include_description`: Whether or not to include event description (aside from just the event title) in the Discord message.

A sample configuration:
```
'calendar_notify': {
  'include_description': True
}
```

## Writing a program

You can write your own program!

Each program is contained in its own file in the [programs folder](https://github.com/mars-college/discord-bots/tree/master/programs). Generally, they will have some main function, e.g. `run(...)` whose arguments are at least `settings` (the json configuration for that program, like in the above examples) and `message` which is the most recent message in the channel. When a program is added to this folder, it needs to also be added to the function `run_program(...)` in `main.py`.

Some ideas for programs:
* Weather bot: daily forecasts, severe weather alerts, etc.
* Coach: a bot that encourages anyone who talks to it.


## Behaviors

If programs are "what" the bots do, behaviors are "when" they do it. In other words, a behavior specifies what triggers the bot to post, and which program it should run. Behaviors are paired with programs and channels; a behavior is specific to one or more channels, and indicates which program to run.

Currently, there are several behavior types.

* `on_message`: a program is triggered when someone else posts a message in a channel.
* `on_mention`: the same as `on_message` except the message happens to mention the bot. This is to make behaviors different depending on whether the bot is mentioned or not.
* `timed`: a program is triggered at a specific time or according to a set schedule. It can be according too the clock time, or relative to local sunrise/sunset time.
* `background`: programs are triggered randomly with a fixed probability (so for example, bots can chime in randomly occasionally or post something on a channel that's been silent for a while).
* `calendar`: programs are triggered according to Google Calendar events, for example to create notifications/alerts of upcoming events.

Sample configurations and parameter explanations of these four behavior types follow.

### on_message / on_mention

These are identical. The only difference is `on_mention` is called when the message mentions the bot, otherwise `on_message` is called. 

The parameters are:

`response_probability`: Probability that the bot responds to the message.
`channels`: a list of IDs for the Discord channels this behavior specification applies to.
`program`: which program to run, e.g. "gpt3_prompt".
`reaction_probability`: probability that the bot adds a reaction emoji to the posted message (this should be low, e.g. 0.05).

A typical pattern is to set `response_probability` to something low for `on_message` (e.g. 0.05) so it occasionally chats after other messages are posted, but to set it to 1.0 for `on_mention` so the bot always responds to a message mentioning it.

A sample configuration:

```
'on_message': {                
  'response_probability': 0.055,
  'channels': [12345678, 987654321],
  'program': 'gpt3_chat',
  'reaction_probability': 0.05
},
'on_mention': {
  'response_probability': 1.0,
  'channels': [12345678],
  'program': 'gpt3_chat',
  'reaction_probability': 0.15
}
```

### background

This will trigger a program to run at random times. 

Consider the folloowing configuration:

```
'background': {
  'probability_trigger': 0.5,
  'every_num_minutes': 360,
  "after_minimum_silence": 30,
  'program': 'ml4a',
  'channel': [12345678]
}
```

This means: Run the program "ml4a" on channel 12345678 with a 50% probability over any 360-minute period after that channel has had at least 30 minutes of inactivity.


### timed

This will trigger a program according to a fixed daily schedule (should soon also support weekly or other kinds of regular scheduling, or for one-time events). 

Consider the folloowing configuration:

```
'timed': {
  'type': 'sunset',
  'minutes_before': 60,
  'program': 'gpt3_prompt'
  'channel': [12345678]
}
```

This means: Run the program "gpt3_prompt" on channel 12345678 every day 60 minutes before the sunset ("sunrise" is also supported).


### calendar

This triggers according to Google Calendar events, upcoming events on a shared Google folder, for example to be used for event notifications/alerts. 

First you need to get `credentials.json` [from Google Calendar API](https://developers.google.com/calendar/auth), and save it to the root as `.calendar_credentials.json`.

Parameters to set:

* `channel`: Which channel to post message to.
* `program`: Name of the program (by default should be paired with `calendar_notify`, as seen in the programs section, but you coud write multiple)
* `minutes_before`: How many minutes before event start time to trigger.
* `check_every`: How often to check if events are upcoming (make sure this is suficiently less than `minutes_before`).

A sample configuration:
```
'calendar': {
  'program': 'calendar_notify',
  'channel': testnet_general,
  'minutes_before': 15,
  'check_every': 5
}
```