
res = []
def combination(n, k, index, current):
    if len(current) > k:
        return
    if len(current) == k:
        res.append(current.copy())
    else:
        for i in range(index, n+1):
            current.append(i)
            combination(n, k, i+1, current)
            current.pop()

combination(4, 2, 1, [])

print(res)