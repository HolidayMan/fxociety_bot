import telebot
import constants
import re

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['start'])
def start(mess):
	bot.send_message(mess.chat.id, 'Привет! Я помогаю фильтровать маты в этом чате! \n Также у меня доступны такие команды: \n\
	/help; \n /petard. \n В планах добавить бомбу. Но то потом)')


@bot.message_handler(commands=['help'])
def help(mess):
	bot.send_message(mess.chat.id, 'Я бот Лёхи')

@bot.message_handler(commands=['petard'])
def petard(mess):
	i = 1
	while True:
		try:
			bot.delete_message(mess.chat.id, mess.message_id - i)
			bot.delete_message(mess.chat.id, mess.message_id)
			break
		except telebot.apihelper.ApiException:
			i+=1

bad_words = constants.bad_words
bad_words1 = constants.bad_words1
@bot.message_handler(content_types=['text'])
def filter_word(mess):
	message = filter(None, re.split("[, \-!?:]+", mess.text))
	for i in message:
		if i.lower() in bad_words:
			bot.delete_message(mess.chat.id, mess.message_id)
	if mess.text.lower() in bad_words1:
		bot.delete_message(mess.chat.id, mess.message_id)

if __name__ == '__main__':
	print('Bot started')
	while True:
	try:
		bot.polling(none_stop=True, timeout=0.02)
	except requests.exceptions.ConnectionError:
		time.sleep(15)
