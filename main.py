import os
import discord
import openai
openai.api_key = os.environ['openai_token']
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'hello world! {client.user} are online.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'{message.author}: {message.content}')
      
    if message.content.startswith('ping'):
        await message.channel.send("pong! i'm here :)")

    if message.content.startswith('draw'):
        try:
            response = openai.Image.create(
            prompt=message.content[7:],
            n=1,
            size="1024x1024"
            )     
            image_url = response['data'][0]['url']
    
            await message.channel.send(image_url)     
        except Exception as e:
            await message.channel.send('error :(')

client.run(os.environ['europa_token'])
