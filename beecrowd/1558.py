import math
while True:
    try:
        n = int(input())

        achou = False

        if n >= 0:
            i = 0
            while(i * i <= n):
                b = n - (i * i)
                r = math.sqrt(b)
                if(r == int(r)):
                    achou = True
                    break
                i += 1

        if achou:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
