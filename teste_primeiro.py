import telebot
import json
import urllib
import tk

bot = telebot.TeleBot(tk.token, parse_mode=None)

@bot.message_handler(commands=['start','começar', 'ajuda'])
def send_start_message(message):
	bot.reply_to(message,   "Bom dia meu querido, como que tá esse sorriso?\n"
                            "Os meu comandos são os seguintes:\n"
                            "/pessoas tripulantes em satélites.")

@bot.message_handler(commands=['pessoas'])
def send_people(message):
	bot.reply_to(message, obter_tripulantes())

@bot.message_handler(commands=['cotacao'])
def send_exchange(message):
	bot.reply_to(message, obter_cotacao())

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

def obter_tripulantes():
    n_pessoa, pessoa = api_tripulantes()
    mensagem = 'Estão presente ' + str(n_pessoa) + ' pessoas.\n'
    for individuo in pessoa:
        mensagem += individuo['name'] + ' conosco em ' + individuo['craft'] + '\n\n'
    return mensagem

def api_tripulantes():
    req = 'http://api.open-notify.org/astros.json'
    resposta = urllib.request.urlopen(req)
    obj = json.loads(resposta.read())
    return obj['number'], obj['people']

def obter_cotacao():
    cotacao = api_cotacao()
    print(cotacao)
    return "Cotação atual para o par BTC-USD\n"+"Compra: US$ "+cotacao[0]+"\nVenda: US$ " +cotacao[0]

def api_cotacao():
    req = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange'
    resposta = urllib.request.urlopen(req)
    obj = json.loads(resposta.read())[0]
    return obj['buy'], obj['sale']


bot.polling()