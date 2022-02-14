from question_model import Questao
from data import question_data
from quiz_brain import QuizBrain

bancoDeQuestoes = []

# Percorrer a lista de perguntas com vários dicionários, armazenando o valor do texto, de acordo com a key "text" e o valor da resposta de acordo com a key "answer"
for question in question_data:
    textoPerg = question["text"]
    respPerg = question["answer"]
    novaPergunta = Questao(textoPergunta = textoPerg, respostaPergunta = respPerg)
    bancoDeQuestoes.append(novaPergunta)

quiz = QuizBrain(bancoDeQuestoes)

quiz.proximaPerg()