class Solution:
    def convert(self, s: str, numRows: int) -> str:
        listas = [[] for i in range(numRows)]

        i = 0
        t = len(s)
        segundaVez = False
        while(i < t):
            if segundaVez:
                for j in range(1, numRows):
                    if i < t:
                        listas[j].append(s[i])
                        i += 1
            else:
                for j in range(numRows):
                    if i < t:
                        listas[j].append(s[i])
                        i += 1

            ultimoIndex = j
            for j in range(ultimoIndex - 1, -1, -1):
                if i < t:
                    listas[j].append(s[i])
                    i += 1

                segundaVez = True

        string = ""
        for j in listas:
            aux = "".join(j)
            string = "".join([string, aux])

        return string





instancia = 1

while True:
  try:
    achou = False
    n = int(input())
    memo = [0] * n
    lista = list(map(int, input().split()))
    memo[0] = lista[0]
    t = len(lista)
    if t == 1:
        if lista[0] == 0:
            print("Instancia", instancia)
            print(0)
    else:
        for i in range(1, t):
            if(lista[i] == memo[i-1]):
                print("Instancia", instancia)
                print(lista[i])
                achou = True
                break
            else:
                memo[i] = memo[i-1] + lista[i]
        if achou == False:
            print("Instancia", instancia)
            print("nao achei")
    
    print()
    instancia += 1
    
  except EOFError:
    break