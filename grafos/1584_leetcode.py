import heapq

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

vertices = []

grafo = {}
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = abs((points[i][0] - points[j][0])) + abs((points[i][1] - points[j][1]))
        if i not in grafo:
            grafo[i] = [(distance, j)]
        else:
            grafo[i].append((distance, j))
        if j not in grafo:
            grafo[j] = [(distance, i)]
        else:
            grafo[j].append((distance, i))

        


def prim(grafo, inicial):
    visitados = set([inicial])
    res = 0
    vertices = [(weight, inicial, to) for weight, to in grafo[inicial]]
    print(vertices)
    heapq.heapify(vertices)

    while vertices:
        weight, frm, to = heapq.heappop(vertices)
        if to not in visitados:
            visitados.add(to)
        
            res += weight

            for distance, next_to in grafo[to]:
                if next_to not in visitados:
                    heapq.heappush(vertices, (distance, to, next_to))
    return res


                     


print(grafo)
print(vertices)
res = prim(grafo, 0)


print(res)

