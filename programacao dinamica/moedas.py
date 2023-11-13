# https://br.spoj.com/problems/MOEDAS/


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


