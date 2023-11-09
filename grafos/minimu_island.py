def island_count(grid):
    visited = set()
    cont = 0
    smaller_island = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            stack = []
            resp = explore(grid, row, col, stack, visited)
            if resp < smaller_island:
                smaller_island = resp

    print(smaller_island)


def explore(grid, row, col, stack, visited):
    if grid[row][col] == "W":
        return float('inf')
    else:
        if (row, col) in visited:
            return float('inf')
        visited.add((row, col))
        global cont
        cont += 1
        if row > 0 and col > 0 and row < len(grid) - 1 and col < len(grid[0]) - 1:
            explore(grid, row+1, col, stack, visited)
            explore(grid, row-1, col, stack, visited)
            explore(grid, row, col+1, stack, visited)
            explore(grid, row, col-1, stack, visited)
        elif row == 0 and col == 0:
            explore(grid, row+1, col, stack, visited)
            explore(grid, row, col+1, stack, visited)
        elif row == 0 and col == len(grid[0]) - 1:
            explore(grid, row+1, col, stack, visited)
            explore(grid, row, col-1, stack, visited)
        elif row == 0:
            explore(grid, row + 1, col, stack, visited)
            explore(grid, row, col-1, stack, visited)
            explore(grid, row, col+1, stack, visited)
        elif row == len(grid) - 1 and col == 0:
            explore(grid, row-1, col, stack, visited)
            explore(grid, row, col+1, stack, visited)
        elif col == 0:
            explore(grid, row+1, col, stack, visited)
            explore(grid, row-1, col, stack, visited)
            explore(grid, row, col+1, stack, visited)
        elif row == len(grid) - 1 and col == len(grid[0]) - 1:
            explore(grid, row-1, col, stack, visited)
            explore(grid, row, col-1, stack, visited)
        elif col == len(grid[0]) - 1:
            explore(grid, row+1, col, stack, visited)
            explore(grid, row-1, col, stack, visited)
            explore(grid, row, col-1, stack, visited)

        elif row == len(grid) - 1:
            explore(grid, row-1, col, stack, visited)
            explore(grid, row, col-1, stack, visited)
            explore(grid, row, col+1, stack, visited)

    return cont


grid = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]

cont = 0
island_count(grid)
