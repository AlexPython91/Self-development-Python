# Напишите программу, которая считывает названия двух основных цветов для смешивания. 
# Цвета: «красный», «синий» или «желтый»
# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.


first_color = input('Enter first color: ')
second_color = input('Enter second color: ')
if (first_color == 'red' or first_color == 'blue') and (second_color == 'blue' or second_color == 'red'):
    if first_color == second_color:
        print(first_color)
    else:
        print('purple')
elif (first_color == 'red' or first_color == 'yellow') and (second_color == 'yellow' or second_color == 'red'):
    if first_color == second_color:
        print(first_color)
    else:
        print('orange')
elif (first_color == 'blue' or first_color == 'yellow') and (second_color == 'yellow' or second_color == 'blue'):
    if first_color == second_color:
        print(first_color)
    else:
        print('green')
else:
    print('Input Error')