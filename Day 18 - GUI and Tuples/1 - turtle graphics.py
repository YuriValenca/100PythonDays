from turtle import Turtle, Screen
# O from... import... é util quando queremos que o objeto importado seja utilizado várias vezes, evitando de, primeiro acessar o módulo, e depois o objeto desejado, indo "direto ao ponto" e acessando diretamente o objeto
# É possível ainda usar Alias na importação de um módulo. Alias é um nome ou identificação que nós mesmos podemos dar a algo. A sintaxe segue da seguinte maneira:
# import turtle as t
# Isso fará com que o acesso ao módulo, em vez de ser feito por turtle.AlgumaFuncaoOuObjeto seja t.AlgumaFuncaoOuObjeto

tartaruga = Turtle()

tela = Screen()

# Comando para desenhar um quadrado
tartaruga.color("red")
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.forward(100)
tartaruga.right(90)

tela.exitonclick()