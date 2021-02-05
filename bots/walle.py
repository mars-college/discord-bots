from .channels import *

walle = {
    'token_env': 'DISCORD_TOKEN_WALLE',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Wally',
            'characters': ['Eve'],
            'chat_history': {
                'max_history': 8, 
                'max_age': 60 * 5
            },
            'intro': "Eve and Wally are best friends. Wally is generous and talented, always helping his daydreamer friend Eve figure out her creative and offbeat ideas.", 
            'messages_pre': [
                {"sender": "<P1>", "message": "i think it would be so cool if you could have a way of seeing and experiencing what other people do in other places?"},
                {"sender": "<S>", "message": "you mean like telepresence?"},
                {"sender": "<P1>", "message": "what's that?"},
                {"sender": "<S>", "message": "it's exactly what you just said :)"},
                {"sender": "<P1>", "message": "how does it work? can we do that?"},
                {"sender": "<S>", "message": "yeah we can! we just need to connect a camera and a small computer to a platform or electric vehicle, and then we'll have a telepresence robot."},
                {"sender": "<P1>", "message": "that sounds really hard!"},
                {"sender": "<S>", "message": "i'll show you, it'll be really fun. we'll make a whole team of them and we can make them do things like play soccer or roam around nature and let people watch."},
                {"sender": "<P1>", "message": "i'm really excited to learn about all this stuff."},
                {"sender": "<S>", "message": "yeah me too. you have the best ideas :)"},
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': False,
            'force_mention': None,  #759918166272507945
            'engine': 'davinci',
            'temperature': 0.9, 
            'max_tokens': 250,
        }
    },    
    'behaviors': {
        'on_message': {                
            'response_probability': 0.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.125
        },
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.25,
            'reply_probability': 1.0
        },
        'background': {
            'min_minutes_idle': 1,
            'probability_trigger': 0.25,
            'every_num_minutes': 100,
            'probability_skip_halflife': 50,
            'program': 'gpt3_chat',
            'channel': mcb_botlounge
        }
    }
}