z = 0
b = 0
a = 0

veet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for z in range(1, 14):
    b = z + 1
    veet[z] = b + (3*z)
    if (z > 0):
        if veet[b] < veet[z]:
            a = a + 2
        else:
            a = a - 1

if(veet[5] > veet[10]):
    for z in range(5, 16):
        veet[z] = veet[z] + 1
else:
    for z in range(1, 11):
        veet[z] = veet[z] - 2

print(veet[5])