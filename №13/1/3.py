# coding=windows-1251
length = int(input("������� ������ ������� "))
arr = []
while length != 0:
    print("���������� ���������� ��������:", length)
    vaule = int(input("������� ���� �������� ������� "))
    arr.append(vaule)
    if vaule != 0:
        length -= 1
for i in arr [::-1]:
    print(i)