import random
import time
import re
import torch
import numpy as np
import time
from datetime import datetime, timedelta
from easydict import EasyDict
from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('distilbert-base-nli-mean-tokens')


default_characters = ['Alice', 'Bob', 'Carol', 'David'] #, 'Emily', 'Frank', 'Gabriela', 'Harry', 'Ingrid']


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
        self.prompt = prompt
        self.messages_pre = prompt.messages_pre
        self.calculate_features()
                   
    def calculate_features(self):
        embed_messages = [m.message for m in self.messages_pre if 'exclude_embed' not in m]
        self.embeddings = model.encode(embed_messages)
               
    def get_affinity(self, query_embeddings, top_k=5):
        cos_sim = util.pytorch_cos_sim(query_embeddings, self.embeddings).cpu()
        scores = torch.sort(cos_sim.flatten(), descending=True).values[:top_k]
        return torch.mean(scores)

    def __str__(self):
        return self.get_prompt([])

    def get_prompt(self, messages_new):
        messages_new = [EasyDict(m) for m in messages_new]
        senders_new = list(set([m.sender for m in messages_new if m.sender != str(self.id)]))
        erase_mentions = 'erase_mentions' in self.prompt and self.prompt['erase_mentions']
        characters = default_characters if 'speakers' not in self.prompt else self.prompt['speakers']
        random.shuffle(characters)
        
        for m in messages_new:
            m.sender = m.sender.replace(str(self.id), '<S>')
            m.message = m.message.replace('<@!%d>'%self.id, '' if erase_mentions else '<S>')
            for s, sender in enumerate(senders_new):
                m.sender = m.sender.replace(sender, '<P%d>'%(s+1))
                m.message = m.message.replace('<@!%s>'%sender, '' if erase_mentions else '<P%d>'%(s+1))
            m.message = re.sub(r'<@![0-9]+>', '', m.message)
        
        prompt_str = self.prompt.intro
        prompt_str += '\n\n' if prompt_str != '' else ''
        for m in self.messages_pre + messages_new:
            next_line = '\n%s: %s' % (m.sender, m.message.strip())
            prompt_str += next_line
        prompt_str += '\n%s:' % self.prompt.name
        prompt_str = prompt_str.replace('<S>', self.prompt.name)
        for n, name in enumerate(characters*5):
            prompt_str = prompt_str.replace('<P%d>'%(n+1), name)
        
        stops = ['\n%s:'%c for c in list(set(characters))[:3]] + ['\n']
        
        return prompt_str, stops
            
