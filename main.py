<<<<<<< HEAD
import telebot
import constants
import re

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['help'])
def help(mess):
	bot.send_message(mess.chat.id, 'Я бот Лёхи')

bad_words = constants.bad_words

@bot.message_handler(content_types=['text'])
def gl(mess):
	message = filter(None, re.split("[, \-!?:]+", mess.text))
	for i in message:
		if i.lower() in bad_words:
			bot.delete_message(mess.chat.id, mess.message_id)
	#else:
	#	if mess.text.lower() == 'a' or mess.text.lower() == 'а':
	#		if mess.text.lower() == 'а':
	#			bot.send_message(mess.chat.id, 'б')
	#	elif mess.text.lower() == 'b' or mess.text.lower() == 'б':
	#		bot.send_message(mess.chat.id, 'a')
	#	else:
	#		bot.send_message(mess.chat.id, 'Ты не умеешь играть в эту игру(')


if __name__ == '__main__':
=======
import telebot
import constants
import re

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['help'])
def help(mess):
	bot.send_message(mess.chat.id, 'Я бот Лёхи')

bad_words = constants.bad_words

@bot.message_handler(content_types=['text'])
def gl(mess):
	message = filter(None, re.split("[, \-!?:]+", mess.text))
	for i in message:
		if i.lower() in bad_words:
			bot.delete_message(mess.chat.id, mess.message_id)
	#else:
	#	if mess.text.lower() == 'a' or mess.text.lower() == 'а':
	#		if mess.text.lower() == 'а':
	#			bot.send_message(mess.chat.id, 'б')
	#	elif mess.text.lower() == 'b' or mess.text.lower() == 'б':
	#		bot.send_message(mess.chat.id, 'a')
	#	else:
	#		bot.send_message(mess.chat.id, 'Ты не умеешь играть в эту игру(')


if __name__ == '__main__':
>>>>>>> e9354c8b0f90fd56f7c86c2a7b64de6d835f69f5
	bot.polling(none_stop=True)