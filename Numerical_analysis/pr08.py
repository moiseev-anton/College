from math import log10, sqrt, log


def first_norm(a: list[list[float]] | list[float]) -> float:
    """Функция для вычисления первой нормы матрицы (норма максимума строк)."""
    if isinstance(a[0], list):
        norm = max(sum(abs(i) for i in row) for row in a)  # для матрицы
    else:
        norm = max(abs(x) for x in a)  # для вектора
    return norm


def second_norm(a: list[list[float]]) -> float:
    """Функция для вычисления второй нормы матрицы (норма максимума столбцов)."""
    norm = max(sum(abs(row[j]) for row in a) for j in range(len(a)))
    return norm


def frobenius_norm(a: list[list[float]]) -> float:
    """Функция для вычисления третьей нормы матрицы (норма Фробениуса)."""
    norm = sqrt(sum(sum(i * i for i in row) for row in a))
    return norm




def check_convergence(a: list[list[float]]) -> bool:
    """Проверка достаточного условия сходимости процесса"""
    return first_norm(a) < 1 or second_norm(a) < 1 or frobenius_norm(a) < 1


def calculate_iterations(a: list[list[float]], b: list[float], tol=0.0001) -> int:
    """Функция для подсчета числа итераций для достижения заданной точности."""
    a_norm = first_norm(a)
    x0 = b[:]
    print(x0)
    x1 = iter_method_one_iter(a,b,x0)
    # x1 = one_iter(a, b, x0)
    print(x1)
    dif_x = [x1[i] - x0[i] for i in range(len(x0))]
    print(*dif_x)
    dif_x_norm = first_norm(dif_x)
    print(dif_x_norm)
    print(log10(tol))
    print(log10(1 - a_norm))

    # iterations = (log(tol) + log(1 - a_norm) - log(first_norm(b))) / (log(a_norm))
    # iterations = (log(tol) + log(1 - a_norm)) / (log(a_norm)  + log(first_norm(b)))

    iterations = (log10(tol) + log10(1 - a_norm)) / (log10(a_norm)  + log10(dif_x_norm))
    # iterations = (log10(tol) + log10(1 - a_norm) - log10(dif_x_norm)) / log10(a_norm)

    print(type(iterations), iterations)
    return int(iterations)


def iter_method_one_iter(a,b, x):
    n = len(b)
    return [sum(a[i][j] * x[j] for j in range(n)) + b[i] for i in range(n)]

def one_iter(a: list[list[float]], b: list[float], x: list[float]) -> list[float]:
    n = len(a)
    res = [0] * n
    for i in range(n):
        sum1 = sum(a[i][j] * res[j] for j in range(i))
        sum2 = sum(a[i][j] * x[j] for j in range(i, n))
        res[i] = b[i] + sum1 + sum2
    return res


def seidel_method(a: list[list[float]], b: list[float], tol=0.0001) -> list[float]:
    """Решение системы линейных уравнений методом Зейделя."""
    if not check_convergence(a):
        raise ValueError("Норма матрицы А больше 1")

    calculate_iterations(a,b)
    n = len(a)
    x = b[:]
    count = 0
    while True:
        new_x = one_iter(a,b,x)
        if all(abs(new_x[j] - x[j]) < tol for j in range(n)):
            break
        x, new_x = new_x, x
        count += 1
        print(count, *new_x, sep='\t')
    return x


if __name__ == "__main__":
    # a_array = [[0.08, -0.03, 0, -0.04],
    #            [0, 0.51, 0.27, -0.08],
    #            [0.33, -4, 0, 0.21],
    #            [0.11, 0, 0.03, 0.58]]
    #
    # b_array = [-1.2, 0.81, -0.92, 0.17]

    a_array = [[0.08, -0.03, 0, -0.04],
               [0, 0.51, 0.27, -0.08],
               [0.33, -4, 0, 0.21],
               [0.11, 0, 0.03, 0.58]]

    b_array = [-1.2, 0.81, -0.92, 0.17]


    try:
        solutions = seidel_method(a_array, b_array)
        # Вывод результата
        print(f"\nРешение:")
        for i, s in enumerate(solutions, start=1):
            print(f"x{i} = {s:.8f}")

    except ValueError as e:
        # Если возникает исключение, выводим сообщение об ошибке
        print(e)
