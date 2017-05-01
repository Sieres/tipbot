import discord

client = discord.Client()
token = input('Token: ')

@client.event
async def on_message(message):
    # keep the bot from replying to itself
    if message.author == client.user:
        return

    # command sheet
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!status'):
        await client.change_presence(game=discord.Game(name="Just testing stuff"))
    if message.content.startswith('!doot'):
        await client.change_presence(game=discord.Game(name="doot"))

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('-----------------------------')

    # startup stuff
    await client.change_presence(game=discord.Game(name="Starting..."))
    await client.change_presence(game=discord.Game(name="!help"))


client.run(token)
