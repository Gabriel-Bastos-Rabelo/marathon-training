while True:
    try:
        res = 0
        d = {}
        n = int(input())
        for i in range(n):
            t, pe = map(str, input().split())
            t = int(t)
            if t not in d:
                d[t] = [pe]
            else:
                if pe == 'D':
                    if 'E' in d[t]:
                        d[t].remove('E')
                        res += 1
                    else:
                        d[t].append('D')
                else:
                    if 'D' in d[t]:
                        d[t].remove('D')
                        res += 1
                    else:
                        d[t].append('E')

        print(res)

            



    except EOFError:
        break