vetor = [81, 37, 51, 77, 19]
nsei = 0
achou = True

while (achou):
    achou = False
    for i in range(4):
        if vetor[i] > vetor [i + 1]:
            nsei = vetor[i]
            vetor[i] = vetor[i + 1]
            vetor[i + 1] = nsei
            achou = True

for i in range (5):
    print(f"{vetor[i]}\n")