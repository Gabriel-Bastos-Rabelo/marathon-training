n = int(input())


def isPossible(value, n, total):
    mid = n//2
    falta = n - mid
    if(falta >= 1):
        return ((total - value)//falta) >= value
    return True


for i in range(n):
    n, s = map(int, input().split())
    l = 0
    r = s
    total = s
    while(l <= r):
        mid = l + (r - l)//2
        if(isPossible(mid, n, total)):
            l = mid + 1
        else:
            r = mid -1

    print(l)

