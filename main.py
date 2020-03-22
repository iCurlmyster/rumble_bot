import os

from discord.ext import commands
from dotenv import load_dotenv

from rumble import rumble
from player import Player

# load in variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="fight")
async def fight(ctx, player):
    message = ""
    p1 = Player(ctx.author.name)
    member = ctx.guild.get_member_named(player)
    if member != None:
        p2 = Player(member.name)
        message = rumble(p1, p2)
    else:
        message = f"{player} is not someone you can fight here."
    await ctx.send(message)

bot.run(TOKEN)
