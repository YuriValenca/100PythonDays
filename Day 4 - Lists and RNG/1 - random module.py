import random
import aux_module # Cada arquivo criado no Python pode ser chamado de módulo, logo, além de importar módulos já presentes no próprio Python, como o random, é possível importar módulos criados e utilizar variáveis e funções presentes nesses módulos, tornando o código altamente enxuto e organizado

# A funcionalidade de import do Python permite que possamos utilizar novas funções de uma maneira muito mais simples do que escrever o código inteiro à mão. É como se pudessemos pegar uma parte do código de alguém emprestado. Nesse caso, importamos o random para utilizar as funções aliadas a esse módulo, pelo padrão nomeDoMódulo.funçãoDoMódulo

randomInt = random.randint(1, 10)
# Seguindo o padrão de chamada da função de um módulo, utilizamos a função randint (random integer) que recebe dois parâmetros (os limites dos numeros a serem randomizados INCLUINDO os parâmetros passados), para alocar à variável um número aleatório. Vale ressaltar que cada vez que o programa é rodado, um novo número é gerado, isso porque a função randint é novamente chamada

print(randomInt)
print(aux_module.pi) # Acessando a variável pi do módulo auxiliar seguindo o mesmo padrão de nomeDoArquivo.funçãoOuVariávelDesejada

randomNum = random.random() # Outra função do random é o random(), que gera um número float de 0 a 1, porém, sem incluir o 1
print(randomNum)

# A função random() parece ser limitada em uso, mas aliado à matemática básica, pode servir de uma grande ferramenta futuramente:

random3 = randomNum * 5 # Desse jeito, será criado um número aleatório entre 0 e 5 (porém, nunca 5), isso porque o resultado da chamada do random() será multiplicado por 5