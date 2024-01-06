#leetcode 2024

#solução com sliding window

def findMaxT(string, k):
    res = 0
    left = 0
    cont = 0
    for i in range(len(string)):
        if(string[i] == 'F'):
            cont += 1

        while(cont > k):
            if(string[left] == 'F'):
                cont -= 1
            left += 1

        
        res = max((i - left + 1), res)
    
    return res

def findMaxF(string, k):
    res = 0
    left = 0
    cont = 0
    for i in range(len(string)):
        if(string[i] == 'T'):
            cont += 1

        while(cont > k):
            if(string[left] == 'T'):
                cont -= 1
            left += 1

        
        res = max((i - left + 1), res)
    
    return res


answerKey = "TTFF"
k = 2
print(max(findMaxT(answerKey, k), findMaxF(answerKey, k)))