# Para que o usuário consiga interagir em tempo real com o código, é possível utilizar dos chamados "event listeners", onde o código espera inputs do usuário e, a depender deles, realiza diferentes ações. Ex.: seta direita para andar para a direita

from turtle import Turtle, Screen

timmy = Turtle()
tela = Screen()

def andar():
    timmy.forward(10)

tela.listen()
tela.onkey(key="space", fun=andar)
# A função onkey espera dois parâmetros, uma tecla, e uma função. Ao receber uma tecla, ela executa a função passada. Nesse caso, ao apertarmos espaço, a função vai chamar outra função, andar(), e isso fará com que a tartaruga ande 10 pixels, ou seja, ao apertarmos espaço, ela anda 10 pixels.

# IMPORTANTE: quando uma função é usada como argumento, quando é passada em outra função, NÃO colocamos parênteses, pois eles fazem com que a função seja executada naquela hora, mas, nesse caso, o que queremos é que, quando espaço for apertado, a tartaruga ande, e não que ela ande imediatamente.

# A função onkey, então, é o que chamamos de Higher Order Function, ou função de ordem superior. Essas funções são capazes de trabalhar com outras funções dentro delas

# Um outro exemplo seria uma função calculate(), que tem como argumentos 2 números e uma função, dentre add, sub, dividir e mult. Ao ser chamada, calculate vai receber 2 números e a função que deve ser executada e processar dentro dela essa função passada na chamada

tela.exitonclick()