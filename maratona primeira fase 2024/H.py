def allCombinations(num):
    for i in range(len(num)):
        if num[i]=='*':
            output  = allCombinations(num[:i]+'0'+num[i+1:])
            output += allCombinations(num[:i]+'1'+num[i+1:])
            return output
    return [num]
        



def mod_exp(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result


def mod_exp2(a, b, m):
    if b == 0:
        return 1 % m
    u = mod_exp2(a, b//2, m)
    u = (u * u) % m

    if b % 2 == 1:
        u = (u * a) % m

    return u

def toInteger(s, left, right):
    val = 0
    bitVal = 1
    for i in range(right, left-1, -1):
        if s[i]=='1':
            val += bitVal
        bitVal *= 2
    return val



def resto(m, n):
    n = toInteger(n, 0, len(n)-1)
    if n == 0:
        return 1
    
    # Inicializa `dec` com o valor do primeiro bit de `m`
    dec = int(m[0]) % n  
    
    # Itera sobre o restante dos bits, começando do segundo bit
    for i in range(1, len(m)):
        dec = (dec * 2 + int(m[i])) % n
    
    return dec


"""
#Solução 1
m = input()
n = input()

lista = []
lista2 = []
#combination(n, 0, [], lista)
#combination2(m, 0, [], lista2)

lista = allCombinations(n)
lista2 = allCombinations(m)
for i in lista2:
    achou = False
    numero = int(i, 2)
    for j in lista:
        if j != 0 and resto(i, j) == 0:
            print(i)
            achou = True
            break

    if achou:
        break
"""


#Solução 2

def validar(aa, bb):
    n = 0
    for i in range(len(bb)):
        n = ((2 * n) + int(bb[i]))

    m = 0

    for i in range(len(aa)):
        m = ((2 * m) + int(aa[i])) % n

    return m == 0


m = input()
n = input()

cnt = 0
for i in m:
    if i == '*':
        cnt += 1

for i in n:
    if i == '*':
        cnt += 1



ind = []

for index, i in enumerate(m):
    if i == '*':
        ind.append((0, index))

for index, i in enumerate(n):
    if i == '*':
        ind.append((1, index))


for mask in range((1 << cnt)):
    aa = list(m)
    bb = list(n)
    for i in range(cnt):
        if (mask & (1 << i)):
            if ind[i][0] == 0:
                aa[ind[i][1]] = '1'
            else:
                bb[ind[i][1]] = '1'

        else:
            if ind[i][0] == 0:
                aa[ind[i][1]] = '0'
            else:
                bb[ind[i][1]] = '0'

    if validar(''.join(aa), ''.join(bb)):
        print(''.join(aa))
        break

