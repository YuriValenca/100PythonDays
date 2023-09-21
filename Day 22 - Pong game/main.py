from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

tela = Screen()
tela.setup(width=800, height=600)
tela.bgcolor("black")
tela.title("Pong")
tela.tracer(0)

# Como a criação da classe pede um parâmetro a mais, é necessário passá-lo a cada chamada da classe
paddle_direito = Paddle((375, 0))
paddle_esquerdo = Paddle((-375, 0))
bola = Ball()
scoreboard = Scoreboard()

tela.listen()
tela.onkey(paddle_direito.cima, "Up")
tela.onkey(paddle_direito.baixo, "Down")
tela.onkey(paddle_esquerdo.cima, "w")
tela.onkey(paddle_esquerdo.baixo, "s")


jogo = True
while jogo:
    tela.update()
    time.sleep(bola.move_speed)
    bola.mover()
    scoreboard.atualizar_pontuacao()

    # Detectar colisão com parede
    if bola.ycor() > 275 or bola.ycor() < -275:
        bola.quicar(direcao="y")

    # Detectar colisão com paddle
    if bola.xcor() > 350 or bola.xcor() < -350:
        # Verifica-se se a bola atingiu um nível que, ou ela atinge o paddle, ou ela passa.
        # Se a bola estiver a uma certa distância do paddle, ela é rebatida
        if bola.distance(paddle_direito) < 50 or bola.distance(paddle_esquerdo) < 50:
            bola.quicar(direcao="x")

    # Detectar se a bola passou do paddle direito
    if bola.xcor() > 400:
        bola.resetar_posicao()
        scoreboard.esq_ponto()

    # Detectar se a bola passou do paddle esquerdo
    if bola.xcor() < -400:
        bola.resetar_posicao()
        scoreboard.dir_ponto()

tela.exitonclick()
