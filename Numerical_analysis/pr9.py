def lagrange_interpolation(x_values, y_values, x):
    """Функция интерполированния по формуле Лагранжа"""
    n = len(x_values)
    result = 0.0
    for i in range(n):
        curr = y_values[i]
        for j in range(n):
            if j != i:
                curr *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += curr
    return result


if __name__ == '__main__':
    x_values = [0.43, 0.48, 0.55, 0.62, 0.70, 0.75]
    y_values = [1.6597, 1.73234, 1.87686, 2.03345, 2.22846, 2.35973]
    x = 0.645
    interpolated_y = lagrange_interpolation(x_values, y_values, x)
    print(f"f({x}) ≈ {interpolated_y:.6f}")

