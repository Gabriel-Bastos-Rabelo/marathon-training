import sys


#Solução 1: TLE
"""
crivo = []
MAX = 10004
def gerarCrivo(n):
    global crivo
    crivo = [True] * (n + 1)
    crivo[0] = crivo[1] = False
    for i in range(2, n + 1):
        if crivo[i]:
            for j in range(i + i, n + 1, i):
                crivo[j] = False



def gerarCrivo2(n):
    global crivo
    primos = []
    crivo = [True] * (n + 1)
    crivo[0] = crivo[1] = False
    for i in range(2, n + 1):
        if crivo[i]:
            primos.append(i)

        for j in range(len(primos)):
            if i * primos[j] > n:
                break

            crivo[i * primos[j]] = False
            if i % primos[j] == 0:
                break

gerarCrivo2(MAX)

while True:
    try:
        n = int(sys.stdin.readline())
        lista = list(map(int, sys.stdin.readline().split()))
        maior = max(lista)
        dif = 0
        total = (n) * (n - 1) * (n - 2) * (n - 3)//24
        for i in range(2, maior + 1):
            if crivo[i] == True:

                cont = 0
                for j in range(n):
                    if lista[j] % i == 0:
                        cont += 1

                if cont >= 4:
                    dif += (cont) * (cont - 1) * (cont - 2) * (cont - 3)//24

        print(total - dif)




    except EOFError:
        break
        
"""


#Solução 2
import math

MAX = 10000


# Precompute the Möbius function up to MAX
def compute_mobius(n):
    mu = [1] * (n + 1)
    isPrime = [True] * (n + 1)
    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i, n + 1, i):
                isPrime[j] = False
                mu[j] *= -1

            for j in range(i * i, n + 1, i * i):
                mu[j] = 0

    return mu


mu = compute_mobius(MAX)


while True:
    try:
        n = int(input())
        lista = list(map(int, input().split()))
        cnt = [0] * (MAX + 1)

        for num in lista:
            divisors = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    if i != num // i:
                        divisors.add(num//i)

            for d in divisors:
                cnt[d] += 1


        total_subsets = n * (n -1) * (n - 2) * (n - 3)//24
        res = 0

        for i in range(1, MAX + 1):
            if cnt[i] >= 4 and mu[i] != 0:
                subsets = cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) * (cnt[i] - 3) // 24
                res += mu[i] * subsets

        print(res)
    except EOFError:
        break