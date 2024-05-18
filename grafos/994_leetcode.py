from collections import defaultdict 
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(grid, visitados, podres, x, y):
    fila = deque()
    fila.append((x, y, 0))
    minutos = 0
    while fila:
        v = fila.popleft()
        minutos = max(minutos, v[2])
        for i in range(4):
            new_x = v[0] + dx[i]
            new_y = v[1] + dy[i]
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and (new_x, new_y) not in visitados and grid[new_x][new_y] == 1:
                visitados[(new_x, new_y)] = 0
                fila.append((new_x, new_y, v[2] + 1))


    return minutos
            

        
        

def orangeRotting():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    podres = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                podres.append((i, j))

    
    visitados = defaultdict()
    visitados[(0, 0)] = 0
    minutos = 0
    for podre in podres:
        minutos = max(minutos, bfs(grid, visitados, [], podre[0], podre[1]))

    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visitados:
                print(-1)
            
    print(minutos)


orangeRotting()