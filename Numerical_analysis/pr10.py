def divided_differences(y: list[float]) -> list[list[float]]:
    """ Функция для нахождения конечных разностей """
    n = len(y)
    result = [y]

    for i in range(1, n):
        prev_diffs = result[i - 1]
        current_diffs = []

        for j in range(n - i):
            diff = (prev_diffs[j + 1] - prev_diffs[j])
            current_diffs.append(diff)

        result.append(current_diffs)

    return result


def newton_interpolation(x: list[float], y: list[float], target: float, reverse=False) -> float:
    """Обобщенная функция интерполяции Ньютона"""
    start = -1 if reverse else 0

    diffs = divided_differences(y)
    n = len(x)
    q = (target - x[start]) / abs(x[0] - x[1])
    coef = 1

    interpolation = diffs[0][start]
    for i in range(1, n):
        if reverse:
            coef *= (q + i - 1) / i
        else:
            coef *= (q - i + 1) / i
        interpolation += coef * diffs[i][start]

    return interpolation


def interpolate(x: list[float], y: list[float], target: float) -> float | str:
    """Функция интерполирования"""
    if not (x[0] <= target <= x[-1]):
        raise ValueError("Целевой аргумент не принадлежит отрезку интерполяции")

    for i, el in enumerate(x):
        if el == target:
            return y[i]

    # Определяем границы отрезка и направление интерполирования
    n = len(x)
    for i in range(n - 1):
        if x[i] < target < x[i + 1]:
            if i <= n // 2:
                # Интерполирование вперед
                return newton_interpolation(x[i:n], y[i:n], target)
            else:
                # Интерполирование назад
                return newton_interpolation(x[:i + 2], y[:i + 2], target, reverse=True)


if __name__ == '__main__':
    x = [0.698,     0.706,   0.714,   0.722,    0.73,   0.738,   0.746,   0.754,   0.762]
    y = [2.22336, 2.24382, 2.26446, 2.29841, 2.32221, 2.35164, 2.38690, 2.41162, 2.44777]
    target = 0.75
    try:
        res = interpolate(x, y, target)
        print(f"f({target}) = {res:.5f}")
    except ValueError as e:
        print(e)

