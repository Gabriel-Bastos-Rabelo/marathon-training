class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(max, weights, days):
            numeroDias = 1
            peso = 0
            for i in weights:
                if i + peso > max:
                    peso = i
                    numeroDias += 1
                else:
                    peso += i

            return numeroDias <= days

        def binarySearch(weights, days):
            l = max(weights)  
            r = sum(weights)  
            while l <= r:
                mid = l + (r - l) // 2
                if isPossible(mid, weights, days):
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        return binarySearch(weights, days)