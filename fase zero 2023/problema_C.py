n, b = map(int, input().split())

res = 0
for i in range(2 * n, 0, -1):
    number = i ** 2
    dif = abs(number - b)
    if dif % ((2 * n) + 1) == 0:
        res = number 
        break

print(res)