# Напишите программу, вычисляющую значение тригонометрического выражения 
# sin x + cos x + tan^ x

from math import *
x = radians(float(input()))
print(sin(x) + cos(x) + tan(x) * tan(x))