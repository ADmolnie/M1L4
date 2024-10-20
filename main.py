import telebot 
from config import token
from logic import Pokemon
import time
feeding = 100

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['go'])
def go(message):
    global feeding
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
    feeding -= 10

@bot.message_handler(commands=['feed'])
def feed(message):
    global feeding
    if feeding < 100:
        bot.reply_to(message, "Ням Ням Ням")
        feeding = (100 - feeding) + feeding + 10
    else:
        bot.reply_to(message, "Я сытый")
    feeding -= 10
    bot.reply_to(message, feeding)
    

bot.infinity_polling(none_stop=True)

