# Os parametros da função build são:
# O índice do nó atual, o l e o r do intervalo representado pelo nó.

def build(node, l, r):
    if l == r:
        tree[node] = vet[l]
        return

    mid = (l+r)//2

    # Chamaremos a função build para as duas metades, que são:
    # O filho da esquerda: Com nó 2*node+1 e com intervalo de l até mid.
    # O filho da direita: Com nó 2*node+2 e com intervalo mid+1 até r.
    build(2*node+1, l, mid)
    build(2*node+2, mid+1, r)

    tree[node] = tree[2*node+1] + tree[2*node+2]


# Os parametros da função Update são:
# O nó atual, tl e tr, o intervalo que o nó atual abrange, idx e x, o índice que queremos atualizar e o seu valor.

def update(node, tl, tr, idx, x):

    # Se o nó atual é uma folha, então ele representa o intervalo de idx até idx.
    # Então, atualizaremos o seu valor e retornaremos a função.
    if tl == tr:
        tree[node] = x
        vet[l] = x
        return

    # Caso contrário, declararemos mid como o índice que divide o nó atual em duas metades.
    mid = (tl+tr)//2

    # Se idx se encontra no intervalo de tl até mid, atualizaremos o filho da esquerda
    # do nó atual, pos ele abrange o intervalo de tl até mid.
    # Senão, então ele se encontra de mid+1 até r, então:
    # Basta atualizarmos o filho da direita do nó atual.

    if idx >= tl and idx <= tr:
        update(node, tl, mid, idx, x)
    else:
        update(node, mid+1, tr, idx, x)

    # Após termos atualizado um dos dois filhos, atualizaremos o valor do nó atual.
    tree[node] = tree[2*node+1] + tree[2*node+2]


vet = [1, 2, 4, 3, 5, 10]

tree = [0] * 15

build(0, 0, len(vet)-1)

print(tree)