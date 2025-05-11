def can_seat_persons(n, m, restrictions):
    graph = [[] for _ in range(n)]

    for a, b in restrictions:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    color = [-1] * n

    def bfs(start):
        queue = [start]
        color[start] = 0  

        while queue:
            node = queue.pop(0)

            for neighbor in graph[node]:
                if color[neighbor] == -1:  
                    color[neighbor] = 1 - color[node]  
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  
                    return False  
        return True

    for i in range(n):
        if color[i] == -1: 
            if not bfs(i):
                return "NO"

    return "YES"

with open("INPUT.TXT", "r") as file:
    n, m = map(int, file.readline().strip().split())
    restrictions = [tuple(map(int, file.readline().strip().split())) for _ in range(m)]

result = can_seat_persons(n, m, restrictions)

with open("OUTPUT.TXT", "w") as file:
    file.write(result)

