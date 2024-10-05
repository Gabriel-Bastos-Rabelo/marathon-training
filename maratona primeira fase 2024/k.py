n = int(input())
arr = list(map(int, input().split()))

res = []
dp = {}

def back(arr, target, total, current, inicial):
    global res
    if total == target:
        res = current.copy()
        return True
    elif total > target:
        return False
    if (inicial, total) in dp:
        return dp[(inicial, total)]
    
    for i in range(inicial, len(arr)):
        current.append((arr[i], i))
        dp[(inicial, total)] = back(arr, target, total + arr[i], current, i + 1) 
        if dp[(inicial, total)]:
            return True
        current.pop()
        
    return False

    
if sum(arr) % 2 != 0:
    print(-1)

else:
    target = sum(arr)//2
    arr.sort()
    resultado = back(arr, target, 0, [], 0)

    if resultado:
        dicionario = {}
        primeiroSaco = []
        segundoSaco = []
        for i in res:
            dicionario[i[1]] = 1
            primeiroSaco.append(i[0])

        for index, i in enumerate(arr):
            if index not in dicionario:
                segundoSaco.append(i)

        res = []
        k = 0
        j = 0
        menina = primeiroSaco[k]
        menino = 0
        res.append(primeiroSaco[k])
        k += 1 
        for i in range(1, n):
            if menina - menino > 0:
                res.append(segundoSaco[j])
                menino += segundoSaco[j]
                j += 1
            else:
                res.append(primeiroSaco[k])
                menina += primeiroSaco[k]
                k += 1

        print(*res)

    else:
        print(-1)
   

        