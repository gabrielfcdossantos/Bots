
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Eu estou bem']
conversa2 = ['Qual é o seu filme preferido?','Escola do Rock','Quantos anos vc tem ?','Fui criado 03/11/2018']
conversa3 = ['Qual é o seu nome ?','Tijolinho']

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)
bot.train(conversa3)

while True:
    quest = input("Você: ")
    resposta = bot.get_response(quest)
    if float(resposta.confidence) > 0.8:
        print('Bot: ',resposta)
    else:
        print('Bot: Eu não sei, Malz ae')
