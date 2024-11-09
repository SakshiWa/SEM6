# BFS, DFS
from collections import deque

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(graph[node])

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

# Example usage:
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("DFS:")
dfs(graph, 2)
print("\nBFS:")
bfs(graph, 2)