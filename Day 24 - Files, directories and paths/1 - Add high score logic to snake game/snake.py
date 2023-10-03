from turtle import Turtle

POSICOES_INICIAIS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_DE_MOVIMENTO = 20
CIMA = 90
BAIXO = 270
ESQUERDA = 180
DIREITA = 0


class Snake:

    def __init__(self):
        self.segmentos = []
        self.criar_cobra()
        self.head = self.segmentos[0]

    def criar_cobra(self):
        for posicao in POSICOES_INICIAIS:
            self.adicionar_segmento(posicao)

    def adicionar_segmento(self, posicao):
        novo_pedaco = Turtle(shape="square")
        novo_pedaco.color("white")
        novo_pedaco.penup()
        novo_pedaco.goto(posicao)
        self.segmentos.append(novo_pedaco)

    # Para correto funcionamento da lógica de reset do scoreboard, a cobra precisa ser "parada"
    # ou "limpa" nesse caso.
    def reset(self):
        # Para evitar que a cobra anterior fique na tela, é necessário mover todos os segmentos
        # para fora da tela. Não é uma solução ideal a longo termo, mas é a mais simples.
        for segmento in self.segmentos:
            segmento.goto(1000, 1000)
        self.segmentos.clear()
        self.criar_cobra()
        self.head = self.segmentos[0]

    def crescer(self):
        self.adicionar_segmento(self.segmentos[-1].position())

    def mover_cobra(self):
        for segmento in range(len(self.segmentos) - 1, 0, -1):
            novo_x = self.segmentos[segmento - 1].xcor()
            novo_y = self.segmentos[segmento - 1].ycor()
            self.segmentos[segmento].goto(novo_x, novo_y)
        self.head.forward(DISTANCIA_DE_MOVIMENTO)

    def cima(self):
        if self.head.heading() != BAIXO:
            self.head.setheading(CIMA)

    def baixo(self):
        if self.head.heading() != CIMA:
            self.head.setheading(BAIXO)

    def esquerda(self):
        if self.head.heading() != DIREITA:
            self.head.setheading(ESQUERDA)

    def direita(self):
        if self.head.heading() != ESQUERDA:
            self.head.setheading(DIREITA)
