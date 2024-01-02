#leetcode 888
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        def binarySearch(target, nums):
            l = 0
            r = len(nums) - 1
            while(l <= r):
                mid = l + (r - l)//2
                if(nums[mid] < target):
                    l = mid + 1
                elif(nums[mid] == target):
                    return True
                else:
                    r = mid -1

            return False
        totalSum = sum(aliceSizes) + sum(bobSizes)
        idealSum = totalSum//2
        aliceSum = sum(aliceSizes)
        bobSizes.sort()
        for i in range(len(aliceSizes)):
            target = idealSum - aliceSum + aliceSizes[i]
            if(binarySearch(target, bobSizes)):
                return [aliceSizes[i], target]