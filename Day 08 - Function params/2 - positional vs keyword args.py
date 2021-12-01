# Funções com mais de um parâmetro

def saudacao(name, location):
    print(f"Opa, {name}!")
    print(f"Tudo bem aí em {location}")

saudacao("Yuri", "Recife")

# Argumentos posicionais são argumentos que dependem da posição, ou da ordem, em que são passados na chamada da função para que possam fazer sentido no contexto e na função. Por exemplo, se a chamada da função saudacao() tivesse seus argumentos invertidos...

saudacao("Recife", "Yuri")

# Os prints vão ficar totalmente sem sentido

# Para combater isso, é possivel utilizar os keyword arguments, dessa forma, é impossível que a função não produza o output desejado pelo usuário:

saudacao(location="Recife", name="Yuri")
# Mesmo passados na ordem errada, como as variáveis foram preenchidas com informações que fazem sentido, a função vai pegar o valor das variáveis e colocar dentro dela, sem haver confusão na passagem dos argumentos