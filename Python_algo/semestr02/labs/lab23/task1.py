"""
Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел,
 которая не содержит инструкции if, а использует стандартную
 функцию min от двух чисел. Считайте четыре целых числа и выведите их минимум
 """


def min4(*args):
    a, b, c, d = args
    return min(min(a, b), min(c, d))


if __name__ == '__main__':
    nums = map(int, input().split())
    print(min4(*nums))

