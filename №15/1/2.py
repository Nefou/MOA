length = int(input("Введите размер массива "))
arr = []
arr1 = []
while length != 0:
    print("Оставшееся количество символов:", length)
    vaule = int(input("Введите одно значение массива "))
    arr.append(vaule)
    if vaule != 0:
        length -= 1
arr1 = [x for x in arr if x >= 0]
print(arr1)
