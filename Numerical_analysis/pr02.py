import math


def func(x):
    return math.cos(0.6 * x) - 4 * x ** 4 + 6.2


if __name__ == "__main__":
    a, b, step = 1, 2, 0.1
    
    current = a
    while current + step <= b:
        start = current
        end = start + step
    
        if func(start) * func(end) < 0:
            print(f"Корень принадлежит отрезку [{start:.1f}, {end:.1f}]")
    
        current += step


