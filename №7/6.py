# coding=windows-1251
vale = int(input("������� ��� ������� �����"))
nalog = 0

if vale < 20000:
    print("���� ��������� ������ 5%")
    nalog = 5
elif vale > 20000 and vale < 50000:
    print("���� ��������� ������ 15%")
    nalog = 15
elif vale >= 50000:
    print ("���� ��������� ������ 25%")
    nalog = 25
else:
    print("��������� ����������� ����� ������")

nalog = 1 - nalog / 100
print(vale * nalog)
