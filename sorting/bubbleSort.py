

def bubbleSort(x):
    size = len(x)
    while True:
        trocas = 0
        for i in range(size - 1):
            if x[i] > x[i + 1]:
                temp = x[i]
                x[i] = x[i + 1]
                x[i + 1] = temp
                trocas += 1

        if trocas == 0:
            return x


#complexidade de tempo: O(n²)

            