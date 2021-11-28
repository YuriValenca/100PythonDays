number = int(input("Coloque um número para verificar se ele é par ou ímpar: "))

if number % 2 == 0:     #O opeador % não tem a ver com porcentagem, ele refere-se ao módulo dessa divisão, ou seja, número/2 se o RESTO for 0 (se for par), ele entrará no bloco condicional do if, se for ímpar, do else. Outro exemplo de %: 6 % 4 = 2, pois o resto da divisão é 2.
    print("Seu número é par!")
else:
    print("Seu número é ímpar!")