
#leetcode 40
res = []
visitados = {}

def permutation(nums, lista, visitados):
    if len(lista) == len(nums) and lista not in res:
        res.append(lista.copy())
        print(lista)

    for index, x in enumerate(nums):
        if index not in visitados:
            visitados[index] = 1
            lista.append(x)
            permutation(nums, lista, visitados)
            visitados.pop(index)
            lista.pop()


nums = [1,3,2]
permutation(nums, [], visitados)