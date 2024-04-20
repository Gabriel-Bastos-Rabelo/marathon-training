#https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        point = points[0]

        for i in range(1, len(points)):
            difX = abs(points[i][0] - point[0])
            difY = abs(points[i][1] - point[1])

            maximo = max(difX, difY)

            time += maximo
            point = points[i]

        return time

