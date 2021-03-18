from .channels import *

oracle = {
    'token_env': 'DISCORD_TOKEN_TAROT',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Oracle',
            'chat_history': {
                'max_history': 1, 
                'max_age': None
            },
            'intro': 'The Oracle is a fortune-teller who reads Tarot cards from random people who ask the Oracle questions. The available Tarot cards are: The Traveler, The Bots, The Rovers, The Iron Martian, The Remote Worker, The Lodestar.',
            'messages_pre': [
                {"sender": "<P1>", "message": "What is my calling?"},
                {"sender": "<S>", "message": "For your present situation, I've pulled The Traveler (Card 0). This card represents what is happening to the you at the present time. It also reflects your state of mind and how you may be perceiving the situation related to your topic. The traveler is present throughout life, and can stand for beginnings, innocence, spontaneity, a free spirit."},
                {"sender": "<P2>", "message": "What should I do to make life meaningful?"},
                {"sender": "<S>", "message": "Card 2, The Iron Martian. This card represents the immediate challenge or problem facing your situation. This is the one thing that, if resolved, would make life a lot easier. I've pulled the Witches of Venus, beware! These can mean Hidden enemies, danger, calumny, darkness, terror, deception, occult forces, error."},
                {"sender": "<P3>", "message": "How should I travel to Mars?"},
                {"sender": "<S>", "message": "I've pulled Card 16, the Lodestar. Beware of unforeseen catastrophe on your journey. This card can mean Misery, distress, indigence, adversity, calamity, disgrace, deception, ruin."}
            ],
            'formatting': {
                'line_breaks_before_sender': 3, 
                'line_breaks_after_sender': 2, 
                'stop_at_line_break': False
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.92, 
            'max_tokens': 350,
            'max_completions': 2
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
            'response_probability': 0.0,
            'channels': all_channels_testnet + all_channels_mc + all_channels_mcb,
            'program': 'gpt3_chat',
            'reaction_probability': 0.125
        }
    }
}
