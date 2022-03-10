from turtle import Turtle, Screen
import random

# Nesse desafio, vamos colocar a tartaruga pra desenhar um triangulo, quadrado, pentágono... até um decágono, sequencialmente

timmy = Turtle()
tela = Screen()

cores = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def desenhar_forma(num_lados):
    angulo = 360/num_lados
    for i in range (num_lados):
        timmy.forward(100)
        timmy.right(angulo)

for num_lados_atual in range(3, 361): #Triângulo (3) a decágono (10), range com 2 números não inclui o número do segundo argumento
    timmy.color(random.choice(cores))
    desenhar_forma(num_lados_atual)

tela.exitonclick()