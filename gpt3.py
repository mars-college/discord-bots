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

from transformers.tokenization_gpt2 import GPT2Tokenizer
import discord
import openai


def count_tokens(text):
    encoding = GPT2Tokenizer.from_pretrained("gpt2-xl")
    tokens = encoding(text)
    return len(tokens["input_ids"])



def gpt3_complete(prompt, 
                  stops=None, 
                  max_tokens=100, 
                  temperature=0.9, 
                  engine='davinci',
                  max_completions=1):
    
    finished = False
    completion = ''
    n_completions = 0
    n_tokens = 0
    
    while not finished:
        response = openai.Completion.create(
            engine=engine, 
            prompt=prompt, 
            max_tokens=max_tokens, 
            temperature=temperature,
            stop=stops)
        
        n_completions += 1
        text = response.choices[0].text
        completion += text
        prompt += text
        n_tokens = count_tokens(prompt)
        print('complete %d/%d (%d):'%(n_completions, max_completions, n_tokens), text)
        finished = response.choices[0].finish_reason == 'stop' \
            or n_completions >= max_completions \
            or n_tokens >= 2048-max_tokens
    
    return completion.strip()



def gpt3_search(documents, query, engine='davinci'):
    data = json.dumps({"documents": documents, "query": query})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % os.getenv('OPENAI_API_KEY'),
    }
    response = requests.post('https://api.openai.com/v1/engines/%s/search' % engine, headers=headers, data=data)
    result = json.loads(response.text)
    return result



def log(prompt_str, completion, search_results):
    text = ''
    if search_results:
        for candidate, score in search_results:
            text += ' -> %s : %0.2f\n' % (candidate, score)
        text += '\n\n\n\n======================\n\n\n'
    text += prompt_str
    text += '\n\n\n\n======================\n\n\n'
    text += completion        
    filename = time.strftime("%Y%m%d-%H%M%S")
    with open("results/%s.txt" % filename, "w") as f:
        f.write(text)

