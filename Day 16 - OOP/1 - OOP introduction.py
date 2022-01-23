# car = CarBlueprint()
# Acima, a classe CarBlueprint é o template que temos para criar quantos objetos quisermos (no caso, o carro), ela determina que características esse objeto terá e, a partir daí, podemos "produzir" carros diferentes mudando atributos das características dadas pela classe.

import turtle

carlinhosBala = turtle.Turtle()
# Aqui, carlinhos bala é o objeto criado acessando o módulo importado turtle (notar a letra minúscula) e a classe Turtle (com letra maiúscula)

# Outro jeito de importar o módulo Turtle, ou qualquer outro, é from MODULO A SER IMPORTADO import CLASSE A SER IMPORTADA, dessa maneira, podemos criar um objeto com a sintaxe vista no começo:
# carlinhosBala = Turtle()

myScreen = turtle.Screen()
print(myScreen.canvheight)
# O ponto após o objeto é usado para acessar os atributos existentes nele. Como a classe Screen do módulo Turtle foi criada com vários atributos, ao criamos um objeto dessa classe, podemos ver esses atributos digitando . após o nome do objeto

# Além das características de um objeto (atributos), ele também pode ter métodos, ou funções, que determinam como ele se comportam, ou até, modificam seus atributos. O acesso aos métodos de um objeto é dado da mesma forma que os atributos, porém, por serem funções, eles se diferenciam com os parênteses no final

carlinhosBala.shape("turtle")
carlinhosBala.color("cyan")
carlinhosBala.forward(100)
# Aqui, chamo um método pra mudar a forma da tartaruga na tela pra uma tartaruaga (por default é uma seta), outro pra mudar a cor dela e outro pra fazer ela andar (e assim, desenhar uma linha)

myScreen.exitonclick()
# Aqui, chamo outro para só fechar o canvas quando houver um clique na tela.