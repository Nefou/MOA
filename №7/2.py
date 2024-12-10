# coding=windows-1251 
vale = int(input("Введите номер вашего месяца"))

if vale >= 1 and vale <= 2 or vale == 12:
    print("Это зимний месяц")
elif vale >= 3 and vale <= 5:
    print("Это весенний месяц")
elif vale >= 6 and vale <= 8:
    print("Это летний месяц")
elif vale >= 9 and vale <= 11:
    print("Это осений месяц")
else:
    print("Вы ввели не верные данные проверьте их коректность")