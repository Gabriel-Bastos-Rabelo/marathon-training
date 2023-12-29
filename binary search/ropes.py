n, k = map(int, input().split())

ropes = []
for i in range(n):
    ropes.append(int(input()))


def isPossible(ropes, k, tamanho):
    partes = 0
    for rope in ropes:
        if tamanho <= rope:
            partes += rope//tamanho