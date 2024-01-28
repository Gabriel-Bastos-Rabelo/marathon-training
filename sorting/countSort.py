def countSort(array):
    maxElement = max(array)

    count_vector = [0] * (maxElement+1)
    
    print(array)

    for i in range(len(array) - 1, -1, -1):
        count_vector[array[i]] += 1

    for i in range(1, len(count_vector)):
        count_vector[i] += count_vector[i-1]

    new_array = [0] * maxElement
    for i in range(len(array)-1, -1, -1):
        new_array[count_vector[array[i]] - 1] = array[i]
        count_vector[array[i]] -= 1

    return new_array

        



countSort([1,4,1,2,7,5,2])