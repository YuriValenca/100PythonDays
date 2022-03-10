import turtle as t
import random

timmy = t.Turtle()
tela = t.Screen()
t.colormode(255)

def cor_randomica():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor = (r, g, b)
    return cor


timmy.speed(0)

def desenhar_espirografo(tamanho_do_circ):
    for i in range (int(360 / tamanho_do_circ)):
        timmy.color(cor_randomica())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + tamanho_do_circ)

desenhar_espirografo(5)
tela.exitonclick()