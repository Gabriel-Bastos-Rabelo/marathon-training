n, m = map(int, input().split())


aux = [0] * (m + 2)
matriz = []
matriz.append(aux)

for i in range(n):
    lista = [0]
    outra = list(input())
    lista += outra
    lista += [0]
    matriz.append(lista)

matriz.append(aux)


res = 0


for i in range(1, len(matriz)-1):
    for j in range(1, len(matriz[1])-1):
        if matriz[i][j] == '#':
            
            if matriz[i-1][j] == '.' or matriz[i-1][j] == 0 or matriz[i+1][j] == '.' or matriz[i+1][j] == 0 or matriz[i][j+1] == '.' or matriz[i][j+1] == 0 or matriz[i][j-1] == '.' or  matriz[i][j-1] == 0:
                res += 1


print(res)