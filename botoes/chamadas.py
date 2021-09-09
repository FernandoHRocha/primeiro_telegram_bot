import telebot
import json
import urllib

class Astronautas:
    def obter_tripulantes(self):
        n_pessoa, pessoa = self.api_tripulantes(self)
        mensagem = 'Estão presente ' + str(n_pessoa) + ' pessoas.\n'
        for individuo in pessoa:
            mensagem += individuo['name'] + ' conosco em ' + individuo['craft'] + '\n\n'
        return mensagem

    def api_tripulantes(self):
        req = 'http://api.open-notify.org/astros.json'
        resposta = urllib.request.urlopen(req)
        obj = json.loads(resposta.read())
        return obj['number'], obj['people']

class Exchange:
    def obter_cotacao(self):
        cotacao = self.api_cotacao(self)
        return "Cotação atual para o par BTC-USD\n"+"Compra: US$ "+cotacao[0]+"\nVenda: US$ " +cotacao[1]

    def api_cotacao(self):
        req = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange'
        resposta = urllib.request.urlopen(req)
        obj = json.loads(resposta.read())[0]
        return obj['buy'], obj['sale']

class Loja:
    def obter_produtos(self):
        result = []
        n_pessoa, pessoal = self.api_tripulantes(self)
        for pessoa in pessoal:
            result.append(
                telebot.types.InlineQueryResultArticle(
                    id=pessoa['name'],
                    title=pessoa['name'],
                    input_message_content=telebot.types.InputTextMessageContent(
                        'Não estamos vendendo astronautas,\nmas esse é o exemplo de um produto R$'+pessoa['craft']
                    ),
                    description='Nome ' + pessoa['name'] + ' -> ' + pessoa['craft'],
                    thumb_url='https://cdn.awsli.com.br/600x450/1628/1628166/produto/117446547/c157e26fba.jpg',
                    thumb_height=100,
                    thumb_width=100,
                    url='www.brainpro.com.br'
                )
            )
        return result

    def api_tripulantes(self):
        req = 'http://api.open-notify.org/astros.json'
        resposta = urllib.request.urlopen(req)
        obj = json.loads(resposta.read())
        return obj['number'], obj['people']