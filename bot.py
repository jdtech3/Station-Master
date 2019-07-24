# SPDX-License-Identifier: MIT
#
# bot.py - init stuff, includes .version
#
# Copyright (c) 2019 Joe Dai.

import discord
from discord.ext import commands

__version__ = "1.0.0"

# Default enabled cogs
initial_cogs = ['cogs.admin', 'cogs.help', 'cogs.fun', 'cogs.tools', 'cogs.listings']

# Bot stuff
bot = commands.Bot(command_prefix='.')


# Disallow calling the bot in PMs
# TODO: Suppress CheckFailure exceptions
@bot.check
async def no_pm(ctx):
    if ctx.message.guild is None:
        embed = discord.Embed(title="Not allowed to use this command in PMs.", colour=discord.Colour(0xd0021b))
        await ctx.channel.send(embed=embed)
        return False
    else:
        return True


# .version
@bot.command()
async def version(ctx):
    embed = discord.Embed(title=f"*Discord Station*  **v{__version__}**", colour=discord.Colour(0xf8e71c))
    await ctx.send(embed=embed)


# Print some info
@bot.event
async def on_ready():
    print('---------------')
    print('Connected. Loading cogs...')
    print('---------------')

    # Try to load initial cogs
    for cog in initial_cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f'Failed to load extension {cog}. {e}')
        else:
            print(f'Loaded extension {cog}.')

    print('---------------')
    print('Logged in as: ')
    print(f'Username: {bot.user.name} | ID: {bot.user.id}')
    print(f'Discord version: {discord.__version__}')
    print(f'Bot version: {__version__}')
    print('---------------')

    await bot.change_presence(activity=discord.Game('.help | ~ made by JDTech ~'))


if __name__ == "__main__":
    from keys import TOKEN

    # Run the bot!
    bot.run(TOKEN)
