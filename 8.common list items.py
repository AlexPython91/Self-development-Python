# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

from random import randint

first_list = [randint(1, 30) for i in range(10)]
print(first_list)

second_list = [randint(1, 30) for i in range(10)]
print(second_list)

def show_common_list(first_list, second_list):
    res = list(filter(lambda i: i in first_list, second_list))
    return res
print(show_common_list(first_list, second_list))


