n = int(input())
res = 0
menor = float('inf')
for i in range(n):
    lista = list(map(int, input().split()))
    if i == 0:
        if lista[0] < menor:
            menor = lista[0]
            res = 0
        if lista[n-1] < menor:
            menor = lista[n-1]
            res = 1
    elif i == (n-1):
        if lista[0] < menor:
            menor = lista[0]
            res = 4
        if lista[n-1] < menor:
            menor = lista[n-1]
            res = 3


print(res)