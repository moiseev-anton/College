def func(x):
    return x ** 3 + 3 * x * x - 24 * x + 1


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


def chord_method(a, b, t):
    prev = a
    while True:
        cur = a - (b - a) * func(a) / (func(b) - func(a))
        if abs(prev - cur) < t:
            return cur
        if func(a) * func(cur) < 0:
            b = cur
        else:
            a = cur
        prev = cur


if __name__ == "__main__":
    a, b = 3, 4
    step = 0.1
    tolerance = 0.000005

    interval = find_root_area(a, b, step)
    root = chord_method(interval[0], interval[1], tolerance)
    print(f"Корень = {root:.8}")
