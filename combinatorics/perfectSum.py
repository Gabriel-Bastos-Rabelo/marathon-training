def fun(pos, soma, arr, dp):
    if pos >= len(arr):
        return soma == 0
    else:

        if dp[pos][soma] != -1:
            return dp[pos][soma]
        
        ans = 0
        ans += fun(pos + 1, soma, arr, dp)

        if arr[pos] <= soma:
            ans += fun(pos + 1, soma - arr[pos], arr, dp)

    dp[pos][soma] = ans
    return ans

soma = 10
n = 6
dp = [[-1] * (soma+1) for i in range(n)]
print(dp)
print(fun(0, 10, [5, 2, 3, 10, 6, 8], dp))

#com programação dinâmica

dp = [[-1] * (soma + 1) for i in range(n)]

dp[0][0] = 1

num = [5, 2, 3, 10, 6, 8]

for i in range(1, len(dp[0])):
    dp[0][i] = 0


for i in range(1, len(dp)):
    for j in range(dp[0][i]):
        if num[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = dp[i-1][j] + + dp[i - 1][j - num[i - 1]]
print(dp)
print(dp[n-1][soma])
