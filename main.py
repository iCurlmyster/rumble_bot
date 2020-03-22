import os
import sys
import logging

from discord.ext import commands
from dotenv import load_dotenv

# load in variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# import this after so load_dotenv pulls in environment variables for db.py
from rumble import rumble
from player import get_player, increase_health, player_summary

bot = commands.Bot(command_prefix='!')

def error_msg():
    """
    error_msg grabs the top error, logs it out, and returns a generic error message for the user.
    """
    e = sys.exc_info()[0]
    logging.error(e)
    return "Oops! Sorry, an error occurred!"

@bot.event
async def on_ready():
    logging.info(f'{bot.user} has connected to Discord!')

def start_rumble(ctx, player):
    """
    start_rumble handles the getting the players and simulating the rumble.
    """
    p1 = get_player(ctx.author.id, ctx.author.name)
    member = ctx.guild.get_member_named(player)
    if member == None:
        return f"{player} is not someone you can fight here."
    p2 = get_player(member.id, member.name)
    return rumble(p1, p2)

@bot.command(name="rumble", help="Fight another user in a simulated rumble")
async def fight(ctx, player=None):
    message = ""
    try:
        if player == None:
            message = "You can't fight alone! Tell me who you want to fight."
        else:
            message = start_rumble(ctx, player)
    except:
        message = error_msg()
    finally:
        await ctx.send(message)

@bot.command(name="lift", help="Workout to try and increase your strength")
async def lift(ctx):
    message = ""
    try:
        message = increase_health(ctx.author.id, ctx.author.name)
    except:
        message = error_msg()
    finally:
        await ctx.send(message)

@bot.command(name="rumble_info", help="Stat summary of the user calling the command or the user given")
async def info(ctx, p1=None):
    message = ""
    try:
        if p1 != None:
            member = ctx.guild.get_member_named(p1)
            if member == None:
                message = f"{p1} has no Rumble info here."
            else:
                message = player_summary(member.id, member.name)
        else:
            message = player_summary(ctx.author.id, ctx.author.name)
    except:
        message = error_msg()
    finally:
        await ctx.send(message)

@bot.command(name="rumble_src", help="Display the github.com repo for this bot")
async def display_info(ctx):
    await ctx.send("This bots code can be found here -> https://github.com/iCurlmyster/rumble_bot")

bot.run(TOKEN)
