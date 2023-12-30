#ALL POSSIBLE FULL BINARY TREES 894 LEETCODE

memo = {}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def backtracking(n):
    if n % 2 == 0:
        return []
    elif n == 1:
        return [TreeNode(0)]
    elif n in memo:
        return memo[n]
    else:
        res = []
        for i in range(1,n,2):
            right = backtracking(i)
            left = backtracking(n-i-1)
            
            print(n)
            for l in left:
                for r in right:
                    print(left, right)
                    newnode = TreeNode(0, l, r)
                    res.append(newnode)
                    print(res)

        memo[n] = res
        return res
    
print(backtracking(7))
