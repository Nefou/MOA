# coding=windows-1251
vaule1 = int(input("������� ������ �����"))
vaule2 = int(input("������� ������ �����"))

a = input ("��� ������ � ������� ����������? \n + �������� \n - ��������� \n * ��������� \n / ������� \n")

if a == "+":
    print (vaule1 + vaule2)
elif a == "-":
    print (vaule1 - vaule2)
elif a == "*":
    print (vaule1 * vaule2)
elif a == "/":
    print (vaule1 / vaule2)
else:
    print ("�� ����� �� ��������� �����")