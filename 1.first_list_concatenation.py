# Напишите функцию, которая будет принимать списки чисел в произвольном количестве и конкатенировать их, 
# возвращая общий список чисел.

from random import randint

first_numbers = ([randint(1, 30) for i in range(5)])
print(first_numbers)
second_numbers = ([randint(1, 30) for i in range(5)])
print(second_numbers)

def return_the_list(new_list):
    return second_numbers + first_numbers
print(return_the_list((first_numbers, second_numbers)))