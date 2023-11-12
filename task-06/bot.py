import os
import discord
from discord.ext import commands
from scrape import live_scrape,csv_scrape
os.environ['APP_ID'] = 'MTE2MzEyODE5ODk5MzgwOTQ1OA.GXvAWc.Q-XTtRBt7t0YWbbnuMQ6w2lYQUHtYt5S2S8QGk'
token = os.getenv('APP_ID')

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')
bot.remove_command('help')
@bot.command()
async def live(ctx):
    score=live_scrape()
    print(score)
    await ctx.send(score)
@bot.command()
async def generate(ctx):
    csv_scrape()
    with open('cricket_scores.csv', 'rb') as file:
        csv_file = discord.File(file, filename='cricket_scores.csv')
        await ctx.send(file=csv_file)
@bot.command()
async def help(ctx):
    await ctx.send("Heyy! \n**Type /livescore to recieve live match updates**\n**Type /generate to recieve a csv of all currently ongoing matches!!**\nHave a great day :)")
try:
    bot.run(token)
except Exception as e:
    print(f"An error occurred: {e}")


