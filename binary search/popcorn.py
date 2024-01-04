#beecrowd 2973

n, c, t = map(int, input().split())


pipocas = list(map(int, input().split()))




def isPossible(tempo, pipocas, max, p):
    r = tempo*max
    n = 1
    i = 0

    while i < len(pipocas):
        if pipocas[i] > tempo * max:
            return False
        if r >= pipocas[i]:
            r -= pipocas[i]

        else:
            n += 1
            r = tempo * max
            i -= 1
            if(n > p):
                return False
        
        i += 1



    return True



l = 0
r = 10 ** 9

while(l <= r):
    mid = l + (r - l)//2
    if(isPossible(mid, pipocas, t, c)):
        r = mid - 1
    
    else:
        l = mid + 1

print(l)


   

