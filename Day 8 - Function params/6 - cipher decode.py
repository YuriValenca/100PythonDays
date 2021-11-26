alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Digite 'encriptar' ou 'decriptar' para realizar a operação que você deseja\n")

texto = input("Digite a mensagem: \n").lower()

shift = int(input("Digite a quantidade do offset do texto: \n"))

# Naturalmente, o processo de decriptação da mensagem fará o processo reverso ao do módulo anterior, com isso em mente, basta apenas modificar os sinais e variáveis para se adaptarem ao funcionamento correto da função

def decriptar(msg, amt):
    textoDecodificado = ""
    for letra in texto:
        posicao = alfabeto.index(letra)
        novaPosicao = posicao - amt 

        if novaPosicao < 0:         # A verificação de posição, caso ela, nesse caso, seja menor que um índice da lista muda um pouco, se o índice for menor que 0, adiciona a quantidade de letras no alfabet (len(alfabeto)) à esse número negativo
            novaPosicao = novaPosicao + len(alfabeto)

        textoDecodificado += alfabeto[novaPosicao]
    
    print(f"O texto encriptado é: {textoDecodificado}")

if operation == "decriptar":
    decriptar(msg = texto, amt = shift)