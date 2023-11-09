def largest_component(graph, current, visited):
    if current in visited:
        return False
    global number_edges
    number_edges += 1
    visited.add(current)
    for node in graph[current]:
        if node not in visited:
            largest_component(graph, node, visited)


largestComponent = {'0': ['8', '1', '5'], '1': ['0'], '5': ['0', '8'], '8': [
    '0', '5'], '2': ['3', '4'], '3': ['2', '4'], '4': ['3', '2']}


nodes = [0, 1, 2, 3, 4, 5, 8]
visited = set()
number_edges = 0
better_case = 0
for i in nodes:
    if i in visited:
        continue

    largest_component(largestComponent, str(i), visited)
    if number_edges > better_case:
        better_case = number_edges
    number_edges = 0
    visited.add(str(i))


print(better_case)
