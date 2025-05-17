import random
from functools import wraps


def is_square_matrix(func):
    """Декоратор для проверки квадратности матрицы"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.is_square:
            return "Матрица не квадратная"
        return func(self, *args, **kwargs)
    return wrapper


class A:
    """Класс для создания и заполнения двумерного массива."""
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.array = []

    @property
    def is_square(self) -> bool:
        """Свойство для проверки, является ли матрица квадратной"""
        return self.rows == self.cols

    def fill_array(self, mode: str = "r"):
        """Заполнение массива: вручную или рандомно"""
        if mode == "m":
            print("Введите элементы массива построчно:")
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(int(input(f"Элемент [{i}][{j}]: ")))
                self.array.append(row)
        elif mode == "r":
            self.array = [[random.randint(1, 100) for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            raise ValueError("Некорректный режим заполнения. Используйте 'm' или 'r'")

    def display_array(self):
        """Вывод массива."""
        for row in self.array:
            print(" ".join(map(str, row)))


class B(A):
    """Класс для операций с диагоналями массива"""
    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols)

    @is_square_matrix
    def calculate_sum_main_diagonal(self):
        """Сумма элементов главной диагонали."""
        return sum(self.array[i][i] for i in range(self.rows))

    @is_square_matrix
    def calculate_sum_secondary_diagonal(self):
        """Сумма элементов побочной диагонали."""
        return sum(self.array[i][self.cols - i - 1] for i in range(self.rows))

    @is_square_matrix
    def calculate_avg_main_diagonal(self):
        """Среднее главной диагонали."""
        return self.calculate_sum_main_diagonal() / self.rows

    @is_square_matrix
    def calculate_avg_secondary_diagonal(self):
        """Среднее побочной диагонали."""
        return self.calculate_sum_secondary_diagonal() / self.rows


# Пример использования
if __name__ == "__main__":
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    arr = B(rows, cols)

    mode = input("Заполнить массив вручную (manual) или случайно (random)? m/r? ").strip().lower()
    arr.fill_array(mode)

    print("\nМассив:")
    arr.display_array()

    print("\nРезультаты:")
    print(f"Сумма главной диагонали: {arr.calculate_sum_main_diagonal()}")
    print(f"Сумма побочной диагонали: {arr.calculate_sum_secondary_diagonal()}")
    print(f"Среднее арифметическое главной диагонали: {arr.calculate_avg_main_diagonal()}")
    print(f"Среднее арифметическое побочной диагонали: {arr.calculate_avg_secondary_diagonal()}")


