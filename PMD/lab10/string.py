class StringСlass:
    """Класс строки"""

    def __init__(self, length: int = 0):
        """Конструктор с одним параметром - длиной строки"""
        self.string = " " * length

    @classmethod
    def from_other_string(cls, other_string, n: int):
        """Метод копирующий первые n символов другой строки"""
        new_str = other_string.string[:n]
        return cls(len(new_str)).set_value(new_str)

    def __del__(self):
        """Деструктор"""
        print(f"Строка '{self.string}' уничтожена")

    def set_value(self, value: str):
        """Сеттер значения строки"""
        self.string = value
        return self

    def to_float(self):
        """Преобразование строки в вещественное число"""
        try:
            return float(self.string)
        except ValueError:
            raise ValueError("Строка не может быть преобразована в вещественное число")

    @classmethod
    def from_float(cls, value: float):
        """Преобразование вещественного числа в строку"""
        return cls().set_value(str(value))


if __name__ == '__main__':
    # Создаем строку с заданной длиной
    s1 = StringСlass(10).set_value("HelloWorld")
    print("Исходная строка:", s1.string)

    # Создаем строку, копируя первые 5 символов из другой строки
    s2 = StringСlass.from_other_string(s1, 5)
    print("Копия первых 5 символов:", s2.string)

    # Преобразуем строку в вещественное число
    s3 = StringСlass().set_value("123.45")
    print("Преобразование строки в число:", s3.to_float())

    # Преобразуем вещественное число в строку
    s4 = StringСlass.from_float(67.89)
    print("Преобразование числа в строку:", s4.string)

    # Создаем строку из символов другой строки
    s5 = StringСlass.from_other_string(s1, 3)
    print("Копия первых 3 символов:", s5.string)

    print('\nРабота деструктора')


