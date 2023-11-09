# leetcode 39

def combination_sum(candidates, target, lista, lista_geral, i):
    if sum(lista) == target:
        lista_geral.append(lista.copy())
        return
    if sum(lista) > target or i >= len(candidates):
        return
    else:

        lista.append(candidates[i])
        combination_sum(candidates, target, lista, lista_geral, i)
        lista.pop()
        combination_sum(candidates, target, lista, lista_geral, i+1)

    return lista_geral


print(combination_sum([2, 3, 6, 7], 7, [], [], 0))
