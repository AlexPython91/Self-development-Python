# Напишите программу, вычисляющую значение \lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ 
# по заданному вещественному числу x.
from math import *

x = float(input())
print(ceil(x) + floor(x))