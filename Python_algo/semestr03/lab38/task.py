# для однотипных атрибутов делаем дескриптор
class SideDescriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Нужно вводить только числа!\n")
        if value <= 0:
            raise ValueError("С отрицательными числами ничего не выйдет!\n")
        setattr(instance, self.name,  value)


class TriangleChecker:
    a = SideDescriptor()
    b = SideDescriptor()
    c = SideDescriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> str:
        """Проверяет, можно ли из отрезков создать треугольник"""
        if (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a):
            return "Ура, можно построить треугольник!\n"
        else:
            return "Жаль, но из этого треугольник не сделать\n"


if __name__ == '__main__':
    try:
        sides = input("Введите длины отрезков через пробел: ").split()
        checker = TriangleChecker(*sides)
        print(checker.is_triangle())
    except ValueError as e:
        print(e)

