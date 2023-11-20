
"""#solução 1, deu erro em tempo de execução
def troco(idx, soma, moedas):
    if idx not in memo:
        memo[idx] = {}
    if soma == valor:
        memo[idx][soma] = 'S'
    
    elif soma > valor or idx >= len(moedas):
        memo[idx][soma] = 'N'
    
    elif(soma in memo[idx]):
        return memo[idx][soma]
       
    else:
        if troco(idx+1, soma+moedas[idx], moedas) == 'S' or troco(idx+1, soma, moedas) == 'S':
            memo[idx][soma] = 'S'
        else:
            memo[idx][soma] = 'N'
    
    return memo[idx][soma]
        """

"""valor, numeroMoedas = list(map(int, input().split()))
moedas = list(map(int, input().split()))
memo = {}

print(troco(0, 0, moedas))"""

#Solução 2



resposta = 'N'
def busca(coin, soma):
    global resposta
    
    if((str(soma) + str(coin)) in memo):
        return
    
    memo[str(soma) + str(coin)] = 1

    if(soma == valor):
        resposta = 'S'
        return
    
    if(soma > valor or coin >= numeroMoedas):
        return
    
    busca(coin+1, soma + moedas[coin])
    busca(coin +1, soma)

    return
    


valor, numeroMoedas = list(map(int, input().split()))
moedas = list(map(int, input().split()))
memo = {}

busca(0, 0)
print(resposta)

