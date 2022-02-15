from numpy import true_divide


class QuizBrain:
    def __init__(self, listaQuestoes):
        self.numQuestao = 0
        self.listaQuestoes = listaQuestoes
        self.score = 0

    def aindaTemPerguntas(self):
        if self.score == self.numQuestao: 
            return self.numQuestao < len(self.listaQuestoes)
        # Aqui o compilador irá retornar se essa comparação de menor que é verdadeira ou falsa, salvando de escrever um if/else com return true/false

    def proximaPerg(self):
        pergAtual = self.listaQuestoes[self.numQuestao]
        self.numQuestao += 1
        respostaUsuario = input(f"Q. {self.numQuestao}: {pergAtual.texto}. True or False?: ")
        self.verificarResposta(respostaUsuario, pergAtual.resposta)

    def verificarResposta(self, respostaUsuario, respostaCorreta):
        if(respostaCorreta.lower() == respostaUsuario.lower()):
            print("Você acertou!")
            self.score += 1
        else:
            print("Você errou...")
        print(f"A resposta correta era {respostaCorreta}\n")
