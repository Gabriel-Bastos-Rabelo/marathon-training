# for this problem i am using bfs

def shortest_path(graph, current, fila, distance, final):
    visited = set()
    visited.add(current)
    fila.append((current, distance))
    while (len(fila) > 0):
        node = fila[0]
        fila.pop(0)
        if node[0] == final:
            return node[1]
        for i in graph[node[0]]:
            if i in visited:
                continue
            fila.append((i, node[1] + 1))

    return -1


def buildGraph(edges):
    adjascent_list = {}
    for edge in edges:
        if edge[0] not in adjascent_list:
            adjascent_list[edge[0]] = []
        if edge[1] not in adjascent_list:
            adjascent_list[edge[1]] = []

        adjascent_list[edge[0]].append(edge[1])
        adjascent_list[edge[1]].append(edge[0])

    return adjascent_list


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


adjascent_list = (buildGraph(edges))

fila = []
print(shortest_path(adjascent_list, "w", fila, 0, "z"))
