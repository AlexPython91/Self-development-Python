# Напишите функцию, которая будет возвращать True, 
# если переданная строка (например, «5 + 4») является математическим выражением. 

def show_math_expression(str):
    return all(symbol in '0123456789 +-*/%' for symbol in str)
print(show_math_expression('55 - 5'))