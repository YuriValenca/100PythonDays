from turtle import Screen, Turtle

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da cobra")

posicoes_iniciais = [(0, 0), (-20, 0), (-40, 0)]

segmentos = []

for posicao in posicoes_iniciais:
    novo_pedaco = Turtle(shape="square")
    novo_pedaco.color("white")
    novo_pedaco.goto(posicao)
    segmentos.append(novo_pedaco)

jogo = True
while jogo:
    for seg in segmentos:
        seg.forward(20)




tela.exitonclick()