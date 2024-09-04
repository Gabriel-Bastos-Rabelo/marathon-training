class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        initPoint = 0
        endPoint = len(height) - 1
        res = 0
        while initPoint < endPoint:
            res = max(res, (min(height[initPoint], height[endPoint]) * (endPoint - initPoint)))
            if height[initPoint] < height[endPoint]:
                initPoint += 1
            else:
                endPoint -= 1

        return res

        