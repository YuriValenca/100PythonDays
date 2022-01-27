# Utilizar as classes alheias é muito bom, mas muitas vezes, é necessário criar classes do zero, e aqui vai uma guideline de como fazer isso

class User:
    pass

# Se estivermos criando uma classe, ou até uma função e, por hora, não é necessário colocar algo dentro desse bloco identado, o Python retornará um erro, porém, é possível contornar isso utilizando o comando pass, que fará com que o compilador pule o bloco identado, pois não há nada ali (se houver, ele vai pular mesmo assim)

user1 = User()

# Vale lembrar que o jeito correto de declarar uma classe é com PascalCase, que diz que a primeira letra de cada palavra deve ser maiúscula, então a classe de um carro de fórmula 1 deve ser: carro_f1 = FormulaOneCar()

# Atributos podem ser criados fora do escopo do construtor da classe
user1.name = "Yuri"
user1.age = 23

print(user1.name)
print(user1.age)

# Porém, isso não é muito indicado, pois em casos onde há muitos objetos de uma classe, cada atributo de cada objeto da classe teria de ser feito "à mão", além de cansativo, extensivo e propenso a erros, é também, difícil de se realizar manutenção num código assim
# Colocando os atributos no construtor da classe, é possível simplificar e melhorar a criação de um objeto, pois ele ja vai conter tais atributos

class Usuario:
    def __init__(self, name):
        # Para inicializar os atributos, é necessário chamar dentro do construtor da classe a função especial __init__, dentro dos argumentos dessa função, passamos os atributos que ela terá, e quando um objeto for criado e chamar a classe, é possível passar diretamente o valor desse atributo
        self.atributo1 = name
        # Self é o próprio objeto, então, passando o argumento name, quando o atributo1 do objeto for invocado, ele vai ser equivalente ao que for passado como name. Em geral, essa linha seria escrita da seguinte maneira: self.name = name, mas nesse caso, escrevi assim para mostrar que o name do self e o name que ele recebe são diferentes

user = Usuario("Yuri")
# Isso é a mesma coisa que user.atributo1 = "Yuri"

print(user.atributo1)

# É interessante notar que, muitas vezes, a classe terá valores default iniciados, isso significa que nem sempre será necessário passar todos os argumentos ao criar um objeto que invoca uma classe:

class InstagramAccount:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        # Quando uma conta do Instagram é criada, o usuário inicia sem seguidores, então em casos como esse, não é necessário passar o valor de followers nos argumentos da função init nem quando a classe é invocada na criação de um objeto

conta_instagram = InstagramAccount("123321123321", "@chechaboy")
print(conta_instagram.username)
# Nesse print, será exibido o valor passado na criação do objeto conta_instagram
print(conta_instagram.followers)
# Porém esse, vai conter o valor default da classe