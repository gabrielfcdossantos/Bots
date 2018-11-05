from chatterbot import ChatBot
import telepot

bot = ChatBot('Test', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
telegram = telepot.Bot('TOKEN')
bot.train('chatterbot.corpus.portuguese')

def recebendoMsg(msg):
    print(msg['text'])
    pergunta = msg['text']
    resposta = bot.get_response(pergunta)
    r = str(resposta)
    telegram.sendMessage(IDchave,r)
    print('Bot: ', resposta)




telegram.message_loop(recebendoMsg,0.1,5)
while True:
    pass
