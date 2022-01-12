R = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
cont = 0
a1 = 0

for i in range(4):
    a1 =+ 1
    for j in range(4):
        a1 = a1 + 2
        for k in range(4):
            a1 = a1 + 3
            R[i, j, k] = 2*i + j - 3*k
            cont += 1

print(R[2, 3, 1])