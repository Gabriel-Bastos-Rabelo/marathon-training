class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.g = {}  
        self.n = n  
        for edge in edges:
            if edge[0] not in self.g:
                self.g[edge[0]] = []
            self.g[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
       
        if edge[0] not in self.g:
            self.g[edge[0]] = [(edge[1], edge[2])]
        else:
            self.g[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        

        distances = {node: float('inf') for node in range(self.n)}  
        distances[node1] = 0  

        queue = [(0, node1)]  
        visited = set()  

        while queue:
            dist, node = heapq.heappop(queue)  

            if node in visited:  
                continue
            visited.add(node)  

           
            for neighbor, weight in self.g.get(node, []):  
                new_dist = dist + weight
                if new_dist < distances[neighbor]:  
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))  

        return distances[node2] if distances[node2] != float('inf') else -1  



