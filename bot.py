
import discord
from discord.ext import commands
import asyncio
import time
import math
import os

bot = commands.Bot(command_prefix = ["n!", "n1", "b2", "n2", "N!", "N1", "B2", "N2"] , description = "A super trivia bot that tries not to suck too much.")
@bot.command()
async def say(ctx, *, something = None):
	"""Prints the given string."""
	if something is not None:
		await ctx.send(something)
	else:
		await ctx.send("lol you're pretty bad at this, use the *say* command with argument, such as: **n!say ooglyoogly**")
    

@bot.event
async def on_ready():
	print("I am running on " + bot.user.name)
	print("With the ID: " + str(bot.user.id))

	await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = "David stuck in Plat. [n!]"))



bot.run(str(os.environ.get("BOT_TOKEN")))
