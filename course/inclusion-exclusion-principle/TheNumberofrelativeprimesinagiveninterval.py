import math

def solve(n, r):
    p = []

    for i in range(2, math.sqrt(n)):
        if n % i == 0:
            p.append(i)

            while n % i == 0:
                n /= i

    if n > 1:
        p.append(i)

    sum = 0
    for i in range(1, 1 << len(p)):
        cur = 1
        bit = 0

        for j in range(len(p)):
            if(i >> j & 1):
                bits += 1
                cur *= p[j]

        res = r//cur

        if bits % 2 == 0:
            sum -= res

        else:
            sum += res

    return r - sum






