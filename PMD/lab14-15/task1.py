from typing import Callable


def selection_sort(arr: list, key: Callable = lambda x: x) -> list:
    """Сортировка выбором с параметром сортировки (по умолчанию сортировка по значению)"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    nums = [64, 25, 12, 22, 11]  # 11, 12, 22, 25, 64
    print(selection_sort(nums))

    words = ["банан", "апельсин", "дыня"]
    print(selection_sort(words, key=len))  # ['дыня', 'банан', 'апельсин'] по длине
    print(selection_sort(words))  # ["апельсин", "банан", "дыня"] лексикографически


