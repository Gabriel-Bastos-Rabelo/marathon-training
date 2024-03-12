class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        self.g = {node: [] for node in range(numCourses)}
        

        for i in prerequisites:
            self.g[i[0]].append(i[1])

        visited = set()
        onPath = set()

        def dfs(node):
            
            if node in onPath:
                return False
            
            if node in visited:
                return True

            
            onPath.add(node)
            visited.add(node)


            for neighbor in self.g[node]:
                if not dfs(neighbor):
                    return False
            
            
            onPath.remove(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True