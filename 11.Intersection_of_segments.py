# На числовой прямой даны два отрезка: [a1;   b1] и [a_2;   b_2]. 
# Напишите программу, которая находит их пересечение.

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 < a1:
    if b2 < a1:
        print('empty set')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('empty set')