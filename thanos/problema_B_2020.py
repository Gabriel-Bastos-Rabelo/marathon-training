n = int(input())

matriz = [[0 for i in range(10)] for i in range(10)]
lista= []
for i in range(n):
    d, l, r, c = map(int, input().split())
    r -= 1
    c -= 1
    lista.append((d, l, r, c))
   
valido = True
for (d, l, r, c) in lista:
    if d == 0:
        for i in range(l):
            if (c + i) >= 10 or matriz[r][c + i] == 1:
                valido = False
                break
            else:
                matriz[r][c + i] = 1
    else:
        for i in range(l):
            if (r + i) >= 10 or matriz[r + i][c] == 1:
                valido = False
                break
            else:
                matriz[r + i][c] = 1

    if valido == False:
        break


if valido:
    print("Y")

else:
    print("N")