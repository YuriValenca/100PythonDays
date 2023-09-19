from turtle import Turtle

POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_DE_MOVIMENTO = 20


class Snake:

    def __init__(self):
        self.segmentos = []
        self.criar_cobra()
        self.mover_cobra()

    def criar_cobra(self):
        for posicao in POSICOES_INICIAIS:
            novo_pedaco = Turtle(shape="square")
            novo_pedaco.color("white")
            novo_pedaco.penup()
            novo_pedaco.goto(posicao)
            self.segmentos.append(novo_pedaco)

    def mover_cobra(self):
        for segmento in range(len(self.segmentos) - 1, 0, -1):
            novo_x = self.segmentos[segmento - 1].xcor()
            novo_y = self.segmentos[segmento - 1].ycor()
            self.segmentos[segmento].goto(novo_x, novo_y)
        self.segmentos[0].forward(DISTANCIA_DE_MOVIMENTO)
