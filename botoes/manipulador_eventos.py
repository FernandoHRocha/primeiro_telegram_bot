import telebot
import tk
import chamadas
from telebot import types

bot = telebot.TeleBot(tk.token, parse_mode=None)
astro = chamadas.Astronautas
exchange = chamadas.Exchange
loja = chamadas.Loja

@bot.message_handler(commands=['start','começar', 'ajuda'])
def send_start_message(message):
	bot.reply_to(message,   "Bom dia meu querido, como que tá esse sorriso?\n"
                            "Os meu comandos são os seguintes:\n"
                            "/pessoas tripulantes em satélites.\n"
                            "/cotacao atual valor do par BTC-USD"
                            "Com o comando @fernando_rocha_bot você pode compartilhar nossos produtos com os seus amigos.")

@bot.message_handler(commands=['pessoas'])
def send_people(message):
	bot.reply_to(message, astro.obter_tripulantes(astro))

@bot.message_handler(commands=['cotacao'])
def send_exchange(message):
	bot.reply_to(message, exchange.obter_cotacao(exchange))

@bot.inline_handler(lambda query: True)
def query_text(inline_query):
    bot.answer_inline_query(
       inline_query.id,
       loja.obter_produtos(loja))

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def send_people(message):
	bot.reply_to(message, astro.obter_tripulantes(astro))

bot.polling()