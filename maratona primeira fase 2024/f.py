n = int(input())

if n == 0 or n == 1:
    print(1)

else:
    a = 1
    b = 2

    for i in range(n-1):
        a, b = b, (a + b)

    print(a)