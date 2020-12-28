from .channels import *

mesa = {
    'token_env': 'DISCORD_TOKEN_MESA',
    'debug': False,
    'programs': {
        'spotify': {
            'name': 'Mesa'
        }
    },    
    'behaviors': {
        'on_message': {
            'response_probability': 0.0,
            'delay': [0, 1],
            'channels': None,
            'reaction_probability': 0.125
        },
        'on_mention': {
            'response_probability': 1.0,
            'channels': None,
            'delay': [0, 1],
            'program': 'spotify',
            'reaction_probability': 0.25
        }
    }
}