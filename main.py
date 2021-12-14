# bot.py
import os

import chart_studio
import chart_studio.plotly as py
from discord.ext import commands
from dotenv import load_dotenv

import discord
from graph1 import *
from graph2 import *
from graph3 import *


#chart_studio log in
username = "Yihan_Zhong" # your username
api_key = 'YgrFLCNEv3Q7bA0qrMlK' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
'''
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
'''

bot = commands.Bot(command_prefix='$')

@bot.command(name='map_country_happiness', help='This command responds to the happiness level of each country on the map.')
async def indicator(ctx):
    filename=Average_score_regional ()
    image = discord.File(filename)
    await ctx.send(file = image)

@bot.command(name='life_expectancy', help='This command shows the different happiness level in a bar chat with its different indicator component grouped by region.')
async def expectancy(ctx):
    url=world_happiness_map ()
    await ctx.send(url)

@bot.command(name='pie_mean_happiness', help='This command takes regional indicator as parameter and returns the mean life expectancy rate per region.')
async def bar (ctx):
    await ctx.send('Choose a region from { Western_Europe , Latin_America_and_Caribbean, Central_and_Eastern_Europe, North_America_and_ANZ, East_Asia, Middle_East_and_North_Africa}')
    message_response = await bot.wait_for('message')
    region=message_response.content
    url=life_expetency_regional(region)
    await ctx.send(url)

bot.run(TOKEN)
