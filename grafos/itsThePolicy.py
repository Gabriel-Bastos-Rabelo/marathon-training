v, e = map(int, input().split())

g = {}

for i in range(e):
    x, y = map(int, input().split())
    if x not in g:
        g[x] = []
    
    if y not in g:
        g[y] = []

    g[x].append(y)
    g[y].append(x)




res = [1] * (v + 1)

lista = []
menor = float('inf')

for i in g:
    if len(g[i]) < menor:
        lista = [i]
        lista += g[i]
        menor = len(g[i])


for i in lista:
    res[i] = 0
    
res.pop(0)
string = " ".join(map(str, res))
print(string)