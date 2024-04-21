from math import log10


def func(x):
    return x*x*log10(x)


def simpson_method(a, b, n):
    h = (b - a) / n
    integral = func(a) + func(b) # сразу можем найти крайние узлы

    for i in range(1, n):
        # определяем коэфициент 2 для четных и 4 для нечетных узлов
        c = 2 if i % 2 == 0 else 4
        integral += c * func(a + i * h)

    integral *= h / 3
    return integral


if __name__ == '__main__':
    a = 1.4
    b = 3
    n = 8
    result = simpson_method(a, b, n)
    print(f"Результат ≈ {result:.6f}")

