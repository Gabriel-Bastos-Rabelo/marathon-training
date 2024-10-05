#https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1266

import math
#solução 1
def solucao1(n, lista):
    cont = 0
    for i in range(1, n+1):
        for j in lista:
            if i % j == 0:
                cont += 1
                break
    return n - cont
    
#solução 2
def solucao2(n, lista):
    m = len(lista)
    res = 0
    for i in range(1, 1 << m):
        lcm = 1
        bits = 0
        for j in range(m):
            if(1 & (i >> j)):
                lcm = math.lcm(lcm, lista[j])
                bits += 1

        lcm = n//lcm
        if bits % 2 == 0:
            res -= lcm
        else:
            res += lcm

    return n - res






while True:
  try:
    
    n, m = map(int, input().split())
    lista = list(map(int, input().split()))
    
    print(solucao1(n, lista))
    print(solucao2(n, lista))
  except EOFError:
    break
  
