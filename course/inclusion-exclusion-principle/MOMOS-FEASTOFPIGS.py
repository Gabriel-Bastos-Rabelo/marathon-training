#https://www.spoj.com/problems/MOMOS/
#Solução 1 - TLE

"""
n, k = map(int, input().split())
dicionario = {}
comidos = 0

for i in range(k):
    porco = int(input())
    for j in range(0, n, porco):
        if j % porco == 0 and j not in dicionario:
            dicionario[j] = 1
            comidos += 1
            


print(n - comidos)
"""
#Solução 2 usando princípio da inclusão-exclusão
import math
n, k = map(int, input().split())
porco = []

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

for i in range(k):
    porco.append(int(input()))

if n <= 1e6 and k > 20:
    eaten = [False] * (n)
    for a in porco:
        for i in range(0, n, a):
            eaten[i] = True
    uneaten = eaten.count(False)
    print(uneaten)

else:
    soma = 0    

    for i in range(1, 1 << k):
        bits = 0
        lcm_value = 1
        for j in range(k):
            if((i >> j & 1) and porco[j] != 0):
                bits += 1
                lcm_value = lcm(lcm_value, porco[j])
        res = (n-1)//lcm_value
        res += 1
        if bits % 2 == 0:
            soma -= res
        else:
            soma += res

    print(n - soma) 
