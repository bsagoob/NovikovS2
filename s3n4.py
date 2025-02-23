import heapq

def dijkstra(graph, start, end):
    min_heap = [(0, start)]
    distances = {station: float('inf') for station in graph}
    distances[start] = 0
    
    while min_heap:
        current_distance, current_station = heapq.heappop(min_heap)
        
        if current_distance > distances[current_station]:
            continue
        
        for neighbor, time in graph[current_station].items():
            distance = current_distance + time
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances[end] if distances[end] != float('inf') else -1

def main():
    v, e = map(int, input("Введите количество станций и соединений: ").split())
    
    graph = {}
    
    for _ in range(e):
        line = input("Введите соединение станции и время: ").strip().split()
        station1, station2, time = line[0], line[1], int(line[2])
        
        if station1 not in graph:
            graph[station1] = {}
        if station2 not in graph:
            graph[station2] = {}
        
        graph[station1][station2] = time
        graph[station2][station1] = time 

    start_station = input("Введите начальную станцию: ")
    end_station = input("Введите конечную станцию: ")

    result = dijkstra(graph, start_station, end_station)
    
    print("Минимальное время в пути:", result)

if __name__ == "__main__":
    main()
