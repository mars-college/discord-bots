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
                {"sender": "<P1>", "message": "<P2>, the hard problem of consciousness is about the nature of mind."},
                {"sender": "<P2>", "message": "<P1>, do you think that phenomenological consciousness is an introspective illusion? like a trick the mind plays on itself."},
                {"sender": "<P1>", "message": "<P2>, do you believe in free will or in a deterministic universe?"},
                {"sender": "<P2>", "message": "<P1>, maybe consciousness is what causes the wave function to collapse."},
                {"sender": "<S>", "message": "<P2>, I'm a compatibilist. I think free will and determinism are independent."}
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
            'channels': all_channels_testnet + all_channels_mc,
            'program': 'gpt3_chat',                
            'reaction_probability': 0.25
        },
        'on_message': {
            'response_probability': 0.025,
            'channels': all_channels_testnet + [mc_ai, mc_lounge],
            'program': 'gpt3_chat',
            'reaction_probability': 0.125
        }
    }
}