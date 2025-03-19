class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def is_reachable(self, start, end):
        def dfs(v, visited):
            if v == end:
                return True
            visited.add(v)
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False

        visited = set()
        return dfs(start, visited)

n = int(input("число узлов в графе: "))
edges = eval(input("пары узлов: "))
start, end = map(int, input("начальный и конечный узел: ").split())

g = DirectedGraph()

for u, v in edges:
    g.add_edge(u, v)

if g.is_reachable(start, end):
    print(True)
else:
    print(False)

