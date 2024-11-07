import calendar


class Date:
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if not 1 <= value <= 31:
            raise ValueError("День должен быть в диапазоне 1-31")

        # Получаем количество дней в месяце
        days_in_month = calendar.monthrange(self.year, self.month)[1]
        # Проверяем корректность даты
        if value > days_in_month:
            raise ValueError(f"Дата {value:02d}.{self.month:02d}.{self.year} некорректна")

        self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if not 1 <= value <= 12:
            raise ValueError("Месяц должен быть в диапазоне 1-12")
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 1:
            raise ValueError("Год должен быть положительным")
        self._year = value

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


if __name__ == "__main__":
    try:
        day, month, year = map(int, input('Введите дату: ').split('.'))
        date = Date(day, month, year)
        print(f"Дата {date} корректна.")
    except ValueError as e:
        print(e)

