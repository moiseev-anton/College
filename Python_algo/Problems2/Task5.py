#5. Даны действительные числа х и у. Получить (asb(x)-abs(y))/(1+abs(xy))

x = float(input("x = "))
y = float(input("y = "))

res = (abs(x) - abs(y)) / (1 + abs(x * y))

print("Результат: ", round(res, 2))