class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        # Insert (priority, item)
        self.queue.append((priority, item))

    def pop(self):
        # Remove and return item with minimum priority
        min_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i
        return self.queue.pop(min_index)

    def is_empty(self):
        return len(self.queue) == 0

def expand(grid, node):
    rows, cols = len(grid), len(grid[0])
    x, y = node
    choraya = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
    for dx, dy in choraya:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield (nx, ny)

def path_cost(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])                                             # Cost Function (Manhattan Distance)

def best_first_search(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    priority_queue = PriorityQueue()# Min Heap based on path cost
    priority_queue.push(start, path_cost(start, end))

    reached = set()
    parent = {start: None}

    choraya = [(-1,0), (1,0), (0,-1), (0,1)]                                                   # Possible Movements (Up, Down, Left, Right)

    while not priority_queue.is_empty():
        h, current = priority_queue.pop()

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        reached.add(current)

        print(f"\nCurrent Node = {current}")
        candidates = []

        for neighbor in expand(grid,current):
            nx, ny = neighbor

            if (nx, ny) not in reached and (nx, ny) not in parent:                        # Check for valid cell
                if grid[nx][ny] == 0:                                                     # Check if cell is Hallway
                        cost = path_cost((nx, ny), end)
                        candidates.append((cost, (nx, ny)))
                else:
                        candidates.append((float('inf'), (nx, ny)))                           # Invalid Cell with High Cost

                parent[(nx, ny)] = current
                priority_queue.push((nx, ny), cost)

        if candidates:
            print("Candidates = ")
            for cost, pos in candidates:
                print(f"Position = {pos}, Path Cost =  {cost}")
            chosen = min(candidates, key=lambda x: x[0])
            print(f"Chosen = {chosen[1]} because it has MINIMUM Path Cost = {chosen[0]}")


grid = [                                                                                       # Based of Diagram in Assignment
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                                                            # 0 for Hallway and 1 for Wall/Rooms
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


start = (5, 2)                                                                                 # Entry
end = (3, 8)                                                                                   # Exit

path = best_first_search(grid, start, end)

if path:
    print("Evacuation Path = ")
    for step in path:
        print(step)
else:
    print("No path found")