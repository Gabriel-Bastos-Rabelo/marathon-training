from itertools import combinations
from collections import defaultdict
import math

#Formal Description
#Given a set of numbers V = {vi} of size n, answer q queries of the following type: for a specific x, how many
#subsets of V , S ⊆ V , satisfy gcd(x, lcm(S)) = 1?


#Solução 1: Não passou no tempo limite

"""
def crivo_erastotones(limit):
    isPrime = [True] * (limit + 1)
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, limit + 1):
        if isPrime[i]:
            for j in range(i*i, limit+1, i):
                isPrime[j] = False

    primes = [num for num, prime in enumerate(isPrime) if prime]
    return primes



dicionario = defaultdict(dict)

def prime_factors(primos, n):
    i = 0
    numero = n
    while numero != 1:
        if numero % primos[i] == 0:
            numero //= primos[i]
            dicionario[n][primos[i]] = True

        else:
            i += 1


def calculte(n):
    pass



primos = crivo_erastotones((10**6) + 2)
n = int(input())
lista = list(map(int, input().split()))
for i in lista:
    prime_factors(primos, i)
q = int(input())



for i in range(q):
    numero = int(input())
    com = []
    for i in lista:
        if numero == 1:
            com.append(i)
        else:
            flag = False
            for j in dicionario[i]:
                if numero % j == 0:
                    flag = True
                    break
            
            if not flag:
                com.append(i)

    result = (2 ** len(com))
    print(result)
"""

"""
Solução 2: Não passa no tempo limite
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
lista = list(map(int, input().split()))
mod = (10 ** 9) + 7
q = int(input())

for i in range(q):
    numero = int(input())
    res = 1
    for j in lista:
        if math.gcd(numero, j) == 1:
            res = (res * 2) % mod

    print(res)

"""
"""
Solução 3: Não passa no tempo limite
MOD = (10 ** 9) + 7
def divisores(numero):
    result = []
    for i in range(2, numero//2 + 1):
        if numero % i == 0:
            result.append(i)

    result.append(numero)
    return result


n = int(input())
lista = list(map(int, input().split()))
q = int(input())

for i in range(q):
    numero = int(input())
    if numero == 1:
        print(2 ** n)
        continue
    div = divisores(numero)
    res = 0
    for j in div:
        for k in lista:
            if(math.gcd(numero, k) == j):
                res += 1
    res = len(lista) - res
    res = 2 ** res
    print(res % MOD)

"""

#Solução 4
"""
import sys
MOD = (10 ** 9) + 7
MAXV = 1000100  # Update MAXV to cover all possible Vi and Xi

def decompose2(n, fator):
    primos = set()
    while n > 1:
        primos.add(fator[n])
        n //= fator[n]
    return list(primos)

def gerarContagem(primos, cont):
    t = len(primos)
    for i in range(1, 1 << t):
        gcd = 1
        for j in range(t):
            if (1 << j) & i:
                gcd *= primos[j]
        cont[gcd] += 1

ehPrimo = [True] * (MAXV)
fator = [0] * (MAXV)
ehPrimo[0] = ehPrimo[1] = False
cont = [0] * (MAXV)
for i in range(2, MAXV):
    if ehPrimo[i]:
        fator[i] = i
        for j in range(i * 2, MAXV, i):
            if ehPrimo[j]:
                fator[j] = i
                ehPrimo[j] = False

n = int(sys.stdin.readline())
lista = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())

for num in lista:
    primos = decompose2(num, fator)
    gerarContagem(primos, cont)

for _ in range(q):
    num = int(sys.stdin.readline())
    primos = decompose2(num, fator)
    res = 0
    for i in range(1, 1 << len(primos)):
        gcd = 1
        bits = 0
        for j in range(len(primos)):
            if (1 << j) & i:
                bits += 1
                gcd *= primos[j]
        if bits % 2 != 0:
            res += cont[gcd]
        else:
            res -= cont[gcd]
    valid = pow(2, n - res, MOD)
    print(valid)

"""


#Solução 5
"""
MOD = 1000000007
MAXN = 1000009
MAXV = 100009
n = int(input())
lista = list(map(int, input().split()))

v = int(input())

pessoas = []

for i in range(v):
    pessoas.append(int(input()))


count = [0] * (MAXN + 1)

def decompose(n, fator):
    primos = set()
    while n > 1:
        primos.add(fator[n])
        n //= fator[n]

    return list(primos)
    

primes = [True] * (MAXN + 1)
fator = [0] * (MAXN + 1)
for i in range(2, MAXN):
    if primes[i]:
        fator[i] = i
        for j in range(i * i, MAXN, i):
            fator[j] = i
            primes[j] = False


for i in lista:
    primos = decompose(i, fator)
    t = len(primos)
    for i in range(1, 1 << t):
        gcd = 1
        for j in range(t):
            if 1 << j & i:
                gcd = gcd * primos[j] % MOD

        count[gcd] += 1


for pessoa in pessoas:
    primos = decompose(pessoa, fator)
    t = len(primos)
    res = 0

    for i in range(1, 1 << t):
        bits = 0
        gcd = 1
        for j in range(t):
            if 1 << j & i:
                gcd = gcd * primos[j]
                bits += 1
        if bits % 2 == 1:
            res += count[gcd] % MOD

        else:
            res -= count[gcd] % MOD

    print(pow(2, n - res, MOD))


"""







    



