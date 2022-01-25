# Com o conhecimento visto de OOP (Object oriented programming), agora é possível reescrever o código da máquina de café utilizando os conceitos de objetos, classes, funções e métodos
# O código do funcionamento em si da máquina de café já nos foi dado, isso porque ele contém assuntos e sintaxes de aulas futuras, então, basta apenas importarmos esses módulos e implementar apenas o input do usuário, aliando isso ao que foi importado
# A documentação da máquina de café pré implementada está no PDF nessa pasta. Nele, é possível decifrar o funcionamento de cada uma das classes, métodos e atributos implementados (documento apenas em inglês)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
# Criando os objetos money_machine e coffe_maker a partir das classes (blueprints) MoneyMachine() e CoffeMaker() (não esquecer os parênteses). Feito isso, agora é possível acessar os métodos e/ou atributos dessas classes, como feito abaixo

# coffee_maker.report()
# money_machine.report()

funcionando = True
menu = Menu()

while funcionando:
    opcoes = menu.get_items()
    # Esse método do objeto menu (da classe Menu()) retorna quais bebidas estão disponíveis no menu para consumo
    escolha = input(f"Que bebida você deseja tomar? As bebidas disponíveis são: {opcoes}\n")
    if escolha == "off":
        funcionando = False
    elif escolha == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        bebida = menu.find_drink(escolha)
        # Outro método do objeto menu, dessa vez, retorna a bebida, se estiver no cardápio, se não, retorna None. É importante ressaltar aqui que o resultado desse método é guardado numa variável bebida, essa variável torna-se um objeto do menu, e passa a ter seus atributos e métodos associados a ele
        if coffee_maker.is_resource_sufficient(bebida):
        # Nesse método do objeto coffee_maker dirá se é possível fazer a bebida especificada no parâmetro do método (se a máquina tem os recursos necessários)
            if money_machine.make_payment(bebida.cost):
            # Como bebida agora é um objeto da classe menu, é possível acessar o atributo cost a partir dele. Esse método, dentro do código de MoneyMachine() é quem irá chamar o outro método de processamento de moedas, por isso, não é necessário implementar um pedaço de código para isso
                coffee_maker.make_coffee(bebida)
                # Por fim, o método de efetivamente "fazer" o café e diminuir a quantidade dos ingredientes, para isso, é necessário passar a bebida (agora, objeto da classe Menu())
            
# É possível ver que o código ficou EXTREMAMENTE mais enxuto, mas isso foi graças ao fato de não ter sido necessario implementar as classes e métodos utilizados. Novamente, por um lado, isso mostra que utilizar classes pré prontas para várias situações pode ser muito favorável, por outro, se for necessário a implementação de todas as classes e métodos, isso exigirá um trabalho extra e minuncioso, para garantir que tudo funciona como deve ser.