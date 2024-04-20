while True:
    n, m = map(int, input().split())
    if(n == 0 and m == 0):
        break

    dic = {}
    res = 0

    lista = list(map(int, input().split()))

    for i in lista:
        if i not in dic:
            dic[i] = 0
        else:
            dic[i] += 1

        if dic[i] == 1:
            res += 1

            
    print(res)