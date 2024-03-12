lista = []
while True:
    a, v = map(int, input().split())

    if a == 0 and v == 0:
        break

    g = {node: [] for node in range(1, a + 1)}

    for i in range(v):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    maior = 0
    aeroporto = []
    for i in g:
        if len(g[i]) > maior:
            maior = len(g[i])
            aeroporto = [i]  
        elif len(g[i]) == maior:
            aeroporto.append(i)

    aeroporto.sort()
    lista.append(aeroporto)

for index, i in enumerate(lista):
    print(f'Teste {index+1}')
    for j in i:
        print(j, end = ' ')
    print()
    print()
