def verificarSubmatriz(linha, coluna, matriz):
    dicionario = {}
    
    for i in range(linha, linha + 3):
        for j in range(coluna, coluna + 3):
            if matriz[i][j] not in dicionario:
                dicionario[matriz[i][j]] = 1
            else:
                
                return False
    return True


def verificarSudoku(matriz, linhas, colunas):    
    for i in range(9):
        for j in range(9):
            if matriz[i][j] not in linhas[i] and matriz[i][j] not in colunas[j]:
                linhas[i][matriz[i][j]] = 1
                colunas[j][matriz[i][j]] = 1
            else:
                return False
            
    return True
            

n = int(input())

instancia = 1
for i in range(n):

    linhas = {}
    colunas = {}
    soduku = []
    for i in range(9):
        colunas[i] = {}

    for i in range(9):
        linhas[i] = {}
        linha = list(map(int, input().split()))
        soduku.append(linha)


    if verificarSudoku(soduku, linhas, colunas):
        submatrizOk = True
        for i in range(3):
            for j in range(3):
                if verificarSubmatriz(i * 3, j * 3, soduku) == False:
                    print(f"Instancia {instancia}")
                    print("NAO")
                    submatrizOk = False
                    break
            if submatrizOk == False:
                break
        if submatrizOk:
            print(f"Instancia {instancia}")
            print("SIM")
    else:
        print(f"Instancia {instancia}")
        print("NAO")

    print()

    instancia += 1
