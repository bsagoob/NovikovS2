def convert_to_uppercase(input_str):
    if len(input_str) < 4:
        return input_str 

    uppercase_count = sum(1 for char in input_str[:4] if char.isupper())
    
    if uppercase_count >= 3:
        return input_str.upper()      else:
        return input_str  

input_string = input("Введите строку: ")


result_string = convert_to_uppercase(input_string)


print(result_string)
