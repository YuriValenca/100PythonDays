# A ideia aqui é criar vários objetos da classe tartaruga, aplicando uma característica diferente a cada um deles (no caso, a cor), para diferenciá-los numa corrida

from turtle import Turtle, Screen
import random

tela = Screen()

tela.setup(width=500, height=400) # Setup ajusta várias coisas da tela, nesse caso, a resolução está sendo ajustada para 500x400, deixamos isso claro com o uso de keyword arguments (ver dia 08)

aposta = tela.textinput(title="Faça sua aposta!!", prompt="Qual tartaruga ganhará a corrida? Digite uma cor:") # Textinput coloca um popup na tela, title será o "nome" dessa janela e prompt, o texto que aparecerá. Colocando esse texto numa variável, poderemos registrar qual será a cor que o usuário escolheu

# Para fazer as tartarugas iniciarem a corrida, é necessário colocálas no "começo" da tela, e em "linhas" separadas, para vermos melhor qual será a vencedora. Ao invés de fazer isso com setheadings, fowards e afins, o Turtle tem uma função de goto(), onde a tartaruga vai para um ponto no canvas, determinado pelos valores da tupla (x, y)

# Porém, para colocarmos as tartarugas nos lugares certos, é primordial entender como funciona o sistema de coordenadas do módulo Turtle. O ponto que a tartaruga geralmente inicia é o (0,0). Como colocamos a resolução pra ser 500x400, isso significa que, na altura (eixo y), o plano cartesiano irá de -200 a 200 e na largura (eixo x), de -250 a 250

# Porém, se colocarmos a tartaruga diretamente no ponto (-250, 0), não conseguiremos visualizá-la no início, por isso, teremos que ter um "offset" para visualizar as tartarugas no iniciio da corrida

corrida_rolando = False
cores = ["red", "orange", "yellow", "green", "blue", "purple"]
posicoes_eixo_y = [-70, -40, -10, 20, 50, 80]
todas_tartarugas = []

for i in range (6):
    tartaruga = Turtle(shape="turtle")
    tartaruga.penup()
    tartaruga.color(cores[i])
    tartaruga.goto(x=-240, y=posicoes_eixo_y[i])
    todas_tartarugas.append(tartaruga)
    # Esse loop for criará 6 objetos iguais, mudando apenas as posições de y e as cores. No fim, colocamos elas numa lista para manipular mais facilmente

if aposta:
    corrida_rolando = True

while corrida_rolando:

    for tartaruga in todas_tartarugas:

        if tartaruga.xcor() > 230:

            corrida_rolando = False
            tartaruga_vencedora = tartaruga.pencolor()

            if tartaruga_vencedora == aposta:
                print(f"Você venceu! A tartaruga {tartaruga_vencedora} ganhou")
            else:
                print(f"Você apostou errado. Quem ganhou foi a tartaruga {tartaruga_vencedora}")

        distancia_random = random.randint(1, 10)
        tartaruga.fd(distancia_random)

tela.exitonclick()