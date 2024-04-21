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
            # Преобразование всей j-й строки
            for k in range(i, n + 1):
                matrix[j][k] -= matrix[i][k] * m

    return matrix


def backward_gauss(array: list[list[float]]) -> list[float]:
    """
    Функция для обратного хода метода Гаусса.
    """
    n = len(array)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = array[i][-1] / array[i][i]
        for j in range(i - 1, -1, -1):
            array[j][-1] -= array[j][i] * x[i]

    return x


def print_array(array):
    """
    Функция для вывода расширенной матрицы
    """
    for row in array:
        for i in range(len(row)):
            if i == len(row) - 1:
                print(" | ", end="\t")
            print(f"{row[i]:.2} ", end="\t")
        print()
    print()


def check_residual(matrix: list[list[float]], solution: list[float]) -> list[float]:
    """
    Функция для вычисления невязок системы уравнений.
    """
    residuals = []
    for equation in matrix:
        left_side = sum(coef * x for coef, x in zip(equation[:-1], solution))
        right_side = equation[-1]
        residuals.append(abs(left_side - right_side))
    return residuals


if __name__ == "__main__":
    matrix = [[0.66, -1.44, -0.18, 1.83],
              [0.48, -0.24, 0.37, -0.84],
              [0.86, 0.43, 0.64, 0.64]]

    triangular_matrix = forward_gauss(matrix)
    print("Преобразованная матрица")
    print_array(triangular_matrix)
    solutions = backward_gauss(triangular_matrix)
    for i, x in enumerate(solutions, start=1):
        print(f"x{i} = {x:.6}")

    res = check_residual(matrix, solutions)
    print()
    for r in res:
        print(r)
