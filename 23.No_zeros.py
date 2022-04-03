# Напишите программу, которая считывает 10 чисел и выводит произведение 
# отличных от нуля чисел.

n = int(input())
product_of_numbers = 1
for i in range(1, n + 1):
    numbers = int(input())
    if numbers != 0:
        product_of_numbers = product_of_numbers * numbers
print(product_of_numbers)

# 8
# 0
# 1
# 2
# 1
# 0
# 0
# 5
# 4
# 12