def linearSieve(n):
    crivo = [True] * (n + 1)
    primos = []
    crivo[0] = crivo[1] = False

    for i in range(2, n + 1):
        if crivo[i]:
            primos.append(i)

        for j in range(len(primos)):
            if i * primos[j] > n:
                break

            crivo[i * primos[j]] = False
            if i % primos[j] == 0:
                break

    print(crivo)
    print(primos)



linearSieve(100)