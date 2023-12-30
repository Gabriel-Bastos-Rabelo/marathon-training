


def dfs(prices, dias, memo):
                
            for i in range(len(prices)-1, -1, -1):
                dias[i] = prices[i] - memo[i]

            return max(dias)

prices = [7,1,5,3,6,4]
dias = [0] * len(prices)

memo = [0 for _ in range(len(prices))]

menor = prices[0]
for i in range(0, len(prices)):
    memo[i] = menor

    if prices[i] < menor:
          menor = prices[i]


print(memo)

print(dfs(prices, dias, memo))

print(dias)