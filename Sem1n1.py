class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):
        if not self.graph:
            return False

        def dfs(v, visited):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        visited = set()
        start_vertex = next(iter(self.graph))
        dfs(start_vertex, visited)

        return len(visited) == len(self.graph)

n = int(input("число пар узлов: "))
g = Graph()

for _ in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

if g.is_connected():
    print(True)
else:
        print(False)
