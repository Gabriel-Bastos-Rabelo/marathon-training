def lastSoldier(row):
    last = -1
    l = 0
    r = len(row) - 1
    target = 1
    while(l <= r):
        mid = l + (r - l)//2
        if(target > row[mid]):
            r = mid -1
        elif (target == row[mid]):
            l = mid + 1
            last = mid

    return last+1



mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]


soldier_count = [(lastSoldier(row), idx) for idx, row in enumerate(mat)]

print(soldier_count)

soldier_count.sort()

print(soldier_count)
    


