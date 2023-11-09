
def triangle(n):
    lista = []
    antigaLista = []

    for i in range(n):
        novaLista = [0] * (i+1)
        novaLista[0] = 1
        novaLista[len(novaLista) - 1] = 1

        

        for j in range(1, len(novaLista)-1):
            novaLista[j] = antigaLista[j] + antigaLista[j-1]

        lista.append(novaLista)
        
        antigaLista = novaLista

    return

triangle(5)
