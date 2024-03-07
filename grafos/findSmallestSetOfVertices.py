class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        g = {}
        lista = [-1] * n
        for i in edges:
            if i[0] not in g:
                g[i[0]] = [i[0]]
            
            lista[i[1]] = 0
            g[i[0]].append(i[1])

        res = []
        for i in range(len(lista)):
            if lista[i] == -1:
                res.append(i)

        return res
