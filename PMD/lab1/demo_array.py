import array
from typing import Union


class DemoArray:
    """Класс целочисленного массива"""
    def __init__(self, arg: Union[int, array.array]):
        if isinstance(arg, int):
            if arg <= 0:
                raise ValueError('Размер массива должен быть натуральным числом')
            # Создаем массив заданного размера, заполненный нулями
            self.array = array.array('i', [0] * arg)

        elif isinstance(arg, array.array):
            # Проверяем тип данных массива
            if arg.typecode != 'i':
                raise ValueError('Массив array.array должен быть типа \'i\'')
            # Используем переданный массив
            self.array = arg
        else:
            raise ValueError('Должен быть передан целое число или массив типа array.array')

    @property
    def size(self) -> int:
        """Свойство возвращает размер массива"""
        return len(self.array)

    def __neg__(self) -> 'DemoArray':
        """Перегрузка унарного минуса"""
        self.array = array.array(self.array.typecode, [-x for x in self.array])
        return self

    def __iadd__(self, value: int) -> 'DemoArray':
        """Перегрузка операции += (замена инкремента)"""
        self.array = array.array(self.array.typecode, [x + value for x in self.array])
        return self


    def sum_elements(self) -> int:
        """Вычиляет сумму элементов"""
        return sum(self.array)

    def __bool__(self) -> bool:
        """Перегрузка для проверки всех элементов массива на положительность"""
        return all(x > 0 for x in self.array)

    def __str__(self) -> str:
        """Строковое отображения массива"""
        return repr(self.array)[11:-1]


if __name__ == '__main__':
    demo = DemoArray(array.array('i', [5, -3, 2]))
    print(demo)

    demo = -demo
    print(demo)

    demo += 4
    print(demo)

    print(bool(demo))