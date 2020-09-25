import os
import random
import time
import discord
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
SELF_ID = int(os.getenv('SELF_ID'))
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY
client = discord.Client()
message_buffer = []
members = {}


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    for member in guild.members:
    	members[member.id] = member.name
    members[SELF_ID] = 'Chatsubot'


@client.event
async def on_message(message):
	global message_buffer, members
	msg = [message.author, message.content]
	message_buffer.append(msg)
	message_buffer = message_buffer[-6:]
	if message.author == client.user:
		return

	if str(SELF_ID) not in message.content:
		return

	prompt = 'The following is a conversation with a chatbot named Chatsubot. The chatbot is kind, patient, and very knowledgeable about philosophy of mind.\n\n'
	prompt += '<Human>: Chatsubot, what do you think about the mind-body problem?\n'
	prompt += '<Chatsubot>: I would say that phenomenological consciousness is an introspective illusion.\n'

	for author, content in message_buffer:
		author_name = 'Human' if int(author.id) != SELF_ID else 'Chatsubot'
		for member_id in members.keys():
			content = content.replace('<@!%s>'%str(member_id), members[member_id])
			content = content.replace('<@%s>'%str(member_id), members[member_id])
		prompt += '<%s>: %s\n'%(author_name, content)
	prompt += '<Chatsubot>:'

	stops = ['\n', '\n<Human>:', '<Human>:']

	idx_try += 1
	response = openai.Completion.create(
		engine="davinci", 
		prompt=prompt, 
		max_tokens=100, 
		temperature=0.9,
		top_p=1.0,
		presence_penalty=0.2,
		stop=stops)
	print(response)
	text = response.choices[0].text
	
	if text=='':
		return
	
	text = text.replace('\n<Chatsubot>: ', '\n')

	await message.channel.send(text)
	time.sleep(2)




client.run(TOKEN)
