class Utility:
    MONTH_DAYS = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Високосный год
    @staticmethod
    def is_leap_year(year: int) -> bool:
        if not isinstance(year, int):
            raise ValueError('Год должен быть целым числом')
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    # Правильная дата
    @staticmethod
    def date(day: int, month: int, year: int) -> bool:
        if not (1 <= month <= 12):
            return False

        # Получаем количество дней месяца из атрибута класса
        days = Utility.MONTH_DAYS[month]

        # Проверка высокостного года с помощью метода класса
        if month == 2 and Utility.is_leap_year(year):
            days = 29

        return 1 <= day <= days

    # Простейшие арифметические операции
    @staticmethod
    def arithmetic(a: float, b: float, operation: str) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Ошибка: a и b должны быть числами')

        match operation:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                if b == 0:
                    raise ValueError('Ошибка: деление на ноль')
                return a / b
            case _:
                raise ValueError('Неизвестная операция')

    # Времена года
    @staticmethod
    def season(month: int) -> str:
        if not isinstance(month, int) or not (1 <= month <= 12):
            raise ValueError('Неверное значение месяца')

        match month:
            case 12 | 1 | 2:
                return "Зима"
            case 3 | 4 | 5:
                return "Весна"
            case 6 | 7 | 8:
                return "Лето"
            case _:
                return "Осень"

    # Банковский вклад
    @staticmethod
    def bank(a: float, years: int) -> float:
        if not isinstance(a, (int, float)) or a <= 0:
            raise ValueError("Сумма вклада должна быть положительным числом")
        if not isinstance(years, int) or years < 0:
            raise ValueError("Количество лет должно быть неотрицательным числом")

        for _ in range(years):
            a += a * 0.1
        return a

    # Простые числа
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

