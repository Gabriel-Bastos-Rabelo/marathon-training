#leetcode combination sum 2 40

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidate, lista, target, lista_geral, index):
            
            if sum(lista) == target and lista not in lista_geral:
                lista_geral.append(lista.copy())
            if sum(lista) > target or index >= len(candidate):
                return
                
            current = candidate[index]
            lista.append(current)
            dfs(candidate, lista, target, lista_geral, index+1)
            lista.pop()
            while index+1 < len(candidate) and candidate[index] == candidates[index+1]:
                index += 1
            dfs(candidate, lista, target, lista_geral, index+1)
            return lista_geral
        lista_geral = []
        candidates.sort()
        return dfs(candidates, [], target, lista_geral, 0)
    
#solution 2

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, lista):
            if sum(lista) > target:
                return
            if sum(lista) == target:
                res.append(lista.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                lista.append(candidates[i])
                dfs(i+1, lista)
                lista.pop()
                
                
        dfs(0, [])
        return res

