
#solução usando força bruta, backtracking
res = []
res_backtracking = []
lista = ["a", "e", "i", "o", "u"]
dicionario = {"a": ["a", "e", "i", "o", "u"], "e": ["e", "i", "o", "u"], "i": ["i", "o", "u"], "o": ["o", "u"], "u": ["u"]}

def backtracking(n, top, lista_atual, letra):

    if n == top:
        res.append(lista_atual.copy())
        return
    else:
        for i in dicionario[letra]:
            lista_atual.append(i)
            backtracking(n+1, top, lista_atual, i)
            lista_atual.pop()

        
    return


for i in lista:
    backtracking(1, 3, [i], i)

print(res)


#solução usando pd

memo = [1 for i in range(5)]

def pd(n):

    for i in range(1, n):
        for j in range(len(memo)-2, -1, -1):
            memo[j] += memo[j+1]

    res = 0
    for i in memo:
        res += i
    return res
    

print(pd(2))








