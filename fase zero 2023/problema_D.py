def isDivisible(number):
    print(number)
    if len(str(number)) == 1:
        return 
    numeroString = str(number)
    numero = (int(numeroString[:len(numeroString)-1])) * 3 + int(numeroString[-1])
    isDivisible(numero)



n = int(input())
isDivisible(n)
