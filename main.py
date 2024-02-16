import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''The duck command returns the photo of the duck'''
    print('hello')
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def hello(ctx):
    await ctx.send(f'hi i am discord bot {bot.user}!')

#final exam command
@bot.command()
async def greeting(ctx):
    await ctx.send("\n greetings everyone, and welcome to my final project, today we are learning about season what is season you may asked?")
    await ctx.send("\n well type: $whats_season")

@bot.command()
async def whats_season(ctx):
    await ctx.send("\n A season is a period of the year that is distinguished by special climate conditions. The four seasons—spring, summer, fall, and winter—follow one another regularly. Each has its own light, temperature, and weather patterns that repeat yearly.")
    await ctx.send("\n oh ya place an image of season: fall, rain, winter, summer and type $check")

@bot.command()
async def whats_fall(ctx):
    await ctx.send("autumn, season of the year between summer and winter during which temperatures gradually decrease. It is often called fall in the United States because leaves fall from the trees at that time")
    await ctx.send("now try rain and type: $check")

@bot.command()
async def whats_rain(ctx):
    await ctx.send("The wet season (sometimes called the rainy season or monsoon season) is the time of year when most of a region's average annual rainfall occurs. Generally, the season lasts at least one month")
    await ctx.send("now try summer and type $check")

@bot.command()
async def whats_summer(ctx):
    await ctx.send("Summer is the hottest and brightest of the four temperate seasons, occurring after spring and before autumn. At or centred on the summer solstice, daylight hours are longest and darkness hours are shortest, with day length decreasing as the season progresses after the solstice")
    await ctx.send("now the final, try winter and type: $check")
@bot.command()
async def whats_winter(ctx):
    await ctx.send("Winter is the coldest and darkest season of the year in polar and temperate climates. It occurs after autumn and before spring. The tilt of Earth's axis causes seasons; winter occurs when a hemisphere is oriented away from the Sun. Different cultures define different dates as the start of winter, and some use a definition based on weather.")
    await ctx.send("ok that's for this final project THANK YOU!")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
            
    else:
        await ctx.send("you forget to attach the image :(")

bot.run("MTEyNzUwOTQ0Mjg5MjY2MDc3Ng.GiNN52.5s4TYNX6VVgmDKz_MRn2kHeDnnH1QL0VtA2aQA")