import math

print(math.gcd(6, 9))
MOD = 998244353
def prime_factors(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            factors.append(i)
        while n % i == 0:
            n /= i
    

    if n != 1:
        factors.append(int(n))

    return factors
def correctMultiples(m, prev, current, uselessNumbers):
    left = prev//current
    left_primes = []
    for i in uselessNumbers:
        if left % i == 0:
            left_primes.append(i)

    totalMultiples = m//current
    res = totalMultiples

    for i in range(1, 1 << len(left_primes)):
        cr = 1
        bits = 0
        for j in range(len(left_primes)):
            if (i & (1 << j)):
                cr *= left_primes[j]
                bits += 1

        if bits % 2 == 0:
            res += (totalMultiples//cr) % MOD

        else:
            res -= (totalMultiples//cr) % MOD
    return res

def solve():
    n, m = map(int, input().split())
    lista = list(map(int, input().split()))


    for i in range(len(lista) - 1):
        if lista[i] % lista[i + 1] != 0:
            return 0
        
    res = 1
    uselessNumbers = prime_factors(lista[0])

    for i in range(1, len(lista)):
        if lista[i] == lista[i-1]:
            res = res * (m // lista[i])
            res %= MOD

        else:
            res = res * correctMultiples(m, lista[i-1], lista[i], uselessNumbers)
            res %= MOD
        
    return res

t = int(input())

for i in range(t):
    print(solve())






