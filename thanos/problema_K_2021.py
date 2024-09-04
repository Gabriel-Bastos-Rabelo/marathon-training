t, d, m = map(int, input().split())



ultimo = 0

achou = False
for i in range(m):
    ref = int(input())
    tempo = ref - ultimo
    ultimo = ref
    if tempo >= t:
        achou = True

if achou:
    print("Y")
else:
    if (d - ultimo) >= t:
        print("Y")
    else:
        print("N")