import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jogador = Player()
screen.listen()
screen.onkey(jogador.move, "Up")

score = Scoreboard()
car_manager = CarManager(score)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.update_score()

    # Criar carros
    car_manager.create_car()

    # Mover carros a cada update da tela
    car_manager.move_cars()

    # Detectar colisão com carro
    for car in car_manager.all_cars:
        if car.distance(jogador) < 20:
            game_is_on = False
            score.game_over()

    # Detectar level up
    if jogador.ycor() > 260:
        jogador.reset_position()
        score.level_up()

screen.exitonclick()
