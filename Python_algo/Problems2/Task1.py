# 1. Вычислить корни квадратного уравнения ах2+ bх+ с = 0 
# с заданными коэффициентами a, b и с (предполагается,
#  что а, b, с не 0 и что дискриминант уравнения неотрицателен).

import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discrim = b**2 - 4*a*c

# Вычисление корней
if discrim > 0:
    x1 = (-b + math.sqrt(discrim)) / (2*a)
    x2 = (-b - math.sqrt(discrim)) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")
elif discrim == 0:
    x = -b / (2*a)
    print(f"x = {x}")
else:
    print("Решений нет")