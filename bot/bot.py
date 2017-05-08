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
async def tip(input):
    await bot.say('''tip''')

@bot.command()
async def withdraw(input):
    await bot.say('''withdraw''')

@bot.command()
async def deposit(input):
    await bot.say('''deposit''')
    if currency = bitcoin
        blockkeyb.get_new_address()
    if currency = dogecoin
        blockkeyd.get_new_address()
@bot.command()
async def balance(input):
    await bot.say('''balance''')

@bot.command()
async def tiphelp(input):
    await bot.say('''```I'll put commands as I add them
    !tip (currency) (amount) (@user)
    !withdraw (currency) (amount) (adress)
    !deposit
    !balance
    !tiphelp```''')

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('-----------------------------')

    await client.change_presence(game=discord.Game(name="Starting..."))
    #load database stuff and maybe connect to wallet
    await client.change_presence(game=discord.Game(name="!tiphelp"))


client.run(token)
