n = int(input())

lista = list(map(int, input().split()))

flechas_ativas = {}

flechas = 0


for altura in lista:
    if altura in flechas_ativas and flechas_ativas[altura] > 0:
        flechas_ativas[altura] -= 1

        if (altura - 1) in flechas_ativas:
            flechas_ativas[altura - 1] += 1
        else:
            flechas_ativas[altura - 1] = 1

    else:
        flechas += 1

        if (altura - 1) in flechas_ativas:
            flechas_ativas[altura - 1] += 1
        else:
            flechas_ativas[altura - 1] = 1



print(flechas)

