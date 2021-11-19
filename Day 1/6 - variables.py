name = input("Qual seu nome?")      #Colocando o input numa variável, é possível reutilizar a informação colocada pelo usuário ao longo do código, bastando apenas invocar o nome da variável para associar o dado do usuário em determinado pedaço de código

print(name)     #Colocando print(name)já é uma reutilização do código, além de evitar esforço repetido do usuário no input

name = "nome1"
print(name)
name = "nome2"
print(name)
#O nome já diz, variável, é possível mudar o conteúdo do que está dentro ao longo do codigo. Porém, caso apenas o segundo print fosse codado, o valor printado seria o último antes da função, no caso, "nome2"
