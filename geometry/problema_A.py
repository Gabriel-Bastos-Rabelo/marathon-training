n = int(input())

lista= list(map(int, input().split()))

def imprimir(lista):
    for i in range(len(lista)):
        if i == len(lista) - 1:
            print(lista[i])
        else:
            print(lista[i], end = " ")

while True:
    imprimir(lista)
    pos = int(input())

    if pos == -1:
        break

    valor = int(input())

    lista[pos] = valor

