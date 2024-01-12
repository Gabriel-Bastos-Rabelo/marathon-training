#leetcode 378

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def binarySearch(matrix, k):
            l = matrix[0][0]
            n = len(matrix)
            r = matrix[n - 1][n - 1]
            ans = 0
            while(l <= r):
                mid = l + (r - l)//2
                if(countLessOrEqual(mid, matrix) >= k):
                    ans = mid 
                    r = mid - 1
                else:
                    l = mid + 1

            return ans

        def countLessOrEqual(mid, matrix):
            r = 0 
            c = len(matrix) - 1
            count = 0
            while True:
                if c == -1 or r == len(matrix):
                    break
                if(matrix[r][c] <= mid):
                    count += c + 1
                    r += 1
                else:
                    c -= 1

            return count

        return binarySearch(matrix, k)