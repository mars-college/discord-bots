import asyncio
import os
import re
import json
import time
import requests
from easydict import EasyDict
import random
import itertools
import numpy as np
from dotenv import load_dotenv

import discord

from bots import *
from prompt import *
from gpt3 import *


botlist = ['FACTS', 'DEEPLEARNING', 'PHILOSOPHY', 'KITCHEN', 'BEYONCE', 'TURING']

botlist = ['FACTS', 'PHILOSOPHY', 'KITCHEN', 'CHATSUBO', 'QA']




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

        all_mentions = re.findall('<@!?[0-9]+>', message.content)
        mentioned = '<@!%d>' % self.user.id in all_mentions or '<@%d>' % self.user.id in all_mentions
        self_author = message.author == self.user
        channel_eligible = True  #(message.channel.id in self.settings.channels) if self.settings.channels != None else True
        strategy = self.settings.strategy.on_mention if mentioned else self.settings.strategy.regular
        gpt_params = self.settings.gpt_params
        
        busy = len(self.timestamps) > 0
        author_is_self = message.author.name == self.user.name   
        decide_to_reply = random.random() < strategy.probability
        debug = self.settings.debug if 'debug' in self.settings else False

        if not author_is_self and channel_eligible and decide_to_reply:  # and not busy?
            timestamp = {"time": time.time(), "delay": 1+1*random.random()}
            self.timestamps.append(timestamp)

            max_history = self.settings.history.max_history
            time_interval = self.settings.history.max_age
            
            message_history = await message.channel.history(limit=max_history).flatten()
            if time_interval is not None:
                message_history = [msg for msg in message_history if (get_utc_time() - msg.created_at).seconds < time_interval]

            messages_new = [{'sender': str(msg.author.id), 'message': msg.content.strip()} 
                            for msg in message_history[::-1]]

            prompt_str, stops, search_results = self.prompt.get_prompt(messages_new)
            
            if prompt_str is None:
                return

            await asyncio.sleep(timestamp['delay'])
            
            if debug:
                print('\n\n===== DEBUG PROMPT (%s) ========\n\n' % self.user.name)
                print('%s' % prompt_str)
                print("\n\n================================\n\n")
            
            else:
                
                completion = gpt3_complete(
                    prompt_str, 
                    stops=stops, 
                    max_tokens=gpt_params.max_tokens, 
                    temperature=gpt_params.temperature, 
                    engine='davinci',
                    max_completions=gpt_params.max_completions if 'max_completions' in gpt_params else 1)
                
                completion = self.prompt.postprocess_gpt(completion)
                log(prompt_str, completion, self.user.name, search_results)
                await message.channel.send(completion.strip())

            self.timestamps.remove(timestamp)

        else:
            print('%s skip: %s %s %s' % (
                self.user.name, 
                'debug' if debug else 'ACTIVE', 
                'busy' if busy else 'FREE',
                'wrongchannel' if channel_eligible else 'CHANNEL'))
            

    
def main(): 
    load_dotenv()
    guild = os.getenv('DISCORD_GUILD')
    
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