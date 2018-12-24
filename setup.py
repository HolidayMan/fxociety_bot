import telebot
import constants
import re
import time
import random

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

		
@bot.message_handler(commands=['petard'])
def petard(mess):
	i = 1
	while True:
		try:
			bot.delete_message(mess.chat.id, mess.message_id - i)
			time.sleep(0.5)
			bot.delete_message(mess.chat.id, mess.message_id)
			break
		except telebot.apihelper.ApiException:
			i+=1

	
@bot.message_handler(commands=['bomb'])
def bomb(mess):
	i = 1
	k=1
	while True:
		try:
			if k < 4: 
				bot.delete_message(mess.chat.id, mess.message_id - i)
				time.sleep(0.2)
				k+=1
			else:
				bot.delete_message(mess.chat.id, mess.message_id)
				break
		except telebot.apihelper.ApiException:
			i+=1

			
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
	print('Bot started')
	while True:
		try:
			bot.polling(none_stop=True,interval=0)
		except urllib3.exceptions.ReadTimeoutError:
			print('[-] Bot is sleeping')
			time.sleep(15)
			print('[-] Bot is working')
