def find_students_with_max_score(input_str):
    parts = input_str.split('student_')[1:]  
    students = [(part[:3], int(part[3:])) for part in parts]  

    max_score = max(score for _, score in students)
    
    max_students = [number for number, score in students if score == max_score]
    
    return '-'.join(max_students)

input_str = input("Введите строку с номерами студентов и баллами: ")

result = find_students_with_max_score(input_str)

print(result)
