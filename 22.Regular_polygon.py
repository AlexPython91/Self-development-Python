# Даны два числа: натуральное число n и вещественное число a. 
# Напишите программу, которая находит площадь указанного правильного многоугольника.
from math import *

n = int(input())
a = float(input())
print(n * pow(a, 2) / (4 * tan(pi / n)))