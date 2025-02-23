def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in range(len(graph)):
        if vertex not in visited:
            if dfs(vertex, -1):
                return True
    return False

def main():
    input_data = [
        (1, 0, 2),
        (2, 4),
        (1, 3),
        (2, 4),
        (1, 3)
    ]

    graph = {}
    for i in range(len(input_data)):
        graph[i] = input_data[i]

    if has_cycle(graph):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
