from .channels import *

deeplearning = {
    'token_env': 'DISCORD_TOKEN_DEEPLEARNING',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Professor',
            'chat_history': {
                'max_history': 5, 
                'max_age': 60*10
            },
            'intro': "<P1> is asking questions to a professor of deep learning who can explain research topics clearly.",   
            'messages_pre': [
                {"sender": "<P1>", "message": "what are transformer networks?"},
                {"sender": "<S>", "message": "Transformer networks use an encoder decoder architecture which, like RNNs, can process sequential data."},
                {"sender": "<P1>", "message": "what are they best for?", "exclude_embed": True},
                {"sender": "<S>", "message": "They are popular for Natural Language Processing."},
                {"sender": "<P1>", "message": "what are their advantages over RNNs?"},
                {"sender": "<S>", "message": "Transformers can process sequences out of order."},
                {"sender": "<P1>", "message": "how do generative adversarial network work?"},
                {"sender": "<S>", "message": "A GAN is two neural networks, a generator which synthesizes new data, and a discriminator which identifies real and fake samples. "}
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.66, 
            'max_tokens': 125
        }
    },    
    'behaviors': {
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.25,
            'reply_probability': 1.0
        }
    }
}