# coding=windows-1251
vaule = [40, 11, 7, 9, 16, 44, 77]
s= 0
g = 0
p = 0
h = int(input("������� ������ �����"))
l = int(input("������� ������ �����"))
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