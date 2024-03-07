class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        g = {}
        n = len(graph) - 1

        for index, i in enumerate(graph):
            if index not in g:
                g[index] = []

            for j in i:
                g[index].append(j)

        def dfs(vertex, current):
            if vertex == n:
                self.ans.append(current.copy())
            else:
                for i in g[vertex]:
                    current.append(i)
                    dfs(i, current)
                    current.pop()



        dfs(0, [0])
        return self.ans