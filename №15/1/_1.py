# coding=windows-1251
length = int(input("Введите размер массива "))
arr = []
arr1 = []
while length != 0:
    print("Оставшееся количество символов:", length)
    vaule = int(input("Введите одно значение массива "))
    arr.append(vaule)
    if vaule != 0:
        length -= 1
arr1 = [x * 2 for x in arr]
print(arr1)