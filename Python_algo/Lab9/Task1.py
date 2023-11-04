# Вычислить длину окружности и площадь круга одного и того же радиуса R.
radius = abs(float(input("Введите радиус: ")))
pi = 3.14
S =  radius ** 2 * pi
L = 2 * pi * radius
print(f"S={S:.2f}\nL={L:.2f}")