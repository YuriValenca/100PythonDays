# Função de ano bissexto do dia 3, arquivo 5 - exercise 3.py

def ehBissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def diasNoMes(ano, mes):
    diasEmUmMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ehBissexto(ano)
    if ehBissexto(ano) and mes == 2:
        return 29
    else:
        return diasEmUmMes[mes-1]


ano = int(input("Digite um ano: "))
mes = int(input("Digite um mês: "))
dias = diasNoMes(ano, mes)
print(dias)
