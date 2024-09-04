import heapq

n, k = map(int, input().split())

heap = []
for i in range(k):
    heap.append([])

lista = []
for i in range(n):
    n, c = map(int, input().split())
    heapq.heappush(heap[c-1], (n, c))
    lista.append((n, c))

nova_lista = []

for bloco in lista:
    bloco_certo = heapq.heappop(heap[bloco[1] -1])
    nova_lista.append(bloco_certo)



ordenado = 'Y'

for i in range(1, len(nova_lista)):
    if nova_lista[i][0] < nova_lista[i-1][0]:
        ordenado = 'N'

print(ordenado)