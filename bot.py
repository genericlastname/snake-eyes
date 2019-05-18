import discord
from discord.ext import commands
import random

client = discord.Client()
TOKEN = 'NTc5MDg2Njg4Nzc3Nzk3NjQy.XN9EBw.AY3vl4svrZc_LPkglMkr3ohiJz8'
bot = commands.Bot(command_prefix='!')

@bot.command()
async def roll(ctx, *args):
    # if argument is a valid die
    if args[0][0] == 'd':
        faces = int(args[0][1:])
        value = 0
        
        random.seed()
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
                output = 'Critical success! A natural 20!'
                print(output)
            elif value == 1:
                output = 'Critical failure! You rolled a 1!'
            else:
                output = f'You rolled a...\n**{value}**'

        else:
            output = f'You rolled a...\n**{value}**'

        print(output)
        await ctx.send(output)


bot.run(TOKEN)
