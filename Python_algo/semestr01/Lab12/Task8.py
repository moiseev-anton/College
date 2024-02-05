# Выведите таблицу умножения от 1 до 10 для какого либо числа.

n = int(input("n = "))

for i in range(10):
    mul = n * (i+1)
    print(f"{n} х {i+1} = {mul}")