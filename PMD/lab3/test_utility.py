from contextlib import nullcontext as does_not_raise

import pytest
from .utility import Utility


# Тест для is_leap_year
@pytest.mark.parametrize(
    "year, expected, exception",
    [
        # Валидные кейсы
        (2020, True, does_not_raise()),  # високосный
        (2021, False, does_not_raise()),  # не високосный
        (1900, False, does_not_raise()),  # не високосный кратный 100, но не 400
        (2000, True, does_not_raise()),  # високосный кратный 400

        # Невалидные тесты
        (15.5, False, pytest.raises(ValueError)),  # не целое
        ('строка', False, pytest.raises(ValueError)),  # не число

    ]
)
def test_is_leap_year(year, expected, exception):
    with exception:
        assert Utility.is_leap_year(year) == expected


# Тест для date
@pytest.mark.parametrize(
    "day, month, year, expected",
    [
        (29, 2, 2020, True),  # високосный год
        (29, 2, 2021, False),  # не високосный год
        (31, 12, 2021, True),  # корректная дата
        (32, 1, 2021, False),  # некорректный день
        (15, 13, 2021, False),  # некорректный месяц
        (1, 1, 2021, True),  # корректная дата
    ]
)
def test_date(day, month, year, expected):
    assert Utility.date(day, month, year) == expected


# Тест для arithmetic
@pytest.mark.parametrize(
    "a, b, operation, expected, exception",
    [
        # Валидные кейсы
        (5, 3, '+', 8, does_not_raise()),  # сложение
        (5, 3, '-', 2, does_not_raise()),  # вычитание
        (5, 3, '*', 15, does_not_raise()),  # умножение
        (5, 3, '/', 1.6666666666666667, does_not_raise()),  # деление

        # Невалидные тесты
        (5, 0, '/', None, pytest.raises(ValueError)),  # деление на ноль
        (5, 3, 'invalid', None, pytest.raises(ValueError)),  # неизвестная операция
        ("5", 3, "+", 8, pytest.raises(ValueError)),  # некорректный тип a
        (5, "3", "+", 8, pytest.raises(ValueError)),  # некорректный тип b
        (5, 3, "", None, pytest.raises(ValueError))  # пустая операция
    ]
)
def test_arithmetic(a, b, operation, expected, exception):
    with exception:
        assert Utility.arithmetic(a, b, operation) == expected


# Тест для season
@pytest.mark.parametrize(
    "month, expected, exception",
    [
        # Валидные кейсы
        (1, "Зима", does_not_raise()),  # январь
        (3, "Весна", does_not_raise()),  # март
        (6, "Лето", does_not_raise()),  # июнь
        (9, "Осень", does_not_raise()),  # сентябрь
        (12, "Зима", does_not_raise()),  # декабрь

        # Невалидные тесты
        (15, "_", pytest.raises(ValueError)),  # некорректный месяц
        (0, "_", pytest.raises(ValueError)),  # некорректный месяц
        (3.5, "_", pytest.raises(ValueError)),  # нецелое
        ('invalid', "_", pytest.raises(ValueError)),  # строка
    ]
)
def test_season(month, expected, exception):
    with exception:
        assert Utility.season(month) == expected


# Тест для bank
@pytest.mark.parametrize(
    "a, years, expected",
    [
        (1000, 1, 1100),  # 1000 через 1 год с 10% годовых
        (1000, 2, 1210),  # 1000 через 2 года с 10% годовых
        (1000, 3, 1331),  # 1000 через 3 года с 10% годовых
        (500, 0, 500),  # 0 лет — деньги не меняются
    ]
)
def test_bank(a, years, expected):
    assert Utility.bank(a, years) == expected


# Тест для is_prime
@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),  # простое
        (3, True),  # простое
        (4, False),  # не простое
        (9, False),  # не простое
        (29, True),  # простое
        (1, False),  # 1 не простое
        (0, False),  # 0 не простое
    ]
)
def test_is_prime(n, expected):
    assert Utility.is_prime(n) == expected


