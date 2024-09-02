"""
Пользователь вводит число х, найдите все числа из списка,
которые кратны введенному числу.
Реализуйте данную задачу через lambda функцию."""


def find_multiples(numbers, x):
    multiples = list(filter(lambda num: num % x == 0, numbers))
    return multiples


if __name__ == '__main__':
    numbers = [10, 15, 20, 25, 30, 35, 40]
    x = int(input("Введите число x: "))

    result = find_multiples(numbers, x)
    print("Числа из списка, кратные", x, ":", result)


