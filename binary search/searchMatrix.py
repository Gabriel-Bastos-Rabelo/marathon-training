#leetcode 240

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = 0
        c = len(matrix[0]) - 1
        while True:
            if c == -1 or r == len(matrix):
                return False
            if target > matrix[r][c]:
                r += 1

            elif matrix[r][c] == target:
                return True

            else:
                c -= 1