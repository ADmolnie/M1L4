import telebot 
from random import randint
from config import token
from logic import Pokemon
from logic import Wizard
from logic import Fighter


feeding = 100


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['go'])
def start(message):
    global feeding
    feeding -= 10
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['feed'])
def feed(message):
    global feeding
    feeding -= 10
    if feeding < 100:
        bot.reply_to(message, "Ням Ням Ням")
        feeding = (100 - feeding) + feeding + 10
    else:
        bot.reply_to(message, "Я сытый")
    bot.reply_to(message, feeding)


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    global feeding
    feeding -= 10
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")
    

@bot.message_handler(commands=['info'])
def attack_pok(message):
    global feeding
    feeding -= 10
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
        bot.send_photo(message.chat.id, pok.show_img())
    else:
        bot.reply_to(message, "Ты ещё не создал себе покемона")

bot.infinity_polling(none_stop=True)

