from easydict import EasyDict
import asyncio
import gpt3


async def run(settings, 
              message,
              program_idx):

    settings = [settings] if not isinstance(settings, list) else settings
    settings = settings[program_idx]
    
    response = gpt3.complete(
        settings.prompt, 
        stops=settings.stops if 'stops' in settings else None, 
        max_tokens=settings.max_tokens if 'max_tokens' in settings else 50, 
        temperature=settings.temperature if 'temperature' in settings else 0.9, 
        engine=settings.engine if 'engine' in settings else 'davinci',
        max_completions=3)
    
    if 'preface' in settings:
        response = settings.preface + response
        
    return response

