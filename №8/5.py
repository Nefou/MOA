# coding=windows-1251
seasons = {
    '����': ['�������', '������', '�������'],
    '�����': ['����', '������', '���'],
    '����': ['����', '����', '������'],
    '�����': ['��������', '�������', '������']
}

user_input = input("������� ����� (����, �����, ����, �����): ")

if user_input in seasons:
    print(f"������ � ������ {user_input}: {', '.join(seasons[user_input])}")
else:
    print("����������� �����. ����������, ������� ����, �����, ���� ��� �����.")