# coding=windows-1251 
vala = []
end = 1

while end !=0:
    vala.append(input("� ������ �����"))
    a = input("�� ���������? \n Y/N\n")
    if a == "Y":
        end = 0
    elif a == "N":
        print("������")
    else:
        print("�� ����� �� ������ �����")
        a = input("�� ���������? \n Y/N\n")
print (min(vala))
print (max(vala))
