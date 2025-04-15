def process_strings(str1, str2):
    first_two = str1[:2]

    reversed_two = first_two[::-1]

    result = f"{reversed_two}-{str2}"
    
    return result

input_str1 = input("Введите первую строку: ")
input_str2 = input("Введите вторую строку: ")

output = process_strings(input_str1, input_str2)
print(output)
