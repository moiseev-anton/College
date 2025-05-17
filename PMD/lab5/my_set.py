from typing import Any, Iterator


class MyHashSet:
    """Класс для собственной реализации множества с использованием хеш-таблицы."""

    def __init__(self):
        """Инициализация множества."""
        self._buckets = [[] for _ in range(16)]  # Создаем список "корзин" для хранения элементов
        self._size = 0  # Текущее количество элементов

    def _hash(self, item: Any) -> int:
        """Вычисление хэша элемента и преобразование в индекс корзины"""
        return hash(item) % len(self._buckets)

    def _resize(self) -> None:
        """Ресайз таблицы, если количество элементов превышает размер корзин"""
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(len(old_buckets) * 2)]
        for bucket in old_buckets:
            for item in bucket:
                self.add(item)

    def add(self, item: Any) -> None:
        """Добавление элемента в множество."""
        index = self._hash(item)
        bucket = self._buckets[index]
        if item not in bucket:
            bucket.append(item)
            self._size += 1
            if self._size > len(self._buckets) * 0.75:  # Если таблица заполнена на 75%, ресайзим ее
                self._resize()

    def remove(self, item: Any) -> bool:
        """Удаление элемента из множества. True, если элемент был удален, иначе False"""
        index = self._hash(item)
        bucket = self._buckets[index]
        if item in self:
            bucket.remove(item)
            return True
        return False

    def union(self, other: 'MyHashSet') -> 'MyHashSet':
        """Объединение"""
        result = MyHashSet()
        for item in self:
            result.add(item)
        for item in other:
            result.add(item)
        return result

    def intersection(self, other: 'MyHashSet') -> 'MyHashSet':
        """Пересечение"""
        result = MyHashSet()
        for item in self:
            if item in other:
                result.add(item)
        return result

    def __contains__(self, item) -> bool:
        """Проверка, содержится ли элемент в множестве."""
        index = self._hash(item)
        return item in self._buckets[index]

    def __len__(self) -> int:
        """Возвращает количество элементов в множестве."""
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """Итерация по элементам множества."""
        for bucket in self._buckets:
            for item in bucket:
                yield item

    def __str__(self) -> str:
        """Представление множества в виде строки"""
        return f"MyHashSet({[str(item) for item in self]})"

