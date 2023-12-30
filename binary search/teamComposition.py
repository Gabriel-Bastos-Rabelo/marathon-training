def isPossible(a, b, n):
    if a >= n and b >= n:
        return True
    return False

n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    l = 0
    r = (a+b)//4
    while(l <= r):
        mid = l + (r-l)//2
        if(isPossible(a, b, mid)):
            l = mid + 1
        else:
            r = mid -1


    print(l-1)



