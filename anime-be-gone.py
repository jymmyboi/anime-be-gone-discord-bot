#anime-be-gone.py v1.0
import discord

TOKEN = 'XXXXXXXX'

class anime_gone(discord.Client):
    async def on_ready(self):
        print('logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if 'anime' in message.content.lower():
            await message.channel.send('Be gone heretic! ')
            await message.channel.send('https://i.redd.it/tpbxinqo1iu11.jpg')


client = anime_gone()
client.run(TOKEN)

