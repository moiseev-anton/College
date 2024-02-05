# 8. Написать программу нахождения суммы большего и меньшего из трех чисел.

a = int(input("n1 = "))
b = int(input("n2 = "))
c = int(input("n3 = "))

max = a
min = a

if b > max:
    max = b
if c > max:
    max = c

if b < min:
    min = b
if c < min:
    min = c

print(max + min)


