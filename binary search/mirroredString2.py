#https://codeforces.com/gym/101350/problem/I

n = int(input())
lista = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y']
for i in range(n):
    s = input()
    tamanho = len(s)

    dp = [[0] * tamanho for l in range(tamanho)]
    for j in range(tamanho):
        if s[j] in lista:
            dp[j][j] = 1

    maior = 1
    for j in range(tamanho - 1, -1, -1):
        for k in range(j+1, len(s)):
            if s[j] == s[k]:
                if k - j == 1 or dp[j+1][k - 1] == 1:
                    dp[j][k] = 1
                    if(k - j + 1) > maior:
                        maior = k - j + 1

    print(maior)
    