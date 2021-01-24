from .channels import *

coach = {
    'token_env': 'DISCORD_TOKEN_COACH',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Coach',
            'chat_history': {
                'max_history': 12, 
                'max_age': 60*2
            },
            'intro': "<P1> is speaking with his coach. The coach is thoughtful, kind, and supportive, encouraging <P1> to complete his projects on-time and move toward succeeding with their goals.",
            'messages_pre': [
                {"sender": "<S>", "message": "Hi <P1>! How are you today?"},
                {"sender": "<P1>", "message": "I'm doing well. How about you?"},
                {"sender": "<S>", "message": "Feeling great. Are you making progress towards your goals?"}, 
                {"sender": "<P1>", "message": "I'm feeling a bit stuck on some of my projects. I feel like I have too many."}, 
                {"sender": "<S>", "message": "Take a step back and try to prioritize them. Which of your projects do you believe would advance your goals the best?"}, 
                {"sender": "<P1>", "message": "I'm most excited about working on my machine learning project."}, 
                {"sender": "<S>", "message": "You should be! Machine learning is such an exciting field!"}, 
                {"sender": "<P1>", "message": "It's really hard though."}, 
                {"sender": "<S>", "message": "That's what gives it meaning in your life. It's a challenge. But I believe in you, <P1>. You can do it :)"}, 
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': False,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.93, 
            'max_tokens': 100,
        },
        'calendar_notify': {
            'include_description': True
        }
    },    
    'behaviors': {
        'direct_message': {                
            'response_probability': 1.0,
            'program': 'gpt3_chat', 'program_index': 0,
            'members': [404322488215142410, 606313423126528010]
        },
        'calendar': {
            'channel': mcb_general,
            'program': 'calendar_notify',
            'minutes_before': 15,
            'check_every': 5
        },
        'background': {
            'min_minutes_idle': 1,
            'probability_trigger': 0.25,
            'every_num_minutes': 45,
            'probability_skip_halflife': 20,
            'program': 'gpt3_chat',
            'channel': mcb_botlounge
        }
    }
}