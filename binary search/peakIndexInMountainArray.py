#leetcode 852 
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        def check(array, position):
            if(position > 0):
                return array[position] > array[position - 1]
            else:
                return True

        def binarySearch(array):
            l = 0
            r = len(array) - 1
            while(l <= r):
                mid = l + (r - l)//2
                if(check(array, mid)):
                    l = mid + 1

                else:
                    r = mid - 1

            return l

        return binarySearch(arr) - 1