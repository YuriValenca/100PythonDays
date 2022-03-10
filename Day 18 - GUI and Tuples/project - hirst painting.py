# Disclaimer: É possível também, fazer esse projeto com a biblioteca colorgram (instalando via pip), que retorna as cores presentes em uma imagem. Porém, pra simplificar, aqui irá ser feito randomizando as cores pelo módulo random.

import turtle as t
import random

timmy = t.Turtle()
tela = t.Screen()
t.colormode(255)
timmy.speed(0)
timmy.penup() # A função penup "levanta a caneta" e faz com que a linha que a tartaruga percorre não seja mostrada
timmy.hideturtle() # Já essa, esconde a seta, ou tartaruga, a depender do que foi escolhido para representar o "lápis"
numero_pontos = 100

# Nesse projeto, faremos uma pintura de Hirst, um artista que ficou famoso por pintar pontos coloridos e tais pinturas serem vendidas por mais de 1 milhão de dólares! É possível fazer isso utilizando o turtle, a tartaruga vai colocar pontos grandes equivalentes e equidistantes na GUI, randomizando suas cores

# É necessário, no entanto, para descentralizar a tartaruga, centralizando a "pintura", que mudemos algumas configurações iniciais dela:
timmy.setheading(225) # Vira Timmy para a diagonal esquerda
timmy.forward(300) # Avança com Timmy
timmy.setheading(0) # Deixa Timmy virado novamente para a direita

def cor_randomica():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor = (r, g, b)
    return cor

def mudanca_linha():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
    # Todos esses comandos fazem com que Timmy, ao terminar uma linha, vá pra cima, pro começo da linha novamente, e vire para o lado direito, para iniciar uma nova linha de pontos coloridos

for count_pontos in range(1, numero_pontos + 1):
    timmy.dot(20, cor_randomica())
    timmy.forward(50)
    if count_pontos % 10 == 0: # Isso fará com que a função de mudança de linha seja chamada a cada 10 pontos coloridos
        mudanca_linha()
    
    
tela.exitonclick()
