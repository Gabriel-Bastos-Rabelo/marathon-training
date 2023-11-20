
dp = [[0] * 6 for i in range(6)]
s = "xyzyyx"
partes = [0] * 6

for i in range(6):
    dp[i][i] = 1

for i in range(len(s)-1, -1, -1):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            if j-i == 1 or dp[i+1][j-1] == 1:
                dp[i][j] = 1

print(dp)
for i in range(0, len(s)):
    if dp[0][i] == 1:
        partes[i] = 1
    else:
        menor = float('inf')

        for j in range(1, i+1):
            if dp[j][i] == 1 and partes[j-1]+1<menor:
                menor = partes[j-1]+1

        partes[i] = menor


                
print(partes[5])
