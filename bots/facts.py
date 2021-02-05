from .channels import *

facts = {
    'token_env': 'DISCORD_TOKEN_FACTS',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Answer',
            'characters': ['Question'],
            'chat_history': {
                'max_history': 3, 
                'max_age': None
            },
            'intro': "I am a highly intelligent question answering bot. Ask me about anything.", 
            'messages_pre': [
                {"sender": "<P1>", "message": "What is human life expectancy in the United States?"},
                {"sender": "<S>", "message": "78 years."},
                {"sender": "<P1>", "message": "Who was president of the United States in 1955?"},
                {"sender": "<S>", "message": "Dwight D. Eisenhower."},
                {"sender": "<P1>", "message": "How does a telescope work?"},
                {"sender": "<S>", "message": "Telescopes use lenses or mirrors to focus light and make objects appear closer."},
                {"sender": "<P1>", "message": "Where were the 1992 Olympics held?"},
                {"sender": "<S>", "message": "Barcelona, Spain."}
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.45, 
            'max_tokens': 250,
        }
    },    
    'behaviors': {
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.15,
            'reply_probability': 1.0
        },
        'on_message': {
            'response_probability': 0.0,
            'channels': None,
            'program': 'gpt3_chat',
            'reaction_probability': 0.035
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