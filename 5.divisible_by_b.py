# Напишите функцию, которая будет принимать два числа: a и b. 
# Она должна возвращать следующее число, которое будет больше a и b и без остатка делиться на b.

def return_next_number(a, b):
    return (a//b + 1)*b
print(return_next_number(12, 4))