
import math
n, s, t = map(int, input().split())

dir = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    dir.append([(a, b), (c, d)])

def calcDistancia(a, b):
    dist = math.sqrt(pow(b[0] - a[0], 2)+ pow(b[1] - a[1], 2))
    return dist
pos = (0, 0)

visitados = 0
dicionario_visit = {}
menor_dist= float('inf')
proximo = (0, 0)
proximo_seg = 0
res = 0


while visitados < n:
    for i in range(n):
        if i not in dicionario_visit:
            distancia1 = calcDistancia(pos, dir[i][0])
            distancia2 = calcDistancia(pos, dir[i][1])
            menor_dist = min(menor_dist, distancia1, distancia2)
            if menor_dist == distancia1:
                proximo = dir[i][0]
                proximo_seg = i
            elif menor_dist == distancia2:
                proximo = dir[i][1]
                proximo_seg = i

    res += (menor_dist/s)
    print(menor_dist/s)
    if proximo == dir[proximo_seg][0]:
        distancia = calcDistancia(proximo, dir[proximo_seg][1])
        pos = dir[proximo_seg][1]

    else:
        distancia = calcDistancia(proximo, dir[proximo_seg][0])
        pos = dir[proximo_seg][0]
    visitados += 1
    dicionario_visit[proximo_seg] = True
    res += (distancia/t)
    print(distancia/t)



print(res)


        