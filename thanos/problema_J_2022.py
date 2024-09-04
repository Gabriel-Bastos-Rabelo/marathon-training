dicionario = {}

for i in range(1, 14):
    dicionario[i] = 4

n = int(input())

def calculaSoma(cartas):
    soma = 0
    for carta in cartas:
        if carta >= 10:
            soma += 10
        else:
            soma += carta
        dicionario[carta] -= 1

    return soma

joao = list(map(int, input().split()))
somaJoao = calculaSoma(joao)


maria = list(map(int, input().split()))
somaMaria = calculaSoma(maria)


usadas = list(map(int, input().split()))
for i in usadas:
    if i >= 10:
        somaJoao += 10
        somaMaria += 10

    else:
        somaJoao += i
        somaMaria += i
    
    dicionario[i] -= 1



if (23 - somaMaria) < 10:
    if dicionario[(23 - somaMaria)] > 0:
        minimoJoaoEstourar = 24 - somaJoao
        estorou = False
        if minimoJoaoEstourar >= 11:
            print((23 - somaMaria))
        else:
            for i in range(minimoJoaoEstourar, 14):
                if dicionario[i] > 0:
                    estorou = True
                    break
            if i >= 10 and estorou and (somaMaria + 10) <= 23:
                print(min((23-somaMaria), 10))
            elif estorou and (somaMaria + i) <= 23:
                print(min((23-somaMaria), i))
            else:
                print((23 - somaMaria))
    else:
        minimoJoaoEstourar = 24 - somaJoao
        estorou = False
        if minimoJoaoEstourar >= 11:
            print(-1)
        else:
            for i in range(minimoJoaoEstourar, 14):
                if dicionario[i] > 0:
                    estorou = True
                    break
            if i >= 10 and estorou and (somaMaria + 10) <= 23:
                print(10)
            elif estorou and (somaMaria + i) <= 23:
                print(i)
            else:
                print(-1)



elif (23 - somaMaria) == 10:
    for i in range(10, 14):
        if dicionario[i] > 0:
            break

    if dicionario[i] > 0:
        minimoJoaoEstourar = 24 - somaJoao
        estorou = False
        if minimoJoaoEstourar >= 11:
            print((23 - somaMaria))
        else:
            for i in range(minimoJoaoEstourar, 14):
                if dicionario[i] > 0:
                    estorou = True
                    break
            if i >= 10 and estorou and (somaMaria + 10) <= 23:
                print(min((23-somaMaria), 10))
            elif estorou and (somaMaria + i) <= 23:
                print(min((23-somaMaria), i))
            else:
                print((23 - somaMaria))

    else:
        minimoJoaoEstourar = 24 - somaJoao
        estorou = False
        if minimoJoaoEstourar >= 11:
            print(-1)
        else:
            for i in range(minimoJoaoEstourar, 14):
                if dicionario[i] > 0:
                    estorou = True
                    break
            if i >= 10 and estorou and (somaMaria + 10) <= 23:
                print(10)
            elif estorou and (somaMaria + i) <= 23:
                print(i)
            else:
                print(-1)


else:

    minimoJoaoEstourar = 24 - somaJoao
    estorou = False
    if minimoJoaoEstourar >= 11:
        print(-1)
    else:
        for i in range(minimoJoaoEstourar, 14):
            if dicionario[i] > 0:
                estorou = True
                break
        if i >= 10 and estorou and (somaMaria + 10) <= 23:
            print(10)
        elif estorou and (somaMaria + i) <= 23:
            print(i)
        else:
            print(-1)





