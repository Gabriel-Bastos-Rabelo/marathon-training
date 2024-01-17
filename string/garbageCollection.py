class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        lastIndexP = 0
        lastIndexM = 0
        lastIndexG = 0

        for i in range(len(garbage)-1, -1, -1):
            res += len(garbage[i])
            if "M" in garbage[i]:
                lastIndexM = max(lastIndexM, i)
            
            if "P" in garbage[i]:
                lastIndexP = max(lastIndexP, i)

            if "G" in garbage[i]:
                lastIndexG = max(lastIndexG, i)

        listaTempo = [travel[0]]
        for i in range(1, len(travel)):
            listaTempo.append(travel[i])
            listaTempo[i] += listaTempo[i-1]

        print(listaTempo)
        if lastIndexG != 0:
            res += listaTempo[lastIndexG-1]
        if lastIndexP != 0:
            res += listaTempo[lastIndexP-1]
        if lastIndexM != 0:
            res += listaTempo[lastIndexM-1]

        return res