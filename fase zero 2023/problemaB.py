lista = list(map(int, input().split()))
n = input()


res = 0
if n == 'A':
    res += lista[0]
    res += (3/2) * lista[1]
    res += (5/2) * lista[2]
    

elif n == 'B':
    res += lista[1]
    res += (2/3) * lista[0]
    res += (2 * (lista[2] * 5)/2)/3

else:
    res += lista[2]
    res += (lista[0] * 2)/(5)
    res += (3/5)  * lista[1]

print(int(res))