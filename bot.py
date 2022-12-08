import strings
import user_data
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

TOKEN = "5734000549:AAGpBRn_T4fOGkINM1yAPl1kjscsg2UdiAc"
bot = telebot.TeleBot(TOKEN)

user_data = user_data.UserData()


def start_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    studio_button = types.KeyboardButton(strings.rooms[0])
    one_button = types.KeyboardButton(strings.rooms[1])
    two_button = types.KeyboardButton(strings.rooms[2])
    three_button = types.KeyboardButton(strings.rooms[3])
    markup.row(studio_button, one_button)
    markup.row(two_button, three_button)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, strings.hello_message, reply_markup=start_markup())


@bot.message_handler(content_types=['text'])
def get_user_message(message):
    chat = message.chat.id
    text = message.text.strip()
    if text in strings.rooms:
        if text == strings.rooms[0]:
            user_data.set_rooms(0)
        elif text == strings.rooms[1]:
            user_data.set_rooms(1)
        elif text == strings.rooms[2]:
            user_data.set_rooms(2)
        elif text == strings.rooms[3]:
            user_data.set_rooms(3)
        bot.send_message(chat, strings.max_price_question, reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_max_price)


def get_max_price(message):
    chat = message.chat.id
    text = message.text.strip()
    try:
        price = int(text)
        user_data.set_max_price(price)
        bot.send_message(chat, "Ура")
    except ValueError:
        bot.send_message(chat, strings.try_again)
        bot.register_next_step_handler(message, get_max_price)


bot.polling(none_stop=True)
