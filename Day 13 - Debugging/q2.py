a = 4

def qualquer(z, k):
    if z == 0 or z == k:
        return 1

    else:
        return qualquer(z-1, k) + qualquer (z-1, k-1)

print(qualquer(a, a-1))