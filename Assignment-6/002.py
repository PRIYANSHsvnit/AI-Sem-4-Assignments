class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, item):
        # item = (priority, node)
        self.data.append(item)

    def pop(self):
        # remove and return minimum priority element
        min_index = 0
        for i in range(1, len(self.data)):
            if self.data[i][0] < self.data[min_index][0]:
                min_index = i

        item = self.data[min_index]
        self.data.pop(min_index)
        return item

    def empty(self):
        return len(self.data) == 0


maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

rows = 5
cols = 5


def find_start_and_goals(maze):
    start = None
    goals = []

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goals.append((i, j))

    return start, goals


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node):
    x, y = node
    neighbors = []

    # U
    if x - 1 >= 0 and maze[x - 1][y] != 1:
        neighbors.append((x - 1, y))

    # D
    if x + 1 < rows and maze[x + 1][y] != 1:
        neighbors.append((x + 1, y))

    # L
    if y - 1 >= 0 and maze[x][y - 1] != 1:
        neighbors.append((x, y - 1))

    # R
    if y + 1 < cols and maze[x][y + 1] != 1:
        neighbors.append((x, y + 1))

    return neighbors


def reconstruct_path(parent, start, goal):
    path = []
    curr = goal

    while curr != None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path


def A_star(start, goal):
    pq = PriorityQueue()

    g = {}
    f = {}
    parent = {}

    # initialize
    g[start] = 0
    f[start] = heuristic(start, goal)
    parent[start] = None

    pq.push((f[start], start))

    closed_list = []  # explored nodes

    while not pq.empty():
        priority, current = pq.pop()

        if current in closed_list:
            continue

        closed_list.append(current)

        print("\nChosen Node = ", current)
        print("g(n) = ", g[current])
        print("h(n) = ", heuristic(current, goal))
        print("f(n) = ", f[current])
        print("Reason = It has the minimum f(n) = g(n)+h(n) in OPEN list.")

        if current == goal:
            print("\nGoal Reached!")
            path = reconstruct_path(parent, start, goal)
            return path, closed_list, g[goal]

        print("\nChecking Neighbors:")

        for neighbor in get_neighbors(current):

            new_g = g[current] + 1

            print("\nNeighbor:", neighbor)
            print("Step Cost = 1")
            print("New g(n) =", new_g)
            print("h(n) =", heuristic(neighbor, goal))
            print("New f(n) =", new_g + heuristic(neighbor, goal))

            if neighbor not in g or new_g < g[neighbor]:
                print("Updating (Better path found or first visit)")
                g[neighbor] = new_g
                f[neighbor] = new_g + heuristic(neighbor, goal)
                parent[neighbor] = current
                pq.push((f[neighbor], neighbor))
            else:
                print("Not Updating (Existing path is better)")

    return None, closed_list, None


def collect_all_rewards(start, goals):
    current = start
    total_cost = 0

    full_path = []
    all_explored = []

    while len(goals) > 0:

        # Choose nearest reward based on heuristic (can also use A* cost)
        nearest_goal = goals[0]
        min_h = heuristic(current, nearest_goal)

        for g in goals:
            if heuristic(current, g) < min_h:
                min_h = heuristic(current, g)
                nearest_goal = g

        print("/nCurrent Position:", current)
        print("Target Reward:", nearest_goal)

        path, explored, cost = A_star(current, nearest_goal)

        if path is None:
            print("No path found to reward:", nearest_goal)
            return None

        print("Path Found:", path)
        print("Explored Tiles:", explored)
        print("Cost to Reward:", cost)

        total_cost += cost

        # Add to final combined record
        if len(full_path) == 0:
            full_path += path
        else:
            full_path += path[1:]  # avoid duplicate node

        all_explored += explored

        # Update current position and remove reward
        current = nearest_goal
        goals.remove(nearest_goal)

    return full_path, all_explored, total_cost


start, goals = find_start_and_goals(maze)
goals_copy = goals.copy()  # for final reporting

print("Start State:", start)
print("Rewards (Goals):", goals)

final_path, explored_tiles, total_cost = collect_all_rewards(start, goals_copy)

print("FINAL RESULT (ALL REWARDS COLLECTED)")
print("Final Combined Path:", final_path)
print("Total Tiles in Final Path:", len(final_path))
print("Total Cost (Moves):", len(final_path) - 1)

print("\nAll Explored Tiles During Search:")
print(explored_tiles)
print("Total Explored Tiles Count:", len(explored_tiles))