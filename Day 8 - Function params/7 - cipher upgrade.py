# Como haviam poucas mudanças entre as funções de decriptar e encriptar, é possível transformá-las em apenas uma função

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Digite 'encriptar' ou 'decriptar' para realizar a operação que você deseja\n")

texto = input("Digite a mensagem: \n").lower()

shift = int(input("Digite a quantidade do offset do texto: \n"))

saida = ''

def caesar(msg, amt, op):
    textoDeSaida = ""

    if op == 'decriptar':       # Se a operação for para decriptar, ou seja, reverter o offset, basta verificar isso e trocar o sinal do shift amount
        amt *= -1
    for letra in msg:
        posicao = alfabeto.index(letra)
        novaPosicao = posicao + amt
        textoDeSaida += alfabeto[novaPosicao]
    
    if op == 'decriptar':
        print(f"A mensagem decriptada é {textoDeSaida}")
    elif op == 'encriptar':
        print(f"A mensagem encriptada é {textoDeSaida}")
    else:
        print("Operação não reconhecida...")

caesar(msg=texto, amt=shift, op=operation)