

# 2685 leetcode
# using DFS
def explore(grafo, current, visited):

    global nodes_number
    nodes_number += 1

    if current in visited:
        return False
    


    number_edges.add(len(grafo[current]))

    visited.append(current)
    for node in grafo[current]:
        if node not in visited:
            explore(grafo, node, visited)
    return True


adjascent_matriz = {}

n = int(input())
for i in range(n):
    adjascent_matriz[i] = []

lista = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]


for edge in lista:

    adjascent_matriz[edge[0]].append(edge[1])
    adjascent_matriz[edge[1]].append(edge[0])





visited = []
number_edges = set()
res = 0
for i in range(n):
    number_edges.clear()
    nodes_number = 0
    if i not in visited:
        explore(adjascent_matriz, i, visited)
        if len(number_edges) == 1 and (nodes_number-1) in number_edges:
            res += 1

print(res)
