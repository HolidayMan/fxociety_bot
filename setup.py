import telebot
import constants
import re
import random
import time

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['start', 'help'])
def start_help(mess):
	bot.send_message(mess.chat.id, 'Привет! Я помогаю фильтровать маты в этом чате! \n \
	Также у меня доступны такие команды: \n\
	/help - информация о боте; \n/petard - удаление одного сообщения перед командой (Бум)\
	\n/bomb - удаление трех сообщений перед командой (Буум)')


@bot.message_handler(commands=['admin_podtverdi'])
def admin_podtverdi(mess):
	okChance = random.randint(0,100)
	bot.send_message(mess.chat.id, 'Вероятность подтверждения {}%'.format(okChance))
	if random.randint(0,100) <= okChance:
		bot.send_message(mess.chat.id, 'Админ подтверждает')
	else:
		bot.send_message(mess.chat.id, 'Не могу такое подтвердить')

			
with open('bad_words.txt','r') as f:
	file = f.read().split()
bad_words = []
for i in file:
	if i == '----':
		break
	bad_words.append(i)
bad_words1 = []
for i in range(len(bad_words)+1,len(file)):
	bad_words1.append(file[i])
	
	
@bot.message_handler(content_types=['text'])
def filter_word(mess):
	message = filter(None, re.split("[, \-_!?:$;#@()%^0&*+]+", mess.text))
	for i in message:
		if i.lower() in bad_words:
			try:
				bot.delete_message(mess.chat.id, mess.message_id)
				return 0
			except telebot.apihelper.ApiException:
				return 0
		if mess.text.lower() in bad_words1:
			try:
				bot.delete_message(mess.chat.id, mess.message_id)
				return 0
			except telebot.apihelper.ApiException:
				return 0
		if mess.text.lower() in ['да','нет','нельзя']:
			try:
				bot.send_message(mess.chat.id, 'По-развернутей, пожалуйста')
				return 0
			except telebot.apihelper.ApiException:
				return 0
if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except:
			time.sleep(15)
