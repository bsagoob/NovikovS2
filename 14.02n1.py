def find_social_clusters(n, relations):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for a, b in relations:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    clusters = []

    def bfs(start):
        queue = deque([start])
        cluster = []
        visited.add(start)

        while queue:
            user = queue.popleft()
            cluster.append(user)
            for neighbor in graph[user]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return cluster

    for user in range(n):
        if user not in visited:
            cluster = bfs(user)
            clusters.append(cluster)

    clusters.sort(key=lambda x: (len(x), x))

    return clusters


n = 5 
relations = [(0, 1), (1, 2), (3, 4)]

result = find_social_clusters(n, relations)
print(result)
