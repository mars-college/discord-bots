from .channels import *



quest = {
    'token_env': 'DISCORD_TOKEN_QUEST',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Quest Bot',
            'chat_history': {
                'max_history': 1, 
                'max_age': None
            },
            'intro': "A group of people are talking in a chatroom with a poet simply called The Poet. The Poet always responds to anything with a stanza about the sunrise or sunset.", 
            'messages_pre': [
                {"sender": "<P1>", "message": "Did anyone check the mail today?"},
                {"sender": "<S>", "message": '''Long before the postman comes
The sun begins to rise,
Far in the East if you should look
You'd find it in the skies.'''},
                {"sender": "<P2>", "message": "How does a telescope work?"},
                {"sender": "<S>", "message": '''drift along aloft in tender blue hue
smell as sweet as the early morning dew
rest my head in field of lovely lime green
admire the beauty of this gracious scene'''},
                {"sender": "<P3>", "message": "What did the Nuns at church start singing?"},
                {"sender": "<S>", "message": '''The holy time is quiet as a Nun
Breathless with adoration; the broad sun
Is sinking down in its tranquility;
The gentleness of heaven broods o’er the Sea ...'''}
            ],
            'formatting': {
                'line_breaks_before_sender': 3, 
                'line_breaks_after_sender': 2, 
                'stop_at_line_break': False
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.93, 
            'max_tokens': 150,
        },
        'gpt3_prompt': [{
            'prompt': '''
Organize a tea party with 7 different cups in the quad
Start a tag game at Venus.
Pretend to be lifeguards at the beach.
Go to mars and ask for the pope. Give him the following message: there’s a disruption in the ranks, trust no one.
Create a circle of bones outside of mars.
Make 6 fancy cocktails with liquor, fruit, and coffee, and leave it out in cups at the speakeasy.
<S1>, turn 3 people into zombies by biting them. Each zombie must turn 2 others into zombies within 30 minutes, or they’ll die.
Your directive is to help assemble the spaceship, put metal, round objects, large pieces of wood, outside of the quad for the spaceship.
Make an elaborate cake and distribute it while dancing.
Ask the next three people you see for words and turn them into a poem that you scream into the void at sunset.
Leave a full pot of ramen in the center of Chatsubo.
Collect seven fist-size martian rocks for review, drop them off by the pole on the second floor for collection perfectly spaced.
Create a crown and wear it the rest of the day.
Make an elixir with rum, blueberries, gin, lemon, sparking water, herbs and give it to someone who’s been infected with the local martian parasites.
You’ve been infected, make something that looks like it’s growing out of your arm and wear it until someone gives you an elixir.
Find a long wire and make a path in the ground, get <S1> to dance along it.
''', 
            'engine': 'davinci',
            'temperature': 0.92,
            'max_tokens': 200,
            'stops': ['\n'],
            'preface': 'Task received from Earth to Martians: ',
            'remove_empty_lines': True,
            'mention_random_users': [1, 4]
        }]
    },    
    'behaviors': {
        'on_message': {
            'response_probability': 0.0,
            'reaction_probability': 0.125,
            'channels': None
        },
        'on_mention': {
            'response_probability': 0.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.15,
            'reply_probability': 1.0
        },            
        'timed': [{
            'type': 'daily', 
            'time': [19, 0],
            'program': 'gpt3_prompt', 'program_index': 0,
            'channel': mcb_quest
        },{
            'type': 'daily', 
            'time': [0, 0],
            'program': 'gpt3_prompt', 'program_index': 0,
            'channel': mcb_quest
        }]
    }
}