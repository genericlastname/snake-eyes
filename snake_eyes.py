#!/usr/bin/env python

'''This script provides a DnD dice rolling discord bot.'''

import os
import random
import discord
from discord.ext import commands

CLIENT = discord.Client()
TOKEN = os.environ['SNAKE_EYES_TOKEN']
BOT = commands.Bot(command_prefix='!')
random.seed()


@BOT.command()
async def roll(ctx, *args):
    '''Rolls the dice.'''
    # if argument is a valid die
    if args[0][0] == 'd':
        faces = int(args[0][1:])
        if faces > 20:
            await ctx.send('Please make sure your number is between d1-20.\nThat means you *Ryan*')
            return
        value = 0

        if faces != 00:
            # normal dice
            value = random.randint(1, faces)
        else:
            # percentile die
            value = random.randint(1, 10) * 10

        output = ''
        if faces == 20:
            # add pithy comments for critical success and failure
            if value == 20:
                output = '**Critical success!** A natural **20**!'
                print(output)
            elif value == 1:
                output = '**Critical failure!** You rolled a **1**!'
            else:
                output = f'You rolled a...\n**{value}**'

        else:
            output = f'You rolled a...\n**{value}**'

        print(output)
        await ctx.send(output)
    else:
        await ctx.send(
            '''Please format the command as !roll d{whatever}
            *Example:* !roll d20'''
        )


BOT.run(TOKEN)
