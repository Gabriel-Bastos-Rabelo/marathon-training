p = input()
n = int(input())



p = list(p)

while True:
    mov = 0
    for i in range(len(p)):
        if i+n < len(p):
            if p[i] > p[i + n]:
                p[i], p[i + n] = p[i + n], p[i]
                mov += 1
        else:
            break

    if mov == 0:
        break


print("".join(p))


import heapq

def lexicographically_minimal_string(S, K):
    n = len(S)
    S = list(S)
    for i in range(K):
        # Usamos uma heap para encontrar a melhor opção de troca
        heap = []
        for j in range(i, n, K):
            heapq.heappush(heap, (S[j], j))
        
        # Agora, começamos as trocas gananciosas
        for j in range(i, n, K):
            smallest_char, idx = heapq.heappop(heap)
            if S[j] != smallest_char:
                # Troca apenas se encontrar uma melhor opção
                S[j], S[idx] = S[idx], S[j]
    
    return ''.join(S)

# Leitura da entrada
S = input().strip()
K = int(input().strip())

# Chamando a função e imprimindo a resposta
result = lexicographically_minimal_string(S, K)
print(result)