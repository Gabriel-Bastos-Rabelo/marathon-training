n, k = map(int, input().split())

ropes = []
for i in range(n):
    ropes.append(int(input()))

maiorCorda = max(ropes)

def isPossible(ropes, k, tamanho):
    partes = 0
    for rope in ropes:
        if tamanho <= rope:
            partes += rope//tamanho


    return partes >= k



l = 0
r = maiorCorda

while(l <= r):
    mid = l + (r - l)/2
    if(isPossible(ropes, k, mid)):
        l = mid + 0.0000001
    else:
        r = mid - 0.0000001

print(f"{l:.2f}")
