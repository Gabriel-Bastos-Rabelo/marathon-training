# leetcode 29

def generate(n, lista, lista_geral, opened, closed):
    if closed > opened:
        return
    if opened > n:
        return

    if opened == n and closed == n:
        lista_geral.append(lista.copy())

    else:
        lista.append("(")
        generate(n, lista, lista_geral, opened+1, closed)
        lista.pop()
        lista.append(")")
        generate(n, lista, lista_geral, opened, closed+1)
        lista.pop()

    return lista_geral


possibilidades = generate(1, [], [], 0, 0)


def paraString(possibilidades):
    listaStrings = []
    texto = ""
    for s in possibilidades:
        texto = texto.join(s)
        listaStrings.append(texto)
        texto = ""

    return listaStrings


print(paraString(possibilidades))
