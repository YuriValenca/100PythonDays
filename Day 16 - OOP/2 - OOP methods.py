from prettytable import PrettyTable
# Importamos a classe PrettyTable do módulo prettytable, essa classe, assim como a classe Turtle do módulo turtle, tem vários métodos (funções) associados a ela

table = PrettyTable()

# O principal método da classe PrettyTable() é o de adicionar uma coluna, invocamos esse método através do objeto table criado acima, seguindo a sintade de NomeDoObjeto.NomeDoMétodo
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

# Como estamos criando um objeto (table) a partir de uma classe pré-pronta, esse objeto virá com vários métodos e atributos embutidos, então precisamos apenas acessar, e não implementar.
# O acesso aos atributos é feita pela mesma sintaxe dos métodos

# table.align = 'l' Esse snippet permitirá que o alinhamento seja feito pela esquerda, e não de forma central, como é o default da classe

# O ponto positivo de utilizar uma classe pré-pronta, é que não é necessário implementar, debuggar, etc. Porém, é necessário ter  um bom conhecimento dela, para um uso ideal, ou consultar regularmente os métodos e atributos online