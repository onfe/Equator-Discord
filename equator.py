#!/usr/bin/env python3

import logging
log = logging.getLogger()

import discord
from discord.ext import commands
import asyncio
import sys
import getopt

helpstr = 'equator.py -t <discord token>'
bot = commands.Bot(command_prefix=commands.when_mentioned_or('/'), description='Pretty-print equations for discord.')

def startup():
    setupLogs()

    token = getToken()
    print(token)

    bot.load_extension('cogs.equations')

    try:
        bot.run(token)
    except discord.errors.loginFailure:
        print('Login Failure. Check Token.')
        sys.exit(1)

def getToken():
    args = sys.argv[1:]

    try:
        opts, args = getopt.getopt(args, 't:')
    except getopt.GetoptError:
        print(helpstr)
    for opt, arg in opts:
        if opt == '-t':
            token = arg

    return token

def setupLogs():

    log.setLevel(logging.INFO)

    handler = logging.FileHandler(
        filename='Equator.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    log.addHandler(handler)

@bot.event
async def on_ready():
    log.info("Connected. Equator is Online.")
    log.debug("Logged in as: '{}' with ID '{}'".format(bot.user.name, bot.user.id))

if __name__ == '__main__':
    startup()
