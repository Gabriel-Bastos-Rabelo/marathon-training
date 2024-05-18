from collections import deque

class Solution:

    def bfs(root):
        fila = deque()

        fila.append((root, 0))

        menorAltura = float('inf')
        while fila:
            v = fila.popleft()
            if v[0].left == None and v[0].right == None:
                menorAltura = min(menorAltura, 1 + v[1])
            elif v[0].left == None:
                fila.append((v[0].right), v[1] + 1)
            elif v[0].right == None:
                fila.append((v[0].left), v[1] + 1)

            else:
                fila.append((v[0].right), v[1] + 1)
                fila.append((v[0].left), v[1] + 1)

        return menorAltura
                


    def dfs(self, root):
        if root.right == None and root.left == None:
            return 0
        if root.left == None:
            return 1 + self.dfs(root.right)
        elif root.right == None:
            return 1 + self.dfs(root.left)

        return min(1 + self.dfs(root.right), 1 + self.dfs(root.left))
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + self.dfs(root)