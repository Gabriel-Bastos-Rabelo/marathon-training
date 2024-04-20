import math

while True:
    s = input().strip()
    if s == '0':
        break

    print(math.factorial(len(s)))