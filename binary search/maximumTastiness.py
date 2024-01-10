class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        def check(x):
            last = price[0]
            count = 1
            current = 1

            while current < len(price) and count < k:
                if price[current] - last >= x:
                    last = price[current]
                    count += 1

                current += 1

            return count == k


        l = 0
        r = max(price) - min(price)

        price.sort()

        while(l <= r):
            mid = l + (r - l)//2
            if(check(mid)):
                l = mid + 1
            else:
                r = mid - 1

        return l-1