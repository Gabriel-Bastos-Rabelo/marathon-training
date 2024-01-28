class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def countSort(array):
            maxElement = max(array)
            t = len(array)

            count_array = [0] * (maxElement + 1)

            for i in range(t-1, -1, -1):
                count_array[array[i]] += 1

            for i in range(1, len(count_array)):
                count_array[i] += count_array[i-1]


            new_array = [0] * t

            for i in range(t-1, -1, -1):
                new_array[count_array[array[i]] - 1] = array[i]
                count_array[array[i]] -= 1

            return new_array


        array = countSort(costs)
        
        s = 0
        for i in array:
            if coins >= i:
                coins -= i
                s += 1
            else:
                break

        return s


