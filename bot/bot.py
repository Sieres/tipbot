import discord

client = discord.Client()

# set bot login token
token = input('Token: ')
print('Logging in...')

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
    if message.content.startswith('!helptip'):
        msg = '''`!tip (username) (currency) (amount)` - Tip a user
        `!deposit (currency)` - Generate a wallet address to deposit currency in
        `!withdraw (address) (currency) (amount)` - withdraw currency
        `!balance` - Displays balance'''.format(message)
    if message.content.startswith('!withdraw'):
        # request address to send to
        msg = ''.format(message)
    if message.content.startswith('!deposit'):
        # generate address and wait for confirmed transfer
        msg = '''Deposit address: insert address here
        *This address will be valid for 15 minutes or until all transactions are verified*'''.format(message)
    if message.content.startswith('!tip'):
        # do tip stuff
        msg = 'Tip sent successfully'.format(message)
    if message.content.startswith('!balance'):
        # call balance info
        msg = 'Balance'.format(message)


@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('-----------------------------')

    # startup stuff
    await client.change_presence(game=discord.Game(name="Starting..."))
    await client.change_presence(game=discord.Game(name="!help"))


client.run(token)
