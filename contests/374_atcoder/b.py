s = input()
t = input()

tam = min(len(s), len(t))

pos = 0

while pos < tam:
    if s[pos] != t[pos]:
        break
    pos += 1


if pos == tam and len(s) == len(t):
    print(0)

elif pos == tam:
    print(pos + 1)


else:
    print(pos + 1)
