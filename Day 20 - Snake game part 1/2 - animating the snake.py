from turtle import Screen, Turtle
import time

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da cobra")
tela.tracer(0)

posicoes_iniciais = [(0, 0), (-20, 0), (-40, 0)]

segmentos = []

for posicao in posicoes_iniciais:
    novo_pedaco = Turtle(shape="square")
    novo_pedaco.color("white")
    novo_pedaco.penup()
    novo_pedaco.goto(posicao)
    segmentos.append(novo_pedaco)


jogo = True
while jogo:
    tela.update()
    time.sleep(0.1)
# Range é uma função que vai de um número até outro, no caso, da quantidade de segmentos -1 (pois é um array) até 0, pulando de -1 em -1
    for segmento in range(len(segmentos) - 1, 0, -1):
        novo_x = segmentos[segmento - 1].xcor()
        novo_y = segmentos[segmento - 1].ycor()
        segmentos[segmento].goto(novo_x, novo_y)
        # Esse for loop faz com que cada segmento siga o segmento anterior, fazendo com que os movimentos da cobra sigam o do primeiro segmento,
        # permitindo curvas e, futuramente, o input do usuário
    segmentos[0].forward(20)
    segmentos[0].left(90)


tela.exitonclick()
