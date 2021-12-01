alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

saida = ''

def caesar(msg, amt, op):
    textoDeSaida = ""

    if op == 'decriptar':
        amt *= -1
    for char in msg:

        if char in alfabeto:
            posicao = alfabeto.index(char)
            novaPosicao = (posicao + amt) % 26        # Prevenção de números maiores ainda colocados como shift
            textoDeSaida += alfabeto[novaPosicao]
        else:       # Esse bloco de if/else faz com que símbolos/números e afins que não estejam no alfabeto, sejam printados mesmo assim, porém, não tratados pelo cipher
            textoDeSaida += char

    if op == 'decriptar':
        print(f"A mensagem decriptada é {textoDeSaida}")
    elif op == 'encriptar':
        print(f"A mensagem encriptada é {textoDeSaida}")
    else:
        print("Operação não reconhecida...")


continuar = True
while continuar:
    operation = input("Digite 'encriptar' ou 'decriptar' para realizar a operação que você deseja\n")
    texto = input("Digite a mensagem: \n").lower()
    shift = int(input("Digite a quantidade do offset do texto: \n"))
    caesar(msg=texto, amt=shift, op=operation)

    resultado = input("Digite 's' para continuar utilizando o programa e 'n' para parar de operar.\n")
    if resultado == 'n':
        continuar = False
        print("Espero que tenha gostado!")
