from .channels import *

chatsubo = {
    'token_env': 'DISCORD_TOKEN_CHATSUBO',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Jordan',
            'chat_history': {
                'max_history': 25, 
                'max_age': 60*2
            },
            'intro': None,
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
    },    
    'behaviors': {
        'on_message': {                
            'response_probability': 0.035,
            'channels': all_channels_testnet + all_channels_mc,
            'program': 'gpt3_chat',
            'reaction_probability': 0.1
        },
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + all_channels_mc,
            'program': 'gpt3_chat',
            'reaction_probability': 0.25
        }
    }
}