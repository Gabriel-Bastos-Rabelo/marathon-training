
#leetcode

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        count = 0
        for i in nums:
            if target.startswith(i):
                restante = target[len(i): ]
                print(restante)
                if restante in counter:
                    if restante != i:
                        count += (counter[restante])
                    else:
                        count += ((counter[restante]) - 1)

        return count
