import discord
from discord.ext import commands
import datetime

client = discord.Client()
TOKEN = 'NTc3OTU2ODM5NzYxNjQxNDky.XNsy-g.dvstEBH_6tIC0i-1NkIaBZU0Gk0'
bot = commands.Bot(command_prefix='!')

# deadlines = []

# @bot.command()
# async def upcoming(ctx):
#     for d in deadlines:
#         await ctx.send(d.info())

# @bot.command()
# async def deadline(ctx, name, date_str, time_str, ampm):
#     combined = f'{date_str} {time_str} {ampm.upper()}'
#     print(combined)
#     dt = datetime.datetime.strptime(combined, '%Y-%m-%d %I:%M %p')
#     deadlines.append(Deadline(name, dt))
#     await ctx.send(f'Adding {name} to calender')

# @bot.command()
# async def delete_deadline(ctx, name):
#     results = []
#     for d in deadlines:
#         if d.name != name:
#             results.append(d)

#     deadlines = results
#     await ctx.send(f'Deleted deadline {name}')


bot.run(TOKEN)

