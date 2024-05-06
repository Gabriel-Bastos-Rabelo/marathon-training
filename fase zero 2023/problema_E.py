n = int(input())
chutes = list(map(int, input().split()))
erro = list(map(int, input().split()))


minimo = chutes[0] - erro[len(erro) - 1]
maximo = chutes[-1] + erro[-1]

dicionario = {}
for i in erro:
    dicionario[i] = 0

def isPossible(n):
    for j in chutes:
        if abs(n - j) not in dicionario:
            return False
    
    return True



for i in range(minimo, maximo + 1):
    if isPossible(i):
        print(i)

