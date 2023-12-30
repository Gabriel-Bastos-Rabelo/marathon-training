while True:
    try:
        n, taxas = list(map(int, input().split()))
        valores = list(map(int, input().split()))
        memo = [0] * n
        for i in range(len(valores)):
            maiorValor = 0
            for j in range(i+1, len(valores)):
                valor = (valores[j] - valores[i] - taxas) + memo[i]
                memo[j] = max(memo[j], valor, maiorValor)
                maiorValor = memo[j]
        print(memo[len(memo)-1])
    except EOFError:
        break





