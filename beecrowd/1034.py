from sys import maxsize
from sys import setrecursionlimit


setrecursionlimit(10000000)

def min_blocks(blocos, m):
    if m == 0:
        return 0
    
    res = maxsize

    for i in blocos:
        if i <= m:
            sub_res = min_blocks(blocos, m - i)

            if sub_res != res and sub_res + 1 < res:
                res = sub_res + 1

    return res


def min_blocksDP(blocos, m, dp):
    if m == 0:
        return 0
    
    if dp[m] != -1:
        return dp[m]
    
    res = maxsize

    for i in blocos:
        if i <= m:
            sub_res = min_blocksDP(blocos, m - i, dp)
            if sub_res != maxsize and 1 + sub_res < res:
                res = sub_res + 1

    dp[m] = res
    return res



def min_blocksTabulation(blocos, m):
    dp = {0: 0}
    for i in range(1, m + 1):
        dp[i] = maxsize

    for i in range(1, m + 1):
        for j in blocos:
            if j <= i:
                if dp[i - j] != maxsize and 1 + dp[i - j] < dp[i]:
                    dp[i] = 1 + dp[i - j]

    return dp[m]




n = int(int(input()))

for i in range(n):
    n, m = map(int, input().split())
    dp = [-1] * (m + 1)
    lista = list(map(int, input().split()))
    print(min_blocksDP(lista, m, dp))
