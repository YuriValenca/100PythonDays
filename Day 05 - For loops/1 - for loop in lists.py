# O loop, ou estrutura de repetição é um asset do Python que ajudará em situações que o mesmo comando deve ser usado repetidamente. O padrão de um for é do tipo: for item in listaTal. Ou seja, para cada item na listaTal, ele vai executar o bloco de comando relativo ao que está identado dentro do for (assim como if/else, a identação está presente nas estruturas de repetição)

frutas = ["maçã", "banana", "pêra"]

for fruta in frutas:  # Aqui, a variável fruta não existe, mas é criada para poder ser iterada no bloco de comando relativo ao for, caso contrário, a lista inteira seria iterada, e não cada item individualmente
    print(fruta)
    print("Torta de " + fruta)  # Esse comando será executado antes da próxima fruta, pois o bloco que é executado diversas vezes, e não linha por linha
