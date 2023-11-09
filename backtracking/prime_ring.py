def ehPrimo(elm1, elm2):
    soma = elm1 + elm2
    if (soma == 2):
        return True
    cont = 0
    for i in range(1, soma):
        if soma % i == 0:
            cont += 1
        if cont > 1:
            return False

    return True


def ring(n, i, lista, lista_geral):
    if len(lista) == n:
        if (ehPrimo(lista[0], lista[n-1])):
            lista_geral.append(lista.copy())

    for j in range(1, n+1):
        if j not in lista:
            if (ehPrimo(j, lista[len(lista) - 1]) == False):
                continue
            else:
                lista.append(j)

                ring(n, i, lista, lista_geral)
                lista.pop()

    return lista_geral


case1 = int(input())
case2 = int(input())

lista_case1 = ring(case1, 2, [1], [])
lista_case2 = ring(case2, 2, [1], [])

print("Case 1:")
for i in lista_case1:

    for index, j in enumerate(i):
        if index == len(i) - 1:
            print(j, end = "")
        else:

            print(j, end=" ")
    print()

print("Case 2:")
for i in lista_case2:
    for index, j in enumerate(i):
        if index == len(i) - 1:
            print(j, end = "")
        else:

            print(j, end=" ")

    print()
