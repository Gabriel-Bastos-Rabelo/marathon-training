#leetcode 1351

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bin(row):
            l = 0
            r = len(row)
            while(l < r):
                middle = (r - l)//2
                if(row[middle] < 0):
                    r = middle
                else:
                    l = middle + 1
            return len(row) - l
        
        cont = 0
        for row in grid:
            cont += bin(row)

        return cont
