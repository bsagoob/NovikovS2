from collections import Counter

def can_form_name(cubes, name):
    
    name_count = Counter(name)
    
    cube_count = Counter()
    
    for cube in cubes:
        cube_count.update(cube)
    
    for letter, count in name_count.items():
        if count > cube_count[letter]:
            return False  
    return True

with open("INPUT.TXT", "r") as file:
    N = int(file.readline().strip())
    name = file.readline().strip()
    cubes = [file.readline().strip() for _ in range(N)]

if can_form_name(cubes, name):
    print("YES")
    result_indices = []
    for letter in name:
        for i, cube in enumerate(cubes):
            if letter in cube and (i + 1) not in result_indices:  
                result_indices.append(i + 1)
                break
    with open("OUTPUT.TXT", "w") as file:
        file.write("YES\n")
        file.write(" ".join(map(str, result_indices)))
else:
    with open("OUTPUT.TXT", "w") as file:
        file.write("NO")
