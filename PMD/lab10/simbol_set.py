class SymbolSet:
    """Класс для представления множества символов."""

    def __init__(self, string: str = ""):
        """Конструктор с параметром строки (или по умолчанию пустой строки)"""
        self.symbols = set(string)

    @classmethod
    def from_other_set(cls, other_set, max_value: str):
        """
        Конструктор, копирующий символы другого множества, не превышающие max_value.
        Сравненеие символов происходит по их коду.
        """
        filtered_symbols = {ch for ch in other_set.symbols if ch <= max_value}
        return cls("".join(filtered_symbols))

    def __del__(self):
        """Деструктор"""
        print(f"Множество {self.symbols} уничтожено.")

    def to_string(self):
        """Преобразование множества в строку"""
        return "".join(sorted(self.symbols))

    @classmethod
    def from_char(cls, char: str):
        """Преобразование символа в множество."""
        return cls(char)


if __name__ == '__main__':
    s1 = SymbolSet("hello world")
    s2 = SymbolSet.from_other_set(s1, "l")
    print("Множество 1:", s1.to_string())

    print("Множество 2:", s2.to_string())

    print('\nРабота деструктора')

