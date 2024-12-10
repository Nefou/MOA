# coding=windows-1251 
vale = int(input("В ведите свой возраст"))

if vale >= 18:
    print("Вы можете голосовать")
elif vale <= 6:
    print("Почему ты сидишь здесь, а не играешь в песочнице?")
else:
    print("Вы не можете голосовать")