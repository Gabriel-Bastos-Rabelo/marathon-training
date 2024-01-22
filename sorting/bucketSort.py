def insertionSort(x):
    for i in range(1, len(x)):
        up = x[i]
        j = i - 1

        while j<=0 and x[j] > up:
            x[j+1] = x[j]
            j -= 1
        x[j + 1] = up

    return x


def bucketSort(x):
    arr = []
    slot_num = 10

    for i in range(slot_num):
        arr.append([])

    for j in x:
        index = int(j * slot_num)
        arr[index].append(j)

    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1

    return x


x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))

    