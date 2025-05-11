def ascii_code_based_on_string_length():
    input_str = input("Введите строку: ")

    length = len(input_str)

    if length <= 2:
        ascii_value = ord(input_str[0])
    elif 2 < length < 10:
        first_ascii = ord(input_str[0])
        last_ascii = ord(input_str[-1])

        if length % 2 == 0:
            ascii_value = (first_ascii + last_ascii) // 2
        else:
            ascii_value = last_ascii
    else:
        ascii_value = ord(input_str[-1])

    print(ascii_value)

ascii_code_based_on_string_length()

