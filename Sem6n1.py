from collections import defaultdict

def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx != 0 or dy != 0) and 0 <= x + dx < max_x and 0 <= y + dy < max_y:
                neighbors.append((x + dx, y + dy))
    return neighbors

def dfs(board, word, x, y, visited):
    if word in dictionary:
        found_words.add(word)
    
    if len(word) > max_word_length:
        return

    visited.add((x, y))
    
    for nx, ny in get_neighbors(x, y, len(board), len(board[0])):
        if (nx, ny) not in visited:
            dfs(board, word + board[nx][ny], nx, ny, visited)
    
    visited.remove((x, y))

def find_words(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, board[i][j], i, j, set())

n = int(input("Введите количество слов в словаре: "))
dictionary = set(input("Введите слова через пробел: ").split())
m, l = map(int, input("Введите размеры доски (M L): ").split())
board = [input("Введите строку {}: ".format(i + 1)).strip() for i in range(m)]

found_words = set()
max_word_length = max(len(word) for word in dictionary)

find_words(board)

print(" ".join(sorted(found_words)))
