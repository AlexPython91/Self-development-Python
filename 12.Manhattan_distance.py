# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

p1 = float(input())
p2 = float(input())
q1 = float(input())
q2 = float(input())
print('Distance = ', int(abs(p1 - q1) + int(abs(p2 - q2))))