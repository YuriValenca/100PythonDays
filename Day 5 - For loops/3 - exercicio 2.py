# Programa para identificar o maior score de uma lista de entrada

scoreInput = input("Quais foram os scores? ")

scores = scoreInput.split(" ")

for maior in scores:
    highest = max(scores) # A função max irá salvar na variável highest o maior valor que ela identificou na lista scores

 # Outra maneira de calcular o máxima (dessa vez, sem a função max()), é a abaixo, onde uma variável iniciada com 0 serve como comparador para cada entrada da lista, se ela for maior que 0 (a primeira geralmente será), fica gravado esse número, até que venha um número maior que o que está gravado no comparador, para tomar seu lugar.
 
highestNoMax = 0
for cur in scores:
    cur = int(cur)
    if(cur > highestNoMax): # Nesse caso, é preciso fazer um cast pois a comparação interna que o max realiza, consegue lidar com strings, isso não é o caso com um simples if, por isso, cur precisa virar um int para ser comparado com 0. O cast pode sim ser feito da maneira da linha 12, onde a variável recebe um cast dela mesma!
        highestNoMax = cur

print(highest)
print(highestNoMax)

