#Solução 1

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        col = len(mat[0])
        dicionario = {}
        for i in range(rows):
            for j in range(col):
                if (i, j) not in dicionario:
                    index = j
                    lista = []
                
                    linha = i
                    coluna = j

                    while(linha < rows and coluna < col):
                        lista.append((linha, coluna))
                        linha += 1
                        coluna += 1


                    print(lista)
                    for k in range(len(lista)):
                        menor = lista[k]
                        for l in range(k+1, len(lista)):
                            if mat[lista[l][0]][lista[l][1]] < mat[menor[0]][menor[1]]:
                                menor = lista[l]

                        mat[lista[k][0]][lista[k][1]], mat[menor[0]][menor[1]] = mat[menor[0]][menor[1]], mat[lista[k][0]][lista[k][1]]
        return mat
    


#solução 2

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat
