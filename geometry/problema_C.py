import sys

sys.setrecursionlimit(100000000)

n = int(input())


def backt(atual, num, memo):
    if atual == num:
        return 1

    if atual > num:
        return 0

    if memo[atual] != -1:
        return memo[atual]

    res = backt(atual + 1, num, memo) + backt(atual + 2, num, memo)
    memo[atual] = res
    return res
    
    
for i in range(n):
    d = int(input())
    memo = [-1] * (d + 1)
    print(backt(0, d, memo))
