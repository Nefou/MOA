a = int(input("Введите размер треугольника"))
y = 1
while a:
    s = a
    while s:
        print(y, end=" ")
        s -= 1
    y += 1
    print()
    a -= 1
