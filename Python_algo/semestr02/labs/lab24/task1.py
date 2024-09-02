"""
Напишите функцию sum_range(start, end), которая суммирует
все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе,
просто поменяйте их местами."""


def sum_range(start, end):
    if start > end:
        start, end = end, start

    return sum(range(start, end + 1))


if __name__ == '__main__':
    start, end = map(int, input().split())
    result = sum_range(start, end)
    print(result)

