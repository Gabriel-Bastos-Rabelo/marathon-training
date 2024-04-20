class Grafo:
    def __init__(self, vertices) -> None:
        self.numVertices = vertices
        self.grafo = [[0 for i in range(vertices)] for j in range(vertices)]


    def inserirAresta(self, a, b) -> bool:
        if a < self.numVertices and a >= 0 and  b < self.numVertices and b >= 0:
            self.grafo[a][b] = 1
            return True
        
        return False

    def removerAresta(self, a, b) -> bool:
        if a < self.numVertices and a >= 0 and  b < self.numVertices and b >= 0:
            self.grafo[a][b] = 0
            return True
        
        return False
    


    

    