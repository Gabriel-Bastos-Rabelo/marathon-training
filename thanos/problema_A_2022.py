n = int(input())

s = input()

cont = 0
res = 0

for i in s:
    if i == 'b':
        if cont > 1:
            res += cont
        cont = 0
    else:
        cont += 1

if cont > 1:
    res += cont

print(res)