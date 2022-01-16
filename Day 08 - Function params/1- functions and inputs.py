# Relembrando o conteúdo de funções...

def saudacao():
    print("Opa")
    print("Bem vindo(a)")
    print("Isso é uma função\n")

saudacao()

# Em geral, o funcionamento de uma função pode ser independente:

# def minhaFuncao():
#     Faça isso
#     Depois isso
#     Por fim isso

# Porém, é possível que, dentro dos parênteses de minhaFuncao(), seja passado o chamado argumento, que fará com que seja possível que a função trabalhe utilizando e modificando esse argumento passado pra ela:

# def minhaFuncao(essaCoisa):
#     Faça isso com essaCoisa
#     Depois isso com essaCoisa
#     Por fim isso          # Não necessariamente todos os comandos da função precisam envolver o argumento passado.

def saudacaoPorNome(name):
    print(f"Opa, {name}. Tudo bem?")
    print("Bem vindo(a)")
    print("Isso é uma função")

saudacaoPorNome("Yuri")  # O argumento passado na chamada da função, levará a informação para dentro dela, e ai a função pode utilizar essa variável interna dentro de seu bloco de código identado

# Note que não foi definido em nenhum momento a variável name e mesmo assim o código rodou tranquilo, isso acontece pois o Python cria internamente uma variável name e, na chamada da função, atribui a essa variável o valor "Yuri". Chamamos então o name de PARÂMETRO e "Yuri" de ARGUMENTO.