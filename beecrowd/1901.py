n = int(input())

floresta = []

for i in range(n-1):
    lista = list(map(int, input().split()))
    floresta.append(lista)


posicoes = []

dicionario = {}
for i in range(n * 2):
    posicoes.append(list(map(int, input().split())))

cont = 0
for i in range(len(posicoes)):
    print(floresta[posicoes[i][0] - 1][posicoes[i][1] - 1])
    if floresta[posicoes[i][0] - 1][posicoes[i][1] - 1] not in dicionario:
        dicionario[ floresta[posicoes[i][0] - 1][posicoes[i][1] - 1]] = 1
        cont += 1
print(dicionario)
print(cont)


