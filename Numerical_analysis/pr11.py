def func(x):
    return 1/(x*x + 0.6)**0.5

def trapezoidal_rule(f, a, b, n):
    """Вычисляет интеграл функции f методом трапеций
        на [a, b] с использованием n трапеций."""
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))  # Вычисляем значение на концах интервала
    for i in range(1, n):
        integral += f(a + i * h)  # Добавляем значения внутри интервала
    integral *= h
    return integral

if __name__ == '__main__':
    a = 2.2
    b = 2.6
    n = 20

    result = trapezoidal_rule(func, a, b, n)
    print(f"Результат ≈ {result:.6f}")

