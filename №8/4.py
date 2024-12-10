# coding=windows-1251
permissions = {
    'W': 'Запись',
    'R': 'Чтение',
    'X': 'Запуск'
}

user_input = input("Введите права доступа (W, R, X), разделенные запятыми: ")

user_permissions = user_input.split(',')

for permission in user_permissions:
    permission = permission.strip() 
    if permission in permissions:
        print(permissions[permission])
    else:
        print(f"Неизвестное право доступа: {permission}")