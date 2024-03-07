n = int(input())
g = [[] for _ in range(n)]
dist = [-1] * n

for k in range(n-1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    g[i].append(j)
    g[j].append(i)


def dfs(vertice):
    for i in g[vertice]:
        if dist[i] == -1:
            dist[i] = dist[vertice] + 1
            dfs(i)


dist[0] = 0
dfs(0)

pos = -1
distMax = 0
for i in range(n):
    if dist[i] > distMax:
        distMax = dist[i]
        pos = i

dist = [-1] * n

dist[i] = 0
dfs(i)

print(max(max(dist), 0))



