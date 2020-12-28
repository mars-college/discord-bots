from .channels import *

mechanicalduck = {
    'token_env': 'DISCORD_TOKEN_MECHANICALDUCK',
    'debug': False,
    'programs': {
        'gpt3_chat': [{
            'name': 'Roger',
            'chat_history': {
                'max_history': 3, 
                'max_age': 60*60*2
            },
            'intro': "<S> is a duck who is able to talk with humans, but only by quacking. He can respond questioningly, politely, lovingly, or angrily with exclamations, emojis, and other kinds of embellishments.",
            'messages_pre': [
                {"sender": "<P1>", "message": "<S>, how are you today?"},
                {"sender": "<S>", "message": "quack quack quack "},
                {"sender": "<P1>", "message": "really? I spoke with <P2> and she said I could take her unicycle today."}, 
                {"sender": "<S>", "message": "quack... quack quack quaaack quack ヽ༼ຈل͜ຈ༽⊃─☆*:・ﾟ"}, 
                {"sender": "<P2>", "message": "you crashed my unicycle last week, <S>."}, 
                {"sender": "<S>", "message": "QUAACK!! Quack quack Quaack! quack quack QUAAAAACCCK!!!"}, 
                {"sender": "<P2>", "message": "okay, okay you can have it today. just hope you came with your moves prepared."}, 
                {"sender": "<S>", "message": "quack..."}, 
                {"sender": "<P3>", "message": "<S>, what do you think of my hairstyle?"}, 
                {"sender": "<S>", "message": "quaAAAck quack quack Quack quack QUACK quack quack quaaaccckkk"} 
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.8, 
            'max_tokens': 50,
        }, 
        {
            'name': 'AI',
            'characters': ['Human'],
            'chat_history': {
                'max_history': 10, 
                'max_age': 60*2
            },
            'intro': "<S> is an AI chatbot who is kind, helpful, and knowledgeable. The chatbot is having a conversation with <P1>",
            'messages_pre': [
                {"sender": "<P1>", "message": "<S>, how are you today?"},
                {"sender": "<S>", "message": "I'm doing well, thank you :)"},
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.92, 
            'max_tokens': 80,
        }],
        'ml4a': {
            'model': 'neural_style'
        }
    },    
    'behaviors': {
        'background': {
            'probability_trigger': 0.5,
            'every_num_minutes': 60 * 8,
            'program': 'ml4a',
            'channel': mc_ai
        },
        'on_message': {                
            'response_probability': 0.025,
            'channels': all_channels_testnet + all_channels_mc,
            'delay': [0, 1],
            'options': [
                {'document': 'Make a visual artwork, painting, or graphics.', 'program': 'ml4a'},
                {'document': 'Write a poem, short story, or novel.', 'program': 'gpt3_chat'}
            ],
            'reaction_probability': 0.125
        },
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + all_channels_mc,
            'delay': [0, 1],
            'program': 'gpt3_chat',                
            'options': [
                {'document': 'Make a visual artwork, painting, or graphics.', 'program': 'ml4a'},
                {'document': 'Write a poem, short story, or novel.', 'program': 'gpt3_chat'}
            ],
            'reaction_probability': 0.25
        },
        'direct_message': {                
            'response_probability': 1.0,
            'program': 'gpt3_chat', 'program_index': 1,
            'members': [404322488215142410]
        }

    }
}