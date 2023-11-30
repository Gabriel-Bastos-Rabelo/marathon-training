N, x, y = list(map(int, input().split()))

posicaoInicial = (2**(N-1), 2**(N-1))
atrator1 = (0,0)
atrator2 = (0, 2**(N))
atrator3 = (2**(N), 2**(N))
atrator4 = (2**(N), 0)
posicaoFinal = (x, y)

memo = {}
def deslocandoParticulas(posicao, posicaoFinal):
    if(posicao[0] == posicaoFinal[0] and posicao[1] == posicaoFinal[1]):
        return 0
    if(posicao[0] % 1 != 0.000 or posicao[1] % 1 != 0.000):
        return float('inf')
    if(posicao in memo):
        return memo[posicao]
    
    primeiraop =  1 + deslocandoParticulas(((posicao[0] + atrator1[0])/2, (posicao[1] + atrator1[1])/2), posicaoFinal)
    segundaop = 1 + deslocandoParticulas(((posicao[0] + atrator2[0])/2, (posicao[1] + atrator2[1])/2), posicaoFinal)
    terceiraop = 1 + deslocandoParticulas(((posicao[0] + atrator3[0])/2, (posicao[1] + atrator3[1])/2), posicaoFinal)
    quartaop = 1 + deslocandoParticulas(((posicao[0] + atrator4[0])/2, (posicao[1] + atrator4[1])/2), posicaoFinal)

    minimo = min(primeiraop, segundaop, terceiraop, quartaop)
    memo[posicao] = minimo

    return minimo


print(deslocandoParticulas(posicaoInicial, posicaoFinal))

    







salas = {"sala1": {"horario1": "solicitacao1"}}