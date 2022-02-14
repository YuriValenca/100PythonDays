class QuizBrain:
    def __init__(self, listaQuestoes):
        self.numQuestao = 0
        self.listaQuestoes = listaQuestoes

    def proximaPerg(self):
        pergAtual = self.listaQuestoes[self.numQuestao]
        self.numQuestao += 1
        input(f"Q. {self.numQuestao}: {pergAtual.texto}. True or False?: ")

