def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return (a * b)/mdc(a, b)

def melhor_divisao(c, l):
  if c % l == 0:
    return (c, l)
  
  else:
    for i in range(2, l + 1):
       if c % (l/i) == 0:
          return (c, int(l/i))
    

while True:
  try:

    c, l = map(int, input().split())
    ml = melhor_divisao(c, l)

    res = (ml[0]/ml[1]) * (l/ml[1])
    print(int(res))


  except EOFError:
    break
  

