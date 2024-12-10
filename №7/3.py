# coding=windows-1251
vale = int(input("Введите сумму займа"))

if vale < 100000:
    print("Ваша ставка 10%")
elif vale > 100000 and vale < 500000:
    print("Ваша ставка 8%")
elif vale >= 500000:
    print ("Ваша ставка 5%")
else:
    print("Проверьте коректность ваших данных")