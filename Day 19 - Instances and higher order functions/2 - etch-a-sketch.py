# Nesse desafio, é proposto fazer um Etch-A-Sketch, uma linha desenhando que será controlada via WASD

from turtle import Turtle, Screen

timmy = Turtle()
tela = Screen()

def andar():
    timmy.fd(10)

def voltar():
    timmy.bk(10)

def virar_dir():
    timmy.rt(7.5)

def virar_esq():
    timmy.lt(7.5)

def reset_desenho():
    timmy.reset()

tela.listen()
tela.onkeypress(key="w", fun=andar) # Onkeypress fará com que pressionar a tecla também avançe a tartaruga, ao invés de apenas pressionar várias vezes
tela.onkeypress(key="s", fun=voltar)
tela.onkeypress(key="d", fun=virar_dir)
tela.onkeypress(key="a", fun=virar_esq)
tela.onkeypress(key="c", fun=reset_desenho)

# Vale ressaltar que as funções foward, backward, left e right, pela documentação, possuem aliases ("apelidos") mais curtos, e estes foram usados nesse desafio'

tela.exitonclick()