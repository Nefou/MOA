vale = int(input("Введите ваш годовой доход"))
nalog = 0

if vale < 20000:
    print("Ваша налоговая ставка 5%")
    nalog = 5
elif vale > 20000 and vale < 50000:
    print("Ваша налоговая ставка 15%")
    nalog = 15
elif vale >= 50000:
    print ("Ваша налоговая ставка 25%")
    nalog = 25
else:
    print("Проверьте коректность ваших данных")

nalog = 1 - nalog / 100
print(vale * nalog)
