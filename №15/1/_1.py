# coding=windows-1251
length = int(input("������� ������ ������� "))
arr = []
arr1 = []
while length != 0:
    print("���������� ���������� ��������:", length)
    vaule = int(input("������� ���� �������� ������� "))
    arr.append(vaule)
    if vaule != 0:
        length -= 1
arr1 = [x * 2 for x in arr]
print(arr1)