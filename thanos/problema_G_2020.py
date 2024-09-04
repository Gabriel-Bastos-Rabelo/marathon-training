n = int(input())
res = 100
atual = 100

for i in range(n):
    cx = int(input())
    atual += cx
    res = max(res, atual)


print(res)