#anime-be-gone.py v2.0
import discord
from bs4 import BeautifulSoup
import requests
from urlextract import URLExtract

TOKEN = 'XXXXXXXXX'

class anime_gone(discord.Client):
    async def on_ready(self):
        print('logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if 'anime' in message.content.lower():
            await message.delete()
            await message.channel.send(f'{message.author.mention} said the bad word! Be gone heretic! ')
            await message.channel.send('https://i.redd.it/tpbxinqo1iu11.jpg')
            print(f"{message.author}")
        
        elif '.com' in message.content.lower():
            rawText = message.content

            extractor = URLExtract()
            extraction = extractor.find_urls(rawText)
            url = ''.join(extraction)
            r = requests.get(url)
            html_content = r.text

            soup = BeautifulSoup(html_content, 'lxml')

            if 'anime' in soup.title.string.lower():
                await message.delete()
                await message.channel.send(f'{message.author.mention} said the bad word! Be gone heretic! ')
                await message.channel.send('https://i.redd.it/tpbxinqo1iu11.jpg')
                print(f"{message.author}")
            else:
                print(f"{message.author} did not post anime here")

client = anime_gone()
client.run(TOKEN)
