l, c = map(int, input().split())
matriz = []

for i in range(l):
    lista = list(input())
    matriz.append(lista)

n = int(input())
palavras = []
for i in range(n):
    p = input()
    palavras.append(p)


dir = [[-1, 0], [1, 0], [1, 1], 
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

res = 0
frequencia = {}
def search(grid, row, col, word):
    global res
    letras = {}
    copia = {}
    for i in word:
        letras[i] = letras.get(i, 0) + 1
        copia[i] = copia.get(i, 0) + 1

    if grid[row][col] not in letras:
        return False
    letras[grid[row][col]] -= 1
    

    for x, y in dir:
        visitados = [(row, col)]
        rd, cd = row + x, col + y

        flag = True

        for i in range(len(word)-1):
            if((rd >= 0 and rd < l) and (cd >= 0 and cd < c)):
                if(grid[rd][cd] in letras and letras[grid[rd][cd]] > 0):
                    visitados.append((rd, cd))
                    letras[grid[rd][cd]] -= 1
                    rd += x
                    cd += y
            
                else:
                    flag = False
                    break

            else:
                flag = False
                break

        if flag:
            for i in visitados:
                if i in frequencia and len(frequencia[i]) == 1 and frequencia[i][0] != word:
                    frequencia[i].append(word)
                    res += 1
                else:
                    if i not in frequencia:
                        frequencia[i] = []
                    if word not in frequencia[i]:
                        frequencia[i].append(word)
            return True
        else:
            letras = copia.copy()
        
    return False
    

for word in palavras:
    for row in range(l):
        for col in range(c):
            search(matriz, row, col, word)
print(res)