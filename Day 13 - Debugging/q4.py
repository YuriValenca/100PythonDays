w = [2, 13, 11, 9, 7, 0]
z = [3, 10, 11, 8, 0, 4]

vet = [1, 2, 3, 4, 5, 6]

i = 0
x = 0
U = 0
P = 0

for i in range(6):
    if(w[i] > z[i]):
        x = z[i]
        z[i] = w[i]
        w[i] = x
    else:
        w[i] = w[i]*2
        z[i] = z[i]*3
U = 0

for i in range(6):
    U = U + w[i]
    P = P + z[i]

print(U, P)