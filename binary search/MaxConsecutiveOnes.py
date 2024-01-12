#leetcode 1004
#sliding window

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maior_seq = 0
        l = 0
        i = 0
        k_used = 0
        while(i < len(nums)):
            
            if nums[i] == 0:
                k_used += 1

                while(k_used > k):
                    if(nums[l] == 0):
                        k_used -= 1
                    l += 1
            i += 1

            maior_seq = max(maior_seq, i - l)

        return maior_seq