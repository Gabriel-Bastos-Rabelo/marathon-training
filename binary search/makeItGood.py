def solve(array):
    n = len(array) - 1
    peek = n
    for i in range(n-1, -1, -1):
        if(array[i] >= array[i+1]):
            peek = i
        else:
            break
    

    if(peek == 0):
        return 0


    goodArray = peek - 1
    for j in range(goodArray, -1, -1):
        if(array[j] <= array[j+1]):
            goodArray = j
        else:
            break

    return goodArray


n = int(input())


for i in range(n):
    numeros = int(input())
    array = list(map(int, input().split()))
    print(solve(array))