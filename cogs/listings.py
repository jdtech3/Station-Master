# SPDX-License-Identifier: MIT
#
# listings.py - includes .listings get / add / remove
#
# Copyright (c) 2019 Joe Dai.

import discord
from discord.ext import commands

from datetime import datetime               # for embeds

from listings.interface import *
from listings.listing import CATEGORIES


class ListingsCog:
    def __init__(self, bot):
        self.bot = bot

    # .listings command group
    @commands.group(aliases=['l'])
    async def listings(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="No operation given.",
                                  description="Usage: `.listings <get|add|remove|categories> [parameters]`",
                                  colour=discord.Colour(0xd0021b))
            await ctx.send(embed=embed)

    # .listings get - get listings
    @listings.command(aliases=['show'])
    async def get(self, ctx, category: str = None):
        if category in CATEGORIES:
            listings = get_listings(category)

            title = category.replace('_', ' ').title()  # for embed title

            # Setup embed
            embed = discord.Embed(title=title, description="⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯",
                                  colour=discord.Colour(0x50e3c2), timestamp=datetime.now())
            embed.set_footer(text="Last update:",
                             icon_url="https://icon-library.net//images/whistle-icon/whistle-icon-23.jpg")

            # Insert the listings
            for listing in listings:
                embed.add_field(name=listing.name, value=listing.url, inline=False)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="Invalid category given.",
                                  description="Usage: `.listings get <category>`",
                                  colour=discord.Colour(0xd0021b))
            await ctx.send(embed=embed)

    # .listings add - add listing
    @listings.command()
    async def add(self, ctx, category: str = None, name: str = None, url: str = None):
        if any([category, name, url]):      # check if any parameters are None
            name = name.replace('_', ' ')   # input spaces by inputting underscores

            listing = add_listing(name, url, category)

            # Confirmation message
            embed = discord.Embed(title=f'Added listing {listing.name}.', colour=discord.Colour(0x7ed321))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient parameters given.",
                                  description="Usage: `.listings add <category> <name> <url>",
                                  colour=discord.Colour(0xd0021b))
            await ctx.send(embed=embed)

    # .listings remove - remove listing
    @listings.command()
    async def remove(self, ctx, category: str = None, name: str = None, url: str = None):
        if any([category, name, url]):      # check if any parameters are None
            name = name.replace('_', ' ')   # input spaces by inputting underscores

            remove_listing(name, url, category)

            # Confirmation message
            embed = discord.Embed(title=f'Removed listing {name}.', colour=discord.Colour(0x7ed321))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient parameters given.",
                                  description="Usage: `.listings remove <category> <name> <url>",
                                  colour=discord.Colour(0xd0021b))
            await ctx.send(embed=embed)

    # .listings categories - show all possible categories
    @listings.command()
    async def categories(self, ctx):
        out = ['```diff']   # opening markdown

        for category in CATEGORIES:
            out.append(f'- {category}')

        out.append('```')   # closing markdown

        await ctx.send('\n'.join(out))


def setup(bot):
    bot.add_cog(ListingsCog(bot))