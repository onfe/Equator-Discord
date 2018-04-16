import discord
from discord.ext import commands

import logging

log = logging.getLogger(__name__)

import re

keywords = {
    '[equil]': '⇌',
    '[to]': '→'
}

superscriptDict = {
    '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵',
    '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰'
}

subscriptDict = {
    '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅',
    '6': '₆', '7': '₇', '8': '₈', '9': '₉', '0': '₀'
}



class Equation():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["eq","equ"])
    async def equation(self, ctx, *args):
        inp = ' '.join(args)

        # Replace sup() with superscript
        inp = self.regreplace(inp, '(sup\([\d]+\))', superscriptDict)

        # Replace sup() with subscript
        inp = self.regreplace(inp, '(sub\([\d]+\))', subscriptDict)

        # replace keywords with their special symbols.
        for word, replace in keywords.items():
            inp = inp.replace(word, replace)

        await ctx.send(inp)

    def regreplace(self, inp, reg, rdict):
        r = re.compile(reg)

        results = r.finditer(inp)
        for result in results:
            match = result.group()[4:-1]
            for char in match:
                if char in rdict:
                    match = match.replace(char, rdict[char])
            inp = inp.replace(result.group(), match)
        return inp


def setup(bot):
    bot.add_cog(Equation(bot))
