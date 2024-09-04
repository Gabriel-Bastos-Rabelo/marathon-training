n, alturaCarlito = map(int, input().split())
lista = list(map(int, input().split()))
cont = 0

for i in lista:
    if alturaCarlito >= i:
        cont += 1

print(cont)