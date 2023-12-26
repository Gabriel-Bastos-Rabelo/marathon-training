t = int(input())


for i in range(t):
    n, k = map(int, input().split())

    sets = k//(n-1)

    rem = k%(n-1)
    total = sets * n - 1
    if(rem > 0):
        total += rem + 1

    print(total)
    