def distributeCandies(n, limit):
    res = 0
    for i in range(min(n, limit) + 1):
        e = max(0, n- i - limit)
        d = min(limit, n- i)
        res += max(d - e + 1, 0)

    return res



print(distributeCandies(3, 3))