import sys
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
    
    
    # fix this
    max_completions=1
    
    
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
            or n_tokens + max_tokens >= 1600
    
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



def log(prompt_str, completion, botname, search_results):
    text = ''
    if search_results:
        for candidate, score in search_results:
            text += ' -> %s : %0.2f\n' % (candidate, score)
        text += '\n\n======================\n\n'
    text += prompt_str
    text += '\n\n======================\n\n'
    text += completion        
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    with open("results/%s_%s.txt" % (timestamp, botname), "w") as f:
        f.write(text)


        
        
        
        
############################

# from https://github.com/openai/openai-python/blob/main/examples/semanticsearch/semanticsearch.py

# from typing import List


# logger = logging.getLogger()
# formatter = logging.Formatter("[%(asctime)s] [%(process)d] %(message)s")
# handler = logging.StreamHandler(sys.stderr)
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# DEFAULT_COND_LOGP_TEMPLATE = (
#     "<|endoftext|>{document}\n\n---\n\nThe above passage is related to: {query}"
# )
# SCORE_MULTIPLIER = 100.0


# class SearchScorer:
#     def __init__(
#         self, *, document, query, cond_logp_template=DEFAULT_COND_LOGP_TEMPLATE
#     ):
#         self.document = document
#         self.query = query
#         self.cond_logp_template = cond_logp_template
#         self.context = self.cond_logp_template.format(
#             document=self.document, query=self.query
#         )

#     def get_context(self):
#         return self.context

#     def get_score(self, choice) -> float:
#         assert choice.text == self.context
#         logprobs: List[float] = choice.logprobs.token_logprobs
#         text = choice.logprobs.tokens
#         text_len = sum(len(token) for token in text)
#         if text_len != len(self.context):
#             raise RuntimeError(
#                 f"text_len={text_len}, len(self.context)={len(self.context)}"
#             )
#         total_len = 0
#         last_used = len(text)
#         while total_len < len(self.query):
#             assert last_used > 0
#             total_len += len(text[last_used - 1])
#             last_used -= 1
#         max_len = len(self.context) - self.cond_logp_template.index("{document}")
#         assert total_len + len(self.document) <= max_len
#         logits: List[float] = logprobs[last_used:]
#         return sum(logits) / len(logits) * SCORE_MULTIPLIER


# def semantic_search(engine, query, documents):
#     # add empty document as baseline
#     scorers = [
#         SearchScorer(document=document, query=query) for document in [""] + documents
#     ]
#     completion = openai.Completion.create(
#         engine=engine,
#         prompt=[scorer.get_context() for scorer in scorers],
#         max_tokens=0,
#         logprobs=0,
#         echo=True,
#     )
#     # put the documents back in order so we can easily normalize by the empty document 0
#     data = sorted(completion.choices, key=lambda choice: choice.index)
#     assert len(scorers) == len(
#         data
#     ), f"len(scorers)={len(scorers)} len(data)={len(data)}"
#     scores = [scorer.get_score(choice) for scorer, choice in zip(scorers, data)]
#     # subtract score for empty document
#     scores = [score - scores[0] for score in scores][1:]
#     data = {
#         "object": "list",
#         "data": [
#             {
#                 "object": "search_result",
#                 "document": document_idx,
#                 "score": round(score, 3),
#             }
#             for document_idx, score in enumerate(scores)
#         ],
#         "model": completion.model,
#     }
#     return data

