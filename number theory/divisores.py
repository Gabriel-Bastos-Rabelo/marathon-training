import math

def divisores(n):
    lista_divisores = []

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            lista_divisores.append(i)
            if i != n//i:
                lista_divisores.append(n//i)

    return lista_divisores


print(divisores(5))