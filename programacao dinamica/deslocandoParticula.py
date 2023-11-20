
#Ainda não consegui
def deslocando(xAtual, yAtual, n):
    if xAtual == x and yAtual == y:
        return 0
    
    if dp[xAtual][yAtual] != -1:
        return dp[xAtual][yAtual]
    
    else:
        atrator1 = 1 + deslocando((xAtual + atratores[0][0])//2, (yAtual + atratores[0][1])//2, n)
        atrator2 = 1 + deslocando((xAtual + atratores[1][0])//2, (yAtual + atratores[1][1])//2, n)
        atrator3 = 1 + deslocando((xAtual + atratores[2][0])//2, (yAtual + atratores[2][1])//2, n)
        atrator4 = 1 + deslocando((xAtual + atratores[3][0])//2, (yAtual + atratores[3][1])//2, n)
        dp[xAtual][yAtual] = min(atrator1, atrator2, atrator3, atrator4)
        return min(atrator1, atrator2, atrator3, atrator4)
    

N = 4
atratores = [(0, 0), (2**(N), 0), (2**(N), 2**(N)), (0, 2**(N))]
x = 12
y = 4

dp = [[-1 for j in range(100)] for i in range(100)]
print(deslocando(2**(N-1), 2**(N-1), N))
