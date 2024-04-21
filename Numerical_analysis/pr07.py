from math import log, sqrt, ceil


def calculate_iterations(A_norm, b_norm):
    """
    Функция для подсчета числа итераций для достижения заданной точности.
    """
    iterations = (log(0.001) - log(A_norm * b_norm)) / log(A_norm)
    return ceil(iterations)


def first_norm(matrix):
    """
    Функция для вычисления первой нормы матрицы (норма максимума строк).
    """
    norm = max(sum(abs(element) for element in row) for row in matrix)
    return norm


def second_norm(matrix):
    """
    Функция для вычисления второй нормы матрицы (норма максимума столбцов).
    """
    norm = max(sum(abs(row[j]) for row in matrix) for j in range(len(matrix)))
    return norm


def frobenius_norm(matrix):
    """
    Функция для вычисления третьей нормы матрицы (норма Фробениуса).
    """
    norm = sqrt(sum(sum(a*a for a in row) for row in matrix))
    return norm


def check_convergence(a):
    return first_norm(a) < 1 or second_norm(a) < 1 or frobenius_norm(a) < 1


def iteration_method(a, b, t=0.0001):
    # Проверяем сходимость итерационного процесса
    if not check_convergence(a):
        # Если процесс расходится, возбуждаем исключение
        raise ValueError("Процесс итерации расходится")

    n = len(b)
    prev_x = b
    for i in range(10000):
        cur_x = [sum(a[i][j] * prev_x[j] for j in range(n)) + b[i] for i in range(n)]

        print(i, cur_x)
        if all(abs(c - p) <= t for p, c in zip(prev_x, cur_x)):
            return cur_x
        prev_x = cur_x


if __name__ == "__main__":
    a_array = [[0.08, -0.03, 0, -0.04],
               [0, 0.51, 0.27, -0.08],
               [0.33, -0.37, 0, 0.21],
               [0.11, 0, 0.03, 0.58]]

    b_array = [-1.2, 0.81, -0.92, 0.17]

    try:
        solutions = iteration_method(a_array, b_array)
        # Вывод результата
        print(f"\nРешение:")
        for i, s in enumerate(solutions, start=1):
            print(f"x{i} = {s:.7f}")

    except ValueError as e:
        # Если возникает исключение, выводим сообщение об ошибке
        print(e)
