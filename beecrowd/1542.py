
while(True):
    lista = list(map(int, input().split()))

    if(len(lista) == 1):
        break
    q, d, p = lista

    res = int((p * d)/abs(p - q) * q)

    if(res == 1):
        print("1 pagina")
    else:
        print(f"{res} paginas")


