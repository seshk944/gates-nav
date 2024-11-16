import heapq

# assume that the map tracer is working

# get distance
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# run the a-star search algorithm using heapq sorting
def astar_search(map, start, goal):
    neighbors = [(0,1),(1,0),(0,-1),(-1,0)]  # 4-connected grid
    close_set = set()
    came_from = {}
    actual = {start:0}
    total = {start:manhattan_distance(start, goal)}
    open_heap = [] # list of highest priority i.e. lowest total costs

    heapq.heappush(open_heap, (total[start], start))

    while open_heap:
        current = heapq.heappop(open_heap)[1]

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        close_set.add(current)
        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries
            if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]):
                if map[neighbor[0]][neighbor[1]] == 0:
                    continue  # Skip obstacles
            else:
                continue  # Skip out-of-bounds positions

            tentative_g_score = actual[current] + 1

            if neighbor in close_set and tentative_g_score >= actual.get(neighbor, 0):
                continue

            if tentative_g_score < actual.get(neighbor, float('inf')):
                came_from[neighbor] = current
                actual[neighbor] = tentative_g_score
                total[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_heap, (total[neighbor], neighbor))

    return None  # No path found


