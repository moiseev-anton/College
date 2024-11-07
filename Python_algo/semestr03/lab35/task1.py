class NumSequence:
    def __init__(self):
        self.numbers = []
        self.positive_sum = 0.0  # Аккумулятор для суммы положительных чисел
        self.negative_count = 0  # Аккумулятор для количества отрицательных чисел

    def add_number(self, number: float) -> None:
        """Добавляет число в последовательность и обновляет аккумуляторы"""
        self.numbers.append(number)

        if number > 0:
            self.positive_sum += number  # Обновляем сумму положительных чисел
        else:
            self.negative_count += 1  # Увеличиваем счетчик отрицательных чисел

    def display_results(self) -> None:
        """Выводит результаты на экран"""
        print(f"Сумма положительных чисел: {self.positive_sum}")
        print(f"Количество отрицательных чисел: {self.negative_count}")


if __name__ == "__main__":
    sequence = NumSequence()

    while True:
        number = float(input("Введите число (0 для завершения): "))
        if number == 0:
            break
        sequence.add_number(number)

    sequence.display_results()

