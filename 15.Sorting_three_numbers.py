# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
max = max(a, b, c)
min = min(a, b, c)
average = (a + b + c) - (min + max)
print(max, average, min, sep='\n')