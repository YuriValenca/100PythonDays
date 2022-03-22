from turtle import Screen, Turtle

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da cobra")

posicoes_iniciais = [(0, 0), (-20, 0), (-40, 0)]

for posicao in posicoes_iniciais:
    novo_pedaco = Turtle(shape="square")
    novo_pedaco.color("white")
    novo_pedaco.goto(posicao)

# O loop for acima criará quadrados que vão representar o corpo inicial da cobra, as posições iniciais desses quadrados são acessados através de uma lista de tuplas, onde as tuplas representam a posição no sistema de coordenadas da tela que, como tem tamanho 600x600, tem seu sistema indo de -300 a 300 em ambos os eixos x e y


tela.exitonclick()