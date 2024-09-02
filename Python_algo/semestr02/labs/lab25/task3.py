"""
Напишите программу возведения числа а в степень n рекурентно
"""

def power(a, n):
    # базовый случай
    if n == 0:
        return 1
    # рекурсия
    else:
        return a * power(a, n - 1)


if __name__ == '__main__':
    a = float(input("Введите а: "))
    n = int(input("Введите n: "))

    result = power(a, n)
    print(f"{a} ^ {n} = {result}")


