class Solution:
    def sortVowels(self, s: str) -> str:

        def mergeSort(array):
            size = len(array)

            if(size == 0):
                return []
            elif(size == 1):
                return array

            elif(size == 2):
                if(array[0] > array[1]):
                    array[0], array[1] = array[1], array[0]

                return array

            else:
                mid = size//2
                l = array[:mid]
                r = array[mid:]

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

                while(left < len(l)):
                    array[index] = l[left]
                    left += 1
                    index += 1

                while(right < len(r)):
                    array[index] = r[right]
                    right += 1
                    index += 1

                return array
            

        string = "aeiouAEIOU"
        lista = []
        positions = []
        for i in range(len(s)):
            if s[i] in string:
                lista.append(s[i])
                positions.append(i)

        
        lista = mergeSort(lista)
        index = 0
        s = list(s)
        for i in positions:
            s[i] = lista[index]
            index += 1


        s = "".join(s)
        return s
