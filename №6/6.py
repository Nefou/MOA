# coding=windows-1251
vaule1 = int(input("Введите первое число"))
vaule2 = int(input("Введите второе число"))

a = input ("Что делать с данными значениями? \n + Сложение \n - Вычитание \n * Умножение \n / Деление \n")

if a == "+":
    print (vaule1 + vaule2)
elif a == "-":
    print (vaule1 - vaule2)
elif a == "*":
    print (vaule1 * vaule2)
elif a == "/":
    print (vaule1 / vaule2)
else:
    print ("Вы ввели не коректный симвл")