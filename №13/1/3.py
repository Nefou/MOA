length = int(input("Введите размер массива "))
arr = []
while length != 0:
    print("Оставшееся количество символов:", length)
    vaule = int(input("Введите одно значение массива "))
    arr.append(vaule)
    if vaule != 0:
        length -= 1
for i in arr [::-1]:
    print(i)
