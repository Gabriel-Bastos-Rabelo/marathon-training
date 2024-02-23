import math

def divisores_primos(n):
    aux = n
    divisores_primos = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if(aux % i == 0):
            divisores_primos.append(i)
            while(aux % i == 0):
                aux = aux//i

    if aux != 1:
        divisores_primos.append(aux)

    return divisores_primos



print(divisores_primos(15))
            





#1 2 3 4 5 6 7 8 9 10 11 12 13 14


#2 7