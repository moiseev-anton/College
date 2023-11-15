# Задана матрица размером nxm. Найти максимальный элемент матрицы.
import random

# заполнение 2-мерного массива
def fill_2D_array(rows: int, cols: int, min: int, max: int) -> list[list[int]]:
    return [[random.randint(min, max) for _ in range(cols)] for _ in range(rows)]

# печать 2-мерного массива
def print_2D_array(array):
    for row in array:
        for item in row:
            print(item, end="\t")
        print()


print("Задайте размер массива n x m")
n = int(input("n = "))
m = int(input("m = "))

matrix = fill_2D_array(n,m,0,30)
max = matrix[0][0]

print_2D_array(matrix)

for row in matrix:
    for item in row:
        if item > max:
            max = item
print(f"max = {max}")