# Напишите программу, которая считывает 10 чисел и выводит произведение 
# отличных от нуля чисел.

n = int(input('Enter number: '))
print(f'Enter {n} numbers: ')
product_of_numbers = 1
for i in range(1, n + 1):
    numbers = int(input())
    if numbers != 0:
        product_of_numbers = product_of_numbers * numbers
print(product_of_numbers)

