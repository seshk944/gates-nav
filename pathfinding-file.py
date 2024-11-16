import heapq

# assume that the map tracer is working
import heapq

map_rep = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

def manhattan_distance(a, b):
    """Calculate Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(map, start, goal):
    """Perform A* search algorithm."""
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    actual = {start: 0}
    total = {start: manhattan_distance(start, goal)}
    open_heap = []

    # Initialize the priority queue with the start position
    heapq.heappush(open_heap, (total[start], start))

    while open_heap:
        current = heapq.heappop(open_heap)[1]

        # Check if we've reached the goal
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return the path from start to goal

        close_set.add(current)

        # Explore neighbors
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check if the neighbor is within bounds
            if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]):
                # Skip walls
                if map[neighbor[0]][neighbor[1]] == 1:
                    continue
            else:
                continue  # Out-of-bounds

            tentative_g_score = actual[current] + 1

            # If neighbor is in closed set and the tentative score is not better, skip
            if neighbor in close_set and tentative_g_score >= actual.get(neighbor, 0):
                continue

            # If it's a better path, update path and push to heap
            if tentative_g_score < actual.get(neighbor, float('inf')):
                came_from[neighbor] = current
                actual[neighbor] = tentative_g_score
                total[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_heap, (total[neighbor], neighbor))

    return None  # No path found

# Testing the function with the provided maze
start = (2, 1)
goal = (8, 8)
path = astar_search(map_rep, start, goal)

# Print the result
if path:
    print("Path found:", path)
else:
    print("No path found")
