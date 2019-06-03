import telebot
from telebot import types

bot= telebot.TeleBot("864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw")

dict_chat = {}

key = {
    1:"Вопрос 1",
    2:"Вопрос 2",
    3:"Вопрос 3",
    4:"Вопрос 4",
    5:"Вопрос 5"
}

question = {
    1:"Какого цвета учебник?",
    2:"Как называется предмет?",
    3:"Как тебя зовут?",
    4:"Как зовут твою маму?",
    5:"В какой стране ты живешь?"
}

reply = {
    1:"чорний",
    2:"украинский",
    3:"маркел",
    4:"лиза",
    5:"украина"
}

def game_start(messege):
    if message.chat.id not in dict_chat:
        dict_chat[message.chat.id] = [0,0,0]

def game_continue(message):
    keyboard = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text=key[1], callback_data=1)
    call2 = types.InlineKeyboardButton(text=key[2], callback_data=2)
    call3 = types.InlineKeyboardButton(text=key[3],callback_data=3)
    call4 = types.InlineKeyboardButton(text=key[4], callback_data=4)
    call5 = types.InlineKeyboardButton(text=key[5], callback_data=5)
    keyboard.row(call1, call2, call3, call4, call5)
    bot.send_message(message.chat.id,"Продолжим игру",reply_markup=keyboard)

@bot.message_handler(commands=['game'])
def game(message):
    keyboard = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text=key[1], callback_data=1)
    call2 = types.InlineKeyboardButton(text=key[2], callback_data=2)
    call3 = types.InlineKeyboardButton(text=key[3], callback_data=3)
    call4 = types.InlineKeyboardButton(text=key[4], callback_data=4)
    call5 = types.InlineKeyboardButton(text=key[5], callback_data=5)
    keyboard.row(call1, call2, call3, call4, call5)
    bot.send_message(message.chat.id,"Начнем игру",reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: call.data=="1")
def call_back_request(call):
        n = int(call.data)
        answer = bot.send_message(call.message.chat.id, question[n] )
        bot.register_next_step_handler(answer, go_answer1)

@bot.callback_query_handler(func = lambda call: call.data=="2")
def call_back_request(call):
        n = int(call.data)
        answer = bot.send_message(call.message.chat.id, question[n])
        bot.register_next_step_handler(answer, go_answer2)

@bot.callback_query_handler(func = lambda call: call.data=="3")
def call_back_request(call):
       n = int(call.data)
       answer = bot.send_message(call.message.chat.id, question[n])
       bot.register_next_step_handler(answer, go_answer3)

@bot.callback_query_handler(func = lambda call: call.data=="4")
def call_back_request(call):
       n = int(call.data)
       answer = bot.send_message(call.message.chat.id, question[n])
       bot.register_next_step_handler(answer, go_answer4)

@bot.callback_query_handler(func = lambda call: call.data=="5")
def call_back_request(call):
       n = int(call.data)
       answer = bot.send_message(call.message.chat.id, question[n])
       bot.register_next_step_handler(answer, go_answer5)


def go_answer1(answer):
    if answer.text.lower() == reply[1]:
        text = "Неплохо"
    else:
        text = "Вы даже книгу не открывали!!!"
    bot.send_message(answer.chat.id,text)
    game_continue(answer)

def go_answer2(answer):
    if answer.text.lower() == reply[2]:
        text = "Хорошо"
    else:
        text = "Ты в школу ходил???"
    bot.send_message(answer.chat.id,text)
    game_continue(answer)

def go_answer3(answer):
    if answer.text.lower() == reply[3]:
        text = "Отлично"
    else:
        text = "Ты не знаешь своего имени???"
    bot.send_message(answer.chat.id,text)
    game_continue(answer)

def go_answer4(answer):
    if answer.text.lower() == reply[4]:
        text = "Круто"
    else:
        text = "Ты маму знаешь???"
    bot.send_message(answer.chat.id,text)
    game_continue(answer)


def go_answer5(answer):
    if answer.text.lower() == reply[5]:
        text = "Супер"
    else:
        text = "Какая-какая ты чего???"
    bot.send_message(answer.chat.id,text)
    game_continue(answer)

@bot.message_handler(content_types=['text'])
def f(message):
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Привет, {0}".format(message.from_user.first_name))


if name == 'main':
    bot.polling(none_stop=True)