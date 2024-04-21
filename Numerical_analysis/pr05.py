def forward_gauss(array: list[list[float]]) -> list[list[float]]:
    """
    Функция для прямого хода метода Гаусса.
    """
    n = len(array)

    # Создаем копию исходной матрицы для преобразования
    matrix = [row[:] for row in array]

    for i in range(n):
        # Находим индекс строки с максимальным по модулю ведущим элементом
        max_index = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_index][i]):
                max_index = k
        # Переставляем строки
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]

        # Формирование i-го столбца
        for j in range(i + 1, n):
            m = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= matrix[i][k] * m

    return matrix


def print_array(array):
    for row in array:
        for col in row:
            print(array[row][col], end="\t")
        print()


def find_det(matrix: list[list[float]]) -> float:
    """
    Функция для нахождения определителя матрицы методом Гаусса.
    """
    triangular = forward_gauss(matrix)
    print("Преобразованная матрица")
    print_array(triangular)
    print()

    det = 1
    for i in range(len(triangular)):
        det *= triangular[i][i]

    return det

def print_array(array):
    for row in array:
        for col in row:
            print(f"{col:.2} ", end= "\t")
        print()


if __name__ == "__main__":
    matrix = [[0.66, -1.44, -0.18],
              [0.48, -0.24, 0.37],
              [0.86, 0.43, 0.64]]

    det = find_det(matrix)
    print(f"Определитель: {det}")

