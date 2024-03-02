
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.visitados = {}
        def backtracking(path, counter):
            if len(path) == len(nums):
                self.ans.append(path.copy())
                return
            else:
                for i in counter:
                    if counter[i] > 0:
                        path.append(i)
                        counter[i] -= 1
                        backtracking(path, counter)
                        path.pop()
                        counter[i] += 1
        
        

        backtracking([], Counter(nums))
        return self.ans