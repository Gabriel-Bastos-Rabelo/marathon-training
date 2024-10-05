#https://atcoder.jp/contests/dp/tasks/dp_y/
import sys
sys.setrecursionlimit(10**6)

#Solução 1: TLE
"""
dx = [1, 0]
dy = [0, 1]
memo = {}
def backtracking(initial, final, current, blocked):
    if current == final:
        return 1
    
    if current[0] > final[0] or current[1] > final[1]:
        return 0
    
    if current in blocked:
        return 0
    
    if current in memo:
        return memo[current]

    res = backtracking(initial, final, (current[0] + dx[0], current[1] + dy[0]), blocked) + backtracking(initial, final, (current[0] + dx[1], current[1] + dy[1]), blocked)
    memo[current] = res
    return res
h, w, n = map(int, input().split())
blocked = {}

for i in range(n):
    x, y = map(int, input().split())
    blocked[(x, y)] = 1


print(backtracking((1, 1), (h, w), (1, 1), blocked))
"""


#Solução 2: Runtime Error por causa do tamanho do vetor
"""
h, w, n = map(int, input().split())

blocks = set()

for _ in range(n):
    x, y = map(int, input().split())
    blocks.add((x, y))

MOD = 10**9 + 7
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[1][1] = 1  # Começa da posição (1, 1)

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if (i, j) not in blocks:
            if i > 1:
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if j > 1:
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD

print(dp[h][w])
"""


h, w, n = map(int, input().split())


blocks = []
MOD = 10**9 + 7

for _ in range(n):
    x, y = map(int, input().split())
    blocks.append((x, y))

fatorial = [1] * (h + w)
inv_fact = [1] * (h + w)

for i in range(2, h + w):
    fatorial[i] = (fatorial[i -1] * i) % MOD

inv_fact[h + w - 1] = pow(fatorial[h + w - 1], MOD - 2, MOD)
for i in range(h + w - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

 
def comb(n, k):
    return fatorial[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

blocks.append((h, w))
blocks.sort()
dp = [1] * (n + 1)
for i in range(n + 1):
    x, y = blocks[i]
    dp[i] = comb(x + y - 2, x - 1) % MOD

    for j in range(i):
        if blocks[j][0] <= x and blocks[j][1] <= y:
            dp[i] = (dp[i] - (comb(x + y - blocks[j][1] - blocks[j][0], x - blocks[j][0]) * dp[j] % MOD)) % MOD


print(int(dp[n]))