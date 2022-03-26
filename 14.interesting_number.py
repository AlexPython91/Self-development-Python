# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней 
# по величине цифре. 
# На вход программе подается целое трехзначное число.

number = int(input())
first_digit = number // 100 % 10
second_digit = number // 10 % 10
last_digit = number % 10
min = (min(first_digit, second_digit, last_digit))
max = (max(first_digit, second_digit, last_digit))
average = (first_digit + second_digit + last_digit) - (min + max)
if max - min == average:
    print('Interesting number')
else:
    print('number is not interesting')