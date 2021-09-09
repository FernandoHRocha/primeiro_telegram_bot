import telebot

bot = telebot.TeleBot("1972365324:AAEK3UcuPoZwYC_9WmJBnpKTUzVWo7ILrY0", parse_mode=None)

@bot.message_handler(commands=['começar'])
def send_welcome(message):
	bot.reply_to(message, "Bom dia meu querido, como que tá esse sorriso?")

@bot.message_handler(commands=['ajuda'])
def send_welcome(message):
	bot.reply_to(message, "Tenho apenas algumas funções.\nSe me disser qualquer coisa que eu não entenda, eu repito. :D")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()