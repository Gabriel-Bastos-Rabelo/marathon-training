#https://codeforces.com/gym/101350/problem/I

n = int(input())
allowed_chars = set(['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y'])


for i in range(n):
    s = input()
    tamanho = len(s)

    dp = [[0] * tamanho for l in range(tamanho)]
    maior = 0
    for j in range(tamanho):
        if(s[j] in allowed_chars):
            dp[j][j] = 1
            maior = 1


    for j in range(tamanho - 1, -1, -1):
        for k in range(j+1, tamanho):
            if s[j] == s[k] and (s[j] in allowed_chars and s[k] in allowed_chars):
                if k - j == 1 or dp[j+1][k - 1] == 1:
                    dp[j][k] = 1
                    
                    maior = max(maior, (k - j + 1))

    print(maior)
    