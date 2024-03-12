class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        self.g = {}
        paths = set()


        for i in connections:
            paths.add((i[0], i[1]))
            if i[0] not in self.g:
                self.g[i[0]] = []
            if i[1] not in self.g:
                self.g[i[1]] = []

            self.g[i[0]].append(i[1])
            self.g[i[1]].append(i[0])
        

        def dfs(node, parent):
            self.res += (parent, node) in paths

            for i in self.g[node]:
                if i == parent:
                    continue
                dfs(i, node)

        
        dfs(0, -1)
        return self.res
