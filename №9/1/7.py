# coding=windows-1251
A = int(input("Введите первое число"))
B = int(input("Введите второе число"))

if A < B:
    for num in range(A, B + 1):
        print(num)
else:
    for num in range(A, B - 1, -1):
        print(num)