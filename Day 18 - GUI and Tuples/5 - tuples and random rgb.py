# A cor da tartaruga pode ser randomizada por uma lista, como foi feito nos dois últimos desafios, mas também, pode ser escrita usando 3 parâmetros, representando o RGB da cor (quantidade de red, green, blue). 
# Esses 3 parâmetros dentro de parênteses representam uma estrutura de dados em Python chamada TUPLA, a sintaxe da tupla é similar à da lista, porém, com o uso de parênteses, ao invés de colchetes. 
# No entando, essas duas estruturas possuem uma grande diferença entre si: a tupla NÃO pode ser alterada. Uma vez que definida, nenhum de seus elementos sofrerá algum tipo de alteração. É um objeto IMUTÁVEL

from turtle import Turtle, Screen
import random

# Nesse desafio, vamos colocar a tartaruga para andar distâncias fixas mas em direções randômicas, porém, utilizando agora tuplas para randomizar mais ainda as cores do percurso

timmy = Turtle()
tela = Screen()
tela.colormode(255) #Linha necessária para a chamada da cor da tartaruga funcionar

def cor_randomica():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor = (r, g, b)
    return cor

direcoes = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed(0)

for i in range(20000):
    timmy.color(cor_randomica())
    timmy.forward(30)
    timmy.setheading(random.choice(direcoes))