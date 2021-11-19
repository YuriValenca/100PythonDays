#Receber um número de 2 dígitos e printar a soma de seus dígitos

number = input()

num1 = number[0]
num2 = number[1]

res = int(num1) + int(num2)

print(res)

#Vale ressaltar que o type default que vem do input é do tipo str (ou string), isso pq o Python leva em conta que qualque tipo de informação pode estar vindo do usuário, e o melhor tipo de dado para manusear isso é a string, por isso, se não fosse feito o cast na linha 8, o print seria a concatenação do 1o com o 2o dígito, resultando no próprio input