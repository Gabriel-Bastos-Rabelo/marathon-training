class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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

        def quickSort(array, low, high):
            if(low == high):
                return
            pivot_location = partitionMiddleElement(array, low, high)
            quickSort(array, low, pivot_location)
            quickSort(array, pivot_location + 1, high)


        def partitionMiddleElement(array, low, high):
            mid = (low + high) // 2
            pivot = sorted([array[low], array[mid], array[high - 1]])[1]
            
            
            pivot_index = None
            for i in range(low, high):
                if array[i] == pivot:
                    pivot_index = i
                    break

            array[pivot_index], array[high - 1] = array[high - 1], array[pivot_index]

            left = low
            right = high - 2
            pivot = array[high - 1]

            while left <= right:
                while left <= right and array[left] <= pivot:
                    left += 1
                while left <= right and array[right] >= pivot:
                    right -= 1
                if left < right:
                    array[left], array[right] = array[right], array[left]
                    left += 1
                    right -= 1

            array[left], array[high - 1] = array[high - 1], array[left]

            return left

        def partitionFirstElement(array, low, high):
            pivot = array[low]
            leftWall = low

            for i in range(low + 1, high):
                if(array[i] < pivot):
                    leftWall += 1
                    array[i], array[leftWall] = array[leftWall], array[i]
                    

            array[low], array[leftWall] = array[leftWall], array[low]

            return leftWall




        quickSort(nums, 0, len(nums))
        return nums