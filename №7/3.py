# coding=windows-1251
vale = int(input("������� ����� �����"))

if vale < 100000:
    print("���� ������ 10%")
elif vale > 100000 and vale < 500000:
    print("���� ������ 8%")
elif vale >= 500000:
    print ("���� ������ 5%")
else:
    print("��������� ����������� ����� ������")