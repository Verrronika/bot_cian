import strings
import counters
from user_data import UserData
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

TOKEN = "5734000549:AAGpBRn_T4fOGkINM1yAPl1kjscsg2UdiAc"
bot = telebot.TeleBot(TOKEN)

user_data = UserData()


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


def okrug_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    szao = types.KeyboardButton(strings.okruga[0])
    sao = types.KeyboardButton(strings.okruga[1])
    svao = types.KeyboardButton(strings.okruga[2])
    zao = types.KeyboardButton(strings.okruga[3])
    cao = types.KeyboardButton(strings.okruga[4])
    vao = types.KeyboardButton(strings.okruga[5])
    uzao = types.KeyboardButton(strings.okruga[6])
    uao = types.KeyboardButton(strings.okruga[7])
    uvao = types.KeyboardButton(strings.okruga[8])
    markup.row(szao, sao, svao)
    markup.row(zao, cao, vao)
    markup.row(uzao, uao, uvao)
    return markup

def get_max_price(message):
    chat = message.chat.id
    text = message.text.strip()
    try:
        price = int(text)
        user_data.set_max_price(price)
        bot.send_message(chat, strings.orkug_question % price, reply_markup=okrug_markup())
        bot.send_photo(chat, open('images/orkuga.png', 'rb'))
        bot.register_next_step_handler(message, get_okrug)
    except ValueError:
        bot.send_message(chat, strings.try_again)
        bot.register_next_step_handler(message, get_max_price)


def get_okrug(message):
    chat = message.chat.id
    text = message.text.strip()
    user_data.set_okrug(text)
    bot.send_message(chat, strings.district_question % text, reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, get_distrcict)


def district_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    go_back = types.KeyboardButton(strings.go_back)
    count_credit = types.KeyboardButton(strings.count_credit)
    markup.row(go_back)
    markup.row(count_credit)
    return markup


def get_distrcict(message):
    chat = message.chat.id
    text = message.text.strip()
    user_data.set_district(text)
    # тут считаем цену
    bot.send_message(chat, "Тут будет итоговая цена", reply_markup=district_markup())
    bot.register_next_step_handler(message, count_or_back)


def count_or_back(message):
    chat = message.chat.id
    text = message.text.strip()
    if text == strings.go_back:
        global user_data
        user_data = UserData()
        bot.send_message(chat, strings.data_reset, reply_markup=start_markup())
        bot.register_next_step_handler(message, get_user_message)
    else:
        bot.send_message(chat, strings.salary, reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_salary)


def get_salary(message):
    chat = message.chat.id
    text = message.text.strip()
    try:
        salary = int(text)
        user_data.set_salary(salary)
        bot.send_message(chat, strings.first_payment)
        bot.register_next_step_handler(message, get_first_payment)
    except ValueError:
        bot.send_message(chat, strings.try_again)
        bot.register_next_step_handler(message, get_salary)


def get_first_payment(message):
    chat = message.chat.id
    text = message.text.strip()
    try:
        payment = int(text)
        user_data.set_first_payment(payment)
        time_to_pay = counters.count_credit(user_data)
        print(time_to_pay)
        bot.send_message(chat, strings.time_to_pay % (time_to_pay[0], time_to_pay[1]))
    except ValueError:
        bot.send_message(chat, strings.try_again)
        bot.register_next_step_handler(message, get_first_payment)


bot.polling(none_stop=True)
