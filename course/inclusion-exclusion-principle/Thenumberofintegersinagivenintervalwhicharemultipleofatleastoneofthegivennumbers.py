import math

def solve(a, r):
    soma = 0
    for i in range(1, 1<<len(a)):
        cont = 0
        res = 1

        for j in range(len(a)):
            if(i >> j & 1):
                cont += 1
                res = math.lcm(res, a[j])

        res = r//res
        if cont % 2 == 0:
            soma -= res

        else:
            soma += res

    return soma



print(solve([2, 4, 3], 100))

