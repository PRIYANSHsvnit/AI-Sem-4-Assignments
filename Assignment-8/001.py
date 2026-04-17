import random

# Distance matrix
dist = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

cities = ['A','B','C','D','E','F','G','H']
n = len(cities)


# Calculate tour cost
def cost(path):
    c = 0
    for i in range(n-1):
        c += dist[path[i]][path[i+1]]
    c += dist[path[-1]][path[0]]
    return c


# Generate random path
def random_path():
    p = list(range(n))
    random.shuffle(p)
    return p


# Generate neighbors by swapping two cities
def neighbors(path):
    neigh = []
    for i in range(n):
        for j in range(i+1,n):
            new = path[:]
            new[i], new[j] = new[j], new[i]
            neigh.append(new)
    return neigh


# Local Beam Search
def beam_search(k, iterations=200):

    states = [random_path() for _ in range(k)]

    best_state = None
    best_cost = float('inf')

    for _ in range(iterations):

        all_neighbors = []

        for s in states:
            all_neighbors.extend(neighbors(s))

        all_neighbors = sorted(all_neighbors, key=cost)

        states = all_neighbors[:k]

        if cost(states[0]) < best_cost:
            best_cost = cost(states[0])
            best_state = states[0]

    return best_state, best_cost


# Run for different beam widths
for k in [3,5,10]:

    best_path, best_cost = beam_search(k)

    tour = [cities[i] for i in best_path]

    print("\nBeam Width = ",k)
    print("Best Tour = ", " -> ".join(tour), "->", tour[0])
    print("Cost = ", best_cost)