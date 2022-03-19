# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман
#  зеленым, красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, 
# которое лежит вне диапазона от 0 до 36.

number = int(input('Enter a number from 1 to 36: '))
if number == 0:
    print('green')
elif number >= 1 and number <= 10:
    if number % 2 == 0:
        print('black')
    else:
        print('red')
elif number >= 11 and number <= 18:
    if number % 2 == 0:
        print('red')
    else:
        print('black')
elif number >= 19 and number <= 28:
    if number % 2 == 0:
        print('black')
    else:
        print('red')
elif number >= 29 and number <= 36:
    if number % 2 == 0:
        print('red')
    else:
        print('black')
else:
    print('Input Error')