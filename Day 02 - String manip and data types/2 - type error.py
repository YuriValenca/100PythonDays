num_char = len(input("Qual seu nome?"))

new_num_char = str(num_char) #Para corrigir o problema visto abaixo, podemos alterar o tipo de dado (fazer um cast). Para alterar para o tipo string, invocamos a função str, que recebe um parâmetro de qualquer tipo e transforma-o em string, permitindo a concatenação

print("Seu nome tem " + new_num_char + " caracteres") #Rodar esse programa causa um typeError, que diz que o Python só concatena strings com strings, e, nesse caso, num_char é int, então essa concatenação não é possível

type(num_char) #A função type retorna qual o tipo de dado do parâmetro

