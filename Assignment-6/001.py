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
    
cities = [
    "Chicago",        # 0
    "Indianapolis",   # 1
    "Columbus",       # 2
    "Cleveland",      # 3
    "Detroit",        # 4
    "Pittsburgh",     # 5
    "Buffalo",        # 6
    "Syracuse",       # 7
    "Baltimore",      # 8
    "Philadelphia",   # 9
    "New York",       # 10
    "Providence",     # 11
    "Boston",         # 12
    "Portland"        # 13
]

h = [
    860,  # Chicago
    780,  # Indianapolis
    640,  # Columbus
    550,  # Cleveland
    610,  # Detroit
    470,  # Pittsburgh
    400,  # Buffalo
    260,  # Syracuse
    360,  # Baltimore
    270,  # Philadelphia
    215,  # New York
    50,   # Providence
    0,    # Boston
    107   # Portland
]

n = len(cities)

graph = [
#   CHI  IND  COL  CLE  DET  PIT  BUF  SYR  BAL  PHL  NY   PRO  BOS  POR
    [0,  182, 0,   345, 283, 0,   0,   0,   0,   0,   0,   0,   0,   0],   # Chicago
    [182,0,   176, 0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   # Indianapolis
    [0,  176, 0,   144, 0,   185, 0,   0,   0,   0,   0,   0,   0,   0],   # Columbus
    [345,0,   144, 0,   169, 134, 189, 0,   0,   0,   0,   0,   0,   0],   # Cleveland
    [283,0,   0,   169, 0,   0,   256, 0,   0,   0,   0,   0,   0,   0],   # Detroit
    [0,  0,   185, 134, 0,   0,   215, 0,   247, 305, 0,   0,   0,   0],   # Pittsburgh
    [0,  0,   0,   189, 256, 215, 0,   150, 0,   0,   0,   0,   0,   0],   # Buffalo
    [0,  0,   0,   0,   0,   0,   150, 0,   0,   253, 254, 0,   312, 0],   # Syracuse
    [0,  0,   0,   0,   0,   247, 0,   0,   0,   101, 0,   0,   0,   0],   # Baltimore
    [0,  0,   0,   0,   0,   305, 0,   253, 101, 0,   97,  0,   0,   0],   # Philadelphia
    [0,  0,   0,   0,   0,   0,   0,   254, 0,   97,  0,   181, 215, 0],   # New York
    [0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   181, 0,   50,  0],   # Providence
    [0,  0,   0,   0,   0,   0,   0,   312, 0,   0,   215, 50,  0,   107], # Boston
    [0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   107, 0]    # Portland
]

    
def reconstruct_path(parent, start, goal):
    path = []
    curr = goal

    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path

def GBS(start, goal):
    pq = PriorityQueue()
    pq.push((h[start], start))

    reached = [0] * n
    parent = [-1] * n

    eo = []

    while not pq.empty():
        priority, node = pq.pop()

        if reached[node]:
            continue

        reached[node] = 1
        eo.append(node)

        print("\nChosen Node = ", cities[node])
        print("h(n) = ", h[node])
        print("Reason =  It has the minimum heuristic value among all nodes in OPEN list.")

        if node == goal:
            print("\nGoal Reached...")
            break

        print("\nNeighbors being checked = ")

        for i in range(n):
            if graph[node][i] != 0 and not reached[i]:

                print("\nNeighbor = ", cities[i])
                print("Step Cost = ", graph[node][i])
                print("h(n) = ", h[i])
                print("f(n) = h(n) = ", h[i])

                if parent[i] == -1:
                    parent[i] = node
                    print("Added to OPEN list")
                else:
                    print("Already discovered")
                pq.push((h[i], i))

    path = reconstruct_path(parent, start, goal)

    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    
    return eo, path, cost

def AStar(start,goal):
    pq = PriorityQueue()

    g = [float('inf')] * n
    g[start] = 0

    f = [float('inf')] * n
    f[start] = h[start]

    pq.push((f[start], start))

    reached = [0] * n
    parent = [-1] * n

    eo = []

    while not pq.empty():
        priority,node = pq.pop()
        if reached[node]:
            continue

        reached[node] = 1
        eo.append(node)

        print("\nChosen Node = ", cities[node])
        print("g(n) =", g[node])
        print("h(n) =", h[node])
        print("f(n) =", f[node])
        print("Reason =  It has the minimum f(n) among all nodes in OPEN list.")

        if node == goal:
            print("\nGoal Reached...")
            break

        print("\nNeighbors being checked = ")

        for i in range(n):
            if graph[node][i] != 0 and not reached[i]:
                newg = g[node] + graph[node][i]
                print("\nNeighbor = ", cities[i])
                print("Step Cost = ", graph[node][i])
                print("New g(n) = ", newg)
                print("h(n) = ", h[i])
                print("New f(n) = ", newg + h[i])

                if newg < g[i]:
                    print("Updating (Better Path Found)")
                    g[i] = newg
                    f[i] = g[i] + h[i]
                    parent[i] = node
                    pq.push((f[i], i))
                else:
                    print("Not Updating (Existing path is better)")
    path = reconstruct_path(parent, start, goal)
    return eo, path, g[goal]

start = 0   # Chicago
goal = 12   # Boston

print("\nGreedy Best First Search = \n")
explored, path, cost = GBS(start, goal)


print("Explored Order:", [cities[i] for i in explored])
print("Path:", " -> ".join([cities[i] for i in path]))
print("Cities explored:", len(explored))
print("Total Cost:", cost)

print("\nA* Search = \n")
explored1, path1, cost1 = AStar(start, goal)

print("Explored Order:", [cities[i] for i in explored1])
print("Path:", " -> ".join([cities[i] for i in path1]))
print("Cities explored:", len(explored1))
print("Total Cost:", cost1)

'''Greedy Best First Search explores fewer cities (5) because it only follows the heuristic.
A* explores more cities (8) because it checks multiple routes using g+h, but it guarantees the optimal path.
So:
 GBFS is faster (less explored cities)
 A* is smarter (more reliable + optimal)'''