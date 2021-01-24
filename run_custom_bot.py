import asyncio
from main import *
from bots.channels import *

# define the bot
my_custom_bot = {
    'token_env': 'DISCORD_TOKEN_CHIBA',
    'debug': False,
    'programs': {
        'my_custom': {
            'name': 'Chiba',
            'data': 'hello world'
        }
    },    
    'behaviors': {
        'on_mention': {
            'response_probability': 1.0,
            'channels': all_channels_testnet,
            'delay': [0, 1],
            'program': 'my_custom',                
            'reaction_probability': 0.25,
            'reply_probability': 1.0
        }
    }
}

# define custom program here
class DiscordBotCustom(DiscordBot):
    async def run_program_custom(self, program, settings):
        await asyncio.sleep(0)
        print('Running custom program: {}'.format(program))
        name, data = settings.name, settings.data
        response = 'My name is {}: "{}"'.format(name, data)
        return response


# overwrite global variables if you want
reactions_enabled = False

# run
load_dotenv()
intents = discord.Intents.default()
intents.members = True
loop = asyncio.get_event_loop()
client = DiscordBotCustom(intents=intents)
loop.create_task(client.setup(my_custom_bot))
loop.run_forever()
