def maxSumDivThree(A):
    dp = [0, 0, 0]
    for a in A:
        for i in dp[:]:
            dp[(i + a) % 3] = max(dp[(i + a) % 3], i + a)
    return dp[0]


A = [3,6,5,1,8]
maxSumDivThree(A)
                