class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        def quickSort(array, low, high):
            if low < high:
                pivot_location = partitionInStart(array, low, high)
                quickSort(array, low, pivot_location)
                quickSort(array, pivot_location + 1, high)

        def partitionInStart(array, low, high):
            pivot = array[low]
            lowerWall = low
            for i in range(low +1, high):
                if(array[i] < pivot):
                    lowerWall += 1
                    array[i], array[lowerWall] = array[lowerWall], array[i]


            array[low], array[lowerWall] = array[lowerWall], array[low]

            return lowerWall

        size = len(piles)
        quickSort(piles, 0, size)
        print(piles)
        right = size - 1
        left = 0
        res = 0
        while(left < right):
            res += piles[right - 1]
            right -= 2
            left += 1

        return res
