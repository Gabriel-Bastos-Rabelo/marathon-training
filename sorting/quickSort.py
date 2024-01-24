def quickSort(array, low, high):
    if(low == high):
        return
    pivot_location = partitionMiddleElement(array, low, high)
    quickSort(array, low, pivot_location)
    quickSort(array, pivot_location + 1, high)



#escolhendo o primeiro elemento como pivot
def partitionFirstElement(array, low, high):
    pivot = array[low]
    leftWall = low

    for i in range(low + 1, high):
        if(array[i] < pivot):
            array[i], array[leftWall] = array[leftWall], array[i]
            leftWall += 1

    array[low], array[leftWall] = array[leftWall], array[low]

    return leftWall

   

#escolhendo o elemento do meio entre o primeiro, o do meio e o último
def partitionMiddleElement(array, low, high):
    mid = (low + high) // 2
    lista = [array[low], array[mid], array[high - 1]]
    lista.sort()
    midElement = lista[1]
    index = array.index(midElement)

    array[index], array[high - 1] = array[high - 1], array[index]

    left = low
    right = high - 2
    pivot = array[high - 1]

    while left <= right:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]

    array[left], array[high - 1] = array[high - 1], array[left]

    return left




array = [5,4,3,2,1,10,9,8,30,34,12,-1,-100,40]

quickSort(array, 0, 14)

print(array)


#complexidade de tempo no pior caso: O(n²)
#ocorre quando o as escolhas do pivo divide o array em partes muito desbalanceadas

    