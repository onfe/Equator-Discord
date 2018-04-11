import discord
from discord.ext import commands

import logging

log = logging.getLogger(__name__)

import re

keywords = {
    '[equil]': '⇌',
    '[to]': '→'
}

class Equation():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def equation(self, ctx, *args):
        inp = ' '.join(args)

        # replace keywords with their special symbols.
        for word, replace in keywords.items():
            inp = inp.replace(word, replace)

        await ctx.send(inp)

def setup(bot):
    bot.add_cog(Equation(bot))
