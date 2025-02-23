import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]

def main():

    n, m, s, f = map(int, input().split())

    graph = {i: [] for i in range(n)}
    
    for _ in range(m):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight)) 

    shortest_path_length = dijkstra(graph, s, f)
    print(shortest_path_length)

if __name__ == "__main__":
    main()
