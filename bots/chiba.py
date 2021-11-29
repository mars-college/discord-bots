from .channels import *

chiba = {
    'token_env': 'DISCORD_TOKEN_CHIBA',
    'debug': False,
    'programs': {
        'ifttt': {
            'key_env': 'IFTTT_KEY',
            'actions': [
                {'keyword': 'on', 'action': 'chibaon', 'reply': 'Chiba on!'},
                {'keyword': 'off', 'action': 'chibaoff', 'reply': 'Chiba off!'}
            ]
        },
        'spotify': {
            'name': 'Chiba'
        },
        'keyword': {
            'programs': [
                {'keywords': ['on', 'off'], 'program': 'ifttt'},
                {'keywords': ['play', 'queue', 'next', 'stop'], 'program': 'spotify'}
            ]
        }
    },   
    'behaviors': {
        'on_mention': [{
            'response_probability': 1.0,
            'channels': [mc22_bots],
            'delay': [0, 1],
            'program': 'ifttt',
            'reaction_probability': 0.0
        },{
            'response_probability': 1.0,
            'channels': [testnet_general],
            'delay': [0, 1],
            'program': 'keyword',
            'reaction_probability': 0.0
        }]
    }
}