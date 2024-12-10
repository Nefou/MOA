# coding=windows-1251
permissions = {
    'W': '������',
    'R': '������',
    'X': '������'
}

user_input = input("������� ����� ������� (W, R, X), ����������� ��������: ")

user_permissions = user_input.split(',')

for permission in user_permissions:
    permission = permission.strip() 
    if permission in permissions:
        print(permissions[permission])
    else:
        print(f"����������� ����� �������: {permission}")