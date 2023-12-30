n, k = map(int, input().split())

def timeToquestion(n):
    if(n == 0):
        return 0
    else:
        return (5 * n) + timeToquestion(n-1)
    


l = 0
r = n
time = 240 - k
while(l <= r):
    mid = l + (r -l)//2
    if(timeToquestion(mid) <= time):
        l = mid+1
    else:
        r = mid-1


print(l)