
boxes = "110"
tamanho = len(boxes)
lista = []
for i in range(tamanho):
    res = 0
    for j in range(tamanho):
        if boxes[j] == 1:
            res += abs(j - i)

    print(res)
    lista.append(res)


print(lista)