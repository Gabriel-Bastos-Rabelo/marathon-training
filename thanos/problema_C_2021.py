
b, l = map(int, input().split())

algs = list(map(int, input().split()))

def soma_digitos(numero, l):
    soma = 0
    for i in range(l):
        if i % 2 == 0:
            soma += int(numero[i])
        else:
            soma -= int(numero[i])

    return soma


soma = soma_digitos(algs, l)

if(soma % (b + 1) == 0):
    print(0, 0)
else:
    menor_substituir = min((soma % (b + 1)), ((b + 1) - soma))
    a = (soma % (b + 1))
    b = ((b + 1) - (soma % (b + 1)))
    achou = False
    for i in range(l):
        if i % 2 == 0:
            if a <= algs[i]:
                algs[i] -= a
                achou = True


        else:
            if b <= algs[i]:
                algs[i] -= b
                achou = True

        if achou:
            print(i + 1, algs[i])
            break

    if achou == False:
        print(-1, -1)

        

    