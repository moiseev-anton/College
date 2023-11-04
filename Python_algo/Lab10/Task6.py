# По российский правилам числа округляются до ближайшего
# целого числа,а если дробная часть числа равна 0.5, 
# то число округляется вверх.
# Дано неотрицательное число x, округлите его по этим правилам.
# Обратите внимание, что функция round не годится для этой задачи! 
# Вводится неотрицательное число.

n = float(input("n = "))

int_part = int(n)
fract_patr = n - int_part

if fract_patr >= 0.5:
    n += 1

print(f"round(n) = {int(n)}")