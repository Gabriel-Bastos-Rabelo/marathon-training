def possible(n, lista):
    salto = 0
    for i in range(len(lista)):
        if(salto >= n):
            return False
        if(lista[i] == 'L'):
            salto += 1
        else:
            salto = 0
    if(salto < n):
        return True
    
    return False
    

            
n = int(input())
for i in range(n):
    s = str(input())
    s = list(s)
    l = 0
    r = len(s)+1
    while(l < r):
        middle = (l+r)//2
        if(possible(middle, s)):
            r = middle
        
        else:
            l = middle+1

    print(l)
            