class SeasonChecker:
    @staticmethod
    def season(month: int) -> str:
        """Определяет время года по номеру месяца"""
        if not isinstance(month, int):
            raise TypeError('Номер меяца должен быть целым числом')
        if not 1 <= month <= 12:
            raise ValueError('Номер месяца должен быть в диапазоне 1-12')

        if month in (12, 1, 2):
            return 'Зима'
        if month in (3, 4, 5):
            return 'Весна'
        if month in (6, 7, 8):
            return 'Лето'
        return 'Осень'


if __name__ == '__main__':
    try:
        month = int(input('Введите номер месяца: '))
        season = SeasonChecker.season(month)
        print(season)
    except (TypeError, ValueError) as e:
        print(e)

