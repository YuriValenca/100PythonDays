# Nada escrito após o return da função é executado, pois esse comando de return diz ao Python que aquele é o fim da função. Então, para que a função possa ter ainda mais uso e retornar possíveis casos diferentes, pode-se fazer o seguinte:

def formatarNome(primeiroNome, sobrenome):
    if primeiroNome == "" or sobrenome == "":
        return "Inputs inválidos"
    pNomeFormatado = primeiroNome.title()
    sNomeFormatado = sobrenome.title()
    return f"{pNomeFormatado} {sNomeFormatado}"

print(formatarNome(input("Qual seu nome? "), input("Qual seu sobrenome? ")))