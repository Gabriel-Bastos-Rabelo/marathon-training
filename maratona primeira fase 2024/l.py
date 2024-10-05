
"""
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
        
"""

#Solução 2 - Não passa no tempo limite O(n²)
"""
n = int(input())
lista = list(map(int, input().split()))
maior = 0
for i in lista:
    maior = max(maior, len(bin(i)[2:]))

lista_binaria = [bin(x) for x in lista]


for i in range(len(lista_binaria)):
    for j in range(i+1, len(lista_binaria)):
       antigo = lista_binaria[i]
       numero = int(lista_binaria[i], 2) | int(lista_binaria[j], 2)
       lista_binaria[i] = bin(numero)
       lista_binaria[j] = bin(int(lista_binaria[j], 2) & int(antigo, 2))
      


for i in range(len(lista_binaria)):
    lista_binaria[i] = int(lista_binaria[i], 2)


print(*lista_binaria)
"""


#Solução 3 com bitmask

from collections import defaultdict 
d = defaultdict(int)

max_len = (10**9).bit_length()

input()
l = list(map(int, input().split()))

for i in l:
    for k in range(max_len):
        if i & (1<<k):
            d[k] +=1

for i in range(len(l)):
    for k in d.keys():
        v = l[i] & (1<<k)
        if d[k] > 0:
            if not v:
                l[i] |= 1 << k
            d[k] -= 1
        else:
            if v:
                l[i] ^= 1 << k
print(*l)

