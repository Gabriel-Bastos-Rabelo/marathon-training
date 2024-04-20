def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return (a * b)/mdc(a, b)


n = int(input())


for i in range(n):
    numero = int(input())

    lista = list(map(int, input().split()))

    res = lista[0]

    for i in range(1, len(lista)):
        res = mmc(res, lista[i])

    print(int(res))