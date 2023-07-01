import telebot
from telebot import types

token = '6041366947:AAElH-b5ett6DhyDkULQJbFWwQC4Ot_9ly8'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здраствуйте, вас приветствует личный бот компании e-market, чем могу помочь?')


# @bot.message_handler(func=lambda message: True)
# def echo(message):
# bot.send_message(message.chat.id, message.text)


# def run_bot():
bot.polling()
