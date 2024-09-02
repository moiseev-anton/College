# Напишите функцию, которая фильтрует четные числа в списке.


def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = filter_even_numbers(numbers)
    print("Четные числа в списке:", filtered_numbers)

    