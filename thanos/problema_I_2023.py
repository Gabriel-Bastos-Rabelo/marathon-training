def count_subarrays_with_odd_ones(N, arr):
    # Inicialização
    count_odd = 0
    count_even = 1  # Começamos com 1 para considerar o prefixo vazio como par
    total_odd_subarrays = 0
    current_ones = 0

    for num in arr:
        # Atualizar a contagem de 1s
        current_ones += num

        if current_ones % 2 == 0:
            # Se par, somamos os subvetores com prefixo ímpar
            total_odd_subarrays += count_odd
            # Atualizamos a contagem de prefixos pares
            count_even += 1
        else:
            # Se ímpar, somamos os subvetores com prefixo par
            total_odd_subarrays += count_even
            # Atualizamos a contagem de prefixos ímpares
            count_odd += 1

    return total_odd_subarrays

1, 10, 100, 10011, 100110


1001101

001101, 01101, 1101, 01, 1

-, 1001, 1 

# Leitura dos dados de entrada
N = int(input())
arr = list(map(int, input().split()))

# Resolução do problema
result = count_subarrays_with_odd_ones(N, arr)

# Impressão do resultado
print(result)
