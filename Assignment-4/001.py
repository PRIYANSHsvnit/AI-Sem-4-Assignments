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


def expand(graph,node):
    for i in graph[node]:
        yield i

def best_first_search(graph, path_cost, start, end):
    priority_queue = PriorityQueue()
    priority_queue.push(start, path_cost[start])      # Min Heap based on path cost

    reached = set()
    parent = {}

    while not priority_queue.is_empty():
        h, current = priority_queue.pop()

        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return path[::-1]                                      # Reversing the path as the path is from leave to root

        reached.add(current)

        print(f"\nCurrent Node = {current}")
        candidates = []

        for neighbor in expand(graph,current):
            if neighbor not in reached and neighbor not in parent:
                candidates.append((path_cost[neighbor], neighbor))
                parent[neighbor] = current
                priority_queue.push(neighbor, path_cost[neighbor])

        if candidates:
            print("Candidates = ")
            for cost, pos in candidates:
                print(f"Position = {pos}, Path Cost =  {cost}")
            chosen = min(candidates, key=lambda x: x[0])
            print(f"Chosen = {chosen[1]} because it has MINIMUM Path Cost = {chosen[0]}")

    return None

graph = {                                                         # Adjacency List for Representation of the Graph
    "Chicago": ["Detroit", "Cleveland", "Indianapolis"],
    "Detroit": ["Chicago", "Cleveland", "Buffalo"],
    "Cleveland": ["Chicago", "Detroit", "Buffalo", "Columbus", "Pittsburgh"],
    "Columbus": ["Cleveland", "Pittsburgh", "Indianapolis"],
    "Indianapolis": ["Chicago", "Columbus"],
    "Pittsburgh": ["Cleveland", "Columbus", "Buffalo", "Philadelphia", "Baltimore"],
    "Buffalo": ["Detroit", "Pittsburgh", "Syracuse", "Cleveland"],
    "Syracuse": ["Buffalo", "Boston", "New York", "Philadelphia"],
    "Philadelphia": ["Pittsburgh", "New York", "Baltimore", "Syracuse"],
    "Baltimore": ["Pittsburgh", "Philadelphia"],
    "New York": ["Syracuse", "Philadelphia", "Boston", "Providence"],
    "Boston": ["New York", "Syracuse", "Providence", "Portland"],
    "Providence": ["Boston", "New York"],
    "Portland": ["Boston"]
}

path_cost = {                                                     # Prioritized Path Cost (Lower is Better)
    "Chicago": 1000,
    "Detroit": 700,
    "Cleveland": 650,
    "Indianapolis": 900,
    "Columbus": 800,
    "Pittsburgh": 500,
    "Buffalo": 300,
    "Syracuse": 150,
    "New York": 100,
    "Philadelphia": 200,
    "Baltimore": 250,
    "Boston": 100,
    "Providence": 50,
    "Portland": 0
}

path = best_first_search(graph, path_cost, "Chicago", "Portland")
print("Path = ", " → ".join(path))

'''Best First Search efficiently reduces the number of explored paths by using path cost information.
Compared to Breadth First Search, it expands fewer nodes and reaches the destination faster.
However, since it does not consider actual path cost, it does not always guarantee the optimal path.'''