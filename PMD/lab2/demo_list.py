from typing import Any, Callable, Optional


class DemoList:
    def __init__(self, *args: Any) -> None:
        """
        Используем args как замену множественным конструкторам:
        - Без аргументов: создаёт пустой список.
        - С несколькими элементами: создаёт объект-список из этих элементов.
        - Если передан объект DemoList: создаёт копию этого объекта.
        """
        if len(args) == 0:
            self.data = []
        elif len(args) == 1 and isinstance(args[0], DemoList):
            self.data = args[0].data[:]  # cоздаем копию
        else:
            self.data = list(args)

    def add(self, element: Any, index: Optional[int] = None) -> None:
        """Добавляет элемент в список в конец или по индексу"""
        if index is None:
            self.data.append(element)
        else:
            self.data.insert(index, element)

    def add_list(self, *elements: Any, index: Optional[int] = None) -> None:
        """
        Добавляет элементы или объект DemoList
        - по умолчанию добавляет в конец.
        - с указанием индекса добавляет на заданную позицию.
        """
        flattened_elements = []
        for element in elements:
            if isinstance(element, DemoList):
                flattened_elements.extend(element.data)
            else:
                flattened_elements.append(element)

        if index is None:
            self.data.extend(flattened_elements)
        else:
            for i, element in enumerate(flattened_elements):
                self.data.insert(index + i, element)

    def remove(self, element: Optional[Any] = None, index: Optional[int] = None) -> None:
        """
        Удаляет элемент из списка:
        - если указан только `index` удаляет элемент на указанной позиции
        - если указан только `element` удаляет первое вхождение элемента.
        - если оба параметра не указаны удаляет последний элемент.
        - если оба параметра указаны вызывает исключение.
        """
        if element is not None and index is not None:
            raise ValueError("Можно задать только 'element' или 'index'")

        if index is not None:
            del self.data[index]
        elif element is not None:
            if element in self.data:
                self.data.remove(element)
        else:
            if self.data:
                self.data.pop()

    def remove_list(self, *elements: Any) -> None:
        """
        Удаляет элементы из списка.
        Принимает несколько элементов или объект DemoList
        """
        for element in elements:
            if isinstance(element, DemoList):
                for item in element.data:
                    self.remove(item)
            else:
                self.remove(element)

    def filter(self, criterion: Callable):
        """
        Создаёт новый DemoList на основе критерия.
        Критерий передаётся в виде функции возвращающей True/False
        """
        return DemoList(*(item for item in self.data if criterion(item)))

    def sort(self, desc: bool = True) -> 'DemoList':
        """
        Сортирует элементы в списке.
        - desc=True: по убыванию.
        - desc=False: по возрастанию (asc)
        """
        sorted_data = sorted(self.data, reverse=desc)
        return DemoList(*sorted_data)

    def __repr__(self):
        """Строковое представление объекта"""
        return f"DemoList({self.data})"
