# Напишите функцию, которая будет проверять, является ли целое число совершенным числом. 
# Например, 6 — совершенное число, ведь 1 + 2 + 3 = 6.

def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
print(is_perfect_number(6))