#https://www.spoj.com/problems/NGM2/
import math
def solucao1(n, lista):
    cont = 0
    for i in range(1, n+1):
        for j in lista:
            if i % j == 0:
                cont += 1
                break

    return n - cont


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solucao2(n, lista):
    m = len(lista)
    res = 0
    for i in range(1, 1 << m):
        lcm_value = 1
        bits = 0
        for j in range(m):
            if(1 & (i >> j)):
                lcm_value = lcm(lcm_value, lista[j])
                bits += 1



        count = n // lcm_value
        if bits % 2 == 0:
            res -= count
        else:
            res += count

    return n - res

n, k = map(int, input().split())
lista = list(map(int, input().split()))

print(solucao2(n, lista))