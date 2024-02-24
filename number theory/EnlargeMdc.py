n = int(input())
valores = list(map(int, input().split()))

def gdc(a, b):
    if b == 0:
        return a
    return gdc(b, a%b)

d = 0

divi = [1] * (max(valores) + 1)

for i in range(2, max(valores) + 1):
    if divi[i] == 1:
        for j in range(i,max(valores) + 1 , i):
            divi[j] = i

for i in valores:
    d = gdc(i, d)

primos_cont = {}

for i in valores:
    primos = []
    while(i > 1):
        print(i)
        print(divi[i])
        primos.append(divi[i])
        i = i//divi[i]

    if primos:
        if primos[0] in primos_cont:
            primos_cont[primos[0]] += 1
        else:
            primos_cont[primos[0]] = 1

    for j in range(1, len(primos)):
        if primos[j] != primos[j-1]:
            if primos[j] in primos_cont:
                primos_cont[primos[j]] += 1
            else:
                primos_cont[primos[j]] = 1


ans = n
for i in primos_cont:
    if n - primos_cont[i] != 0:
        ans = min(ans, n - primos_cont[i])

if ans == n:
    print(-1)
else:
    print(ans)

            

    