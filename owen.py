import bot_token
import bot_utils
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('do you listen to death grips?')

    if (message.content.find("the") > -1 and message.content.find("the") < message.content.find("store")):
        await message.channel.send('{}? is that that one death grips album?'.format(bot_utils.capture_store_string(message.content)))

client.run(bot_token.token)

