def prim(graph):
    mst, visited = set(), set()
    start = next(iter(graph.keys()))
    visited.add(start)
    while len(visited) < len(graph):
        edge = min((u, v, w) for u in visited for v, w in graph[u].items() if v not in visited)
        mst.add((edge[0], edge[1]))
        visited.add(edge[1])
    return mst

# Example usage:
graph = {'A': {'B': 2, 'D': 3}, 'B': {'A': 2, 'C': 1, 'D': 4}, 'C': {'B': 1, 'D': 5}, 'D': {'A': 3, 'B': 4, 'C': 5}}
print("Minimum Spanning Tree:", prim(graph))