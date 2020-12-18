from easydict import EasyDict
import sys
import os
import re
import json
import time
import requests
import random
import numpy as np

from transformers.tokenization_gpt2 import GPT2Tokenizer
import openai

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

default_characters = ['Alyssa', 'Brady', 'Chloe', 'Derrick', 
                      'Eleanor', 'Fletcher', 'Greta', 'Harold', 
                      'Irina', 'Jeremy', 'Kathryn', 'Lionel', 
                      'Margaret', 'Nathan', 'Ophelia', 'Patricio', 
                      'Quinne', 'Raymond', 'Stacy', 'Tobias', 
                      'Vincenzo', 'Wendy']


def count_tokens(text):
    encoding = GPT2Tokenizer.from_pretrained("gpt2-xl")
    tokens = encoding(text)
    return len(tokens["input_ids"])


def complete(prompt, 
             stops=None, 
             max_tokens=100, 
             temperature=0.9, 
             engine='davinci',
             max_completions=1):
    
    n_completions = 0
    n_tokens = 0
    finished = False
    completion = ''
        
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
        finished = (response.choices[0].finish_reason == 'stop') \
            or (n_completions >= max_completions) \
            or (n_tokens + max_tokens >= 2000)  # maximum token limit
    
    return completion.strip()


def search(documents, query, engine='davinci'):
    data = json.dumps({"documents": documents, "query": query})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % os.getenv('OPENAI_API_KEY'),
    }
    response = requests.post('https://api.openai.com/v1/engines/%s/search' % engine, headers=headers, data=data)
    result = json.loads(response.text)
    return result


def log(prompt, stops, completion, member2var, var2member, char2var, var2char, search_results, name):
    data = {
        'name': name,
        'prompt': prompt,
        'completion': completion,
        'stops': stops,
        'member2var': member2var, 
        'var2member': var2member, 
        'char2var': char2var, 
        'var2char': var2char
    }
#     if options_search:
#         data['options_search'] = [{'candidate': candidate, 'score': score}
#                                   for candidate, score in options_search]
    if search_results:
        data['search'] = [{'candidate': candidate, 'score': score}
                          for candidate, score in search_results]
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open('results/{}_{}.json'.format(timestamp, name), 'w') as outfile:
        json.dump(data, outfile)


def display_log(filename):
    with open(filename) as json_file:
        data = EasyDict(json.load(json_file))        
        print('=================================')
        print('Log: {}, bot: {}'.format(data.name, filename))
        print('=================================')
        print('Prompt:')
        print(data.prompt)
        print('------------------')
        print('Stops:')
        print(data.stops)
        print("=================================")
        print('Completion:')
        print(data.completion)
        print("=================================")
        print('Lookup tables:')
        print('member2var', data.member2var) 
        print('------------------')
        print('var2member', data.var2member) 
        print('------------------')
        print('char2var', data.char2var)
        print('------------------')
        print('var2char', data.var2char)
        print("=================================")


def run(settings, messages_new):

    # if requested, first run a query on candidate prompts to get most relevant one
    if 'messages_candidates' in settings and settings.messages_candidates:
        candidates = [mc[0]['message'] for mc in settings.messages_candidates]
        responses = [mc[1]['message'] for mc in settings.messages_candidates]

        sender = messages_new[-1].sender
        query = messages_new[-1].message

        result = search(candidates, query, engine='curie')

        scores = [doc['score'] for doc in result['data']]
        ranked_queries = list(reversed(np.argsort(scores)))
        search_results = [{'candidate': candidates[idx], 'score': scores[idx]} 
                          for idx in ranked_queries]
        
        for result in search_results:
            print(" -> %s : %0.2f" % (result['candidate'], result['score']))

        idx_top = ranked_queries[0]
        settings.messages_pre = [
            EasyDict({'sender': '<P1>', 'message': candidates[idx_top]}),
            EasyDict({'sender': '<S>', 'message': responses[idx_top]})
        ]
        
    else:
        search_results = None
 
    # lookup tables to convert variable names (<P1>, <S>) to character names and back
    characters = settings.characters if 'characters' in settings else default_characters
    random.shuffle(characters)
    num_speakers = len(set([k.sender for k in settings.messages_pre if '<P' in k.sender]))
    characters *= int(1+num_speakers/len(characters))
    var2char = {'<P{}>'.format(c+1): character for c, character in enumerate(characters)}
    var2char['<S>'] = settings.name
    char2var = {v: k for k, v in var2char.items()}

    # erase beginning mention of account if requested
    if settings.erase_mentions:
        for m in messages_new:
            m.message = re.sub('^<S>,?[ ]?', '', m.message).strip()

    # introduction
    prompt  = settings.intro if 'intro' in settings and settings.intro else ''
    prompt += '\n\n' if prompt != '' else ''

    # pre-written messages + discord buffer
    for msg in settings.messages_pre + messages_new:
        if not msg.message or msg.message.isspace():
            continue            
        prompt += '\n' * settings.formatting.line_breaks_before_sender
        prompt += '{}:'.format(msg.sender)
        prompt += ' ' if settings.formatting.line_breaks_after_sender==0 else ''
        prompt += '\n' * settings.formatting.line_breaks_after_sender
        prompt += '{}'.format(msg.message.strip())
    
    # append speaker name at end
    prompt += '\n' * settings.formatting.line_breaks_before_sender
    prompt += '<S>:'

    # post-processing
    prompt  = re.sub(' +', ' ', prompt)  # remove double spaces
    prompt  = re.sub(',+', ',', prompt)  # remove double commas

    # convert variable names (<P1>, <S>, etc) to character names
    prompt = re.sub('({})'.format('|'.join(var2char.keys())),
                    lambda m: var2char[m.group(1)], 
                    prompt).strip()
    
    # stop sequences
    stops  = ['\n{}:'.format(c) for c in characters[:3]]
    stops += ['\n'] if settings.formatting.stop_at_line_break else []

    # call GPT-3 complete
    completion = complete(
        prompt = prompt, 
        stops = stops, 
        max_tokens = settings.max_tokens, 
        temperature = settings.temperature, 
        engine = settings.engine,
        max_completions = settings.max_completions if 'max_completions' in settings else 1)

    # convert character names back to variable names
    completion = re.sub('({})'.format('|'.join(char2var.keys())),
                        lambda m: char2var[m.group(1)], 
                        completion).strip()

    return prompt, stops, completion, char2var, var2char, search_results
