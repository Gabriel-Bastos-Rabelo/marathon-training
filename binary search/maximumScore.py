class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = k
        j = k
        n = len(nums)
        minimo = nums[k]
        res = nums[k] * 1
        while(i > 0 or j < n - 1):
            if(j >= n -1):
                i -= 1
            elif(i <= 0):
                j += 1
            elif(nums[i- 1] < nums[j + 1]):
                j += 1
            else:
                i -= 1

            minimo = min(minimo, nums[i], nums[j])
            res = max(res, minimo * (j - i + 1))

        return res