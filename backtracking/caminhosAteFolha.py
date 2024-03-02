class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.lista = []
        def dfs(root, current):
            if root.right == None and root.left == None:
                current.append(root.val)
                
                self.lista.append("->".join(map(lambda x: str(x), current.copy())))
            else:
                current.append(root.val)
                
                if(root.left != None):
                    dfs(root.left, current)
                    current.pop()
                
                if(root.right != None):
                    dfs(root.right, current)
                    current.pop()

        dfs(root, [])
        return self.lista