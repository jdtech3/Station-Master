# SPDX-License-Identifier: MIT
#
# tools.py - includes .ping / .pong
#
# Copyright (c) 2019 Joe Dai.

import discord
from discord.ext import commands


class ToolsCog:
    def __init__(self, bot):
        self.bot = bot

    # .ping
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = ":ping_pong: Pong!", description = f"*...took ~{round(self.bot.latency * 1000, 3)}ms*", colour = discord.Colour(0xf8e71c))
        await ctx.send(embed = embed)

    # .pong
    @commands.command()
    async def pong(self, ctx):
        embed = discord.Embed(title = ":ping_pong: Ping!", description = f"*...took ~{round(self.bot.latency * 1000, 3)}ms*", colour = discord.Colour(0xf8e71c))
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(ToolsCog(bot))
