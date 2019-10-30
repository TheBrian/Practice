import discord

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NjI3MDA5MzMyNDgzMDYzODA5.XY2Z9g.zhgkEUX41-I3XqqPo0MejMIkHjc')
