# Toda vez que chamamos uma fução pertencente ao Python, ou algum módulo importado, vemos uma pequena descrição, um tooltip, do que aquela função faz e/ou retorna, isso é um docstring, e é possível fazer isso com as funções criadas também!

def formatarNome(primeiroNome, sobrenome):
    """Essa é a docstring dessa função. formatarNome irá receber o nome e sobrenome do usuário e retornar em title case (primeira letra maiúscula)."""
    if primeiroNome == "" or sobrenome == "":
        return "Inputs inválidos"
    pNomeFormatado = primeiroNome.title()
    sNomeFormatado = sobrenome.title()
    return f"{pNomeFormatado} {sNomeFormatado}"

formatarNome("yURI", "vALENÇA")

# As docstrings são delimitadas pelas aspas triplas e têm de estar na primeira linha da função. As aspas triplas permitem, ainda, comentários de múltiplas linhas. Contudo, se associadas a uma variável, as aspas triplas funcionam como um input ou texto de múltiplas linhas, por isso não é boa prática utilizar as aspas triplas como comentários. Assim que a função for chamada, o programador conseguirá ver a tooltip contendo a docstring dada pela função.