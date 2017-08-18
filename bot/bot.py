#!python3.5

# Discord.py
import discord
from discord.ext import commands
# Allows us to use terminal commands
import subprocess

client = discord.Client()

token = input('Discord token: ')

print('Logging in...')

bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):

    # Tip
    @bot.command()
    async def tip(user, currency, amount):
        await bot.say('''tip''')

    # Withdraw
    @bot.command()
    async def withdraw(input):
        await bot.say('''withdraw''')

    # Deposit
    @bot.command()
    async def deposit(currency : str, amount : int, user):
        await bot.say('''deposit''')
        #test print, remove when done
        print(currency + amount + user)
        if currency == 'bitcoin':
            await bot.say('bitcoin deposit')

    # Balance
    @bot.command()
    async def balance():
        await bot.say('''balance''')

    # About
    @bot.command()
    async def tipabout():
        await bot.say('''Tip Bot: a bot made by Dizee
        Get the code here: https://github.com/Dizeeee/tipbot
        This project is licensed under the MIT License. Feel free to share and modify it as you please!''')

    # Help
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
