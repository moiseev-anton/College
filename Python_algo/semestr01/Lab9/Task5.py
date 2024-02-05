# Дано трехзначное число, нужно вывести количество единиц, десятков и сотен.

num = abs(int(input("Введите трехзначное число: ")))

if num > 99 and num < 1000:
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    print(f"Сотни: {hundreds}")
    print(f"Десятки: {tens}")
    print(f"Единицы: {units}")
else:
    print("Число не трехзначное")