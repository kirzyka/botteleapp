from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy
import telebot
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yxknmcxpzndojz:9be74bd43768c270c596eb2f8f37c053470ace1990948484a30874eed3ee1825@ec2-54-217-225-16.eu-west-1.compute.amazonaws.com:5432/d97vkrolk83d6e'
db = SQLAlchemy(app)

bot = telebot.TeleBot("864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw")

# Create our database model
class Story(db.Model):
    __tablename__ = "story"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), unique=True)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<description %r>' % self.description

@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Кнопка 1', 'Кнопка 2')
    user_markup.row('Большая кнопка')
    user_markup.row('Кнопа1', 'Кнопа2', 'Кнопа3')
    user_markup.row('Ещё кнопка 1', 'Ещё кнопка 2')
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)

@bot.message_handler(func=lambda mess: "два два" == mess.text, content_types=['text'])
def handle_text(message):
    reg = Story('два два')
    db.session.add(reg)
    db.session.commit()
    bot.send_message(message.chat.id, 'два')

@app.route('/' + "864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw", methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@app.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://botteleapp.herokuapp.com/' + "864277689:AAF12Kz_E-rUrEAy35i6gVKZC1c-nJ-tCUw")
    return "CONNECTED", 200

app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))