"""
Дана последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.
"""

def reverse_():
    num = int(input("> "))
    if num != 0:
        reverse_()
        print(num, end=' ')
    else:
        print("\nВ обратном порядке:")


if __name__ == '__main__':
    print("Вводите числа последовательно (0 для завершения):")
    reverse_()

