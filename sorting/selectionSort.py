def selection_sort(x):
    size = len(x)

    for i in range(size):
        cur = i
        for j in range(i+1, size):
            if x[j] < x[cur]:
                cur = j

        aux = x[i]
        x[i] = x[cur]
        x[cur] = aux    

    return x



print(selection_sort([2,3,1,5,4]))


#complexidade de tempo: O(n²)


