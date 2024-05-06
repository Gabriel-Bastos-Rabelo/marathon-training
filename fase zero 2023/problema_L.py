

n, m = map(int, input().split())
s = int(input())

def mapear(x, y, r, n, m):
    xInicio = 0
    yInicio = 0
    xFinal = 0
    yFinal = 0
    if x - r < 1:
        xInicio = 1
    else:
        xInicio = x - r
    
    if y - r < 1:
        yInicio = 1
    else:
        yInicio = y - r

    if x + r > n:
        xFinal = n
    else:
        xFinal = x + r

    if y + r > m:
        yFinal = m
    else:
        yFinal = y + r

    return (xInicio, yInicio), (xFinal, yFinal)

matriz = [[0 for i in range(m)] for j in range(n)]


setores = [0 for i in range(s + 1)]

for i in range(s):
    x, y, r = map(int, input().split())
    inicio, fim = mapear(x, y, r, n, m)


    for i in range(inicio[0] - 1, fim[0]):
        for j in range(inicio[1] - 1, fim[1]):
            matriz[i][j] += 1
            


for i in range(n):
    for j in range(m):
        setores[matriz[i][j]] += 1

res = 0

for i in range(len(setores)):
    res += i * setores[i]

res = res/(n * m)

print(int(res))

    