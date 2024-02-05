# Даны вещественные числа a, b, c, d, e, f.
# Известно, что система линейных уравнений:
#  ax + by = e  и 
#  cx + dy = f
# имеет ровно одно решение. Выведите два числа x и y,
#  являющиеся решением этой системы.

# nums = list(map(int,input("Введите значения a, b, c, d, e, f через пробел").split(" ")))

# d = (nums[0] * nums[3]) - (nums[2] * nums[1])
# dx = (nums[4] * nums[3]) - (nums[5] * nums[1])
# dy = (nums[0] * nums[5]) - (nums[2] * nums[4])


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
e = float(input("e = "))
f = float(input("f = "))

# метод Крамера
d = (a * d) - (c * b)
dx = (e * d) - (f * b)
dy = (a * f) - (c * e)

x = dx/d
y = dy/d
print(f"x = {x}\ny = {y}")