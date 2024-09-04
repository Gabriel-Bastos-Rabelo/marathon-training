lista = list(map(int, input().split()))


achou = False
for i in lista:
    if i == 9:
        achou = True
        break

if achou:
    print("F")
else:
    print("S")