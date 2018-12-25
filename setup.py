import os
from flask import Flask, request
import constants
import telebot

TOKEN = constants.token
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
		bot.reply_to(message, message.text)


@server.route('/bot' + TOKEN, methods=['POST'])
def getMessage():
	print('started getMessage')
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200


@server.route("/")
def webhook():
	print('started webhook')
	bot.remove_webhook()
	bot.set_webhook(url='https://whtesting.herokuapp.com/' + TOKEN)
	return "!", 200


if __name__ == "__main__":
	server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 80)))
