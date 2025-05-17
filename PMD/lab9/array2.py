import random


class A:
    """Класс двумерного массива"""
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.array = []

    def _random_fill(self):
        "Рандомное заполнение"
        self.array = [[random.randint(-20, 50) for _ in range(self.cols)] for _ in range(self.rows)]

    def _manual_fill(self):
        "Ручное заполнение"
        print("Введите элементы массива построчно:")
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(int(input(f"Элемент [{i}][{j}]: ")))
            self.array.append(row)

    def fill(self, mode: str = "r"):
        """Заполнение массива: вручную или рандомно."""
        match mode:
            case 'm':
                self._manual_fill()
            case 'r':
                self._random_fill()
            case _:
                raise ValueError("Некорректный режим заполнения. Используйте 'm' (вручную) или 'r' (случайно).")

    def display(self):
        """Вывод массива"""
        for row in self.array:
            print("\t".join(map(str, row)))


class B(A):
    """Класс для операций с массивом"""

    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols)

    def count_rows_without_zeros(self):
        """Количество строк без нулей"""
        count = 0
        for row in self.array:
            if 0 not in row:
                count += 1
        return count

    def find_max_repeated_number(self):
        """Наиболее повторяющееся число"""
        flat_array = [item for row in self.array for item in row]
        repeated_numbers = {num: flat_array.count(num) for num in set(flat_array) if flat_array.count(num) > 1}
        if repeated_numbers:
            return max(repeated_numbers, key=repeated_numbers.get)
        return "Нет повторяющихся чисел"

    def count_columns_without_zeros(self):
        """Количество столбцов без нулей"""
        count = 0
        for j in range(self.cols):
            if all(self.array[i][j] != 0 for i in range(self.rows)):
                count += 1
        return count

    def multiply_non_negative_rows(self):
        """Произведение строк без отрицательных элементов"""
        result = []
        for row in self.array:
            if all(x >= 0 for x in row):  # Проверка на отсутствие отрицательных элементов в строке
                product = 1
                for num in row:
                    product *= num
                result.append(product)
        return result

    def sum_rows_with_negatives(self):
        """Сумма строк c хотя бы одним отрицательным элементом"""
        total_sum = 0
        for row in self.array:
            if any(x < 0 for x in row):  # Если в строке хотя бы один отрицательный элемент
                total_sum += sum(row)
        return total_sum


if __name__ == "__main__":
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    arr = B(rows, cols)

    mode = input("Заполнить массив вручную (manual) или случайно (random)? m/r? ").strip().lower()
    arr.fill(mode)

    print("\nМассив:")
    arr.display()

    print("\nРезультаты:")
    print(f"Количество строк без нулевых элементов: {arr.count_rows_without_zeros()}")
    print(f"Максимальное число, встречающееся более одного раза: {arr.find_max_repeated_number()}")
    print(f"Количество столбцов без нулевых элементов: {arr.count_columns_without_zeros()}")
    print(f"Произведение элементов в строках без отрицательных элементов: {arr.multiply_non_negative_rows()}")
    print(f"Сумма элементов в строках с отрицательными элементами: {arr.sum_rows_with_negatives()}")
