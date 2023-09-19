import discord
import os

class SpeedtestClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = SpeedtestClient(intents=intents)
client.run(os.environ['SPEEDTEST_DISCORD_TOKEN'])
