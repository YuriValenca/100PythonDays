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

    # Detectar colisão com comida e crescer a cobra
    if cobra.head.distance(comida) < 15:
        comida.nova_posicao()
        cobra.crescer()
        scoreboard.aumentar_pontuacao()

    # Detectar colisão com parede
    if cobra.head.xcor() > 280 or cobra.head.xcor() < -280 or cobra.head.ycor() > 280 or cobra.head.ycor() < -280:
        scoreboard.reset()
        cobra.reset()

    # Detectar colisão com a cauda
    for segmento in cobra.segmentos[1:]:
        # Loop que verifica se a cabeça da cobra colidiu com algum segmento da cauda, '[1:]' significa que o loop é a partir do elemento 1, pulando o 0
        # Isso chama-se slicing. Pode ser feito indicando o começo e o fim também, por exemplo '[2:5]' significa que o loop será entre o elemento 2 e o 5
        # Pode-se ainda reverter a lista, por exemplo '[::-1]' significa que o loop será do último elemento até o primeiro
        if cobra.head.distance(segmento) < 10:
            scoreboard.reset()
            cobra.reset()

tela.exitonclick()
