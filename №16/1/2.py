vaule = [40, 11, 7, 9, 16, 44, 77]
s= 0
g = 0
p = 0
h = int(input("Введите первое число"))
l = int(input("Введите второе число"))
for i in vaule:
    if i %2 != 2:
        s += i
for i in vaule:
    if i % 6 == 0:
        p += i
for i in vaule:
    if i % h == 0 or i % l == 0:
        g += i
print(p)
print(s)
print(g)
