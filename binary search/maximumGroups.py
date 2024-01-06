class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        

        def binarySearch(grades):
            l = 0
            r = len(grades)
            while(l <= r):
                mid = l + (r - l)//2
                if(mid * (mid + 1)/2 <= len(grades)):
                    l = mid + 1

                else:
                    r = mid -1

            return l-1

        return binarySearch(grades)