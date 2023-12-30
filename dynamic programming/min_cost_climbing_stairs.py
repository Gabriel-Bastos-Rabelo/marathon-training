def minCostClimbingStairs(cost):

        tamanhoLista = len(cost)
        memo = [float('inf')] * tamanhoLista
        memo[0] = cost[0]
        memo[1] = cost[1]

        for i in range(tamanhoLista):
            for j in range(i+1, i+3):
                print(memo)
                if j < tamanhoLista:
                    memo[j] = min(memo[j], memo[i] + cost[j])
                else:
                    memo[tamanhoLista - 1] = min(memo[tamanhoLista-1], memo[i])
        return memo[tamanhoLista - 1]


print(minCostClimbingStairs([10,15,20]))
