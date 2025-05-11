from collections import deque

def knight_moves(n, start):

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    

    steps = [[float('inf')] * n for _ in range(n)]
    

    queue = deque([start])
    steps[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        current_steps = steps[x][y]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and steps[nx][ny] == float('inf'):
                steps[nx][ny] = current_steps + 1
                queue.append((nx, ny))

    return steps


n = 5  
start_position = (2, 2) 
result = knight_moves(n, start_position)


for row in result:
    print(row)
