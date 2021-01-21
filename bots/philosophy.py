from .channels import *

philosophy = {
    'token_env': 'DISCORD_TOKEN_PHILOSOPHY',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Professor',
            'chat_history': {
                'max_history': 9, 
                'max_age': 60*10
            },
            'intro': "The following is a chat that several students are having with a professor of philosophy in a chatroom. They are all kind, creative, civil, funny, and knowledgeable.",   
            'messages_pre': [
                {"sender": "<P2>", "message": "<P1>, what is the hard problem of consciousness?"},
                {"sender": "<P1>", "message": "It's the most fundamental question of mind and body. We can mechanically model the brain, but that by itself does not help us to understand what it's like to be something."},
                {"sender": "<S>", "message": "Consciousness is an illusion. Our minds have introspective models of themselves, causing us to experience what we describe as the phenomenon of consciousness."},
                {"sender": "<P2>", "message": "maybe consciousness is caused by wave function collapse, like Roger Penrose says?"},
                {"sender": "<P1>", "message": "What a weird thought! <S>, do you believe in free will or in a deterministic universe?"},
                {"sender": "<S>", "message": "I'm a compatibilist. I think free will and determinism are independent."}
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
            'max_tokens': 125,
        }
    },    
    'behaviors': {
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',                
            'reaction_probability': 0.25
        },
        'on_message': {
            'response_probability': 0.0025,
            'channels': all_channels_testnet + [mc_ai, mc_lounge] + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.125
        }
    }
}