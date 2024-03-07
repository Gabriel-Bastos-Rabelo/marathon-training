class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = {}
        for i in edges:
            if i[0] not in g:
                g[i[0]] = []

            if i[1] not in g:
                g[i[1]] = []

            g[i[0]].append(i[1])
            g[i[1]].append(i[0])

        def dfs(vertex, destination):
            if vertex == destination:
                return True

            visited[vertex] = 0
            for i in g[vertex]:
                if visited[i] == -1:
                    if dfs(i, destination):
                        return True

            return False



        visited = [-1] * n
        return dfs(source, destination)