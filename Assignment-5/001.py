class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def empty(self):
        return len(self.data) == 0

Total_Girls = 3
Total_Boys = 3

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] # (x,y) -> x for no. of girls and y for no. of boys

def is_valid(x,y): # x , y means in Left Side
    t = Total_Girls - x  # t , u means in Right Side
    u = Total_Boys - y

    if (x < 0 or y < 0 or x > Total_Girls or y > Total_Boys):
        return False
    
    if (x > 0 and y > x):
        return False
    
    if(t > 0 and u > t):
        return False
    
    return True

def generator(state):
    x , y , boat = state

    for i in moves:
        if(boat == 0):
            new_state = (x - i[0], y - i[1], 1)
        else:
            new_state = (x + i[0], y + i[1], 0)
    
        if(is_valid(new_state[0], new_state[1])):
            yield new_state

def state_to_index(state):
    x , y , boat = state
    return x * 8 + y * 2 + boat

def index_to_state(index):
    boat = index % 2
    index //= 2
    y = index % 4
    x = index // 4
    return (x, y, boat)

def reconstruct_path(parent, start_index, goal_index):
    path = []
    current_index = goal_index

    while current_index != -1:
        path.append(index_to_state(current_index))
        current_index = parent[current_index]

    path.reverse()
    
    if(len(path) > 0 and state_to_index(path[0]) == start_index):
        return path
    return None

def DLS(start, goal, limit):
    explored = 0

    start_idx = state_to_index(start)
    goal_idx = state_to_index(goal)

    best_depth = [999] * 32          # 4 * 4 * 2 = 32 possible states
    parent = [-1] * 32

    stack = Stack()
    stack.push((start, 0))

    best_depth[start_idx] = 0

    while not stack.empty():
        state, depth = stack.pop()
        explored += 1

        print(f"Exploring State = {state} at Depth = {depth}")

        if state == goal:
            return reconstruct_path(parent, start_idx, goal_idx), explored

        if depth == limit:
            print(f"Reached depth limit at State = {state}, skipping further exploration.")
            continue

        reached = []
        for s in generator(state):
            reached.append(s)

        for i in range(len(reached) - 1, -1, -1):
            child = reached[i]
            child_idx = state_to_index(child)

            # allow revisit if found at smaller depth
            if depth + 1 < best_depth[child_idx]:
                best_depth[child_idx] = depth + 1
                parent[child_idx] = state_to_index(state)
                stack.push((child, depth + 1))

    print("No solution found within depth limit.")

    return None, explored


def IDS(start, goal, max_depth):
    total_explored = 0

    for depth in range(max_depth + 1):
        print(f"\nStarting Iteration with Depth Limit = {depth}")
        path, explored = DLS(start, goal, depth)
        total_explored += explored

        if path is not None:
            print(f"Solution found at depth {depth} with {explored} states explored in this iteration.")
            return path, total_explored, depth
        
    print("No solution found within maximum depth limit.")

    return None, total_explored, None


def print_solution(path):
    if path is None:
        print("No solution found !")
        print()
        return

    print("\nStep | Left Side(G,B) | Right Side(G,B) | Boat")
    print()

    for i in range(len(path)):
        x, y, boat = path[i]
        t = Total_Girls - x
        u = Total_Boys - y

        boat_side = "Left" if boat == 0 else "Right"

        print(f"{i:>4} | ({x},{y})         | ({t},{u})          | {boat_side}")

start_state = (3, 3, 0)
goal_state = (0, 0, 1)

print("DEPTH LIMITED SEARCH (Limit = 3) = ")

dls_path, dls_explored = DLS(start_state, goal_state, limit=3)
print_solution(dls_path)
print("Explored States = ", dls_explored)

print("\nITERATIVE DEEPENING SEARCH = ")

ids_path, ids_explored, found_depth = IDS(start_state, goal_state, max_depth=20)
print_solution(ids_path)

print("Explored States = ", ids_explored)
print("Solution Found at Depth = ", found_depth)