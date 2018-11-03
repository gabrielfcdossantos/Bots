from chatterbot import ChatBot

bot = ChatBot('Test', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

bot.train('chatterbot.corpus.portuguese')

while True:
    pergunta = input('Você: ')
    resposta = bot.get_response(pergunta)
    print('Bot: ', resposta)
