from itertools import permutations

def min_assignment_cost(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')

    for perm in permutations(range(n)):
        current_cost = sum(cost_matrix[i][perm[i]] for i in range(n))
        min_cost = min(min_cost, current_cost)

    return min_cost

with open("INPUT.TXT", "r") as file:
    n = int(file.readline().strip())
    cost_matrix = [list(map(int, file.readline().strip().split())) for _ in range(n)]

result = min_assignment_cost(cost_matrix)

with open("OUTPUT.TXT", "w") as file:
    file.write(str(result))

