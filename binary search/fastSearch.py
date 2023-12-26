n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
k = int(input())

for i in range(k):
    l, r = map(int, input().split())

    
    left = 0
    right = len(arr)
    while(left < right):
        middle = (left + right)//2
        if(arr[middle] >= l):
            right = middle
        
        else:
            left = middle+1


    x = left

    left = 0
    right = len(arr)
    while(left < right):
        middle = (left + right)//2
        if(arr[middle] > r):
            right = middle
        else:
            left = middle+1


    y = left

    print(y - x)


        
    
