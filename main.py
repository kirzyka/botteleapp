from flask import Flask, request
from reply_keyboard_markups import Keyboard
import telebot
import os

server = Flask(__name__)

bot = telebot.TeleBot("864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw")
keyboard = Keyboard(bot)

@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Кнопка 1', 'Кнопка 2')
    user_markup.row('Большая кнопка')
    user_markup.row('Кнопа1', 'Кнопа2', 'Кнопа3')
    user_markup.row('Ещё кнопка 1', 'Ещё кнопка 2')
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)

@bot.message_handler(commands=['grid'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', '.', '.', '0', '0', '0')
    user_markup.row('0', '0', '0', '0', '0', 'X', 'X', 'X', 'X', '0')
    user_markup.row('0', '0', '0', '0', '0', '0', '0', '0', '0', '0')
    bot.send_message(message.from_user.id, 'Поле боя:', reply_markup=user_markup)

@server.route('/' + "864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw", methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://botteleapp.herokuapp.com/' + "864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw")
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))