import os
import telebot
import requests
import json
import csv 

# TODO: 1.1 Get your evironment variables
os.environ['bot_id']='5633461619:AAEj08yNGL5cZwtJUj18sCp33H-9c8i-Xg0'
os.environ['your_key']='91da752c'


your_key = os.getenv('your_key')
bot_id = os.getenv('bot_id')

bot = telebot.TeleBot(bot_id)
fields=['Title', 'Year', 'Rating']

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    Movie_name=message.text.replace('/movie', "")
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    
  
    Movie=requests.get(f"http://www.omdbapi.com/?apikey={your_key}&t={Movie_name}")
    response=Movie.json()
    print(response)

    Poster=response['Poster']
    Title=response['Title']
    Year=response['Year']
    Rating=response['imdbRating']
    

    bot.send_photo(message.chat.id, Poster, f'Title: {Title}\n Year released :{Year}\n Rating: {Rating}')
    with open('Movie_details.csv','w')as cs:
        csvdata=csv.writer(cs)
        csvdata.writerow(fields)
        csvdata.writerow([Title, Year, Rating])

        
 
    
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    mov=open('Movie_details.csv','r')
              
    bot.send_document(message.chat.id,mov)
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
