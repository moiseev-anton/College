# Найти произведение элементов двумерного массива( матрицы).
from Task3 import fill_2D_array, print_2D_array

print("Задайте размер массива n x m")
n = int(input("n = "))
m = int(input("m = "))
result = 1

matrix = fill_2D_array(n,m,1,6)
print_2D_array(matrix)

for row in matrix:
    for item in row:
        result *= item
print(f"result = {result}")