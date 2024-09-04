d, c, r = map(int, input().split())

cansativas = []
for i in range(c):
    num = int(input())
    cansativas.append(num)

for i in range(r):
    d += int(input())

res = r
i = 0
while d > 0 and i < len(cansativas) and d > cansativas[i]:
    d -= cansativas[i]
    i += 1
    res += 1

print(res)