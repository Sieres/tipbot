import discord
from block_io import BlockIo
#I'm throwing in subprocess just in case
import subprocess

client = discord.Client()

token = input('Discord token: ')
blockkeyb = input('Block.io Bitcoin key: ')
blockkeyd = input('Block.io Dogecoin key: ')

print('Logging in...')

bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):

@bot.command()
async def tip(user, currency, amount):
    await bot.say('''tip''' + user + currency +amount)

@bot.command()
async def withdraw(input):
    await bot.say('''withdraw''')

@bot.command()
async def deposit(currency : str):
    await bot.say('''deposit''')
    if currency == 'bitcoin':
        await bot.say('bitcoin deposit')
        #block.io stuff
    elif currency == 'dogecoin':
        await bot.say('bitcoin deposit')
        #block.io stuff
@bot.command()
async def balance():
    await bot.say('''balance''')

@bot.command()
async def tipabout():
    await bot.say('''Tip Bot: a bot made by Dizee
    Get the code here: https://github.com/Dizeeee/tipbot
    This project is licensed under the MIT License. Feel free to share and modify it as you please!''')

@bot.command()
async def tiphelp():
    await bot.say('''```Commands:
    !tip (currency) (amount) (@user)
    !withdraw (currency) (amount) (adress)
    !deposit (currency)
    !balance
    !tiphelp
    !tipabout```''')

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('-----------------------------')

    await client.change_presence(game=discord.Game(name="Starting..."))
    #load database stuff and maybe connect to wallet
    await client.change_presence(game=discord.Game(name="!tiphelp"))


client.run(token)
