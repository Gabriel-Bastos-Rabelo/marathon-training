
def quickSort(array, low, high):
    if low < high:
        pivot_location = partitionMiddleElement(array, low, high)
        quickSort(array, low, pivot_location)
        quickSort(array, pivot_location + 1, high)


def partitionMiddleElement(array, low, high):
    mid = (high + low) //2
    pivot = sorted([array[low][0], array[mid][0], array[high - 1][0]])[1]

    # Encontrar o índice do elemento pivô
    for i in [low, mid, high - 1]:
        if array[i][0] == pivot:
            pivot_index = i
            break

    # Trocar o pivô com o último elemento
    array[pivot_index], array[high - 1] = array[high - 1], array[pivot_index]
    pivot = array[high - 1][0]

    left = low
    right = high - 2

    while left < right:
        while left < right and array[left][0] <= pivot:
            left += 1
        while left < right and array[right][0] >= pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]

    if array[left][0] > pivot:
        array[left], array[high - 1] = array[high - 1], array[left]

    return left

            


points = [[58,71],[64,41],[96,14],[26,37],[11,67],[84,2],[72,0],[16,95],[74,100],[60,98],[8,45],[6,59],[69,32],[93,12],[26,56],[9,39],[61,84],[54,93],[43,47],[84,40],[95,82],[17,85],[99,41],[96,24],[83,10],[82,62],[26,81],[74,96],[53,0],[11,72],[51,35],[33,3],[33,52],[58,94],[89,92],[54,85]]
    
quickSort(points, 0, len(points))
maior = 0
print(points)
for i in range(1, len(points)):
    if points[i][0] - points[i-1][0] > maior:
        maior = points[i][0] - points[i-1][0]

print(maior)