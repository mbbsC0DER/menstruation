from collections import deque

graph = {
    'A' : ['B', 'C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

visited = set()
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node in visited:
        continue
    visited.add(node)
    print(node, end = " ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append(neighbour)