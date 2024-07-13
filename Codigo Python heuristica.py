     import heapq
def a_star_search(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    g_cost = {start: 0}
    came_from = {start: None}
    while open_set:  
        current_f_cost, current_node = heapq.heappop(open_set)  
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]
        for neighbor, cost in graph[current_node].items():
            tentative_g_cost = g_cost[current_node] + cost
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_cost, neighbor))
                came_from[neighbor] = current_node
    return None
def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)
graph = {
    (0, 0): {(1, 0): 1, (0, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (2, 1): 1, (1, 2): 1},
    (2, 1): {(1, 1): 1, (2, 2): 1},
    (1, 2): {(1, 1): 1, (2, 2): 1},
    (2, 2): {(2, 1): 1, (1, 2): 1}
}
start = (0, 0)
goal = (2, 2)
path = a_star_search(graph, start, goal, heuristic)
print("Path found:", path)
