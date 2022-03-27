# На вход программе подается два вещественных числа a и b​, каждое на отдельной строке.
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from cmath import *


a = float(input())
b = float(input())
print('Arithmetic mean of numbers =', (a + b) / 2)
print('Geometric mean of numbers =', sqrt(a * b).real)
print('Harmonic mean of numbers =', (a * b) * 2 / (a + b)) 
square = (a ** 2 + b ** 2) / 2
print('Root mean square of numbers =', sqrt(square).real)

