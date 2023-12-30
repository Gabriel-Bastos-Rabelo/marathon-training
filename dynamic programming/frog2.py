n, k = map(int, input().split())
lista = list(map(int, input().split()))

def menorCusto(n, k, lista):
    dp = [float('inf')] * (n)

    dp[0] = 0

    for i in range(n):
        for j in range(i+1, i+k+1):
            if j < n:
                dp[j] = min(dp[j], dp[i] + abs(lista[j] - lista[i]))

        
    
    return dp[n-1]

    


print(menorCusto(n, k, lista))