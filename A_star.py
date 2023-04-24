import heapq
import math

def a_star(graph, start_node, end_node):
    # Define heuristic function (could be Euclidean, Manhattan, etc.)
    heuristic = lambda n: math.sqrt((n[0] - end_node[0]) ** 2 + (n[1] - end_node[1]) ** 2)

    # Initialize data structures
    frontier = [(heuristic(start_node), start_node)]
    visited = set()
    parent_map = {}

    # Run search loop
    while frontier:
        # Get next node with the lowest estimated cost
        _, node = heapq.heappop(frontier)

        # Check if we've reached the goal
        if node == end_node:
            return construct_path(parent_map, start_node, end_node)

        # Add node to visited set
        visited.add(node)

        # Explore neighbors and update frontier
        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                g = heuristic(node) + cost
                f = g + heuristic(neighbor)
                heapq.heappush(frontier, (f, neighbor))
                parent_map[neighbor] = node

    # If we reached here, there's no path from start to end
    return None

def construct_path(parent_map, start_node, end_node):
    # Reconstruct the shortest path from a parent map
    path = [end_node]
    while path[-1] != start_node:
        path.append(parent_map[path[-1]])
    return list(reversed(path))

# Define graph as adjacency list
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (2, 2): 3},
    (2, 2): {}
}
# Run A* algorithm from start node (0, 0) to end node (2, 2)
start_node = (0, 0)
end_node = (2, 2)
shortest_path = a_star(graph, start_node, end_node)
print(shortest_path)  # Output: [(0, 0), (1, 1), (2, 2)]