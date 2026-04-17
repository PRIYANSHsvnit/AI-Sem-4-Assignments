import random

cities = ['A','B','C','D','E','F','G','H']

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

N = len(cities)

# cost function
def cost(path):
    c = 0
    for i in range(N-1):
        c += dist[path[i]][path[i+1]]
    c += dist[path[-1]][path[0]]
    return c

# create random chromosome
def random_path():
    p = list(range(N))
    random.shuffle(p)
    return p

# create population
def init_population(size):
    return [random_path() for _ in range(size)]

# selection
def selection(pop):
    pop = sorted(pop, key=cost)
    return pop[:len(pop)//2]

# one-point crossover
def one_point_crossover(p1, p2):
    point = random.randint(1, N-2)
    child = p1[:point]

    for city in p2:
        if city not in child:
            child.append(city)

    return child

# two-point crossover
def two_point_crossover(p1, p2):
    a,b = sorted(random.sample(range(N),2))
    child = [-1]*N
    child[a:b] = p1[a:b]

    ptr = 0
    for city in p2:
        if city not in child:
            while child[ptr] != -1:
                ptr += 1
            child[ptr] = city

    return child

# mutation
def mutate(path):
    i,j = random.sample(range(N),2)
    path[i],path[j] = path[j],path[i]

# genetic algorithm
def GA(crossover_type):

    population = init_population(30)

    for generation in range(200):

        population = selection(population)
        new_pop = population[:]

        while len(new_pop) < 30:

            p1,p2 = random.sample(population,2)

            if crossover_type == "one":
                child = one_point_crossover(p1,p2)
            else:
                child = two_point_crossover(p1,p2)

            if random.random() < 0.1:
                mutate(child)

            new_pop.append(child)

        population = new_pop

    best = min(population, key=cost)

    return best, cost(best)


# run algorithm
best1, cost1 = GA("one")
best2, cost2 = GA("two")

print("One-point crossover")
print([cities[i] for i in best1], cost1)

print("\nTwo-point crossover")
print([cities[i] for i in best2], cost2)