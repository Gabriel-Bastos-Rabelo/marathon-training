class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums[0] += k

        for i in range(1, len(nums)):
            x = nums[i-1] - nums[i]
            print(x)
            if x >= -k and x <= k:
                nums[i] += x
            else:
                if x > 0:
                    nums[i] += k
                else:
                    nums[i] -= k
            
           

        print(nums)
        return max(nums) - min(nums)