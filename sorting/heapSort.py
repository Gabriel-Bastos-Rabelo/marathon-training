def maxheapify(array, size, i):
    largest = i
    l = (2 * i) + 1
    r = (2 * i) + 2

    if l < size and array[l] > array[largest]:
        largest = l

    if r < size and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        maxheapify(array, size, largest)


def minHeapify(array, size, i):
    minimum = i
    l = (2 * i) + 1
    r = (2 * i) + 2

    if l < size and array[l] < array[minimum]:
        minimum = l

    if r < size and array[r] < array[minimum]:
        minimum = r

    if minimum != i:
        array[i], array[minimum] = array[minimum], array[i]

        minHeapify(array, size, minimum)
        

def heapSort(arr, size):
    for i in range((size//2)-1, -1, -1):
        maxheapify(arr, size, i)

    print(arr)

    for i in range(size -1, -1, -1):
        print(arr, " terminando com i = ", i)
        arr[i], arr[0] = arr[0], arr[i]
        maxheapify(arr, i, 0)


def doubleHeapSort(array, size):
    maxHeap = array.copy()
    minHeap = array.copy()
    
    aux = [0] * (size)

    for i in range((size//2)-1, -1, -1):
        maxheapify(maxHeap, size, i)

    for i in range((size//2)-1, -1, -1):
        minHeapify(minHeap, size, i)

    

    for i in range(size//2+1):
        aux[size-i-1] = maxHeap[0]
        maxHeap[size - i - 1], maxHeap[0] = maxHeap[0], maxHeap[size - i - 1]
        maxheapify(maxHeap, size - i - 1, 0)
        aux[i] = minHeap[0]
        minHeap[size - i - 1], minHeap[0] = minHeap[0], minHeap[size - i - 1]
        minHeapify(minHeap, size - i - 1, 0)

    print(aux)



    
    

lista = [4, 2, 8, 7, 1, 5, 3, 6, 10]

doubleHeapSort(lista, len(lista))

