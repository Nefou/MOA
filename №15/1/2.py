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
arr1 = [x for x in arr if x >= 0]
print(arr1)