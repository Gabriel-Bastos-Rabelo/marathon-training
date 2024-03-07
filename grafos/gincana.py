n, m = map(int, input().split())

g = [[] for i in range(n)]
visitados = [0] * n

for k in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    g[i].append(j)
    g[j].append(i)



def dfs(vertice, vizinhos):
    if visitados[vertice] == 0:
        visitados[vertice] = 1
        for i in vizinhos:
            dfs(i, g[i])


res = 0
for i in range(n):
    if visitados[i] == 0:
        res += 1
        dfs(i, g[i])

print(res)


        




