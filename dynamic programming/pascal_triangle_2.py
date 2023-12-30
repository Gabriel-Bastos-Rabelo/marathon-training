
def triangle(n, lista, top):
    if n == top:
        
        return lista
    else:
        novaLista = [0] * (len(lista)+1)
        novaLista[0] = 1
        novaLista[len(novaLista)-1] = 1
        for i in range(1, len(novaLista)-1):
            novaLista[i] = lista[i-1] + lista[i]

       
        
        return triangle(n+1, novaLista, top)

   

print(triangle(0, [1], 3))