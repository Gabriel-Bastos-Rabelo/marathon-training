
def trailingZeroes(n):
    fatorial = [1] * (n + 1)

    for i in range(1, n+1):
        fatorial[i] = fatorial[i-1] * i

    print(fatorial)

    
trailingZeroes(20)