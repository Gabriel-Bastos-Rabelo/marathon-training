# https://br.spoj.com/problems/MOEDAS/

#solução 1, está dando erro em tempo de execução no spoj
"""
def minimo_moedas(valor, moedas, memo, idx):
    if(valor == 0):
        return 0
    if(valor < 0):
        return float("inf")
    if(idx >= len(moedas) and valor > 0):
        return float("inf")
    if(memo[idx][valor] == -1):
        memo[idx][valor] = min(1+minimo_moedas(valor-moedas[idx], moedas, memo, idx), minimo_moedas(valor, moedas, memo, idx+1))
    
    return memo[idx][valor]



while True:
    inputsUser = list(map(int, input().split()))
    if inputsUser[0] == 0:
        break
    valor, numeroMoedas = inputsUser
    moedas = list(map(int, input().split()))
    memo = [[-1 for j in range(valor+1)] for i in range(len(moedas))]

    minimoMoedas = minimo_moedas(valor, moedas, memo, 0)
    
    if minimoMoedas == float("inf"):
        print("Impossível")
    else:
        print(minimoMoedas)
"""

#solução 2

"""
def minimo_moedas(coins, m, V):
    if V == 0:
        return 0
    
    else:
        res = float('inf')
        for i in range(0, m):
            if coins[i] <= V:
                sub_res = minimo_moedas(coins, m, V-coins[i])

                if(sub_res != float('inf') and sub_res +1 < res):
                    res = sub_res + 1
        
    return res



while True:
    inputsUser = list(map(int, input().split()))
    if inputsUser[0] == 0:
        break
    valor, numeroMoedas = inputsUser
    moedas = list(map(int, input().split()))
    

    minimoMoedas = minimo_moedas(moedas, numeroMoedas, valor)
    
    if minimoMoedas == float("inf"):
        print("Impossível")
    else:
        print(minimoMoedas)
"""

#solução 3

"""def minimo_moedas(coins, m, V):
    memo = [0] * (V+1)

    memo[0] = 0

    for i in range(1, len(memo)):
        memo[i] = float('inf')


    for i in range(0, len(memo)):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                sub_res = memo[i-coins[j]]
                if(sub_res != float('inf') and sub_res + 1 < memo[i]):
                    memo[i] = sub_res+1
    
    if memo[V] == float('inf'):
        print("Impossível")
    else:
        print(memo[V])
    
while True:
    inputsUser = list(map(int, input().split()))
    if inputsUser[0] == 0:
        break
    valor, numeroMoedas = inputsUser
    moedas = list(map(int, input().split()))
    

    minimoMoedas = minimo_moedas(moedas, numeroMoedas, valor)
   """ 
    

def minimo_moedas(valor, moedas, index):
    if valor == 0:
        return 0
    elif valor < 0:
        return float("inf")
    elif index >= numeroMoedas:
        return 0
    elif memo[index][moedas] != -1:
        return memo[index][moedas]
    else:
        memo[index][valor] = min(1+minimo_moedas(valor-moedas[index], moedas, index+1), minimo_moedas(valor, moedas, index+1))

    return memo[index][valor]
    