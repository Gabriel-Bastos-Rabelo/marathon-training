class Solution:
    def frequencySort(self, s: str) -> str:
        dicionario = {}
        for i in s:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1

        lista = []

        for i in dicionario:
            lista.append([i, dicionario[i]])

        lista.sort(reverse=True, key=lambda x: x[1])

        string = ""

        for i in lista:
            while(i[1] != 0):
                string += i[0]
                i[1] -= 1

        return string
    


#solução 2
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)
        
        ans = []
        for freq in range(n, -1, -1):
            for c in bucket[freq]:
                ans.append(c * freq)
        return "".join(ans)
