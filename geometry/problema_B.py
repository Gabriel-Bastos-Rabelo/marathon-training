import math


n = int(input())

#pi * r²

areaC = math.pi * (n/2) ** 2

print(f"{((n * n) - areaC):.2f}")