n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

grafo = {}
for road in roads:
    if road[0] not in grafo:
        grafo[road[0]] = [road[1]]
    else:
        grafo[road[0]].append(road[1])

    if road[1] not in grafo:
        grafo[road[1]] = [road[0]]
    else:
        grafo[road[1]].append(road[0])

grafo_ordenado = dict(sorted(grafo.items(), key=lambda item: len(item[1])))

valores = {}
valor = 1
for i in grafo_ordenado:
    valores[i] = valor
    valor += 1

print(grafo)
print(valores)
def checagem(grafo, atual, lidos):
    res = 0
    for i in grafo[atual]:
        if (i, atual) not in lidos:
            res += (valores[i] + valores[atual])
            lidos.append((atual, i))
    return res
lidos = []
res = 0
for i in grafo:
    res += checagem(grafo, i, lidos)            
print(res)