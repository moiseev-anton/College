"""
Напишите программу возведения числа а в степень n,
применяя рекурентные соотношения: aⁿ = (a²)ⁿ/² при четном n,
aⁿ=a⋅aⁿ⁻¹ при нечетном n
"""

def power(a, n):
    # базовый случай
    if n == 0:
        return 1
    # рекурсия
    elif n % 2 == 0:
        return power(a * a, n // 2)
    else:
        return a * power(a, n - 1)


if __name__ == '__main__':
    a = float(input("Введите а: "))
    n = int(input("Введите n: "))

    result = power(a, n)
    print(f"{a} ^ {n} = {result}")


