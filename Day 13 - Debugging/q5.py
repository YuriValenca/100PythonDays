a = 0
b = 0
c = 0

def calc(a):
    if(a < 1):
        return 0
    elif a == 1:
        return 1
    else:
        return (a + calc(a-1))

while a < 4:
    b = calc(a)
    c = c + b
    a += 1

print(c)