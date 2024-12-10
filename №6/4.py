# coding=windows-1251 
vala = []
end = 1

while end !=0:
    vala.append(input("В ведите число"))
    a = input("Вы закончили? \n Y/N\n")
    if a == "Y":
        end = 0
    elif a == "N":
        print("хорошо")
    else:
        print("Вы ввели не верный симвл")
        a = input("Вы закончили? \n Y/N\n")
print (min(vala))
print (max(vala))
