def mergeSort(array):

    mid = len(array)//2
    l = array[:mid]
    r = array[mid: ]


    if(len(array) == 0):
        return []
    
    elif(len(array) == 1):
        return array
    


    mergeSort(l)

    mergeSort(r)

    left = 0
    right = 0
    index = 0
    while(left < len(l) and right < len(r)):
        if l[left] < r[right]:
            array[index] = l[left]
            left += 1
        else:
            array[index] = r[right]
            right += 1
        
        index += 1

    if left < len(l):
        while(left < len(l)):
            array[index] = l[left]
            index += 1
            left += 1

    elif right < len(r):
        while(right < len(r)):
            array[index] = r[right]
            index += 1
            right += 1

    return array


print(mergeSort([38, 27, 43, 10, 11, 1, 4, 5, -3]))


#complexidade de tempo O(nlogn)
