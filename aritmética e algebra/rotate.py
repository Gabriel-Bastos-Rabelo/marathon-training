matriz = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matriz)):
    for j in range(i, len(matriz[0])):
        aux = matriz[i][j]
        matriz[i][j] = matriz[j][i]
        matriz[j][i] = aux



c = len(matriz[0]) - 1
for i in range(len(matriz)):
    for j in range(0, c//2+1):
        aux = matriz[i][j]
        matriz[i][j] = matriz[i][c - j]
        matriz[i][c - j] = aux


