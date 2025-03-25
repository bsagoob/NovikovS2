def assign_workers(cost_matrix):
    from itertools import permutations
    
    n = len(cost_matrix)
    min_cost = float('inf')

    for perm in permutations(range(n)):
        current_cost = sum(cost_matrix[i][perm[i]] for i in range(n))
        min_cost = min(min_cost, current_cost)

    return min_cost

def main():
    with open('INPUT.TXT', 'r') as infile:
        n = int(infile.readline().strip())
        cost_matrix = [list(map(int, infile.readline().strip().split())) for _ in range(n)]

    result = assign_workers(cost_matrix)

    with open('OUTPUT.TXT', 'w') as outfile:
        outfile.write(str(result) + '\n')

if __name__ == "__main__":
    main()
