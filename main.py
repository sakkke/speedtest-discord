import discord
import os
import subprocess

class SpeedtestClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if (message.content == '/speedtest' or
            message.content == '!speedtest' or
            self.user.mentioned_in(message)):
            speedtest = subprocess.run(['speedtest'], capture_output=True, text=True)
            await message.channel.send(f'```\n{speedtest.stdout}\n```', silent=True)

intents = discord.Intents.default()
intents.message_content = True

client = SpeedtestClient(intents=intents)
client.run(os.environ['SPEEDTEST_DISCORD_TOKEN'])
