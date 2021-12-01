alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operation = input("Digite 'encriptar' ou 'decriptar' para realizar a operação que você deseja\n")

texto = input("Digite a mensagem: \n").lower()

shift = int(input("Digite a quantidade do offset do texto: \n"))

def encriptar(msg, amt):
    textoCodificado = ""    # Texto inicialmente em branco, que vai receber concatenações das letras encriptadas
    for letra in texto:
        posicao = alfabeto.index(letra)         #Função index que retorna a posição da letra no alfabeto
        novaPosicao = posicao + amt             # A nova posição será a posição da letra atualmente + a quantidade passada pelo usuário

        if novaPosicao > len(alfabeto)-1:                  # Esse if vai gerenciar possíveis erros de out of bounds, por exemplo um texto 'zz' com amount 2, ao inves de resultar em 
            novaPosicao = novaPosicao - len(alfabeto)      # 'bb', resultaria num erro, pois não seria possível localizar o b após o z na lista

        textoCodificado += alfabeto[novaPosicao]           # A letra nova é colocada na string de texto codificado

    print(f"O texto encriptado é: {textoCodificado}")

if operation == "encriptar":
    encriptar(msg = texto, amt = shift)  # Idealmente, o método keyword é feito na chamada da função, e não na sua definição