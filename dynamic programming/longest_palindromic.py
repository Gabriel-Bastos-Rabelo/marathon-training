


#Solução 1: Modo recursivo usando DP para guardar valores já calculados no memo, não passa no tempo limite
def ehPalindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    return False

def dfs(palavra, left, right, memo):
    print(palavra[left: right])
    if ehPalindromo(palavra[left: right]):
        return palavra[left: right]
    elif palavra[left: right] in memo:
        return memo[palavra[left: right]]
    else:
        Lleft = dfs(palavra, left+1, right, memo)
        Lright = dfs(palavra, left, right-1, memo)
        if len(Lleft) > len(Lright):
            if palavra[left: right] not in memo:
                memo[palavra[left: right]] = Lleft
            return Lleft
        else:
            if palavra[left: right] not in memo:
                memo[palavra[left: right]] = Lright

            return Lright
        

#Solução 2

def longestPalindrome(s):

    reslen = 0
    res = ""

    for i in range(len(s)):
        l, r = i, i

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if(r-l + 1 > reslen):
                res = s[l: r+1]
                reslen = (r-l+1)
            
            l -= 1
            r += 1

        # este outro while irá servir para conseguir pegar as substring que tem tamanho par

        l, r = i, i+1

        while l>=0 and r < len(s) and s[l] == s[r]:
            if(r-l+1 > reslen):
                res = s[l : r + 1]
                reslen = r-l+1
            l -= 1
            r += 1

    return res





#solução 3


dp = [[0] * 5  for i in range(5)]

print(dp)

for i in range(5):
    dp[i][i] = True




def longest_palindromo(s):

    maiorPalindromo = s[len(s)-1: len(s)]

    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):

            if s[i] == s[j]:
                if j-i == 1 or dp[i+1][j-1] == True:
                    dp[i][j] = True

                    if len(maiorPalindromo) < len(s[i:j]):
                        maiorPalindromo = s[i:j+1]


    return maiorPalindromo


print(longest_palindromo("ababa"))



