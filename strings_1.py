data = input("введите строку с номерами студентов и их баллами: ")

students_scores = []
max_score = -1


i = 0
while i < len(data):

    if data[i:i + 8] == 'student_':
        student_id = data[i:i + 8] + data[i + 8:i + 11]  
        score = int(data[i + 11:i + 15]) 
        students_scores.append((student_id, score))

        if score > max_score:
            max_score = score
        i += 15  
    else:
        i += 1 

top_students = [student_id for student_id, score in students_scores if score == max_score]
result = '-'.join(top_students)

print(result)
