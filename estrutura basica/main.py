import telebot
import os
from telebot import types
import estado

token = os.environ['FERNANDO_TELEGRAM_BOT_TOKEN']
estado = estado.Estado(estado.Estado)
estado.resetar()
bot = telebot.TeleBot(token, parse_mode = None)

markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('Ótimo')
itembtn2 = types.KeyboardButton('Neutro')
itembtn3 = types.KeyboardButton('Péssimo')
markup.add(itembtn1, itembtn2, itembtn3)
markup_avaliacao = markup

@bot.message_handler(commands=['particular'])
def mensagem_particular(message):
	bot.send_message(message.from_user.id,'Foi requisitada uma mensagem particular.',reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['avaliacao','avaliação'])
def send_welcome(message):
	estado.estado = 1
	bot.send_message(message.chat.id, "Sua avaliação é importante para nós.\nComo você avalia nossos serviços?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def receber_avaliacao(message):
	if(message.text == 'Ótimo'):
		bot.send_message(message.chat.id,'Agradecemos a sua avaliação.',reply_markup=types.ReplyKeyboardRemove())
	if(message.text == 'Neutro'):
		bot.send_message(message.chat.id,'Procuramos melhorar a cada dia.',reply_markup=types.ReplyKeyboardRemove())
	if(message.text == 'Péssimo'):
		bot.send_message(message.chat.id,'Infelizmente houve um erro de conexão durante o envio da sua avaliação.',reply_markup=types.ReplyKeyboardRemove())
	estado.resetar()

	#bot.reply_to(message, "Confirmando comando.")

bot.polling()