import os
import discord
import openai

openai.api_key = os.environ['openai_token']
intents = discord.Intents.default()
intents.message_content = True

class Europa(discord.Client):
    async def on_ready(self):
        print(f'hello world! {self.user.name} are online.')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        print(f'{message.author}: {message.content}')

class Chatting(Europa):
    async def on_message(self, message):
        if message.content.startswith('ping'):
            await message.channel.send("pong! i'm here :)")

class DallE(Europa):
    async def on_message(self, message):
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

client = Europa(intents=intents)
client.run(os.environ['europa_token'])
