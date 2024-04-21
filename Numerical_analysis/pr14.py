from math import sin


def euler_method(x0, y0, a, b, h) -> (list[float], list[float]):
    """
    Функция для решения дифф.ур. y' = f(x, y) методом Эйлера
    """
    n = int((b - a) / h)

    x_values = [x0]
    y_values = [y0]

    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]
        d = h * func(x, y)
        x_values.append(x + h)
        y_values.append(y + d)

    # возвращаем кортеж из 2 списков (массивов)
    return x_values, y_values


# Функция - правая часть дифф.ур.
def func(x, y):
    return x + sin(y / (10 ** 0.5))


if __name__ == '__main__':
    # задаем начальное условие
    x0 = 0.6
    y0 = 0.8
    a = 0.6
    b = 1.6
    h = 0.1

    # вычисление (раскрываем полученный кортеж)
    x, y = euler_method(x0, y0, a, b, h)

    # вывод в консоль
    for i in range(len(x)):
        print(f"x{i} = {x[i]:.2f}\t y{i} = {y[i]:.4f}")


