from turtle import Turtle, Screen
import random

# Nesse desafio, vamos colocar a tartaruga para andar distâncias fixas mas em direções randômicas

timmy = Turtle()
tela = Screen()

cores = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direcoes = [0, 90, 180, 270]
timmy.pensize(15) #Comando para deixar a linha mais grossa
timmy.speed(0)

for i in range(20000):
    timmy.color(random.choice(cores))
    timmy.forward(30)
    timmy.setheading(random.choice(direcoes))
