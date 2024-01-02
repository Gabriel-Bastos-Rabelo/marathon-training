#leetcode 222

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def rightHeight(root):
            height = 0
            while(root != None):
                height += 1
                root = root.right

            return height

        def leftHeight(root):
            height = 0
            while(root != None):
                height += 1
                root = root.left

            return height
        
        rightHeight = rightHeight(root)
        leftHeight = leftHeight(root)

        if(rightHeight == leftHeight):
            return 2 ** leftHeight - 1
        
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


