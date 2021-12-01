# Dicionários em python são similares aos da vida real, um termo, uma chave aliada a um valor, ou definição

dicionarioDeProgramacao = {
    "Bug" : "Um erro que ocorre num programa que impede que ele execute corretamente e/ou até o fim",
    "Funcao": "Um pedaço de código que pode ser executado se for chamado durante o código",     #É dito ser boa prática de dicionários, deixá-los com uma vírgula no final
    }
# O dicionário pode também ser visto como uma tabela:
# =========================================
# |      termo      |        valor        |
# |       Bug       |         ---         |
# |      Função     |         ---         |
# =========================================

# Busca de um valor pelo termo em um dicionário:
print(dicionarioDeProgramacao["Bug"])   # É NECESSÁRIO estar entre aspas se for uma string

# Adicionar itens ao dicionário:
dicionarioDeProgramacao["Loop"] = "Um pedaço de código que opera repetidamente"
print(dicionarioDeProgramacao)      # Lembrar que a adição ao dicionário é com colchetes [] e o dicionário em si, com chaves {}

print("\n")

# Deletar um dicionário inteiro:
novoDicionario = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
}
novoDicionario = {}
print (novoDicionario)

print("\n")

# Editar um elemento do dicionário:
dicionarioDeProgramacao["Bug"] = "Um erro no programa que impede que ele execute, gerando um código de erro para o usuário"
print(dicionarioDeProgramacao)

# Percorrendo um dicionário:
for key in dicionarioDeProgramacao:
    print(key)
# O laço for retorna somente os termos, ou chaves do dicionário

print("\n")

# Percorrendo um dicionário para imprimir tudo:
for key in dicionarioDeProgramacao:
    print(key)
    print(dicionarioDeProgramacao[key])