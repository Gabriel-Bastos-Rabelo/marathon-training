import math

def totiente(n):
    ret = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            while(n % i == 0):
                n //= i
            
            ret -= ret//i

        
    if n > 1:
        ret -= ret//n

    return ret


print(totiente(14))