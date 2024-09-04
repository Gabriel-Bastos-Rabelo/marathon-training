n = int(input())

grafo = {}

for i in range(n):
    lista = list(map(int, input().split()))
    grafo[i] = {}
    for j in range(n):
        grafo[i][j] = lista[j]


def verificarCoerencia(grafo, acumulate, visited, current, final, initial):
    # Se o nó atual já foi visitado, retornamos 0 (nenhuma ação adicional necessária)
    if current in visited:
        return 0

    # Marca o nó atual como visitado
    visited.add(current)

    # Se chegamos ao destino final
    if current == final:
        # Verifica se o caminho acumulado é menor que o custo direto
        if acumulate < grafo[initial][final]:
            return -1  # Incoerente
        return 0  # Coerente

    # Se o caminho acumulado já excede o custo direto, paramos a exploração desse caminho
    if acumulate > grafo[initial][final]:
        return 0

    # Explora os vizinhos
    for i in grafo[current]:
        # Verifica recursivamente os caminhos a partir dos vizinhos
        result = verificarCoerencia(grafo, acumulate + grafo[current][i], visited, i, final, initial)
        if result == -1:
            return -1  # Se encontramos um caminho incoerente, propagamos o erro

    # Remover da lista de visitados ao voltar da recursão para outras possibilidades
    visited.remove(current)

    return 0  # Se todas as explorações foram coerentes, retornamos 0


def contarRemoviveis(N, grafo):
    removiveis = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Verificar se há algum k que faz o voo i-j desnecessário
            pode_remover = False
            for k in range(N):
                if k != i and k != j and grafo[i][j] == grafo[i][k] + grafo[k][j]:
                    pode_remover = True
                    break
            if pode_remover:
                removiveis += 1
    
    return removiveis


incoerente = False
for i in range(n):
    for j in range(i + 1, n):
        if verificarCoerencia(grafo, 0, set(), i, j, i) == -1:
            incoerente = True
            break

    if incoerente:
        break


if incoerente:
    print(-1)

else:
    print(contarRemoviveis(n, grafo))
        

        
        


