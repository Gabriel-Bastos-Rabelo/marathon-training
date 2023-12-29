#leetcode 2389
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixo = [0] * len(nums)
        prefixo[0] = nums[0]
        for i in range(1, len(nums)):
            prefixo[i] = prefixo[i-1] + nums[i]

        def binarySearch(prefixo, target):
            l = 0
            r = len(prefixo)-1
            res = -1
            while (l <= r):  
                mid = (l + r) // 2
                if (target < prefixo[mid]):
                    r = mid - 1
                else:
                    l = mid + 1 
                    res = mid

            return res + 1

        res = []
        for q in queries:
            res.append(binarySearch(prefixo, q))

        return res
                