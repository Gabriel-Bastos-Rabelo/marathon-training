import math

def lcm(a, b):
    return (a * b)//gcd(a, b)

def lcm_2(a, b):

    lista1 = divisores_primos(a)
    lista2 = divisores_primos(b)
    lista2_modificada = lista2.copy()

    
    for elemento in lista1:
        if elemento in lista2_modificada:
            lista2_modificada.remove(elemento)

    
    resultado = lista1 + lista2_modificada
    return math.prod(resultado)



    


def divisores_primos(n):
    primos = []
    for i in range(2, n + 1):
        if n % i == 0:
            
            while n % i == 0:
                primos.append(i)
                n = n//i
    return primos


print(divisores_primos(15))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



def crivo(n):
    divi = [1] * (n + 1)
    for i in range(2, n+1):
        if divi[i] == 1:
            for j in range(i, n+1, i):
                divi[j] = i
    
    return divi



print(lcm(15, 20))
print(lcm_2(15, 20))

print(crivo(15))


#a x b = LCM(a, b) * GCD (a, b)
#LCM(a, b) = (a x b) / GCD(a, b)