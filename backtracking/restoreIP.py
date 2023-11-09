res = []

def dfs(path, s, ip, index):
    if index > 4:
        return
    if index == 4 and len(s) == 0:
        
        res.append(path)
        return
    else:
        for i in range(1, len(s) + 1):
            sol = s[:i]
            
            if int(s[:i]) < 256 and int(s[:i]) >=0 and (s[0] != "0" or (s[0] == "0" and len(s[:i]) == 1)):
                if(index == 3):
                    dfs(path+sol, s[i:], ip, index+1)
                else:
                    dfs(path+sol + ".", s[i:], ip, index+1)



lista = [3,4,5,1,7,2,6]

for i in range(len(lista)):
    minimo = lista[i]
    indice = i
    for j in range(i, len(lista)):
        if lista[j] < minimo:
            minimo = lista[j]
            indice = j
    aux = lista[i]
    lista[i] = minimo
    lista[indice] = aux

print(lista)





