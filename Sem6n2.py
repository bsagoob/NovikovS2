class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(n, edges, exclude_edge=None):
    uf = UnionFind(n)
    total_weight = 0
    count = 0
    
    for (u, v, weight) in sorted(edges, key=lambda x: x[2]):
        if (u, v, weight) == exclude_edge:
            continue
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            total_weight += weight
            count += 1
            if count == n - 1:
                break
                
    return total_weight if count == n - 1 else float('inf')


def main():
    n, m = map(int, input().split())
    edges = []
    
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((u - 1, v - 1, w))
    
    results = []
    
    for i in range(m):
        min_spanning_tree_weight = kruskal(n, edges, edges[i])
        results.append(min_spanning_tree_weight)

    for weight in results:
        print(weight)

if __name__ == "__main__":
    main()
