def insertionSort(x):
    size = len(x)
    for i in range(1, size):
        up = x[i]
        j = i - 1

        while j >= 0 and x[j] > up:
            x[j + 1] = x[j]
            j -= 1

        x[j + 1] = up

    return x

#complexidade de tempo: O(n²) no pior caso
#O(n) no melhor caso