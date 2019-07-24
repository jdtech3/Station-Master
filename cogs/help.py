# SPDX-License-Identifier: MIT
#
# help.py - includes .help
#
# Copyright (c) 2019 Joe Dai.

import discord
from discord.ext import commands


class HelpCog:
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    # .help
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""```css
[ Command List ]

- Use .help [command] for details -

.help         :: Displays this message.
.ping         :: Ping/pong, pretty self-explanatory.
.pong         :: Needs no description :P

.listings get        :: Returns listings in a given category
.listings add        :: Adds listing to a given category
.listings remove     :: Removes a listing
.listings categories :: All possible categories
```
""")


def setup(bot):
    bot.add_cog(HelpCog(bot))
