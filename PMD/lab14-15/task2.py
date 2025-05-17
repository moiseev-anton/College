from typing import Callable


def array_sum(arr: list[int], key: Callable = lambda x: x) -> int:
    return sum(key(x) for x in arr)


if __name__ == '__main__':
    print('Сумма всех: ', array_sum([1, 2, 3, 4, 5]))  # просто сумма

    print('Сумма квадратов: ', array_sum([1, 2, 3, 4, 5], key=lambda x: x * x))  # сумма квадратов

    print('Сумма четных: ', array_sum([1, 2, 3, 4, 5], key=lambda x: x if x % 2 == 0 else 0))  # сумма четных

