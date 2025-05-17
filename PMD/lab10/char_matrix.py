class CharMatrix:
    """Класс для представления матрицы из символов."""

    def __init__(self, rows: int = 1, cols: int = 1):
        """Конструктор с размерами матрицы."""
        self.rows = rows
        self.cols = cols
        self.matrix = [[" " for _ in range(cols)] for _ in range(rows)]

    @classmethod
    def from_other_matrix(cls, other_matrix, increment: int):
        """Конструктор копирования с увеличением элементов другой матрицы."""
        new_matrix = cls(other_matrix.rows, other_matrix.cols)
        new_matrix.matrix = [
            [chr(ord(c) + increment) for c in row]
            for row in other_matrix.matrix
        ]
        return new_matrix

    def __del__(self):
        """Деструктор."""
        print("Матрица уничтожена.")

    def fill_from_char(self, char: str):
        """Заполнение матрицы одним символом."""
        self.matrix = [[char for _ in range(self.cols)] for _ in range(self.rows)]

    def average_ascii(self):
        """Среднее арифметическое ASCII-кодов элементов матрицы."""
        total_ascii = sum(ord(c) for row in self.matrix for c in row)
        return total_ascii // (self.rows * self.cols)

    def display(self):
        """Вывод матрицы."""
        for row in self.matrix:
            print(" ".join(row))


if __name__ == '__main__':
    # Создание матрицы размером 2x3 и заполнение символом 'A'
    m1 = CharMatrix(2, 3)
    m1.fill_from_char("A")
    print("Матрица m1:")
    m1.display()

    # Создание матрицы на основе m1 с увеличением на 2 (получится C)
    m2 = CharMatrix.from_other_matrix(m1, 2)
    print("\nМатрица m3 (увеличение на 2):")
    m2.display()

    # Создание матрицы с увеличением символов на -1 (получится @)
    m3 = CharMatrix.from_other_matrix(m1, -1)
    print("\nМатрица m4 (уменьшение на 1):")
    m3.display()

    # Среднее ASCII-кодов элементов матрицы m2
    print("\nСреднее ASCII матрицы m2:", m2.average_ascii())

    print('\nРабота деструктора')



