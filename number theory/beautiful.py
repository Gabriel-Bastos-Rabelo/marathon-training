

a, b, n = map(int, input().split())

fatorial = [0] * (n+1)

fatorial[0] = 1
fatorial[1] = 1

for i in range(2, n+1):
    fatorial[i] = i * fatorial[i - 1]


res = 0
MOD = (10 ** 9 + 7)
def fexp(a, b):
    if b == 0:
        return 1
    if b %2 == 0:
        return fexp(a*a%MOD, b//2)
    
    return a * fexp(a, b-1) % MOD


def inverso(a):
    return fexp(a, MOD - 2)
def ehBonito(value, a , b):
    numero = str(value)
    for i in numero:
        if i != str(a) and i != str(b):
            return False
    return True

for i in range(n+1):
    soma = i * a + (n - i) * b
    if ehBonito(soma , a, b):
        res += fatorial[n] * inverso(fatorial[i]) % MOD * inverso(fatorial[n - i]) % MOD


print(int(res % (10**9 + 7)))

