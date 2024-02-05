# Дана прямоугольная матрица. Найти сумму элементов построчно.
from Task3 import fill_2D_array, print_2D_array

print("Задайте размер массива n x m")
n = int(input("n = "))
m = int(input("m = "))

matrix = fill_2D_array(n,m,0,10)
print_2D_array(matrix)
result = list()

for row in matrix:
    row_sum = 0
    for item in row:
        row_sum += item
    result.append(row_sum)

# result = [sum(row) for row in matrix]
print(result)