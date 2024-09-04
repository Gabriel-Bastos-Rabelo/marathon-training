n = int(input())
lista = list(map(int, input().split()))

maior = 0

for i in lista:
    maior = max(maior, len(bin(i)[2:]))

lista_binaria = [bin(x)[2:].zfill(maior) for x in lista]

dicionario = {}
for i in range(maior):
    dicionario[2 ** i] = 0


for num in lista_binaria:
    for i in range(len(num)-1, -1, -1):

        dicionario[2 ** (maior-1 - i)] += int(num[i])


res = []
for i in range(n):
    valor = 0
    for key in dicionario:
        if dicionario[key] > 0:
            valor += key
            dicionario[key] -= 1

    res.append(valor)


print(*res)
        
