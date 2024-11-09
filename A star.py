import heapq

def astar(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]

        for neighbor in graph.get(current_node, []):
            tentative_g_score = g_score[current_node] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + (abs(neighbor[0] - goal[0]) + abs(neighbor[1] - goal[1]))
                heapq.heappush(open_list, (f_score, neighbor))

    return []

# Example usage:
graph = {(0, 0): [(0, 1), (1, 0)], (0, 1): [(0, 0), (1, 1)], (1, 0): [(0, 0), (1, 1), (2, 0)], (1, 1): [(0, 1), (1, 0), (2, 1)], (2, 0): [(1, 0), (2, 1)], (2, 1): [(1, 1), (2, 0)]}
start = (0, 0)
goal = (2, 1)

print("Path:", astar(graph, start, goal))