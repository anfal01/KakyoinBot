# TODO: replace filepaths as fp variable
# TODO: fix issue of directory locality

import discord
import random
import os
from random import randint
#import numpy as np
from discord.ext import commands

TOKEN = '' #token here

fp = 'images/'

#open and read the sources files
with open("jk_links.txt") as f:
    jk_sources = [line.split() for line in f]

with open("hearts.txt") as f:
    hearts = f.readlines()
hearts = [x.strip("\n") for x in hearts]

with open("gif.txt") as f:
    gif_list = f.readlines()
gif_list = [x.strip("\n") for x in gif_list]

# open pics txt
with open("pics.txt") as f:
    pic_list = f.readlines()
pic_list = [x.strip("\n") for x in pic_list]

#open and read the stories file, line by line
with open("randomStories.txt") as f:
    storydata = f.readlines()
storydata = [x.strip("\n") for x in storydata]

#open and read the stories file, line by line
with open("quotes.txt") as f:
    quotedata = f.readlines()
quotedata = [x.strip("\n") for x in quotedata]

#open and read the facts file, line by line
with open("randomFacts.txt") as f:
    factsdata = f.readlines()
factsdata = [x.strip("\n") for x in factsdata]

#open and read the s*x file, line by line
with open("haram.txt") as f:
    haramdata = f.readlines()
haramdata = [x.strip("\n") for x in haramdata]

#open and read the interact file, line by line
with open("interact.txt") as f:
    interactdata = f.readlines()
interactdata = [x.strip("\n") for x in interactdata]

jk_sourcesLen = len(jk_sources)
heartsLen = len(hearts)
gifLen = len(gif_list)
picLen = len(pic_list)
factsize = len(factsdata)
storysize = len(storydata)
quotesize = len(quotedata)
haramsize = len(haramdata)
interactsize = len(interactdata)

bot = commands.Bot(command_prefix = ['k.', 'K.'])
client = commands.Bot(command_prefix = ['k.', 'K.'])

@bot.event
async def on_ready():
    print("**************************")
    print("*\n*")
    print("Ready! Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("*\n*")
    print("**************************")
    print("Number of facts:", factsize)
    print("Number of stories:", storysize)
    print("Number of quotes:", quotesize)
    print("Number of interactions:", interactsize)
    print("**************************")

#facts
@bot.command(aliases = ['FACTS', 'fax', 'FAX', 'fact', 'FACT'])
async def facts(ctx):
    msg = random.choice(factsdata)
    await ctx.send(f'{msg}')

#story
@bot.command()
async def story(ctx):
    msg = random.choice(storydata)
    await ctx.send(msg)

#quote
@bot.command()
async def quote(ctx):
    msg = random.choice(quotedata)
    await ctx.send(msg)

#interact
@bot.command()
async def interact(ctx):
    msg = random.choice(interactdata)
    await ctx.send(f'{msg}')

#ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

#s*x
@bot.command(aliases = ['haram'])
async def sex(ctx):
    msg = random.choice(haramdata)
    await ctx.send(msg)

#YEAHHH
@bot.command(aliases = ['YEAH'])
async def yeah(ctx):
    picture = discord.File(fp + 'YEAH.gif')
    await ctx.send(file=(picture))

#vore
@bot.command(aliases = ['VORE'])
async def vore(ctx):
    picture = discord.File(fp + 'vore.jpg')
    await ctx.send(file=(picture))

#whore
@bot.command(aliases = ['WHORE', 'hor', 'HOR'])
async def whore(ctx):
    picture = discord.File(fp + 'videos/whore.mp4')
    await ctx.send(file=(picture))

#roxanne
@bot.command(aliases = ['ROXANNE'])
async def roxanne(ctx):
    picture = discord.File(fp + 'videos/roxanne.mp4')
    await ctx.send(file=(picture))

#orara
@bot.command(aliases = ['ORARA'])
async def orara(ctx):
    picture = discord.File(fp + 'videos/orara.mp4')
    await ctx.send(file=(picture))

#pics
@bot.command(aliases = ['SELFIE', 'pic', 'PICS', 'pics', 'PIC'])
async def selfie(ctx):
    #sending a discrod URL through files
    '''
    f = random.choice(os.listdir((fp + 'pics/')))
    picture = discord.File(fp + 'pics/' + f)
    await ctx.send(file=(picture))
    '''

    #sending a selfie through discord URL, with embedding
    '''
    f = random.randrange(picLen)

    embed = discord.Embed(
        color = discord.Color.green()
    )

    embed.set_image(url=pic_list[f])
    await ctx.send(embed=embed)
    '''

    #sending a selfie through discord URL, without embedding
    f = random.randrange(picLen)
    await ctx.send(f'{pic_list[f]}')
    
#gifs
@bot.command(aliases = ['GIFS', 'gifs', 'GIF'])
async def gif(ctx):
    f = random.randrange(gifLen)

    embed = discord.Embed(
        color = discord.Color.blue()
    )

    embed.set_image(url=gif_list[f])
    await ctx.send(embed=embed)

#heart
@bot.command(aliases = ['HEARTS', 'hearts', 'HEART'])
async def heart(ctx):
    '''
    f = random.randrange(heartsLen)

    embed = discord.Embed(
        color = discord.Color.red()
    )

    embed.set_image(url=hearts[f])
    await ctx.send(embed=embed)
    '''

    #sending a selfie through discord URL, without embedding
    f = random.randrange(heartsLen)
    await ctx.send(f'{hearts[f]}')

#jotakak
@bot.command(aliases = ['joka', 'jk', 'JK', 'JOTAKAK', 'JOKA'])
async def jotakak(ctx):
    f = random.randrange(jk_sourcesLen)

    embed = discord.Embed(
        description = 'Source: ' + jk_sources[f][1],
        color = discord.Color.red()
    )

    embed.set_image(url=jk_sources[f][0])
    
    await ctx.send(embed=embed)
    '''
    f = random.choice(os.listdir((fp + 'jotakak/')))
    picture = discord.File(fp + 'jotakak/' + f)
    await ctx.send(file=(picture))
    '''

#kinky
@bot.command(aliases = ['kink', 'KINK', 'KINKY'])
async def kinky(ctx):
    f = random.choice(os.listdir((fp + 'kinky/')))
    picture = discord.File(fp + 'kinky/' + f)
    await ctx.send(file=(picture))

#helloworld
@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

#8ball
@bot.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    _8ballAnswers = ["It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
    await ctx.send(f'{random.choice(_8ballAnswers)}')
 
#options for morning messages
morningsMsg = ['Good morning! Make sure you so do some stretches before starting your day!', 'Morning! Don\'t let others steal the fun of everything from you :heart:', 'Gm! Lovely day, isn\'t it?', 'Good morning! My favorite saying these days is \'Carpe Diem\', which means *Seize the day*', 'Is it though?']

nightMsg = ['Good night. Make sure you follow through with your evening routine. :blush:', 'Sleep is for the weak. Good night.', 'Good night gamer :sunglasses:']

#certain mentions
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.lower().startswith("polnareff"):
        msg = ":unamused:".format(message)
        await message.channel.send(msg)
    elif message.content.lower().startswith("jotaro"):
        msg = ":flushed:".format(message)
        await message.channel.send(msg)
    elif message.content.lower().startswith("good morning") or message.content.lower().startswith("gm"):
        msg = random.choice(morningsMsg)
        await message.channel.send(msg)
    elif message.content.lower().startswith("good night") or message.content.lower().startswith("gn"):
        msg = random.choice(nightMsg)
        await message.channel.send(msg)
    await bot.process_commands(message)

bot.run(TOKEN)
