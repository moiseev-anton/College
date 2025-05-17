from contextlib import nullcontext as does_not_raise

import pytest

from .demo_list import DemoList  # Замените на фактический импорт


@pytest.mark.parametrize(
    "args, expected",
    [
        ((), []),  # пустой список
        ((1, 2, 3), [1, 2, 3]),  # несколько элементов
        ((DemoList(1, 2),), [1, 2]),  # объект DemoList
    ]
)
def test_initialization(args, expected):
    dl = DemoList(*args)
    assert dl.data == expected


@pytest.mark.parametrize(
    "element, index, expected",
    [
        (4, None, [1, 2, 3, 4]),  # Добавляем элемент в конец
        (0, 0, [0, 1, 2, 3]),  # Добавляем элемент в начало
        (4, 2, [1, 2, 4, 3]),  # Добавляем элемент по индексу
    ]
)
def test_add(element, index, expected):
    dl = DemoList(1, 2, 3)
    dl.add(element, index)
    assert dl.data == expected


@pytest.mark.parametrize(
    "elements, index, expected",
    [
        ((4, 5), None, [1, 2, 3, 4, 5]),  # несколько элементов в конец
        ((4, 5), 1, [1, 4, 5, 2, 3]),  # несколько элементов в середину
        ((4, 5, 6), 0, [4, 5, 6, 1, 2, 3]),  # несколько элементов в начало
        ((DemoList(7, 8),), None, [1, 2, 3, 7, 8]),  # DemoList в конец
        ((DemoList(7, 8),), 1, [1, 7, 8, 2, 3]),  # DemoList в середину
    ]
)
def test_add_list(elements, index, expected):
    dl = DemoList(1, 2, 3)
    dl.add_list(*elements, index=index)
    assert dl.data == expected


@pytest.mark.parametrize(
    "element, index, expected, exception",
    [
        # Валидные кейсы
        (None, 0, [2, 3], does_not_raise()),  # удаляем первый элемент по индексу
        (None, 1, [1, 3], does_not_raise()),  # удаляем второй элемент по индексу
        (1, None, [2, 3], does_not_raise()),  # удаляем конкретный элемент
        (4, None, [1, 2, 3], does_not_raise()),  # удаляем элемент которого нет в списке
        (None, None, [1, 2], does_not_raise()),  # по умолчанию удаляем последний элемент

        # Невалидные кейсы
        (1, 1, [1, 2, 3], pytest.raises(ValueError)),  # задан элемент и индекc -> ошибка
    ]
)
def test_remove(element, index, expected, exception):
    dl = DemoList(1, 2, 3)
    with exception:
        dl.remove(element=element, index=index)
        assert dl.data == expected


@pytest.mark.parametrize(
    "elements, expected",
    [
        ((2, 3), [1]),  # удаляем несколько элементов
        ((DemoList(2, 3),), [1]),  # удаляем DemoList
        ((4,), [1, 2, 3]),  # удаляем элемент, которого нет в списке
    ]
)
def test_remove_list(elements, expected):
    dl = DemoList(1, 2, 3)
    dl.remove_list(*elements)
    assert dl.data == expected


@pytest.mark.parametrize(
    "criterion, expected",
    [
        (lambda x: x > 2, [3]),  # элементы больше 2
        (lambda x: x < 3, [1, 2]),  # элементы меньше 3
        (lambda x: x % 2 == 0, [2]),  # только чётные элементы
    ]
)
def test_filter(criterion, expected):
    dl = DemoList(1, 2, 3)
    filtered = dl.filter(criterion)
    assert filtered.data == expected


@pytest.mark.parametrize(
    "desc, expected",
    [
        (True, [3, 2, 1]),  # по убыванию
        (False, [1, 2, 3]),  # по возрастанию
    ]
)
def test_sort(desc, expected):
    dl = DemoList(3, 1, 2)
    sorted_dl = dl.sort(desc)
    assert sorted_dl.data == expected
