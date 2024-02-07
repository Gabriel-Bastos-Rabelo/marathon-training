n = 4
dp = [-1] * (n+1)
def numeroTree(n):
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]

    dp[n] = 0
    
    for i in range(1, n + 1):
        dp[n] += numeroTree(i-1) * numeroTree(n - i)

    print(dp)
    return dp[n]

    



numeroTree(4)
