# coding=windows-1251
import random

vaule = random.randint(0,100)
end = 0
print("� ������� ����� ������ ��� \n��� �� ������ 100 � �� ������ 0")
while end != 1:
    a = int(input("� ������ ���� �����"))
    if a > vaule:
        print("����� ������")
    elif a < vaule:
        print("����� ������")
    elif a == vaule:
        print("�� �������, ����������")
        end = 1

s = input("������ ������� ��� ���? \n Y/N \n")
if s == "YES":
    end = 0

