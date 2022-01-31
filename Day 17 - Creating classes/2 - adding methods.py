# Os atributos são as coisas que um objeto TEM, enquanto os métodos são as coisas que o objeto FAZ

# Neste objeto de exemplo, temos um carro que tem, por default, 5 lugares (além de um modelo que pode ser alterado pelo usuário)

class Car:
    def __init__(self, modelo):
        self.assentos = 5
        self.modelo = modelo

    def enter_race_mode(self):
        self.assentos = 2
    # Criamos, para esse objeto, um método de ativar modo de corrida, onde o carro fica só com 2 assentos, para ir mais rápido. A criação desse método segue o padrão de qualquer outra função do Pyhton, PORÉM, como um método (geralmente) altera os atributos do objeto, é necessário passar como argumento o self, para que o método seja capaz de alterar o objeto (self)

carro = Car("EcoSport")
print(carro.assentos)

carro.enter_race_mode()
print(carro.assentos)