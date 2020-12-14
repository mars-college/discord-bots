from easydict import EasyDict
from datetime import datetime, timedelta
import re
import time
import asyncio
import gpt3


def get_utc_time():
    now = datetime.now()
    ts = time.time()
    utc_offset = datetime.utcfromtimestamp(ts) - datetime.fromtimestamp(ts)
    now = now + timedelta(0, utc_offset.total_seconds())
    return now


async def run(gpt3_settings, 
              message, 
              member2var, 
              var2member):
    
    max_history = gpt3_settings.chat_history.max_history
    max_age = gpt3_settings.chat_history.max_age

    # get channel's message history and limit it according to chat_history settings
    message_history = await message.channel.history(limit=max_history).flatten()
    if max_age is not None:
        message_history = [msg for msg in message_history 
                           if (get_utc_time()-msg.created_at).seconds < max_age]

    # convert all member ids to name variables, e.g. <P1>, <S>, etc
    messages_new = [EasyDict({
        'sender': member2var[str(msg.author.id)], 
        'message': re.sub('<@!?([0-9]+)>', lambda m: member2var[m.group(1)], msg.content).strip()}) 
        for msg in message_history[::-1]
    ]

    # run GPT-3, given prompt settings and truncated history
    prompt, stops, completion, char2var, var2char, search_results = gpt4.run(
        gpt3_settings, 
        messages_new)

    # convert all name variables back to member ids
    completion = re.sub('({})'.format('|'.join(var2member.keys())),
                        lambda m: var2member[m.group(1)], 
                        completion).strip()

    #force_mention = gpt3_settings.force_mention if 'force_mention' in gpt3_settings else None       
    gpt4.log(prompt, stops, completion, 
             member2var, var2member, char2var, var2char, 
             search_results, gpt3_settings.name)
    
    return completion
