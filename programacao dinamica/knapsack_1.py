

#Minha solução usando recursividade, não passa no tempo limite
numeroItens, maxPeso = map(int, input().split())

listaItens = []
for i in range(numeroItens):
    peso, valor = map(int, input().split())
    listaItens.append((peso, valor))


def knapsack(pesoAtual, pesoMaximo, numeroItens, itemAtual, listaItens, listaAtual):
    if pesoAtual > pesoMaximo:
        return 0
    else:
        for i in range(itemAtual, numeroItens):
            listaAtual.append(listaItens[i])
            op1 = knapsack(pesoAtual + listaAtual[len(listaAtual) - 1][0], pesoMaximo, numeroItens, i+1, listaItens, listaAtual)
            listaAtual.pop()
            op2 = knapsack(pesoAtual, pesoMaximo, numeroItens, i+1, listaItens, listaAtual)
            

            return max(op1, op2)
        valor = 0
        for j in listaAtual:
            valor += j[1]
        return valor



#Solução usando dynamic programming, não passou no tempo limite

def knaspack_dp(listaItens, numeroItens, maxPeso):

    memo = [[0 for i in range(maxPeso+1)] for j in range(numeroItens+1)]
   
    
    for i in range(1, numeroItens+1):
        for j in range(1, maxPeso+1):
            if j < listaItens[i-1][0]:
                memo[i][j] = memo[i-1][j]
                
            else:
                memo[i][j] = max(listaItens[i-1][1] + memo[i-1][j-listaItens[i-1][0]], memo[i-1][j])
                


    return memo[numeroItens][maxPeso]





print(knaspack_dp(listaItens, numeroItens, maxPeso))