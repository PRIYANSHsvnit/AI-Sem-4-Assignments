from collections import defaultdict, deque
import sys

class Graph:
    def __init__(self):
        # Adjacency list
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # MIN

    def bfs(self, start, end):
        result = []
        q = deque()
        q.append(([start], 0))

        min_hops = sys.maxsize

        while q:
            path, cost = q.popleft()

            if len(path) > min_hops:
                continue

            curr = path[-1]

            if curr == end:
                min_hops = len(path)
                result.append((path, cost))
                continue

            for nxt, wt in self.adj[curr]:
                if nxt not in path:
                    q.append((path + [nxt], cost + wt))

        return result
    
    #BFS

    def bfs_all_paths(self, start, end):
        result = []
        q = deque()
        q.append(([start], 0))

        while q:
            path, cost = q.popleft()
            curr = path[-1]

            if curr == end:
                result.append((path, cost))
                continue

            for nxt, wt in self.adj[curr]:
                if nxt not in path: 
                    q.append((path + [nxt], cost + wt))

        return result
    
    #DFS

    def _dfs_util(self, curr, end, path, cost, result, visited):
        if curr == end:
            result.append((path.copy(), cost))
            return

        visited.add(curr)

        for nxt, wt in self.adj[curr]:
            if nxt not in visited:
                path.append(nxt)
                self._dfs_util(nxt, end, path, cost + wt, result, visited)
                path.pop()

        visited.remove(curr)

    def dfs(self, start, end):
        result = []
        visited = set()
        self._dfs_util(start, end, [start], 0, result, visited)
        return result


if __name__ == "__main__":
    g = Graph()

    g.add_edge("Syracuse", "Buffalo", 150)
    g.add_edge("Syracuse", "Boston", 312)
    g.add_edge("Syracuse", "New York", 254)
    g.add_edge("Syracuse", "Pittsburgh", 253)
    g.add_edge("Syracuse", "Portland", 107)
    g.add_edge("Buffalo", "Detroit", 256)
    g.add_edge("Buffalo", "Cleveland", 189)
    g.add_edge("Buffalo", "Pittsburgh", 215)
    g.add_edge("Detroit", "Cleveland", 169)
    g.add_edge("Detroit", "Chicago", 283)
    g.add_edge("Cleveland", "Chicago", 345)
    g.add_edge("Cleveland", "Columbus", 144)
    g.add_edge("Cleveland", "Pittsburgh", 134)
    g.add_edge("Columbus", "Pittsburgh", 185)
    g.add_edge("Columbus", "Indianapolis", 176)
    g.add_edge("Indianapolis", "Chicago", 182)
    g.add_edge("Pittsburgh", "Philadelphia", 305)
    g.add_edge("Pittsburgh", "Baltimore", 247)
    g.add_edge("Philadelphia", "Baltimore", 101)
    g.add_edge("Philadelphia", "New York", 97)
    g.add_edge("New York", "Providence", 181)
    g.add_edge("New York", "Boston", 215)
    g.add_edge("Providence", "Boston", 50)
    g.add_edge("Portland", "Boston", 107)

    start = "Syracuse"
    end = "Chicago"

    print("MIN PATHS (BFS) =")
    for path, cost in g.bfs(start, end):
        print(" -> ".join(path), f"| Cost = {cost} miles")

    print("\nALL PATHS (BFS) =")
    for path, cost in g.bfs_all_paths(start, end):
        print(" -> ".join(path), f"| Cost = {cost} miles")

    print("\nALL PATHS (DFS) =")
    for path, cost in g.dfs(start, end):
        print(" -> ".join(path), f"| Cost = {cost} miles")