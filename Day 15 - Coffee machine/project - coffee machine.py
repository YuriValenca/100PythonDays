# Primeiro pergunta qual café o usuário quer (podendo aceitar um report como entrada);
# Digitar off acaba o programa;
# Checar se os recursos são suficientes pra fazer o café;
# Processar moedas e troco, verificando se a quantia total paga o café;
# Fazer o café e consumir os recursos.

MENU = {
    "espresso": {
        "ingredientes": {
            "água": 50,
            "café": 18,
        },
        "valor": 1.5,
    },
    "latte": {
        "ingredientes": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "valor": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "valor": 3.0,
    }
}

recursos = {
    "água": 300,
    "leite": 200,
    "café": 100,
}

saldo = 0

maqLigada = True

def contarMoedas():
    print("Favor inserir moedas")
    total = int(input("Quantas de 1 real? "))
    total += int(input("Quantas de 50 centavos? ")) * 0.5
    total += int(input("Quantas de 25 centavos? ")) * 0.25
    total += int(input("Quantas de 10 centavos? ")) * 0.1
    total += int(input("Quantas de 5 centavos? ")) * 0.05
    return total

def verificarTransacao(dinheiroRecebido, custoBebida):
    if dinheiroRecebido >= custoBebida:
        troco = round(dinheiroRecebido - custoBebida, 2)
        print(f"Aqui está R$ {troco:.2f} de troco.")
        global saldo
        saldo += custoBebida
        return True
    else:
        print("Dinheiro não foi suficiente, receba ele de volta.")
        return False

def recursosSuficientes(ingredientes):
    for item in ingredientes:
        if ingredientes[item] > recursos[item]:
            print(f"Desculpe, não há {item} suficiente para essa escolha.")
            return False
    return True

def passarCafe(nomeBebida, ingredientes):
    for item in ingredientes:
        recursos[item] -= ingredientes[item]
    print(f"Aqui está seu {nomeBebida}, aproveite!")


while maqLigada:
    userInput = input("Que café você vai querer? Espresso, Cappuccino ou Latte?\n")
    if userInput == "off":
        maqLigada = False
    elif userInput == "report":
        print(f"Nível de água: {recursos['água']}ml")
        print(f"Nível de café: {recursos['café']}mg")
        print(f"Nível de leite: {recursos['leite']}ml")
        print(f"Receita da máquina: R$ {saldo:.2f}")
    else:
        bebida = MENU[userInput]
        if recursosSuficientes(bebida["ingredientes"]):
            pagamento = contarMoedas()
            if verificarTransacao(pagamento, bebida["valor"]):
                passarCafe(userInput, bebida["ingredientes"])