#leetcode 2089

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def firstOcurrence(lista, target):
            left, right = 0, len(lista) - 1
            firstOcu = -1
            while left <= right:
                mid = left + (right - left) // 2
                if lista[mid] < target:
                    left = mid + 1
                else:
                    if lista[mid] == target:
                        firstOcu = mid
                    right = mid - 1
            return firstOcu

        def lastOcurrence(lista, target):
            left, right = 0, len(lista) - 1
            lastOcu = -1
            while left <= right:
                mid = left + (right - left) // 2
                if lista[mid] <= target:
                    if lista[mid] == target:
                        lastOcu = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return lastOcu
        
        nums.sort()
        first = firstOcurrence(nums, target)
        last = lastOcurrence(nums, target)

        if first == -1 or last == -1:
            return []

        return [i for i in range(first, last + 1)]