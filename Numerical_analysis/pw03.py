import math


def func(x):
    return math.cos(0.6 * x) - 4 * x ** 4 + 6.2


def find_root_area(a, b, step):
    current = a
    while current + step <= b:
        start = current
        end = start + step

        if func(start) * func(end) < 0:
            print(f"Корень принадлежит отрезку [{start:.1f}, {end:.1f}]")
            return (start, end)
        current += step
    return None


def bisection_method(left, right, t):
    while abs(right - left) / 2 > t:
        mid = (left + right) / 2
        if func(left) * func(mid) < 0:
            right = mid
        else:
            left = mid

    return (left + right) / 2


if __name__ == "__main__":
    a, b = 1, 2
    step = 0.1
    tolerance = 0.0001

    interval = find_root_area(a, b, step)
    root = bisection_method(interval[0], interval[1], tolerance)
    print(f"Корень = {root:.7}")
