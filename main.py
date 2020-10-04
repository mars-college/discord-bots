import asyncio
import os
import re
import time
from easydict import EasyDict
import random
import itertools
import numpy as np
from dotenv import load_dotenv

import discord
import openai

from bots import *
from prompt import *


botlist = ['FACTS', 'DEEPLEARNING', 'PHILOSOPHY', 'KITCHEN', 'BEYONCE', 'TURING']



def run_gpt3(prompt, max_tokens, temperature, stops, engine='curie'):
    print("go gpt: ", max_tokens, temperature, stops, engine)
    response = openai.Completion.create(
        engine=engine, 
        prompt=prompt, 
        max_tokens=max_tokens, 
        temperature=temperature,
        stop=stops)
    text = response.choices[0].text
    return text.strip()



class DiscordBot(discord.Client):
    

    async def setup(self, token, prompt_settings):
        self.ready = False
        self.timestamps = []
        self.settings = EasyDict(prompt_settings)
        await self.start(token)
        
    async def on_ready(self):
        self.ready = True
        self.prompt = Prompt(self.settings, self.user.id)
        print('%s has connected to guilds: %s'%(self.user, ','.join([g.name for g in self.guilds])))
    
    async def on_message(self, message):
        if not self.ready:
            return

        all_mentions = re.findall('<@![0-9]+>', message.content)
        mentioned = '<@!%d>' % self.user.id in all_mentions
        self_author = message.author == self.user
        channel_eligible = (message.channel.id in self.settings.channels) if self.settings.channels != None else True        
        strategy = self.settings.strategy.on_mention if mentioned else self.settings.strategy.regular
        gpt_params = self.settings.gpt_params
        
        busy = len(self.timestamps) > 0
        author_is_self = message.author.name == self.user.name        
        decide_to_reply = random.random() < strategy.probability
        if self.user.name == 'gpt3-philosophy':
            print(strategy.probability, "thats the prob", self.user.name, decide_to_reply, author_is_self, busy)
        
        if not busy and not author_is_self and channel_eligible and decide_to_reply:
            timestamp = {"time": time.time(), "delay": 1+1*random.random()}
            self.timestamps.append(timestamp)

            max_history = self.settings.history.max_history
            time_interval = self.settings.history.max_age
            
            message_history = await message.channel.history(limit=max_history).flatten()
            if time_interval is not None:
                message_history = [msg for msg in message_history if (get_utc_time() - msg.created_at).seconds < time_interval]

            messages_new = [{'sender': str(msg.author.id), 'message': msg.content.strip()} 
                            for msg in message_history[::-1]]

            prompt_str, stops = self.prompt.get_prompt(messages_new)
            print("\n\n---------------\n\n%s\n\n-------------\n\n" % prompt_str)

            # convert mentions to names
            
            await asyncio.sleep(timestamp['delay'])
            
            completion = run_gpt3(
                prompt_str, 
                max_tokens=gpt_params.max_tokens, 
                temperature=gpt_params.temperature, 
                stops=stops, 
                engine='davinci')
            
            # convert names to mentions
            
            await message.channel.send(completion.strip())

            self.timestamps.remove(timestamp)

        else:
            print("SKIP!")
            

    
def main(): 
    load_dotenv()
    guild = os.getenv('DISCORD_GUILD')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    loop = asyncio.get_event_loop()
    for botname in botlist:
        client = DiscordBot()
        loop.create_task(
            client.setup(
                os.getenv('DISCORD_TOKEN_%s'%botname), 
                bots[botname]
            ))
        
    loop.run_forever()



if __name__ == "__main__":
    main()