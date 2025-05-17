import pytest
import array
from .demo_array import DemoArray
from contextlib import nullcontext as does_not_raise


# тест инициализации
@pytest.mark.parametrize('arg, expected_exception', [
    # Валидные кейсы
    (5, does_not_raise()),  # целое положительное число
    (array.array('i', [1, 2, 3]), does_not_raise()),  # массив типа 'i'

    # Невалидные кейсы
    ('invalid', pytest.raises(ValueError)),  # неверный тип аргумента
    (-5, pytest.raises(ValueError)),  # отрицательное целое число
    (array.array('f', [1.0, 2.0]), pytest.raises(ValueError))  # массив типа 'f'
])
def test_create_array(arg, expected_exception):
    with expected_exception:
        DemoArray(arg)


# тест метода sum_elements
@pytest.mark.parametrize('arr, expected_sum', [
    (array.array('i', [1, 2, 3]), 6),   # Сумма 1 + 2 + 3 = 6
    (array.array('i', [1, -2, 3]), 2),  # Сумма 1 - 2 + 3 = 2
    (array.array('i', [-1, -1, -1]), -3),  # Сумма -1 - 1 - 1 = -3
    (array.array('i', [1, 0, 3]), 4),   # Сумма 1 + 0 + 3 = 4
])
def test_sum_elements(arr, expected_sum):
    demo = DemoArray(arr)
    assert demo.sum_elements() == expected_sum


# тест унарного минуса
@pytest.mark.parametrize('arg, expected_result', [
    (array.array('i', [1, -2, 3]), -2),
    (array.array('i', [1, 2, 3]), -6),
    (3, 0), # массив из нулей размером 3
])
def test_negate_array(arg, expected_result):
    demo = DemoArray(arg)
    demo = -demo
    assert demo.sum_elements() == expected_result


# тест iadd (замена инкремента)
@pytest.mark.parametrize('arr, add_value, expected_result', [
    (array.array('i', [1, 2, 3]), 2, 12),  # += 2
    (array.array('i', [1, -1, 1]), 3, 10)   # += 3
])
def test_iadd_array(arr, add_value, expected_result):
    demo = DemoArray(arr)
    demo += add_value
    assert demo.sum_elements() == expected_result


# тест метода __bool__
@pytest.mark.parametrize('arr, expected_bool', [
    (array.array('i', [1, 2, 3]), True),   # Все элементы положительные
    (array.array('i', [1, -2, 3]), False), # Не все элементы положительные
    (array.array('i', [1, 0, 3]), False),  # Есть 0
])
def test_all_positive_elements(arr, expected_bool):
    demo = DemoArray(arr)
    assert bool(demo) == expected_bool


# тест __str__ (строковое представление)
@pytest.mark.parametrize('arr, expected_str', [
    (array.array('i', [1, 2, 3]), '[1, 2, 3]'),   # Проверка строкового представления
    (array.array('i', [1, -2, 3]), '[1, -2, 3]')   # Проверка строкового представления
])
def test_str_method(arr, expected_str):
    demo = DemoArray(arr)
    assert str(demo) == expected_str
