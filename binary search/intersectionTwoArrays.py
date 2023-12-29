#leetcode 349
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def binarySearch(nums, target):
            l = 0
            r = len(nums) - 1
            while(l <= r):
                mid = l + (r-l)//2
                if(target > nums[mid]):
                    l = mid + 1

                elif(target == nums[mid]):
                    return 1

                else:
                    r = mid - 1

            return -1

        if(len(nums1) > len(nums2)):
            menor = nums2
            maior = nums1
        else:
            menor = nums1
            maior = nums2
        
        res = []
        maior.sort()
        for i in menor:
            if i not in res:
                if(binarySearch(maior, i) == 1):
                    res.append(i)

        return res
    
