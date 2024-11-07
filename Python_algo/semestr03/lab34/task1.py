class YearChecker:
    @staticmethod
    def is_year_leap(year: int) -> bool:
        """Определяет время года по номеру месяца"""
        if not isinstance(year, int):
            raise TypeError('Год должен быть целым числом')
        if year < 0:
            raise ValueError('Год должен быть положительным')

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False


if __name__ == '__main__':
    try:
        year = int(input('Введите год: '))
        result = YearChecker.is_year_leap(year)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)

