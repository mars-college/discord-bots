from dotenv import load_dotenv
from easydict import EasyDict
from datetime import datetime, timedelta, timezone
from suntime import Sun, SunTimeException
import sched
import asyncio
import itertools
import time
import math
import os
import re
import json
import random
import requests
import numpy as np

import discord
import spotipy
import gpt3

from programs import gpt3_chat
from programs import ml4a_client
from programs import spotify

from bots import bots

    
botlist = ['qa', 'mechanicalduck'] 
botlist = ['mesa']
botlist = ['mesa', 'mechanicalduck', 'chatsubo', 'wall-e', 'eve', 'facts', 'philosophy', 'deeplearning', 'kitchen', 'qa']


# spotify program & json (credentials)
#  - add to playlist
# gpt3_prompt
# setup dms???
# mesa timed switch to mc


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


class DiscordBot(discord.Client):
       
    async def setup(self, settings):
        self.ready = False
        self.settings = EasyDict(settings)
        self.timestamps = []
        self.last_senders = {}
        token = os.getenv(self.settings.token_env) 
        await self.start(token)
        
        
    async def on_ready(self):
        self.ready = True
        guild_names = [guild.name for guild in self.guilds]
        print('{} has connected to guilds: {}'.format(self.user, ','.join(guild_names)))
        if 'background' in self.settings.behaviors:
            self.loop.create_task(self.background_process())
        if 'timed' in self.settings.behaviors:
            self.loop.create_task(self.schedule_timed_events())
        
        
    async def update_member_lookup(self, message):
        channel = message.channel
        last_senders = self.last_senders[channel.id] if channel.id in self.last_senders else None
        
        if last_senders is None:
            message_history = await channel.history(limit=50).flatten()
            last_senders  = [member.id for member in message.guild.members]
            last_senders += [msg.author.id for msg in message_history[::-1]]
        else:
            last_senders += [message.author.id]
            
        last_senders = list(dict.fromkeys(reversed(last_senders)))
        if self.user.id in last_senders:
            last_senders.remove(self.user.id)

        self.last_senders[channel.id] = last_senders
        
        member2var = {str(member): '<P{}>'.format(m+1) for m, member in enumerate(last_senders)}
        member2var[str(self.user.id)] = '<S>'        
        var2member = {v: '<@!{}>'.format(k) for k, v in member2var.items()}
        
        # duplicate var2members in case vars > members
        num_vars = len(var2member)-1
        for v in range(num_vars+1, 25):
            var2member['<P{}>'.format(v)] = var2member['<P{}>'.format(1+(v-1)%num_vars)]
        
        return member2var, var2member

    
    async def on_message(self, message):
        if not self.ready:
            return
        
        # lookup & replace tables from member id's to variables e.g. <P1>, <S>
        member2var, var2member = await self.update_member_lookup(message)

        # mentions and metadata
        all_mentions = re.findall('<@!?([0-9]+)>', message.content)
        mentioned = str(self.user.id) in all_mentions
        author_is_self = message.author.id == self.user.id
        
        # which context (on_message, on_mention, or background)
        behavior = self.settings.behaviors
        if mentioned:
            context = behavior.on_mention if 'on_mention' in behavior else None
        else:
            context = behavior.on_message if 'on_message' in behavior else None

        # skipping conditions
        channel_eligible = (message.channel.id in context.channels) if context and context.channels else True
        busy = len(self.timestamps) > 0
        decide_to_reply = False if not context else (random.random() < context.probability)

        # if any skipping conditions are True, stop
        if busy or author_is_self or not decide_to_reply or not channel_eligible:
            return
        
        # bot has decided to reply. add timestamp and delay
        delay = context.delay[0]+(context.delay[1]-context.delay[0])*random.random() if 'delay' in context else 0
        timestamp = {"time": time.time(), "delay": delay}
        self.timestamps.append(timestamp)

        # choose program based on search query, if specified
        options_search = None
        if 'options' in context and len(context.options):
            candidates = [opt['document'] for opt in context.options]
            query = re.sub('<@!?[0-9]+>', '', message.content)
            result = gpt3.search(candidates, query, engine='curie')
            scores = [doc['score'] for doc in result['data']]
            ranked_queries = list(reversed(np.argsort(scores)))
            options_search = [{'candidate': candidates[idx], 'score': scores[idx]} 
                              for idx in ranked_queries]
            for result in options_search:
                print(" -> %s : %0.2f" % (result['candidate'], result['score']))
            idx_top = ranked_queries[0]
            print("idx top",  idx_top)
            program = context.options[idx_top]['program']
            print("the program is", program)
        
        else:
            program = context.program if 'program' in context else None
            if not program:
                print('No program selected')
                return
        
        # optional delay
        await asyncio.sleep(timestamp['delay'])
        
        
        ##########################################
        ## Program: GPT-3 chat
        ##########################################
        
        if program == 'gpt3_chat':
            settings = self.settings.programs.gpt3_chat
            completion = await gpt3_chat.run(
                settings, 
                message, 
                member2var, 
                var2member) 
            await message.channel.send(completion[:2000])
            
            
        ##########################################
        ## Program: GPT-3 single prompt
        ##########################################

        elif program == 'gpt3_prompt':
            settings = self.settings.programs.gpt3_prompt
            completion = gpt3.complete(
                settings.prompt, 
                stops=settings.stops if 'stops' in settings else None, 
                max_tokens=settings.max_tokens if 'max_tokens' in settings else 50, 
                temperature=settings.temperature if 'temperature' in settings else 0.9, 
                engine=settings.engine if 'engine' in settings else 'davinci',
                max_completions=3)            
            await message.channel.send(completion[:2000])

            
        ##########################################
        ## Program: ml4a generate
        ##########################################

        elif program == 'ml4a':
            settings = self.settings.programs.ml4a
            filename = ml4a_client.run(settings)
            message_str = 'hello world'
            await message.channel.send(message_str, 
                file=discord.File(filename, filename=filename))
         
                
        ##########################################
        ## Program: Spotify                    
        ##########################################

        elif program == 'spotify':
            message_out, embed_out = spotify.run(message, self.user.id)
            if embed_out:
                embed = discord.Embed()
                embed.set_image(url=embed_out)
                await message.channel.send(message_out, embed=embed)         
            else:                   
                await message.channel.send(message_out)
                    
        # when done, remove the timestamp, freeing up bot
        self.timestamps.remove(timestamp)


    async def timed_event(self, event):
        channel = self.get_channel(event.channel)
        
        if event.program == 'gpt3_prompt':
            pass
        
        await channel.send('hello world')
        
        
    async def schedule_timed_events(self):
        await self.wait_until_ready()
        
        if len(self.settings.behaviors.timed) == 0:
            return
        
        while True:
            now = datetime.now()
            timed_events = []
            for t in self.settings.behaviors.timed:
                if t.type == 'daily':
                    target_time = now.replace(hour=t.time[0], minute=t.time[1], second=0)
                elif t.type == 'sunset':
                    latitude = float(os.getenv('LOCAL_LATITUDE'))
                    longitude = float(os.getenv('LOCAL_LONGITUDE'))
                    sunset = Sun(latitude, longitude).get_sunset_time()
                    sunset = utc_to_local(sunset).replace(tzinfo=None)
                    target_time = sunset - timedelta(seconds=t.minutes_before * 60)
                while target_time < now:
                    target_time += timedelta(days=1)
                timed_events.append({'event': t, 'time': target_time})
            timed_events = sorted(timed_events, key=lambda k: k['time']) 
            next_event = timed_events[0]
            time_until = next_event['time'] - now
            print('time until now', time_until, time_until.seconds)

            await asyncio.sleep(time_until.seconds)
            await self.timed_event(next_event['event'])
            await asyncio.sleep(60)
            
      
    async def background_process(self):
        await self.wait_until_ready()
        bg = self.settings.behaviors.background
        if not 'probability_trigger' in bg or not 'every_num_minutes' in bg:
            return
        prob_trigger = 1.0-math.pow(1.0-bg.probability_trigger, 
                                    1.0/bg.every_num_minutes)
        while not self.is_closed():
            
            if (random.random() < prob_trigger):
                #channel = self.get_channel(758719600895590444) # channel ID goes here
                #await channel.send('hello !')
                pass # disabled for a minute
            
            
            
            await asyncio.sleep(60)  # run every 60 seconds



def main(): 
    load_dotenv()
    intents = discord.Intents.default()
    intents.members = True
    loop = asyncio.get_event_loop()
    for botname in botlist:
        client = DiscordBot(intents=intents)
        loop.create_task(client.setup(bots[botname]))
    loop.run_forever()


if __name__ == "__main__":
    main()