from implementaçãoMatriz import Grafo


n, c = map(int, input().split())

grafo = Grafo(n)

for i in range(c):
    lista = list(map(int, input().split()))
    grafo.inserirAresta(lista[2], lista[0])
    for i in range(3, len(lista)):
        grafo.inserirAresta(lista[i], lista[i - 1])

print(grafo.grafo)
for i in range(1, n):
    if sum(grafo.grafo[i]) == 0:
        print(i)