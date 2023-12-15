#solução recursiva usando programação dinâmica

def editDistance(m, n):
    if m == 0:
        
        return n
    elif n == 0:

        return m
    
    elif memo[m][n] != -1:
        return memo[m][n]
    

    elif stringA[m] == stringB[n]:
        return editDistance(m-1, n-1)
    
    else:
        minimo = 1 + min(editDistance(m, n-1), editDistance(m-1, n-1), editDistance(m-1, n))
        memo[m][n] = minimo

        return minimo
    


stringA = "MONEYB"
stringB = "MONEY"
memo = [[-1 for _ in range(len(stringB)+1)] for _ in range(len(stringA)+1)]
print(editDistance(len(stringA)-1, len(stringB)-1))

print(memo)


#solução iterativa usando programação dinâmica
def editDistance(m, n):
    
    memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                memo[i][j] = j
            elif j == 0:
                memo[i][j] = i

            elif stringA[m-1] == stringB[n-1]:
                memo[i][j] = memo[i-1][j-1]

            else:
                memo[i][j] = 1 + min(
                                memo[i-1][j], #remove
                                memo[i-1][j-1], #replace
                                memo[i][j-1]) #insert
                
    return memo[m][n]

            

