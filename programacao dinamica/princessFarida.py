n = int(input())

for i in range(1, n+1):
    numeroMonstros = int(input())

    a = list(map(int, input().split()))

    d = [0] * numeroMonstros

    if(numeroMonstros > 1):
        d[0] = a[0]
        d[1] = max(a[0], a[1])
        for j in range(2, len(a)):
            d[j] = max(d[j-1], a[j] + d[j-2])
    elif(numeroMonstros == 0):
        print(f"Case {i}: 0")
        continue
    elif(numeroMonstros == 1):
        print(f"Case {i}: {a[0]}")
        continue

    print(f"Case {i}: {d[len(a)-1]}")
