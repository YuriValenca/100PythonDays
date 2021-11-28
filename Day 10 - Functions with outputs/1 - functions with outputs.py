# Já foram vistas funções "normais", com parâmetros e argumentos e funções que aceitam inputs, agora, será a hora das funções com output:

# def minhaFuncao():
#     Faça 3 + 2
#     Armazena em resultado
#     return resultado

# A função com output fará com que a linha que chamou a função minhaFuncao() seja substituída pela variável que saiu da função via a palavra reservada "return"

# output = minhaFuncao()
# output = resultado


# Função com parâmetros e print dentro
def formatarNome(primeiroNome, sobrenome):
    print(primeiroNome.title())
    print(sobrenome.title())

formatarNome("YURI", "VaLenÇA")

print("\n")


# Função em que o print é substituído por output e esse output é armazenado em uma variável (notar que a chamada da função poderia, ainda, estar dentro do print())
def formatarNome2(primeiroNome, sobrenome):
    pNomeFormatado = primeiroNome.title()
    sNomeFormatado = sobrenome.title()
    return f"{pNomeFormatado} {sNomeFormatado}"

stringFormatada = formatarNome2("YURI", "VaLenÇA")
print (stringFormatada)

# À primeira vista, é possível ver que funções com outputs provêem muita flexibilidade ao código, visto que uma chamada de função possa querer modificar o output (mas ainda necessitar do que o bloco de código da função faz), enquanto outra chamada pode necessitar da saída da função "crua"