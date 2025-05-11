def wrap_in_html_tag(input_string, tag):
    valid_tags = ['abbr', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'body']
    
    if tag in valid_tags:
        return f"<{tag}>{input_string}</{tag}>"
    else:
        return "Введён неверный тег."

input_string = input("Введите строку: ")
html_tag = input("Введите HTML тег: ")

result_html = wrap_in_html_tag(input_string, html_tag)

print(result_html)
