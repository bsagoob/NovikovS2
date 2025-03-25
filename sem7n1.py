def can_seat(N, conflicts):
    graph = [[] for _ in range(N)]

    for a, b in conflicts:
        graph[a].append(b)
        graph[b].append(a)

    color = [-1] * N

    def dfs(node, c):
        color[node] = c
        for neighbor in graph[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for i in range(N):
        if color[i] == -1: 
            if not dfs(i, 0):
                return False
    return True

with open('INPUT.TXT', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    conflicts = [tuple(map(int, file.readline().strip().split())) for _ in range(m)]

result = can_seat(n, conflicts)

with open('OUTPUT.TXT', 'w') as file:
    file.write('YES' if result else 'NO')
