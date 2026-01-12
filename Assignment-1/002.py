from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def display(self):
        for i in self.adj:
            print(i, "->", self.adj[i])


g = Graph()

edges = [
    ("Priya", "Raj"),
    ("Priya", "Aarav"),
    ("Raj", "Sunil"),
    ("Priya", "Akash"),
    ("Raj", "Neha1"),
    ("Akash", "Sunil"),
    ("Neha1", "Akash"),
    ("Aarav", "Neha1"),
    ("Neha2", "Aarav"),
    ("Sunil", "Sneha"),
    ("Sunil", "Maya"),
    ("Sneha", "Rahul"),
    ("Rahul", "Neha1"),
    ("Neha1", "Rahul"),
    ("Rahul", "Neha2"),
    ("Neha2", "Rahul"),
    ("Aarav", "Arjun1"),
    ("Neha2", "Arjun1"),
    ("Arjun1", "Rahul"),
    ("Rahul", "Arjun1"),
    ("Rahul", "Pooja"),
    ("Pooja", "Arjun2"),
    ("Maya", "Arjun2"),
    ("Arjun2", "Maya"),
]

for u, v in edges:
    g.add_edge(u, v)

# BFS Tree

def bfstree(g, s):
    visited = set([s])
    parent = {s: None}

    q = Queue()
    q.put(s)

    while not q.empty():
        n = q.get()

        for x in g.adj[n]:
            if x not in visited:
                visited.add(x)
                parent[x] = n
                q.put(x)

    return parent

# DFS Tree

def dfstree(g, s):
    visited = set()
    parent = {}

    def dfs(a, b):
        visited.add(a)
        parent[a] = b
        for x in g.adj[a]:
            if x not in visited:
                dfs(x, a)

    dfs(s, None)
    return parent


start = "Priya"

print("Adjacency List =\n")
g.display()

print("\nBFS Tree =\n")
bfs = bfstree(g, start)
for i in bfs:
    print(f"{bfs[i]} -> {i}")

print("\nDFS Tree =\n")
dfs = dfstree(g, start)
for i in dfs:
    print(f"{dfs[i]} -> {i}")