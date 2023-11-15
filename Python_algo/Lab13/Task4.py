# Дана прямоугольная матрица. Найти сумму элементов всей матрицы.
from Task3 import fill_2D_array, print_2D_array

print("Задайте размер массива n x m")
n = int(input("n = "))
m = int(input("m = "))
result = 0

matrix = fill_2D_array(n,m,0,10)
print_2D_array(matrix)

for row in matrix:
    for item in row:
        result += item

# result = sum(sum(row) for row in matrix)
print(f"sum = {result}")