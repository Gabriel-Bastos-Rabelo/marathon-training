class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(current, n, ans, nums):
            if len(current) == n:
                ans.append(current.copy())
            else:
                for i in range(n):
                    if nums[i] not in current:
                        current.append(nums[i])
                        backtracking(current, n, ans, nums)
                        current.pop()
                    
        n = len(nums)
        ans = []
        backtracking([], n, ans, nums)
        return ans