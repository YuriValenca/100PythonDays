# Implementando uma calculadora

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

# O dicionário abaixo irá guardar o sinal como chave e a função associada como valor (pulo do gato!)
operations = {
    "+" : adicao,
    "-" : subtracao,
    "*" : multiplicacao,
    "/" : divisao,
}

def calculadora():
    continua = True
    numero1 = float(input("Qual o 1º número? "))
    # O for abaixo irá imprimir apenas as chaves do dicionário!
    for simbolo in operations:
        print(simbolo)

    while continua:

        operacaoUser = input("Escolha uma das operações acima para realizar: ")
        numero2 = float(input("Qual o próximo número? "))

        # Pega o input e chama a função de acordo com o dicionário
        funcaoCalculo = operations[operacaoUser]

        # Como as funções de cálculo possuem um return, funcaoCalculo pode ser armazenado em uma variável de resposta
        res = funcaoCalculo(numero1, numero2)

        print(f"{numero1} {operacaoUser} {numero2} = {res}")
        if input(f"Digite 's' para continuar operando com o número {res:.4f}, ou 'n' para começar de novo. ") == 's':
            numero1 = res
        else:
            continua = False
            calculadora()       # Primeira recursão do curso. Quando o usuário quiser começar de novo, a função se chama novamente, resetando TODAS as variáveis. Recursão deve ser tratada com cuidado, pois é fácil de se chegar num loop infinito com ela. TODA FUNÇÃO RECURSIVA, DEVE TER UMA CONDIÇÃO DE PARADA.

calculadora()