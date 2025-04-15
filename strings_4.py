def capitalize_string(input_string):

    if len(input_string) < 4:
 
        if input_string.isupper():
            return input_string
        else:
            return input_string

    upper_count = sum(1 for c in input_string[:4] if c.isupper())

    if upper_count >= 3:
        return input_string.upper()
    else:
        return input_string

user_input = input("Введите строку: ")

result = capitalize_string(user_input)
print(result)
