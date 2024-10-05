
import math



def numDivisible(l, r, arr):
    m = len(arr)
    res = 0

    for i in range(1, (1 << m)):
        lcm = 1
        cnt = 0
        for j in range(m):
            if((i >> j) & 1):
                cnt += 1
                lcm = math.lcm(arr[j], lcm)

        if(cnt % 2 == 0):
            res -= ((r//lcm) - ((l - 1)//lcm))

        else:
            res += ((r//lcm) - ((l - 1)//lcm)) 

    return res


print(numDivisible(1, 10, [4, 8]))

