from turtle import Screen, Turtle
from snake import Snake
import time

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("Jogo da cobra")
tela.tracer(0)

segmentos = []

cobra = Snake()

jogo = True
while jogo:
    tela.update()
    time.sleep(0.1)
    cobra.mover_cobra()

tela.exitonclick()
