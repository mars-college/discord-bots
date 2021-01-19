from .channels import *

kitchen = {
    'token_env': 'DISCORD_TOKEN_KITCHEN',
    'debug': False,
    'programs': {
        'gpt3_chat': {
            'name': 'Expert',
            'chat_history': {
                'max_history': 3, 
                'max_age': 60*5
            },
            'intro': "<P1> is asking questions to a world expert on health and fitness, who is also an excellent cook.",   
            'messages_pre': [
                {"sender": "<P1>", "message": "What's a good recipe for asparagus?"},
                {"sender": "<S>", "message": "Preheat an oven to 425°, drizzle olive oil on the asparagus, sprinkle with parmesan and garlic, bake until just tender."},
                {"sender": "<P1>", "message": "How long will it take?", "exclude_embed": True},
                {"sender": "<S>", "message": "12 to 15 minutes depending on thickness.", "exclude_embed": True},
                {"sender": "<P1>", "message": "Does it take any spices?"},
                {"sender": "<S>", "message": "Some black pepper."},
                {"sender": "<P1>", "message": "What are the nutritional benefits of blueberries?"}, 
                {"sender": "<S>", "message": "They are a good source of antioxidants, phytoflavinoids, these berries are also high in potassium. They are anti-inflammatory and lower your risk of heart disease and cancer."}
            ],
            'formatting': {
                'line_breaks_before_sender': 1, 
                'line_breaks_after_sender': 0, 
                'stop_at_line_break': True
            },
            'erase_mentions': True,
            'force_mention': None,
            'engine': 'davinci',
            'temperature': 0.85, 
            'max_tokens': 250,
        }
    },    
    'behaviors': {
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet + [mc_ai, mc_lounge, mc_food],
            'program': 'gpt3_chat',
            'reaction_probability': 0.25
        },
        'on_message': {
            'response_probability': 0.0,
            'channels': all_channels_testnet + [mc_ai, mc_lounge, mc_food],
            'program': 'gpt3_chat',
            'reaction_probability': 0.125
        }
    }
}
