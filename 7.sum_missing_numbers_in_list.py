# Создайте функцию, которая будет принимать список чисел и 
# возвращать сумму чисел, пропущенных в списке.


from random import randint, random

numbers = ([randint(1, 15) for i in range(3)])
numbers.sort()
print(numbers)

def sum_missing_numbers(numbers):
    return sum(i for i in range(min(numbers), max(numbers)) if i not in numbers)
print(sum_missing_numbers(numbers))