from collections import defaultdict, deque
import sys

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self,u,v):
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
    ("Sunil", "Maya"),         # neha1 = middle , neh2 = right
    ("Sneha", "Rahul"),        # arjun1 = right , arjun2 = bottom
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

for u,v in edges:
    g.add_edge(u,v)

def bfstree(g,s):
    visi = set([s])
    parent = {s:None}
    q = deque([s])
    while q:
        n = q.popleft()
        for x in g.adj[n]:
            if x not in visi:
                visi.add(x)
                parent[x] = n
                q.append(x)

    return parent

def dfstree(g,s):
    visi = set()
    parent = {}
    def dfs(a,b):
        visi.add(a)
        parent[a] = b
        for x in g.adj[a]:
            if x not in visi:
                dfs(x,a)
    dfs(s,None)
    return parent

start = "Priya"
print("Adjancy List = \n")
g.display()
print("\n BFS Tree = \n")
bfs = bfstree(g,start)
for i in bfs:
    print(f"{bfs[i]}->{i}")
print("\n DFS Tree = \n")
dfs = dfstree(g,start)
for i in dfs:
    print(f"{dfs[i]}->{i}")