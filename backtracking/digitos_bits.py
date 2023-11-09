def recursao(n, lista):
    if len(lista) == n:
        print(lista)
    else:
        for i in range(1, n+1):
            if i not in lista:
                lista.append(i)
                recursao(n, lista)
                lista.pop()


recursao(3, [])
