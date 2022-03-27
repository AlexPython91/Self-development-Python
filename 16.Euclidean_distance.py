# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

from math import *

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = pow((x1 - x2), 2) + pow((y1 - y2), 2)
print(sqrt(p))