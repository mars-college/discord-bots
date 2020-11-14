import random
import time
import itertools
import re
import torch
import numpy as np
import time
from datetime import datetime, timedelta
from easydict import EasyDict
from sentence_transformers import SentenceTransformer, util

from gpt3 import *

default_characters = ['Alice', 'Bob', 'Carol', 'David', 'Emily', 'Frank', 'Gabriela', 'Harry', 'Ingrid']

model = SentenceTransformer('distilbert-base-nli-mean-tokens')



def get_utc_time():
    now = datetime.now()
    ts = time.time()
    utc_offset = datetime.utcfromtimestamp(ts) - datetime.fromtimestamp(ts)
    now = now + timedelta(0, utc_offset.total_seconds())
    return now



class Prompt:
    
    def __init__(self, prompt, user_id):
        prompt = EasyDict(prompt)
        self.id = user_id
        self.name = prompt.name
        self.prompt = prompt
        
        self.messages_pre = prompt.messages_pre if 'messages_pre' in prompt else None
        self.messages_candidates = prompt.messages_candidates if 'messages_candidates' in prompt else None
        
        #self.calculate_features()
                   
    def calculate_features(self):
        if self.messages_pre:
            embed_messages = [m.message for m in self.messages_pre if 'exclude_embed' not in m]
            self.embeddings = model.encode(embed_messages)
        else:
            self.embeddings = None
            
    def get_affinity(self, query_embeddings, top_k=5):
        cos_sim = util.pytorch_cos_sim(query_embeddings, self.embeddings).cpu()
        scores = torch.sort(cos_sim.flatten(), descending=True).values[:top_k]
        return torch.mean(scores)

    def __str__(self):
        return self.get_prompt([])
    
    def postprocess_gpt(self, msg):
        for char, user in self.char2user.items():
            msg = msg.replace(char, '<@!%s>'%user)
            msg = msg.replace(char, '<@%s>'%user)
        force_mention = self.prompt.force_mention if 'force_mention' in self.prompt else False       
        if force_mention and str(force_mention) not in msg:
            print('msg was:')
            print(msg)
            msg = '<@!{}> {}'.format(str(force_mention), msg)
            print('msg is now:')
            print(msg)
        return msg

    def get_prompt(self, messages_new):
        erase_mentions = 'erase_mentions' in self.prompt and self.prompt.erase_mentions        
        line_breaks_pre = self.prompt.formatting.line_breaks_before_sender
        line_breaks_post = self.prompt.formatting.line_breaks_after_sender
        stop_at_line_breaks = self.prompt.formatting.line_breaks_after_sender

        messages_new = [EasyDict(m) for m in messages_new]
        search_results = None
        
        if erase_mentions:
            for m in messages_new:
                m.message = m.message.replace('<@!%s>,'%str(self.id), '').strip()
                m.message = m.message.replace('<@%s>,'%str(self.id), '').strip()
                m.message = m.message.replace('<@!%s>'%str(self.id), '').strip()
                m.message = m.message.replace('<@%s>'%str(self.id), '').strip()

        if self.messages_candidates:
            candidates = [mc[0]['message'] for mc in self.messages_candidates]
            responses = [mc[1]['message'] for mc in self.messages_candidates]

            sender = messages_new[-1].sender
            query = messages_new[-1].message

            result = gpt3_search(candidates, query, engine='davinci')

            scores = [doc['score'] for doc in result['data']]
            ranked_queries = np.argsort(scores)
            ranked_queries = list(reversed(ranked_queries))
            
            search_results = [[candidates[idx], scores[idx]] for idx in ranked_queries]
            for candidate, score in search_results:
                print(" -> %s : %0.2f" % (candidate, score))

            idx_top = ranked_queries[0]
            self.messages_pre = [
                EasyDict({'sender': '<P1>', 'message': candidates[idx_top]}),
                EasyDict({'sender': '<S>', 'message': responses[idx_top]})
            ]

        
        # set up dicts to map between different aliases for speakers
        # - variables (<P1>, <P2>, <S>)
        # - characters (Alice, Bob, Carol)
        # - discord accounts (<@!4743857923502143>)
        characters = default_characters if 'speakers' not in self.prompt else self.prompt['speakers']
        random.shuffle(characters)
        users = [[m.sender] + re.findall('@!([0-9]+)>', m.message) for m in messages_new]
        users = [u for u in list(set(itertools.chain.from_iterable(users))) if u != str(self.id)]
        pre_speakers = list(set([m.sender for m in self.messages_pre if m.sender != '<S>']))
        num_speakers = max(len(pre_speakers), len(users))
        variables = ['<P%d>'%(i+1) for i in range(num_speakers)]
        user2var, var2user, var2char, char2user, user2char = {}, {}, {}, {}, {}
        user2var[str(self.id)] = '<S>'
        var2user['<S>'] = str(self.id)
        var2char['<S>'] = self.name
        char2user[self.name] = str(self.id)
        user2char[str(self.id)] = self.name
        
#         print('pre speakers', pre_speakers)
#         print('users', users)
#         print('num_speakers', num_speakers)
#         print('vars', variables)

        for u, user in enumerate(users):
            user2var[user] = '<P%d>'%(u+1)
            var2user['<P%d>'%(u+1)] = user
        for v, var in enumerate(variables):
            var2char['<P%d>'%(v+1)] = characters[v % len(characters)]
        for var, char in var2char.items():
            user = str(self.id) if var not in var2user else var2user[var] # hack!
            if var not in var2user:
                print("HACK FOR", var)
            char2user[char] = user
            user2char[user] = char
            
#         print('user2var', user2var)    
#         print('char2user', char2user)
#         print('var2user', var2user)
#         print('var2char', var2char)
        
        self.char2user = char2user  # save for post-prompt
        
        # introduction
        prompt_str = self.prompt.intro
        prompt_str += '\n\n' if prompt_str != '' else ''
        for var, char in var2char.items():
            prompt_str = prompt_str.replace(var, char) 
        
        # pre-written lines
        for m in self.messages_pre:
            sender, message = var2char[m.sender], m.message
            for var, char in var2char.items():
                message = message.replace(var, char) 
            if message or not message.isspace():
                prompt_str += '\n'*line_breaks_pre
                prompt_str += '%s:'%sender
                if line_breaks_post==0:
                    prompt_str += ' '
                prompt_str += '\n'*line_breaks_post
                prompt_str += '%s'%message.strip()
        
        # message history from discord 
        for m in messages_new:
            sender, message = user2char[m.sender], m.message
            for user, char in user2char.items():
                message = re.sub(r'^(<@!?[0-9]+>)', r'\1,', message)
                message = message.replace('<@!%s>'%user, char) 
                message = message.replace('<@%s>'%user, char) 
            if message or not message.isspace():
                prompt_str += '\n'*line_breaks_pre
                prompt_str += '%s:'%sender
                if line_breaks_post==0:
                    prompt_str += ' '
                prompt_str += '\n'*line_breaks_post
                prompt_str += '%s'%message.strip()

        # post-processing
        prompt_str = re.sub(' +', ' ', prompt_str)  # remove double spaces
        prompt_str = re.sub(',+', ',', prompt_str)  # remove double commas
        prompt_str += '\n'*line_breaks_pre
        prompt_str += '%s:' % self.name
        
        stops = ['\n%s:'%c for c in list(set(characters))[:3]]
        stops += ['\n'] if self.prompt.formatting.stop_at_line_break else []

        print("PROMPT:\n", prompt_str)
        print("STOPS:\n", stops)

        return prompt_str, stops, search_results
            
