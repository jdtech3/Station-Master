# SPDX-License-Identifier: MIT
#
# fun.py - includes .dog, .dogfact, .cat, .catfact
#
# Copyright (c) 2019 Joe Dai.

import discord
from discord.ext import commands

import aiohttp

from datetime import datetime       # for embeds


class FunCog:
    def __init__(self, bot):
        self.bot = bot

    # Get URLs and parse them as json
    @staticmethod
    async def get(url, session):
        async with session.get(url) as response:
            return await response.json(content_type=None)

    # .dog
    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            resp = await self.get("https://dog.ceo/api/breeds/image/random", session)
        img_link = resp['message']

        embed = discord.Embed(title="*Aww...*", colour=discord.Colour(0xf8e71c), timestamp=datetime.now())
        embed.set_image(url=img_link)
        embed.set_footer(text="daVinci | Provided by: https://dog.ceo/dog-api/", icon_url="http://icons.iconarchive.com/icons/google/noto-emoji-animals-nature/1024/22215-dog-icon.png")

        await ctx.send(embed=embed)

    # .dogfact
    @commands.command(name='dogfact')
    async def dog_fact(self, ctx):
        async with aiohttp.ClientSession() as session:
            resp = await self.get("https://some-random-api.ml/dogfact", session)

        fact = resp['fact']

        embed = discord.Embed(title="Dogfact!", colour=discord.Colour(0xf8e71c), description=fact, timestamp=datetime.now())
        embed.set_footer(text="daVinci | Provided by: https://some-random-api.ml/dogfact", icon_url="http://icons.iconarchive.com/icons/google/noto-emoji-animals-nature/1024/22215-dog-icon.png")
        await ctx.send(embed=embed)

    # .cat
    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            resp = await self.get("https://api.thecatapi.com/v1/images/search?mime_types=jpg,png", session)
        img_link = resp[0]['url']

        embed = discord.Embed(title="*Aww...*", colour=discord.Colour(0xf8e71c), timestamp=datetime.now())
        embed.set_image(url=img_link)
        embed.set_footer(text="daVinci | Provided by: https://thecatapi.com/", icon_url="http://icons.iconarchive.com/icons/sonya/swarm/256/Cat-icon.png")

        await ctx.send(embed=embed)

    # .catfact
    @commands.command(name='catfact')
    async def cat_fact(self, ctx):
        async with aiohttp.ClientSession() as session:
            resp = await self.get("https://catfact.ninja/fact", session)

        fact = resp['fact']

        embed = discord.Embed(title="Catfact!", colour=discord.Colour(0xf8e71c), description=fact, timestamp=datetime.now())
        embed.set_footer(text="daVinci | Provided by: https://catfact.ninja/fact", icon_url="http://icons.iconarchive.com/icons/sonya/swarm/256/Cat-icon.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FunCog(bot))
