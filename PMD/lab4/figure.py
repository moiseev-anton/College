from abc import ABC, abstractmethod
from math import pi, sqrt


class LengthDescriptor:
    """Дескриптор длины"""

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        try:
            value = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"{self.name[1:]} должно быть числом.")

        if value < 0:
            raise ValueError(f"{self.name[1:]} не может быть меньше 0.")
        setattr(instance, self.name, value)


class Figure(ABC):
    """Абстрактный базовый класс фигур"""
    size1 = LengthDescriptor()
    size2 = LengthDescriptor()

    def __init__(self, size1: float, size2: float):
        self.size1 = size1
        self.size2 = size2

    @abstractmethod
    def get_area(self) -> float:
        """Абстрактный метод вычисления площади"""
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        """Абстрактный метод вычисления периметра"""
        pass

    def get_hypotenuse(self) -> float:
        """Абстрактный метод вычисления гипотенузы (только для Rhombus)"""
        pass


class Rhombus(Figure):
    """Класс ромба"""

    def __init__(self, diagonal1: float, diagonal2: float):
        # Вызываем "конструктор" родительского класса
        super().__init__(size1=diagonal1, size2=diagonal2)

    @property
    def side(self) -> float:
        """Свойство: Сторона ромба"""
        return self.get_hypotenuse()

    def get_hypotenuse(self) -> float:
        """Метод для вычисления гипотенузу"""
        return sqrt((self.size1 / 2) ** 2 + (self.size2 / 2) ** 2)

    def get_area(self) -> float:
        """Вычисление площади ромба"""
        return (self.size1 * self.size2) / 2

    def get_perimeter(self) -> float:
        """Вычисление периметра ромба"""
        return 4 * self.side


class Rectangle(Figure):
    """Класс прямоугольника"""

    def __init__(self, width: float, height: float):
        # Вызываем "конструктор" родительского класса
        super().__init__(size1=width, size2=height)

    def get_area(self) -> float:
        """Вычисление площади прямоугольника."""
        return self.size1 * self.size2

    def get_perimeter(self) -> float:
        """Вычисление периметра прямоугольника."""
        return 2 * (self.size1 + self.size2)


class Ellipse(Figure):
    """Класс эллипса"""

    def __init__(self, major_semi_axis: float, minor_semi_axis: float):
        # Вызываем "конструктор" родительского класса
        super().__init__(size1=major_semi_axis, size2=minor_semi_axis)

    def get_area(self) -> float:
        """Вычисление площади эллипса."""
        return pi * self.size1 * self.size2

    def get_perimeter(self) -> float:
        """Периметр эллипса (формула Рамануджана)"""
        a, b = self.size1, self.size2
        return pi * (3 * (a + b) - sqrt((3 * a + b) * (a + 3 * b)))


if __name__ == '__main__':
    # Ромб
    rhombus = Rhombus(diagonal1=10, diagonal2=8)
    print('Ромб:')
    print(f'  Площадь: {rhombus.get_area():.2f}')
    print(f'  Периметр: {rhombus.get_perimeter():.2f}')

    # Прямоугольник
    rectangle = Rectangle(width=10, height=5)
    print('\nПрямоугольник:')
    print(f'  Площадь: {rectangle.get_area():.2f}')
    print(f'  Периметр: {rectangle.get_perimeter():.2f}')

    # Эллипс
    ellipse = Ellipse(major_semi_axis=7, minor_semi_axis=5)
    print('\nЭллипс:')
    print(f'  Площадь: {ellipse.get_area():.2f}')
    print(f'  Периметр: {ellipse.get_perimeter():.2f}')
