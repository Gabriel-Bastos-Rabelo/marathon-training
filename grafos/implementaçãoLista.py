class Grafo:
    def __init__(self, vertices) -> None:
        self.grafo = [[] for i in range(vertices)]
        self.numVertices = vertices

    def inserirAresta(self, a, b):
        if a >= 0 and a < self.numVertices and b >= 0 and b < self.numVertices:
            self.grafo[a].append(b)
            return True
        return False

    def removerAresta(self, a, b):
        if a >= 0 and a < self.numVertices and b >= 0 and b < self.numVertices:
            self.grafo[a].remove(b)
            return True
        return False





grafo = Grafo(5)
grafo.inserirAresta(1, 2)
print(grafo.grafo)

