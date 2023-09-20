from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da cobra")
tela.tracer(0)

segmentos = []

cobra = Snake()
comida = Food()
scoreboard = Scoreboard()

tela.listen()
tela.onkey(cobra.cima, "Up")
tela.onkey(cobra.baixo, "Down")
tela.onkey(cobra.esquerda, "Left")
tela.onkey(cobra.direita, "Right")

jogo = True
while jogo:
    tela.update()
    time.sleep(0.1)
    cobra.mover_cobra()
    scoreboard.atualizar_pontuacao()

    if cobra.head.distance(comida) < 15:
        comida.nova_posicao()
        scoreboard.aumentar_pontuacao()

tela.exitonclick()
