class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        def binarySearch(lista, x):
            l = 0
            r = len(lista) - 1
            while(l <= r):
                mid = l + (r - l)//2
                if(lista[mid] > x):
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        lista = []
        for i, x in enumerate(obstacles):
            if i == 0 or x >= lista[len(lista) - 1]:
                lista.append(x)
                obstacles[i] = len(lista)

            else:
                idx = binarySearch(lista, x)
                lista[idx] = x
                obstacles[i] = idx + 1

        return obstacles