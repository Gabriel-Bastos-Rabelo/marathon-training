n = 4
g = {0: [(2, 5), (1, 2)], 1: [(2, 1), (3, 4)], 3: [(0, 3)]}

def shortestPathDijkstra(node1, node2):
    global n
    distances = {node: float('inf') for node in range(n)}

    distances[node1] = 0
    queue = [(0, node1)]
    visited = set()

    while queue:
        dist, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)

        for n, w in g.get(node, []):
            new_dist = dist + w
        
            if new_dist < distances[n]:
                distances[n] = new_dist
                queue.append((new_dist, n))

    return distances[node2]


print(shortestPathDijkstra(0, 0))

