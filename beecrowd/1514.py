while True:
    n, m = map(int, input().split())
    if(n + m == 0):
        break
    
    dicionario = {}
    for i in range(m):
        dicionario[i] = 0
    contest = []
    for i in range(n):
        lista = list(map(int, input().split()))
        contest.append(lista)
        for j in range(len(lista)):
            dicionario[j] += lista[j]

    cont = 0
    for i in dicionario:
        if dicionario[i] == 0:
            cont += 1
            break

    for i in dicionario:
        if dicionario[i] == n:
            cont += 1
            break


   

    for i in contest:
        if sum(i) == 0:
            cont += 1
            break

    for i in contest:
        if sum(i) == m:
            cont += 1
            break

        
    print(4 - cont)