n = int(input())

last = 0
esperando = False
curr = 0
for i in range(n):

    a, b = map(int, input().split())

    if(a > last and esperando):
        last = last + 10
        esperando = False
        curr ^= 1

    if(a > last):
        last = a + 10
        curr = b


    elif(a < last):
        if(curr != b):
            esperando = True

        else:
            last = a + 10


if esperando:
    last += 10


print(last)



