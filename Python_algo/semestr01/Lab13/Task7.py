# Заданы две целочисленные матрицы, каждая из которых состоит из N строк и M столбцов. Требуется вычислить их сумму.
from Task3 import fill_2D_array, print_2D_array

print("Задайте размер матриц n x m")
n = int(input("n = "))
m = int(input("m = "))

# генерируем 2 матрицы размером n x m
matrixA = fill_2D_array(n,m,1,10)
matrixB = fill_2D_array(n,m,1,10)

# выводим матрицы
print('\nматрица А')
print_2D_array(matrixA)
print('\nматрица B')
print_2D_array(matrixB)

# получаем и сразу выводим результат
print('\nA+B')
for i in range(n):
    for j in range(m):
        item = matrixA[i][j]+matrixB[i][j]
        print(item,end='\t')
    print()

