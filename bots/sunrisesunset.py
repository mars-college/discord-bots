from .channels import *

sunrisesunset = {
    'token_env': 'DISCORD_TOKEN_SUNRISESUNSET',
    'debug': False,
    'programs': {
        'spotify': {
            'name': 'Sunrise Sunset'
        },
        'gpt3_prompt': [{
            'prompt': '''Here is a short poem about the beginning of a new day.

    I'll tell you how the sun rose, —
    A ribbon at a time.
    The steeples swam in amethyst,
    The news like squirrels ran.

    The hills untied their bonnets,
    The bobolinks begun.
    Then I said softly to myself,
    "That must have been the sun!" 



    Here is a short poem about the beginning of a new day.

    Dawn
    Is beautiful.
    Its new and raw.
    It's  beautifully honest.
    There's something redeeming
    about the early minutes our day
    It imitates the early minutes of our existence
    And erodes the nonsense and lies
    Of day-to-day survival.



    Here is a short poem about the beginning of a new day.

    Long before the postman comes
    The sun begins to rise,
    Far in the East if you should look
    You'd find it in the skies.
    At first it's just a streak of light
    Then all at once the world gets bright.

    Here is a short poem about the beginning of a new day.''', 
            'engine': 'davinci',
            'temperature': 0.9,
            'max_tokens': 200,
            'stops': ['\nHere is a short'],
            'preface': 'A new day begins 😎\nHere is my poem of the day:\n\n'
        }, {
            'prompt': '''Here is a short poem about the sunset.

    Out of the sunset's red
    Into the blushing sea,
    The winds of day drop dead
    And dreams come home to me. —
    The sea is still,— and apart
    Is a stillness in my heart.



    Here is a short poem about the sunset.

    It is a beauteous evening, calm and free,
    The holy time is quiet as a Nun
    Breathless with adoration; the broad sun
    Is sinking down in its tranquility;
    The gentleness of heaven broods o’er the Sea …



    Here is a short poem about the sunset.

    The sun's still keeping the sky
    somewhat colored,
    even though it's already gone down
    beyond the horizon.



    Here is a short poem about the sunset.''', 
            'engine': 'davinci',
            'temperature': 0.9, 
            'max_tokens': 200,
            'stops': ['\nHere is a short'],
            'preface': 'One hour until sunset! 😎\nHere is this evening\'s incantation:\n\n'
        }]
    },    
    'behaviors': {
        'on_message': {
            'response_probability': 0.0,
            'reaction_probability': 0.125,
            'channels': None
        },
        'on_mention': {
            'response_probability': 0.0,
            'reaction_probability': 0.25,
            'channels': None
        },            
        'timed': [{
            'type': 'sunrise', 
            'minutes_before': 0,
            'program': 'gpt3_prompt', 'program_index': 0,
            'channel': mc_general
        },{
            'type': 'sunset',
            'minutes_before': 60,
            'program': 'gpt3_prompt', 'program_index': 1,
            'channel': mc_general
        }]
    }
}