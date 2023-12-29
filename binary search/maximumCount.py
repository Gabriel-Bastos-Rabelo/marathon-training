class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def findPositive(nums):
            res = -1
            l = 0
            r = len(nums) - 1
            while(l <= r):
                mid = l + (r - l)//2
                if(nums[mid] > 0):
                    r = mid - 1
                    res = mid

                else:
                    l = mid + 1

            return res

        def findNegative(nums):
            res = -1
            l = 0
            r = len(nums) - 1
            while(l <= r):
                mid = l + (r-l)//2
                if(nums[mid] < 0):
                    l = mid + 1
                    res = mid
                else:
                    r = mid-1
            return res

        negative = findNegative(nums)
        positive = findPositive(nums)

        
        if(positive == -1 and negative == -1):
            return 0
        if(positive == -1):
            return negative +1

        return max((negative + 1), (len(nums) - positive))