#leetcode 1277


def countSquares(matriz):
    result = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1:
                if i == 0 or j == 0:
                    result += 1
                else:
                    matriz[i][j] = matriz[i][j] + min(matriz[i-1][j], matriz[i][j-1], matriz[i-1][j-1])
                    result += matriz[i][j]

    
    return result



print(countSquares([[0,0,0],[0,1,0],[0,1,0],[1,1,1],[1,1,0]]))