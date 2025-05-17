from collections import defaultdict


class ArrayProcessor:
    def __init__(self, length: int):
        if length <= 0:
            raise ValueError("Размер массива должен быть натуральным числом")
        self.array = self._generate_array(length)

    @staticmethod
    def _generate_array(length: int) -> list[int]:
        """Генерация массива с запросом элементов у пользователя."""
        print(f"Введите {length} целых чисел для массива:")
        return [int(input(f"Элемент {i}: ")) for i in range(length)]

    def find_duplicates(self) -> None:
        """Находит и выводит дублирующиеся элементы и их индексы"""
        counter = defaultdict(list)

        for i, value in enumerate(self.array):
            counter[value].append(i)

        has_duplicates = False
        for value, indices in counter.items():
            if len(indices) > 1:
                has_duplicates = True
                print(f"Элемент {value} встречается в индексах {indices}")

        if not has_duplicates:
            print("Дублирующихся элементов не найдено.")

    def transform_array(self) -> None:
        """Удваивает все элементы массива, которые меньше 15, и выводит массив."""
        for i, num in enumerate(self.array):
            if num < 15:
                self.array[i] *= 2
        print("Преобразованный массив:", self.array)


if __name__ == "__main__":
    try:
        size = int(input("Введите размер массива: "))
        processor = ArrayProcessor(size)

        print("\nИщем дубликаты:")
        processor.find_duplicates()

        print("\nПреобразуем массив:")
        processor.transform_array()
    except ValueError as e:
        print("Ошибка:", e)


