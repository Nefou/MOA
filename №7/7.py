# coding=windows-1251
import random

vaule = random.randint(0,100)
end = 0
print("Я загадал число угадай его \nОно не больше 100 и не меньше 0")
while end != 1:
    a = int(input("В ведите ваше число"))
    if a > vaule:
        print("Число меньше")
    elif a < vaule:
        print("Число больше")
    elif a == vaule:
        print("Вы выграли, Поздравляю")
        end = 1

s = input("хотите сыграть ещё раз? \n Y/N \n")
if s == "YES":
    end = 0

