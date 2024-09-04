
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



"""resposta = 'N'
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
"""

#solução 4

def solve(n, moedas, index):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if(memo[n] != -1):
        return memo[n]
    
    for i in range(index, len(moedas)):
        if(solve(n-moedas[i], moedas, i+1) == 1):
            memo[n] = 1
        
    return memo[n] == 1


valor, numeroMoedas = list(map(int, input().split()))
moedas = list(map(int, input().split()))
memo = [-1] * (valor+1)
res = solve(valor, moedas, 0)
if(res):
    print("S")
else:
    print("N")


#solução 5
"""
def solve(i, left):
    if left == 0:
        return 1
    if left < 0:
        return 0
    if i >= numeroMoedas:
        return 0
    
    if(resp[i][left] == -1):
        resp[i][left] = solve(i+1, left-valores[i]) + solve(i+1, left)

    return resp[i][left]
    

valor, numeroMoedas = list(map(int, input().split()))
valores = list(map(int, input().split()))
resp = [[-1] * (valor+1)] * (numeroMoedas)
res = solve(0, valor)
if(res == 1):
    print("S")
else:
    print("N")

"""

