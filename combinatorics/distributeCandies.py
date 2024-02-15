def distributeCandies(n, limit):
    res = 0
    for i in range(limit + 1):
        for j in range(limit + 1):
            if n - (i + j) <= limit and (i + j) <= n:
                res += 1

    return res



print(distributeCandies(3, 3))